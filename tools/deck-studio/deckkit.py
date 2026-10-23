"""deckkit — shared core for the deck-studio engine.

One geometry model (1280x720 stage) drives BOTH outputs:
  * build_deck.py  -> studio deck.html
  * export_pptx.py -> editable .pptx

Every layout is compiled to a flat list of elements:
  {kind: 'text'|'rect'|'roundrect'|'oval'|'image'|'gradient'|'glasssphere'
        |'art'|'scrim',
   x, y, w, h,                      # stage px (1280x720)
   text, role, size, color, align,  # text-only fields
   bold, italic, font, spacing, line,   # text styling
   fill, line_color, line_w, alpha,     # shape styling
   src}                                 # image-only
Roles map to theme fonts: display / body / mono.
Colors are theme palette keys: bg, surface, ink, muted, accent, accent2, line.

Inline emphasis in text: **bold** segments are parsed by parse_runs().
"""
import json
import re

STAGE_W, STAGE_H = 1280, 720
EMU_PER_PX = 9525  # 12192000 EMU (13.333in) / 1280 px == 6858000 / 720

PALETTE_KEYS = ("bg", "surface", "ink", "muted", "accent", "accent2", "line")


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def parse_runs(text):
    """Split inline markup into [(text, bold, serif, italic), ...].

    '**bold**' = bold run (in the element's own font);
    '~serif~'  = serif run (theme display font, never bold) — used by
    mixed-type headlines that pair a grotesk with a serif voice;
    '*italic*' = italic run (element's own font) — used by serif
    catalogues that mix roman and italic lines in one headline.
    """
    if text is None:
        return []
    parts = re.split(r"(\*\*.+?\*\*|~.+?~|\*[^*\n]+?\*)", str(text))
    runs = []
    for p in parts:
        if not p:
            continue
        if p.startswith("**") and p.endswith("**") and len(p) > 4:
            runs.append((p[2:-2], True, False, False))
        elif p.startswith("~") and p.endswith("~") and len(p) > 2:
            runs.append((p[1:-1], False, True, False))
        elif p.startswith("*") and p.endswith("*") and len(p) > 2:
            runs.append((p[1:-1], False, False, True))
        else:
            runs.append((p, False, False, False))
    return runs or [(str(text), False, False, False)]


def _density_factor(theme):
    return {"airy": 1.06, "standard": 1.0, "dense": 0.92}.get(
        theme.get("density", "standard"), 1.0)


class El(dict):
    """Element dict with defaults filled lazily by renderers."""


def text_el(x, y, w, h, text, role="body", size=20, color="ink", align="left",
            bold=False, italic=False, spacing=None, line=None, font=None,
            valign="top"):
    return El(kind="text", x=x, y=y, w=w, h=h, text=text, role=role,
              size=size, color=color, align=align, bold=bold, italic=italic,
              spacing=spacing, line=line, font=font, valign=valign)


def shape_el(kind, x, y, w, h, fill=None, line_color=None, line_w=1.0, alpha=None,
             radius=None, glass=False, shadow=False):
    el = El(kind=kind, x=x, y=y, w=w, h=h, fill=fill,
            line_color=line_color, line_w=line_w, alpha=alpha)
    if radius is not None:
        el["radius"] = radius
    if glass:
        el["glass"] = True
    if shadow:
        el["shadow"] = True
    return el


def art_el(src, x, y, w, h):
    """Free artwork element (PNG with alpha: rendered orbs, motifs,
    illustrations). Placed exactly; renderers use contain-fit so the
    artwork's own aspect is preserved inside the box."""
    return El(kind="art", x=x, y=y, w=w, h=h, src=src)


def scrim_el(x, y, w, h, color="#041E38", a0=42, a1=4):
    """Soft vertical dark gradient over a photo zone: a0 = alpha (0-100)
    at the top easing to a1 at the bottom. Lifts white caps/serif text
    off bright photography without a visible band edge."""
    return El(kind="scrim", x=x, y=y, w=w, h=h, color=color, a0=a0, a1=a1)


