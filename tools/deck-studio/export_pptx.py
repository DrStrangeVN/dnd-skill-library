#!/usr/bin/env python3
"""export_pptx.py — deck.json + theme.json -> editable .pptx (16:9).

Run with the deck venv python (python-pptx):
  ~/workspace/tools/deck-venv/bin/python export_pptx.py DECK.json THEME.json [-o out.pptx]

All text is native, editable text boxes mirroring the HTML geometry
(shared deckkit model). Decorations are native shapes. Speaker notes
go to the notes slides. Fonts are named (not embedded).
"""
import argparse
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckkit import (EMU_PER_PX, STAGE_H, STAGE_W, compile_deck, load_json,
                     parse_runs, resolve_color)

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Pt

ALIGN = {"left": PP_ALIGN.LEFT, "center": PP_ALIGN.CENTER, "right": PP_ALIGN.RIGHT}
SHAPES = {"rect": MSO_SHAPE.RECTANGLE, "roundrect": MSO_SHAPE.ROUNDED_RECTANGLE,
          "oval": MSO_SHAPE.OVAL}


def E(px):
    return Emu(int(round(px * EMU_PER_PX)))


def _append_alpha(clr, alpha_pct):
    a = clr.makeelement(qn("a:alpha"), {"val": str(int(alpha_pct * 1000))})
    clr.append(a)


def set_alpha(shape, alpha_pct):
    """alpha_pct: 0 transparent .. 100 opaque (matches deckkit semantics)."""
    sp = shape.fill._xPr.find(qn("a:solidFill"))
    if sp is None:
        return
    clr = sp.find(qn("a:srgbClr"))
    if clr is None:
        return
    _append_alpha(clr, alpha_pct)


def set_line_alpha(shape, alpha_pct):
    ln = shape.line._get_or_add_ln()
    sp = ln.find(qn("a:solidFill"))
    if sp is None:
        return
    clr = sp.find(qn("a:srgbClr"))
    if clr is None:
        return
    _append_alpha(clr, alpha_pct)


def style_fill(shape, el, pal, theme=None):
    if el.get("glass"):
        g = (theme or {}).get("glass") or {}
        base = resolve_color(pal, el["fill"]) if el.get("fill") else "#FFFFFF"
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor.from_string(base.lstrip("#"))
        set_alpha(shape, g.get("fill_alpha", 0.12) * 100)
        shape.line.color.rgb = RGBColor.from_string("FFFFFF")
        shape.line.width = Pt(1.0)
        set_line_alpha(shape, g.get("border_alpha", 0.45) * 100)
    elif el.get("fill"):
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor.from_string(
            resolve_color(pal, el["fill"]).lstrip("#"))
        if el.get("alpha") is not None:
            set_alpha(shape, el["alpha"])
    else:
        shape.fill.background()
    if not el.get("glass"):
        if el.get("line_color"):
            shape.line.color.rgb = RGBColor.from_string(
                resolve_color(pal, el["line_color"]).lstrip("#"))
            shape.line.width = Pt(el.get("line_w", 1.0))
        else:
            shape.line.fill.background()
    shape.shadow.inherit = False


_GRADIENT_CACHE = {}