def resolve_color(pal, c):
    """Colors are palette keys, but a literal '#hex' passes through."""
    if c is None:
        return None
    return pal.get(c, c)


def photo_el(src, x=0, y=0, w=STAGE_W, h=STAGE_H):
    return El(kind="image", x=x, y=y, w=w, h=h, src=src)


def gradient_el(th, x=0, y=0, w=STAGE_W, h=STAGE_H):
    g = th.get("gradient") or {}
    return El(kind="gradient", x=x, y=y, w=w, h=h,
              g_from=g.get("from", "#0A2A47"), g_to=g.get("to", "#2E7FC2"),
              g_angle=g.get("angle", 180))


def chrome_elements(s, color, counter_color=None):
    """Sky-glass style chrome: bold caps header top-left + a
    'concept label  NN / TT' counter top-right (replaces the footer)."""
    els = []
    if s.get("header"):
        els.append(text_el(48, 36, 620, 24, s["header"], role="body", size=13,
                           color=color, bold=True, spacing=1.6))
    if s.get("counter"):
        label = s.get("counter_label", "")
        txt = f"{label}  {s['counter']}" if label else s["counter"]
        els.append(text_el(732, 36, 500, 24, txt, role="body", size=13,
                           color=counter_color or color, align="right"))
    return els


# ---------------------------------------------------------------- decor

def decor_elements(theme, idx, total, deck_title):
    """Per-slide chrome: theme decor + footer (page number / deck title)."""
    els = []
    decor = theme.get("decor", "none")
    if decor == "frame":
        els.append(shape_el("rect", 22, 22, STAGE_W - 44, STAGE_H - 44,
                            fill=None, line_color="line", line_w=1.5))
    elif decor == "corner":
        L, T = 34, 10  # arm length, thickness
        for (cx, cy, sx, sy) in [(36, 36, 1, 1), (STAGE_W - 36, STAGE_H - 36, -1, -1)]:
            els.append(shape_el("rect", cx if sx > 0 else cx - L, cy, L, T, fill="accent"))
            els.append(shape_el("rect", cx, cy if sy > 0 else cy - L, T, L, fill="accent"))
    elif decor == "band":
        els.append(shape_el("rect", 0, 0, STAGE_W, 10, fill="accent"))
        els.append(shape_el("rect", 0, STAGE_H - 3, STAGE_W, 3, fill="line"))
    elif decor == "grid":
        for gx in range(160, STAGE_W, 160):
            els.append(shape_el("rect", gx, 0, 1, STAGE_H, fill="line", alpha=35))
        for gy in range(180, STAGE_H, 180):
            els.append(shape_el("rect", 0, gy, STAGE_W, 1, fill="line", alpha=35))
    elif decor == "dots":
        for r in range(3):
            for c in range(5):
                els.append(shape_el("oval", STAGE_W - 150 + c * 26,
                                    STAGE_H - 110 + r * 26, 7, 7, fill="accent2"))
    # footer
    els.append(text_el(72, STAGE_H - 44, 700, 24, deck_title, role="mono",
                       size=11, color="muted", spacing=1.5))
    els.append(text_el(STAGE_W - 172, STAGE_H - 44, 100, 24,
                       f"{idx + 1:02d} / {total:02d}", role="mono", size=11,
                       color="muted", align="right", spacing=1.5))
    return els


# ---------------------------------------------------------------- layouts
# Each builder returns elements for one slide (before decor/footer).

def _pill(els, x, y, label, style, fs):
    """A pill button (light = pale fill/dark text, accent = theme accent)."""
    w = max(120, int(len(label) * 8.6 * fs) + 52)
    if style == "light":
        els.append(shape_el("roundrect", x, y, w, 50, fill="#FFFFFF", radius=13))
        els.append(text_el(x, y, w, 50, label, role="body", size=15.5 * fs,
                           color="#0E2A44", align="center", bold=True,
                           valign="middle"))
    else:
        els.append(shape_el("roundrect", x, y, w, 50, fill="accent", radius=13))
        els.append(text_el(x, y, w, 50, label, role="body", size=15.5 * fs,
                           color="#FFFFFF", align="center", bold=True,
                           valign="middle"))
    return x + w