def gradient_png(el):
    """Pre-render a theme gradient to a PNG sized to the element (Pillow).
    PPTX glass/gradient parity trick: the gradient becomes a picture and
    editable text sits on top — no live gradient fill needed."""
    key = (el["g_from"], el["g_to"], el.get("g_angle", 180),
           int(el["w"]), int(el["h"]))
    if key in _GRADIENT_CACHE:
        return _GRADIENT_CACHE[key]
    import hashlib
    import tempfile

    from PIL import Image
    w, h = max(2, int(el["w"])), max(2, int(el["h"]))
    c0 = tuple(int(el["g_from"].lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    c1 = tuple(int(el["g_to"].lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    angle = el.get("g_angle", 180) % 360
    if angle in (90, 270):
        strip = Image.new("RGB", (256, 1))
        strip.putdata([tuple(round(c0[i] + (c1[i] - c0[i]) * t / 255)
                             for i in range(3)) for t in range(256)])
        if angle == 270:
            strip = strip.transpose(Image.FLIP_LEFT_RIGHT)
        img = strip.resize((w, h))
    else:
        strip = Image.new("RGB", (1, 256))
        strip.putdata([tuple(round(c0[i] + (c1[i] - c0[i]) * t / 255)
                             for i in range(3)) for t in range(256)])
        if angle == 0:
            strip = strip.transpose(Image.FLIP_TOP_BOTTOM)
        img = strip.resize((w, h))
        if angle not in (0, 180):
            img = img.rotate(angle - 180, resample=Image.BILINEAR, expand=False)
    name = "deckgrad-" + hashlib.md5(repr(key).encode()).hexdigest() + ".png"
    path = os.path.join(tempfile.gettempdir(), name)
    img.save(path)
    _GRADIENT_CACHE[key] = path
    return path


def _rgb(hex_color):
    h = hex_color.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def _tmp_png(img, prefix):
    fd, path = tempfile.mkstemp(suffix=".png", prefix=prefix)
    os.close(fd)
    img.save(path)
    return path


class SlideCanvas:
    """Pillow composite of everything painted so far on one slide.

    The PPTX exporter keeps this running picture of the slide so glass
    panels can be *baked*: the panel's fill becomes a blurred crop of
    the real background beneath it (see baked_glass), which is what
    makes PPTX glass read as frosted instead of merely translucent.
    Text is not drawn (it never sits under a glass panel in our
    layouts); shapes are drawn approximately — close enough to blur.
    """

    def __init__(self, bg_hex):
        self.img = Image.new("RGBA", (STAGE_W, STAGE_H), _rgb(bg_hex) + (255,))

    def paste_file(self, path, el):
        im = Image.open(path).convert("RGBA")
        w, h = max(1, int(el["w"])), max(1, int(el["h"]))
        im = im.resize((w, h))
        self.img.paste(im, (int(el["x"]), int(el["y"])), im)

    def paste_image(self, im, x, y):
        self.img.paste(im, (int(x), int(y)), im)

    def draw_shape(self, el, pal, theme):
        if el.get("kind") == "glasssphere":
            color, a = (191, 224, 245), 140
        else:
            if not el.get("fill"):
                return
            color = _rgb(resolve_color(pal, el["fill"]))
            alpha = el.get("alpha")
            a = 255 if alpha is None else int(alpha * 2.55)
        ov = Image.new("RGBA", (STAGE_W, STAGE_H), (0, 0, 0, 0))
        d = ImageDraw.Draw(ov)
        box = [el["x"], el["y"], el["x"] + el["w"], el["y"] + el["h"]]
        if el["kind"] == "oval" or el.get("kind") == "glasssphere":
            d.ellipse(box, fill=color + (a,))
        elif el["kind"] == "roundrect":
            d.rounded_rectangle(
                box, radius=el.get("radius", theme.get("radius", 10)),
                fill=color + (a,))
        else:
            d.rectangle(box, fill=color + (a,))
        self.img.alpha_composite(ov)


_SCRIM_CACHE = {}


def scrim_png(el):
    """Render a scrim element (vertical alpha gradient) to a PNG."""
    key = (el.get("color"), el.get("a0"), el.get("a1"),
           int(el["w"]), int(el["h"]))
    if key in _SCRIM_CACHE:
        return _SCRIM_CACHE[key]
    w, h = max(1, int(el["w"])), max(1, int(el["h"]))
    r, g, b = _rgb(el.get("color", "#041E38"))
    a0, a1 = float(el.get("a0", 42)), float(el.get("a1", 4))
    strip = Image.new("RGBA", (1, h))
    strip.putdata([(r, g, b, int(2.55 * (a0 + (a1 - a0) * t / max(1, h - 1))))
                    for t in range(h)])
    path = _tmp_png(strip.resize((w, h)), "deckscrim-")
    _SCRIM_CACHE[key] = path
    return path


def baked_glass(canvas, el, theme):
    """Bake one frosted-glass panel: crop the slide background under
    the panel from the running canvas, blur it, lift saturation, tint
    it toward white by the theme's glass fill_alpha, round its corners
    and (when the element asks) bake a soft drop shadow underneath on
    a padded transparent canvas. Returns (png_path, pad, panel_image).
    The panel is placed as a picture; the caller adds a native border
    shape on top and the panel's text stays native."""
    g = theme.get("glass") or {}
    fill_a = float(g.get("fill_alpha", 0.12))
    blur = float(el.get("blur", g.get("blur_px", 14)))
    x, y, w, h = (int(el["x"]), int(el["y"]), int(el["w"]), int(el["h"]))
    region = canvas.img.crop((x, y, x + w, y + h)).convert("RGB")
    if blur > 0:
        region = region.filter(ImageFilter.GaussianBlur(blur))
    region = ImageEnhance.Color(region).enhance(1.15)
    if fill_a > 0:
        region = Image.blend(
            region, Image.new("RGB", region.size, (255, 255, 255)), fill_a)
    radius = el.get("radius", theme.get("radius", 10))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle(
        [0, 0, w - 1, h - 1], radius=radius, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(0.8))
    region = region.convert("RGBA")
    region.putalpha(mask)
    pad = 30 if el.get("shadow") else 2
    panel = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    if el.get("shadow"):
        sh = Image.new("RGBA", panel.size, (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle(
            [pad, pad + 12, pad + w, pad + 12 + h], radius=radius,
            fill=(5, 25, 45, 72))
        panel.alpha_composite(sh.filter(ImageFilter.GaussianBlur(16)))
    panel.paste(region, (pad, pad), region)
    return _tmp_png(panel, "deckglass-"), pad, panel


def add_text(slide, el, theme):
    pal, fonts = theme["palette"], theme["fonts"]
    box = slide.shapes.add_textbox(E(el["x"]), E(el["y"]), E(el["w"]), E(el["h"]))
    tf = box.text_frame
    tf.word_wrap = True
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, 0)
    tf.vertical_anchor = (MSO_ANCHOR.MIDDLE if el.get("valign") == "middle"
                          else MSO_ANCHOR.TOP)
    lines = str(el["text"]).split("\n")
    for li, line_text in enumerate(lines):
        p = tf.paragraphs[0] if li == 0 else tf.add_paragraph()
        p.alignment = ALIGN[el["align"]]
        if el.get("line"):
            p.line_spacing = el["line"]
        for txt, bold, serif, italic in parse_runs(line_text):
            r = p.add_run()
            r.text = txt
            f = r.font
            f.name = fonts["display"] if serif else fonts[el["font"] or el["role"]]
            f.size = Pt(el["size"] * 0.75)  # stage px @96dpi -> pt
            f.bold = (bold or el["bold"]) and not serif
            f.italic = bool(el["italic"] or italic)
            f.color.rgb = RGBColor.from_string(
                resolve_color(pal, el["color"]).lstrip("#"))
            if el.get("spacing"):
                r.font._rPr.set("spc", str(int(el["spacing"] * 100)))
    return box


def export(spec, theme, out_path, deck_dir):
    slides = compile_deck(spec, theme)
    pal = theme["palette"]
    prs = Presentation()
    prs.slide_width = E(STAGE_W)
    prs.slide_height = E(STAGE_H)
    blank = prs.slide_layouts[6]
    for sl in slides:
        slide = prs.slides.add_slide(blank)
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = RGBColor.from_string(pal["bg"].lstrip("#"))
        canvas = SlideCanvas(pal["bg"])
        for el in sl["elements"]:
            kind = el["kind"]
            if kind == "text":
                add_text(slide, el, theme)
            elif kind in ("image", "art"):
                src = el["src"]
                if src.startswith(("http://", "https://")):
                    raise SystemExit(f"image layout needs a local file, got URL: {src}")
                p = src if os.path.isabs(src) else os.path.join(deck_dir, src)
                slide.shapes.add_picture(p, E(el["x"]), E(el["y"]),
                                         E(el["w"]), E(el["h"]))
                canvas.paste_file(p, el)
            elif kind == "gradient":
                gp = gradient_png(el)
                slide.shapes.add_picture(gp, E(el["x"]), E(el["y"]),
                                         E(el["w"]), E(el["h"]))
                canvas.paste_file(gp, el)
            elif kind == "scrim":
                sp = scrim_png(el)
                slide.shapes.add_picture(sp, E(el["x"]), E(el["y"]),
                                         E(el["w"]), E(el["h"]))
                canvas.paste_file(sp, el)
            elif kind == "glasssphere":
                # Legacy approximation (v3 decks use real art PNGs via
                # "orbs"/"art" instead): a translucent pale oval with a
                # light rim stands in for the CSS glass sphere.
                shp = slide.shapes.add_shape(MSO_SHAPE.OVAL, E(el["x"]), E(el["y"]),
                                             E(el["w"]), E(el["h"]))
                shp.fill.solid()
                shp.fill.fore_color.rgb = RGBColor.from_string("BFE0F5")
                set_alpha(shp, 55)
                shp.line.color.rgb = RGBColor.from_string("FFFFFF")
                shp.line.width = Pt(1.0)
                set_line_alpha(shp, 70)
                shp.shadow.inherit = False
                canvas.draw_shape(el, pal, theme)
            elif el.get("glass"):
                # Frosted glass (v3): bake the blurred background crop
                # as the panel's picture fill; a native no-fill shape
                # on top carries the crisp border. Text stays native.
                done = False
                try:
                    gp, pad, panel = baked_glass(canvas, el, theme)
                    slide.shapes.add_picture(
                        gp, E(el["x"] - pad), E(el["y"] - pad),
                        E(el["w"] + 2 * pad), E(el["h"] + 2 * pad))
                    shp = slide.shapes.add_shape(
                        SHAPES[kind], E(el["x"]), E(el["y"]),
                        E(el["w"]), E(el["h"]))
                    if kind == "roundrect":
                        try:
                            shp.adjustments[0] = min(
                                0.5, el.get("radius", theme.get("radius", 10))
                                / max(1, min(el["w"], el["h"])))
                        except Exception:
                            pass
                    shp.fill.background()
                    g = theme.get("glass") or {}
                    shp.line.color.rgb = RGBColor.from_string("FFFFFF")
                    shp.line.width = Pt(1.0)
                    set_line_alpha(shp, g.get("border_alpha", 0.45) * 100)
                    shp.shadow.inherit = False
                    canvas.paste_image(panel, el["x"] - pad, el["y"] - pad)
                    done = True
                except Exception:
                    done = False
                if not done:  # fallback: v2 translucent-fill behaviour
                    shp = slide.shapes.add_shape(
                        SHAPES[kind], E(el["x"]), E(el["y"]),
                        E(el["w"]), E(el["h"]))
                    if kind == "roundrect":
                        try:
                            shp.adjustments[0] = min(
                                0.5, el.get("radius", theme.get("radius", 10))
                                / max(1, min(el["w"], el["h"])))
                        except Exception:
                            pass
                    style_fill(shp, el, pal, theme)
                    canvas.draw_shape(el, pal, theme)
            else:
                shp = slide.shapes.add_shape(SHAPES[kind], E(el["x"]), E(el["y"]),
                                             E(el["w"]), E(el["h"]))
                if kind == "roundrect":
                    try:
                        shp.adjustments[0] = min(
                            0.5, el.get("radius", theme.get("radius", 10))
                            / max(1, min(el["w"], el["h"])))
                    except Exception:
                        pass
                style_fill(shp, el, pal, theme)
                canvas.draw_shape(el, pal, theme)
        if sl["notes"]:
            slide.notes_slide.notes_text_frame.text = sl["notes"]
    prs.save(out_path)
    return len(slides)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("theme")
    ap.add_argument("-o", "--out", default="deck.pptx")
    a = ap.parse_args()
    spec, theme = load_json(a.deck), load_json(a.theme)
    n = export(spec, theme, a.out, os.path.dirname(os.path.abspath(a.deck)))
    print(f"wrote {a.out} ({n} slides, theme {theme['slug']})")


if __name__ == "__main__":
    main()