def lay_cover_split(s, th, fs):
    """Sky-glass cover: photo left (46%) + deep-blue gradient panel right.

    Grammar (from the original's cover): serif headline over the photo,
    one large glass card with caps label + grotesk title + subline, a
    smaller glass chip overlapping its bottom-left; on the gradient side
    a caps kicker, a mixed grotesk/serif headline, muted body and up to
    two pill buttons.
    """
    PW = 588  # photo width (46% of stage)
    els = [photo_el(s.get("photo") or th.get("photo_bg", ""), 0, 0, PW, STAGE_H),
           gradient_el(th, PW, 0, STAGE_W - PW, STAGE_H)]
    if s.get("scrim"):
        sc = s["scrim"] if isinstance(s["scrim"], dict) else {}
        els.insert(1, scrim_el(0, 0, PW, STAGE_H,
                               a0=sc.get("a0", 42), a1=sc.get("a1", 4)))
    els += chrome_elements(s, "#FFFFFF")
    # serif headline over the photo
    els.append(text_el(14, 104, PW - 28, 140, s.get("headline", ""),
                       role="display", size=42 * fs, color="#FFFFFF",
                       align="center", line=1.16))
    # glass shapes first (chip tucked UNDER the card, as in the original),
    # then all texts on top so nothing is ever covered.
    chip = shape_el("roundrect", 36, 452, 252, 128, glass=True, radius=22,
                    shadow=True)
    card = shape_el("roundrect", 190, 292, 336, 300, glass=True, radius=26,
                    shadow=True)
    if s.get("glass_blur") is not None:
        # Per-slide frost override: over a face, the theme's full blur
        # reads as anonymisation; a gentler blur keeps the portrait
        # readable behind the glass, as in the original's cover.
        chip["blur"] = card["blur"] = s["glass_blur"]
    els += [chip, card]
    els.append(text_el(218, 322, 282, 20, s.get("card_label", ""), role="body",
                       size=11.5 * fs, color="#FFFFFF", spacing=2.2))
    els.append(text_el(218, 492, 296, 40, s.get("card_title", ""), role="body",
                       size=28 * fs, color="#FFFFFF", bold=True))
    els.append(text_el(218, 538, 292, 24, s.get("card_sub", ""), role="body",
                       size=14.5 * fs, color="#EAF3FA"))
    els.append(text_el(58, 478, 214, 18, s.get("chip_label", ""), role="body",
                       size=10.5 * fs, color="#FFFFFF", spacing=2.0))
    els.append(text_el(58, 508, 150, 56, s.get("chip_text", ""), role="body",
                       size=16 * fs, color="#FFFFFF", line=1.3))
    # gradient panel content
    X = PW + 52
    els.append(text_el(X, 224, 580, 22, s.get("kicker", ""), role="body",
                       size=12.5 * fs, color="#D7E7F3", spacing=2.6))
    els.append(text_el(X, 258, 584, 226, s.get("title", ""), role="body",
                       size=57 * fs, color="#FFFFFF", bold=True, line=1.1))
    if s.get("body"):
        els.append(text_el(X, 498, 500, 58, s["body"], role="body",
                           size=16.5 * fs, color="#C9DFEF", line=1.45))
    bx = X
    for b in (s.get("buttons") or [])[:2]:
        bx = _pill(els, bx, 578, b.get("label", ""), b.get("style", "light"), fs) + 14
    if s.get("footer_note"):
        els.append(text_el(X, 664, 560, 20, s["footer_note"], role="body",
                           size=11.5 * fs, color="#A9C6DC"))
    return els


def lay_statement(s, th, fs):
    """Light 'concept' slide: near-white ground, caps header + counter,
    optional glass-sphere artwork, centred mixed-type headline, subline,
    one dark pill button, footer note bottom-left."""
    ink, muted = "#10161C", "#5A6B76"
    els = [shape_el("rect", 0, 0, STAGE_W, STAGE_H, fill=s.get("bg_color", "#F4F6F7"))]
    els += chrome_elements(s, ink, counter_color="#3C4A54")
    if s.get("orbs"):
        # Real artwork (v3): up to 7 alpha-PNG orbs placed on a gentle arc.
        arc = [(282, 182, 96), (397, 155, 104), (512, 132, 112),
               (619, 118, 118), (734, 132, 112), (849, 155, 104),
               (956, 182, 96)]
        for (x, y, d), src in zip(arc, s["orbs"][:7]):
            els.append(art_el(src, x, y, d, d))
    elif s.get("spheres"):
        for (x, y, d) in [(404, 122, 118), (578, 88, 152), (756, 122, 118)]:
            els.append(El(kind="glasssphere", x=x, y=y, w=d, h=d))
    els.append(text_el(240, 292, 800, 22, s.get("kicker", ""), role="body",
                       size=12 * fs, color="#3C4A54", align="center", spacing=2.6))
    els.append(text_el(170, 330, 940, 140, s.get("title", ""), role="body",
                       size=56 * fs, color=ink, align="center", bold=True,
                       line=1.12))
    if s.get("subline"):
        els.append(text_el(330, 486, 620, 54, s["subline"], role="body",
                           size=16 * fs, color=muted, align="center", line=1.45))
    if s.get("button"):
        label = s["button"]
        w = max(180, int(len(label) * 8.6 * fs) + 64)
        x = (STAGE_W - w) / 2
        els.append(shape_el("roundrect", x, 566, w, 50, fill="#10161C", radius=13))
        els.append(text_el(x, 566, w, 50, label, role="body", size=15.5 * fs,
                           color="#FFFFFF", align="center", valign="middle"))
    if s.get("footer_note"):
        els.append(text_el(48, 676, 680, 20, s["footer_note"], role="body",
                           size=11.5 * fs, color="#7A8894"))
    return els


def lay_glass_panel(s, th, fs):
    """Full-gradient slide: kicker + mixed headline + body on the left,
    one large glass card with numbered explanation rows on the right."""
    els = [gradient_el(th)] + chrome_elements(s, "#FFFFFF")
    els.append(text_el(72, 148, 560, 22, s.get("kicker", ""), role="body",
                       size=12.5 * fs, color="#C9DFEF", spacing=2.6))
    els.append(text_el(72, 184, 600, 150, s.get("title", ""), role="body",
                       size=52 * fs, color="#FFFFFF", bold=True, line=1.1))
    if s.get("body"):
        els.append(text_el(72, 356, 520, 120, s["body"], role="body",
                           size=17.5 * fs, color="#C9DFEF", line=1.5))
    els.append(shape_el("roundrect", 700, 148, 508, 424, glass=True, radius=24,
                        shadow=True))
    els.append(text_el(736, 184, 436, 20, s.get("card_label", ""), role="body",
                       size=11.5 * fs, color="#FFFFFF", spacing=2.2))
    y = 240
    for i, it in enumerate(s.get("card_items") or []):
        if i:
            els.append(shape_el("rect", 736, y - 22, 436, 1, fill="#FFFFFF", alpha=30))
        els.append(text_el(736, y, 56, 34, it.get("n", ""), role="display",
                           size=24 * fs, color="#FFFFFF", bold=True))
        els.append(text_el(800, y + 2, 372, 84, it.get("text", ""), role="body",
                           size=16.5 * fs, color="#EAF3FA", line=1.4))
        y += 148
    if s.get("footer_note"):
        els.append(text_el(48, 676, 680, 20, s["footer_note"], role="body",
                           size=11.5 * fs, color="#A9C6DC"))
    return els


def lay_cover(s, th, fs):
    if s.get("variant") == "split-glass":
        return lay_cover_split(s, th, fs)
    els = [shape_el("rect", 72, 128, 64, 7, fill="accent")]
    els.append(text_el(72, 152, 1050, 30, s.get("kicker", ""), role="mono",
                       size=15 * fs, color="accent", spacing=3.5))
    els.append(text_el(72, 196, 1100, 210, s.get("title", ""), role="display",
                       size=80 * fs, color="ink", bold=True, line=1.04))
    if s.get("subtitle"):
        els.append(text_el(72, 436, 860, 90, s["subtitle"], role="body",
                           size=23 * fs, color="muted", line=1.35))
    if s.get("meta"):
        els.append(text_el(72, 612, 1000, 26, s["meta"], role="mono",
                           size=13 * fs, color="muted", spacing=2.0))
    return els


def lay_section(s, th, fs):
    els = [text_el(72, 148, 500, 190, s.get("number", ""), role="display",
                   size=170 * fs, color="accent2", bold=True)]
    els.append(shape_el("rect", 76, 348, 88, 6, fill="accent"))
    els.append(text_el(72, 376, 1080, 90, s.get("title", ""), role="display",
                       size=58 * fs, color="ink", bold=True, line=1.08))
    if s.get("lede"):
        els.append(text_el(72, 486, 880, 80, s["lede"], role="body",
                           size=21 * fs, color="muted", line=1.4))
    return els


def _header(s, fs, els):
    els.append(text_el(72, 58, 1136, 54, s.get("title", ""), role="display",
                       size=38 * fs, color="ink", bold=True))
    els.append(shape_el("rect", 72, 122, 56, 5, fill="accent"))
    if s.get("lede"):
        els.append(text_el(72, 140, 1050, 34, s["lede"], role="body",
                           size=19 * fs, color="muted"))
    return 196 if s.get("lede") else 168


def lay_content(s, th, fs):
    els = []
    y = _header(s, fs, els)
    for b in s.get("bullets", []):
        els.append(shape_el("rect", 74, y + 11, 11, 11, fill="accent"))
        els.append(text_el(106, y, 1090, 48, b, role="body", size=21 * fs,
                           color="ink", line=1.3))
        y += 54 * fs
    return els


def lay_two_col(s, th, fs):
    glass = s.get("bg") == "photo"
    els = []
    if glass:
        els.append(photo_el(s.get("photo") or th.get("photo_bg", "")))
        els += chrome_elements(s, "#FFFFFF")
        els.append(text_el(72, 104, 1136, 54, s.get("title", ""), role="display",
                           size=38 * fs, color="#FFFFFF", bold=True))
    else:
        _header(s, fs, els)
    for i, side in enumerate(("left", "right")):
        col = s.get(side) or {}
        x = 72 + i * 572
        if glass:
            els.append(shape_el("roundrect", x, 196, 536, 396, glass=True,
                                radius=22, shadow=True))
            els.append(text_el(x + 34, 232, 470, 40, col.get("heading", ""),
                               role="display", size=24 * fs,
                               color="#FFFFFF", bold=True))
            els.append(text_el(x + 34, 288, 470, 280, col.get("body", ""),
                               role="body", size=19 * fs, color="#EAF3FA",
                               line=1.45))
        else:
            els.append(shape_el("roundrect", x, 180, 536, 430, fill="surface",
                                line_color="line", line_w=1.0))
            els.append(shape_el("rect", x, 180, 536, 6, fill="accent" if i == 0 else "accent2"))
            els.append(text_el(x + 34, 216, 470, 40, col.get("heading", ""),
                               role="display", size=24 * fs,
                               color="accent" if i == 0 else "accent2", bold=True))
            els.append(text_el(x + 34, 272, 470, 320, col.get("body", ""),
                               role="body", size=19 * fs, color="ink", line=1.45))
    return els


def lay_data(s, th, fs):
    glass = s.get("bg") == "photo"
    els = []
    if glass:
        els.append(photo_el(s.get("photo") or th.get("photo_bg", "")))
        els += chrome_elements(s, "#FFFFFF")
        els.append(text_el(72, 104, 1136, 54, s.get("title", ""), role="display",
                           size=38 * fs, color="#FFFFFF", bold=True))
        if s.get("lede"):
            els.append(text_el(72, 166, 1050, 34, s["lede"], role="body",
                               size=19 * fs, color="#EAF3FA"))
        card_y, card_h, take_y = 372, 196, 596
    else:
        _header(s, fs, els)
        card_y, card_h, take_y = 190, 238, 478
    stats = (s.get("stats") or [])[:4]
    if stats:
        gap = 24
        cw = (1136 - gap * (len(stats) - 1)) / len(stats)
        for i, st in enumerate(stats):
            x = 72 + i * (cw + gap)
            if glass:
                els.append(shape_el("roundrect", x, card_y, cw, card_h,
                                    glass=True, radius=20, shadow=True))
                els.append(text_el(x + 22, card_y + 26, cw - 44, 84,
                                   st.get("value", ""), role="display",
                                   size=56 * fs, color="#FFFFFF", bold=True))
                els.append(text_el(x + 22, card_y + 122, cw - 44, 66,
                                   st.get("label", ""), role="mono",
                                   size=14 * fs, color="#EAF3FA",
                                   spacing=1.2, line=1.35))
            else:
                els.append(shape_el("roundrect", x, card_y, cw, card_h, fill="surface",
                                    line_color="line", line_w=1.0))
                els.append(text_el(x + 22, card_y + 36, cw - 44, 84, st.get("value", ""),
                                   role="display", size=56 * fs, color="accent",
                                   bold=True))
                els.append(text_el(x + 22, card_y + 132, cw - 44, 66, st.get("label", ""),
                                   role="mono", size=14 * fs, color="muted",
                                   spacing=1.2, line=1.35))
    if s.get("takeaway"):
        if glass:
            els.append(shape_el("roundrect", 72, take_y, 1136, 84, glass=True,
                                radius=18, shadow=True))
            els.append(text_el(104, take_y, 1072, 84, s["takeaway"], role="body",
                               size=20 * fs, color="#FFFFFF", line=1.35,
                               valign="middle"))
        else:
            els.append(shape_el("roundrect", 72, take_y, 1136, 96, fill="surface",
                                line_color="line", line_w=1.0))
            els.append(shape_el("rect", 72, take_y, 7, 96, fill="accent"))
            els.append(text_el(104, take_y, 1072, 96, s["takeaway"], role="body",
                               size=21 * fs, color="ink", line=1.35, valign="middle"))
    return els


def lay_chart(s, th, fs):
    els = []
    _header(s, fs, els)
    bars = s.get("bars") or []
    base_y, max_h = 548, 300
    if bars:
        vmax = max(float(b.get("value", 0)) for b in bars) or 1
        n = len(bars)
        slot = 1136 / n
        bw = min(110, slot * 0.52)
        for i, b in enumerate(bars):
            v = float(b.get("value", 0))
            bh = max(6, max_h * v / vmax)
            x = 72 + i * slot + (slot - bw) / 2
            els.append(shape_el("rect", x, base_y - bh, bw, bh,
                                fill="accent" if i == n - 1 else "accent2"))
            els.append(text_el(x - 30, base_y - bh - 38, bw + 60, 30,
                               _fmt_num(v), role="display", size=20 * fs,
                               color="ink", align="center", bold=True))
            els.append(text_el(72 + i * slot, base_y + 14, slot, 26,
                               b.get("label", ""), role="mono", size=13 * fs,
                               color="muted", align="center", spacing=0.8))
    els.append(shape_el("rect", 72, base_y, 1136, 2, fill="line"))
    if s.get("takeaway"):
        els.append(text_el(72, 606, 1136, 34, s["takeaway"], role="body",
                           size=18 * fs, color="muted"))
    return els


def _fmt_num(v):
    return str(int(v)) if float(v) == int(v) else f"{v:g}"


def lay_quote(s, th, fs):
    els = [text_el(96, 108, 200, 130, "“", role="display", size=120 * fs,
                   color="accent", bold=True)]
    els.append(text_el(120, 252, 1020, 240, s.get("quote", ""), role="display",
                       size=42 * fs, color="ink", line=1.3, italic=True))
    els.append(shape_el("rect", 122, 512, 64, 5, fill="accent"))
    if s.get("attribution"):
        els.append(text_el(120, 534, 900, 30, s["attribution"], role="mono",
                           size=15 * fs, color="accent", spacing=2.0))
    return els


def lay_image(s, th, fs):
    els = [El(kind="image", x=0, y=0, w=STAGE_W, h=STAGE_H, src=s.get("image", ""))]
    els.append(shape_el("rect", 0, STAGE_H - 208, STAGE_W, 208, fill="bg", alpha=82))
    if s.get("title"):
        els.append(text_el(72, STAGE_H - 168, 1100, 58, s["title"],
                           role="display", size=40 * fs, color="ink", bold=True))
    if s.get("caption"):
        els.append(text_el(72, STAGE_H - 102, 1050, 34, s["caption"],
                           role="body", size=18 * fs, color="muted"))
    return els


def lay_closing(s, th, fs):
    if s.get("bg") == "gradient":
        els = [gradient_el(th)] + chrome_elements(s, "#FFFFFF")
        els.append(shape_el("roundrect", 320, 148, 640, 424, glass=True,
                            radius=28, shadow=True))
        els.append(text_el(380, 208, 520, 130, s.get("title", ""), role="body",
                           size=44 * fs, color="#FFFFFF", align="center",
                           bold=True, line=1.14))
        if s.get("cta"):
            label = s["cta"]
            w = max(220, int(len(label) * 8.6 * fs) + 64)
            x = (STAGE_W - w) / 2
            els.append(shape_el("roundrect", x, 392, w, 56, fill="accent", radius=15))
            els.append(text_el(x, 392, w, 56, label, role="body",
                               size=17 * fs, color="#FFFFFF", align="center",
                               bold=True, valign="middle"))
        if s.get("contact"):
            els.append(text_el(360, 492, 560, 26, s["contact"], role="mono",
                               size=13 * fs, color="#D7E7F3", align="center",
                               spacing=1.6))
        return els
    els = [text_el(140, 208, 1000, 170, s.get("title", ""), role="display",
                   size=62 * fs, color="ink", align="center", bold=True, line=1.12)]
    if s.get("cta"):
        els.append(shape_el("roundrect", 452, 416, 376, 70, fill="accent"))
        els.append(text_el(452, 416, 376, 70, s["cta"], role="body",
                           size=21 * fs, color="bg", align="center", bold=True,
                           valign="middle"))
    if s.get("contact"):
        els.append(text_el(140, 534, 1000, 28, s["contact"], role="mono",
                           size=14 * fs, color="muted", align="center", spacing=1.6))
    return els


def lay_free(s, th, fs):
    """Freeform layout: the spec lists explicit elements (stage px), for
    style decks whose originals use one-off compositions no fixed layout
    covers (poster fields, catalogue spreads). Grammar:

      slide:  {"layout": "free", "bg_color": "#hex|palette-key",
               "elements": [ ... ]}
      element dicts ("t" = type):
        rect|roundrect|oval {x,y,w,h, fill, alpha, line_color, line_w,
                             radius, glass, shadow}
        text   {x,y,w,h, text, role, size, color, align, bold, italic,
                spacing, line, font, valign}   (**bold**, ~serif~,
                *italic* inline markup works as everywhere)
        image  {src, x,y,w,h}   (cover-stretched; pre-crop to box aspect)
        art    {src, x,y,w,h}   (alpha PNG, contain-fit)
        gradient {x,y,w,h, from, to, angle}
        scrim  {x,y,w,h, color, a0, a1}
    Free slides carry their own chrome and skip the default footer.
    """
    els = []
    if s.get("bg_color"):
        els.append(shape_el("rect", 0, 0, STAGE_W, STAGE_H, fill=s["bg_color"]))
    for e in s.get("elements") or []:
        t = e.get("t")
        if t in ("rect", "roundrect", "oval"):
            els.append(shape_el(
                t, e["x"], e["y"], e["w"], e["h"], fill=e.get("fill"),
                line_color=e.get("line_color"), line_w=e.get("line_w", 1.0),
                alpha=e.get("alpha"), radius=e.get("radius"),
                glass=bool(e.get("glass")), shadow=bool(e.get("shadow"))))
        elif t == "text":
            els.append(text_el(
                e["x"], e["y"], e["w"], e["h"], e.get("text", ""),
                role=e.get("role", "body"), size=e.get("size", 20),
                color=e.get("color", "ink"), align=e.get("align", "left"),
                bold=bool(e.get("bold")), italic=bool(e.get("italic")),
                spacing=e.get("spacing"), line=e.get("line"),
                font=e.get("font"), valign=e.get("valign", "top")))
        elif t == "image":
            els.append(photo_el(e["src"], e["x"], e["y"], e["w"], e["h"]))
        elif t == "art":
            els.append(art_el(e["src"], e["x"], e["y"], e["w"], e["h"]))
        elif t == "gradient":
            els.append(El(kind="gradient", x=e["x"], y=e["y"], w=e["w"],
                          h=e["h"], g_from=e.get("from", "#0A2A47"),
                          g_to=e.get("to", "#2E7FC2"),
                          g_angle=e.get("angle", 180)))
        elif t == "scrim":
            els.append(scrim_el(e["x"], e["y"], e["w"], e["h"],
                                color=e.get("color", "#041E38"),
                                a0=e.get("a0", 42), a1=e.get("a1", 4)))
        else:
            raise ValueError(f"free layout: unknown element type {t!r}")
    return els


LAYOUTS = {
    "cover": lay_cover, "section": lay_section, "content": lay_content,
    "two-col": lay_two_col, "data": lay_data, "chart": lay_chart,
    "quote": lay_quote, "image": lay_image, "closing": lay_closing,
    "statement": lay_statement, "glass-panel": lay_glass_panel,
    "free": lay_free,
}


def compile_deck(spec, theme):
    """Return list of slides; each slide = list of elements (content + decor)."""
    fs = _density_factor(theme)
    total = len(spec.get("slides", []))
    out = []
    for i, s in enumerate(spec.get("slides", [])):
        fn = LAYOUTS.get(s.get("layout"))
        if fn is None:
            raise ValueError(f"unknown layout: {s.get('layout')!r} (slide {i + 1})")
        els = fn(s, theme, fs)
        # Generic artwork: a slide may carry "art": [{src, x, y, w, h}]
        # (alpha PNGs). Inserted just before the first text element, so
        # artwork always sits above backgrounds/shapes, below copy.
        if s.get("art"):
            arts = [art_el(a["src"], a["x"], a["y"], a["w"], a["h"])
                    for a in s["art"]]
            idx = next((j for j, e in enumerate(els) if e["kind"] == "text"),
                       len(els))
            els = els[:idx] + arts + els[idx:]
        # Slides that carry their own chrome (full-bleed image, glass/photo/
        # gradient backgrounds, statement & glass-panel layouts, and any
        # slide with an explicit header/counter) skip the default footer.
        bare = (s.get("layout") in ("image", "statement", "glass-panel", "free")
                or s.get("variant") == "split-glass"
                or s.get("bg") in ("photo", "gradient")
                or "header" in s or "counter" in s)
        if not bare:
            els = decor_elements(theme, i, total, spec.get("title", "")) + els
        out.append({"layout": s.get("layout"), "notes": s.get("notes", ""),
                    "elements": els})
    return out
