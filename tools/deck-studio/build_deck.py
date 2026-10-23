#!/usr/bin/env python3
"""build_deck.py — deck.json + theme.json -> single-file studio deck.html.

Studio features: keyboard/click navigation, overview grid (O), speaker
notes panel (N), in-browser text editing (E toggles contenteditable),
print stylesheet (one slide per page). Works offline via file://
(Google Fonts degrade gracefully to system fonts).

Usage:
  python3 build_deck.py DECK.json THEME.json [-o deck.html]
Image paths in the spec are copied next to the HTML (assets/) unless
they already resolve relative to the output file.
"""
import argparse
import html
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from deckkit import compile_deck, load_json, parse_runs, resolve_color

FONT_STACKS = {
    "display": '"{f}", "Be Vietnam Pro", "Segoe UI", Arial, sans-serif',
    "body": '"{f}", "Segoe UI", Arial, sans-serif',
    "mono": '"{f}", "SFMono-Regular", Consolas, monospace',
}


def esc(s):
    return html.escape(str(s), quote=True)


def runs_html(text, theme):
    out = []
    serif_fam = FONT_STACKS["display"].format(f=theme["fonts"]["display"]).replace('"', "'")
    for txt, bold, serif, italic in parse_runs(text):
        if serif:
            out.append(f'<span style="font-family:{serif_fam};font-weight:400">'
                       f'{esc(txt)}</span>')
        elif bold and italic:
            out.append(f"<strong><em>{esc(txt)}</em></strong>")
        elif bold:
            out.append(f"<strong>{esc(txt)}</strong>")
        elif italic:
            out.append(f"<em>{esc(txt)}</em>")
        else:
            out.append(esc(txt))
    return "".join(out)


def _rgba(hex_color, alpha):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return f"rgba({r},{g},{b},{alpha:g})"


GLASS_SPHERE_BG = ("radial-gradient(circle at 32% 28%, rgba(255,255,255,.95), "
                   "rgba(190,220,245,.45) 42%, rgba(120,175,220,.30) 68%, "
                   "rgba(255,255,255,.14))")


def el_html(el, theme):
    pal = theme["palette"]
    fonts = theme["fonts"]
    x, y, w, h = el["x"], el["y"], el["w"], el["h"]
    kind = el["kind"]
    if kind == "image":
        return (f'<img class="el img" src="{esc(el["src"])}" '
                f'style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:cover">')
    if kind == "art":
        return (f'<img class="el art" src="{esc(el["src"])}" '
                f'style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;object-fit:contain">')
    if kind == "scrim":
        c = el.get("color", "#041E38")
        style = (f"left:{x}px;top:{y}px;width:{w}px;height:{h}px;"
                 f"background:linear-gradient(180deg, "
                 f"{_rgba(c, el.get('a0', 42) / 100)}, "
                 f"{_rgba(c, el.get('a1', 4) / 100)});")
        return f'<div class="el shape" style="{style}"></div>'
    if kind == "gradient":
        style = (f"left:{x}px;top:{y}px;width:{w}px;height:{h}px;"
                 f"background:linear-gradient({el.get('g_angle', 180)}deg, "
                 f"{el['g_from']}, {el['g_to']});")
        return f'<div class="el shape" style="{style}"></div>'
    if kind == "glasssphere":
        style = (f"left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:50%;"
                 f"background:{GLASS_SPHERE_BG};"
                 f"border:1px solid rgba(255,255,255,.7);"
                 f"box-shadow:inset -12px -14px 28px rgba(90,150,200,.35), "
                 f"inset 8px 10px 18px rgba(255,255,255,.8);"
                 f"backdrop-filter:blur(2px);-webkit-backdrop-filter:blur(2px);")
        return f'<div class="el shape" style="{style}"></div>'
    if kind in ("rect", "roundrect", "oval"):
        rad = "50%" if kind == "oval" else (
            f"{el.get('radius', theme.get('radius', 10))}px" if kind == "roundrect" else "0")
        if el.get("glass"):
            g = theme.get("glass") or {}
            fill_a = g.get("fill_alpha", 0.12)
            border_a = g.get("border_alpha", 0.45)
            blur = el.get("blur", g.get("blur_px", 14))
            base = resolve_color(pal, el["fill"]) if el.get("fill") else "#FFFFFF"
            style = (f"left:{x}px;top:{y}px;width:{w}px;height:{h}px;"
                     f"background:{_rgba(base, fill_a)};"
                     f"border:1px solid {_rgba('#FFFFFF', border_a)};"
                     f"border-radius:{rad};"
                     f"backdrop-filter:blur({blur}px) saturate(1.25);"
                     f"-webkit-backdrop-filter:blur({blur}px) saturate(1.25);")
            if el.get("shadow"):
                style += ("box-shadow:0 16px 38px rgba(6,28,48,.20), "
                          "0 3px 10px rgba(6,28,48,.12);")
            return f'<div class="el shape" style="{style}"></div>'
        fill = resolve_color(pal, el["fill"]) if el.get("fill") else "transparent"
        alpha = el.get("alpha")
        style = f"left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{fill};"
        if alpha is not None:
            style += f"opacity:{alpha / 100:.2f};"
        if el.get("line_color"):
            style += f"border:{el.get('line_w', 1)}px solid {resolve_color(pal, el['line_color'])};"
        style += f"border-radius:{rad};"
        return f'<div class="el shape" style="{style}"></div>'
    # text (single quotes: fam sits inside a double-quoted style attribute)
    fam = FONT_STACKS[el["role"]].format(
        f=fonts[el["font"] or el["role"]]).replace('"', "'")
    style = (f"left:{x}px;top:{y}px;width:{w}px;height:{h}px;"
             f"font-family:{fam};font-size:{el['size']}px;color:{resolve_color(pal, el['color'])};"
             f"text-align:{el['align']};font-weight:{700 if el['bold'] else 400};")
    if el.get("italic"):
        style += "font-style:italic;"
    if el.get("spacing"):
        style += f"letter-spacing:{el['spacing']}px;"
    style += f"line-height:{el.get('line') or 1.25};"
    if el.get("valign") == "middle":
        style += "display:flex;align-items:center;"
        if el["align"] == "center":
            style += "justify-content:center;"
    return (f'<div class="el txt" data-edit style="{style}">'
            f'{runs_html(el["text"], theme)}</div>')


CSS = """
:root{ --bg:{bg}; --surface:{surface}; --ink:{ink}; --muted:{muted};
  --accent:{accent}; --accent2:{accent2}; --line:{line};
  --fd:{fd}; --fb:{fb}; --fm:{fm}; }
*{margin:0;padding:0;box-sizing:border-box}
html,body{height:100%;background:#0a0a0c;font-family:var(--fb);overflow:hidden}
#viewport{position:fixed;inset:0;display:flex;align-items:center;justify-content:center}
#stage{position:relative;width:1280px;height:720px;flex:none;transform-origin:center center}
.slide{position:absolute;inset:0;background:var(--bg);overflow:hidden;display:none}
.slide.active{display:block}
.el{position:absolute}
.txt{white-space:pre-wrap;word-break:break-word;z-index:3}
.shape{z-index:1}
.img{z-index:0}
.art{z-index:2}
body.editing .txt{outline:1px dashed var(--accent);outline-offset:2px;cursor:text}
#hud{position:fixed;left:50%;transform:translateX(-50%);bottom:14px;z-index:50;
  display:flex;gap:8px;align-items:center;background:rgba(12,12,16,.82);color:#e8e8ee;
  padding:7px 12px;border-radius:99px;font:12px var(--fm);backdrop-filter:blur(6px)}
#hud button{background:#23232c;color:#e8e8ee;border:1px solid #3a3a46;border-radius:99px;
  padding:4px 11px;font:12px var(--fm);cursor:pointer}
#hud button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
#progress{position:fixed;top:0;left:0;height:3px;background:var(--accent);z-index:60;transition:width .25s}
#notes{position:fixed;left:0;right:0;bottom:0;z-index:40;background:rgba(10,10,14,.94);
  color:#dcdce4;padding:16px 26px 52px;font-size:15px;line-height:1.55;display:none;
  border-top:2px solid var(--accent);max-height:34vh;overflow:auto;white-space:pre-wrap}
#notes.show{display:block}
#notes b{color:var(--accent);font-family:var(--fm);font-size:11px;letter-spacing:2px;display:block;margin-bottom:6px}
body.overview #stage{transform:none!important}
body.overview #viewport{display:block;overflow:auto;padding:26px}
body.overview .slide{display:block;position:relative;float:left;margin:0 18px 18px 0;
  transform:scale(.243);transform-origin:top left;margin-right:-967px;margin-bottom:-527px;cursor:pointer}
@media print{
  @page{size:13.333in 7.5in;margin:0}
  html,body{background:#fff;overflow:visible}
  #hud,#notes,#progress{display:none!important}
  #viewport{position:static;display:block}
  #stage{transform:none!important;width:1280px;height:auto}
  .slide{display:block!important;position:relative;page-break-after:always;
    width:1280px;height:720px}
}
"""

JS = """
const slides=[...document.querySelectorAll('.slide')];
let cur=0;
const counter=document.getElementById('counter'),notesEl=document.getElementById('notes'),
      notesBody=document.getElementById('notesBody'),prog=document.getElementById('progress');
function show(i){
  cur=Math.max(0,Math.min(slides.length-1,i));
  slides.forEach((s,k)=>s.classList.toggle('active',k===cur));
  counter.textContent=(cur+1)+' / '+slides.length;
  notesBody.textContent=slides[cur].dataset.notes||'(không có ghi chú)';
  prog.style.width=((cur+1)/slides.length*100)+'%';
  if(document.body.classList.contains('overview')) toggleOverview(false);
}
function toggleOverview(force){
  const on=force!==undefined?force:!document.body.classList.contains('overview');
  document.body.classList.toggle('overview',on);
  document.getElementById('btnOverview').classList.toggle('on',on);
}
function fit(){
  if(document.body.classList.contains('overview'))return;
  const s=Math.min(innerWidth/1280,innerHeight/720);
  document.getElementById('stage').style.transform='scale('+s+')';
}
addEventListener('resize',fit);
document.getElementById('btnPrev').onclick=()=>show(cur-1);
document.getElementById('btnNext').onclick=()=>show(cur+1);
document.getElementById('btnOverview').onclick=()=>toggleOverview();
document.getElementById('btnNotes').onclick=e=>{
  notesEl.classList.toggle('show');e.target.classList.toggle('on',notesEl.classList.contains('show'));};
document.getElementById('btnEdit').onclick=e=>{
  const on=document.body.classList.toggle('editing');e.target.classList.toggle('on',on);
  document.querySelectorAll('[data-edit]').forEach(el=>el.contentEditable=on);};
slides.forEach((s,k)=>s.addEventListener('click',()=>{if(document.body.classList.contains('overview'))show(k);}));
addEventListener('keydown',e=>{
  if(document.body.classList.contains('editing')&&e.key!=='Escape')return;
  if(e.key==='ArrowRight'||e.key===' '||e.key==='PageDown')show(cur+1);
  else if(e.key==='ArrowLeft'||e.key==='PageUp')show(cur-1);
  else if(e.key==='Home')show(0); else if(e.key==='End')show(slides.length-1);
  else if(e.key==='o'||e.key==='O')toggleOverview();
  else if(e.key==='n'||e.key==='N')document.getElementById('btnNotes').click();
  else if(e.key==='e'||e.key==='E')document.getElementById('btnEdit').click();
  else if(e.key==='Escape')toggleOverview(false);
});
window.__deck={goto:show,count:slides.length};
fit();show(0);
"""


def _with_z(markup, i):
    """Inline z-index = compile order. The class layer scheme
    (.img 0 / .shape 1 / .art 2 / .txt 3) already matches the order
    deckkit compiles fixed layouts in, so this is a no-op there; the
    `free` layout composes shapes over photos on purpose, and there
    the spec order must win."""
    return markup.replace('style="', f'style="z-index:{i};', 1)


def build(spec, theme):
    slides = compile_deck(spec, theme)
    pal, fonts = theme["palette"], theme["fonts"]
    css = CSS
    for k in ("bg", "surface", "ink", "muted", "accent", "accent2", "line"):
        css = css.replace("{" + k + "}", pal[k])
    css = (css.replace("{fd}", FONT_STACKS["display"].format(f=fonts["display"]))
              .replace("{fb}", FONT_STACKS["body"].format(f=fonts["body"]))
              .replace("{fm}", FONT_STACKS["mono"].format(f=fonts["mono"])))
    fams = sorted(set(fonts.values()))
    gfonts = "&family=".join(f.replace(" ", "+") + ":ital,wght@0,400;0,700;1,400;1,700"
                             for f in fams)
    sections = []
    for sl in slides:
        els = "\n".join(_with_z(el_html(e, theme), i)
                        for i, e in enumerate(sl["elements"]))
        sections.append(
            f'<section class="slide" data-notes="{esc(sl["notes"])}">\n{els}\n</section>')
    return f"""<!DOCTYPE html>
<html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(spec.get('title', 'Deck'))}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family={gfonts}&display=swap" rel="stylesheet">
<style>{css}</style></head>
<body>
<div id="progress"></div>
<div id="viewport"><div id="stage">
{chr(10).join(sections)}
</div></div>
<div id="notes"><b>SPEAKER NOTES</b><span id="notesBody"></span></div>
<div id="hud"><button id="btnPrev">&#8592;</button><span id="counter"></span>
<button id="btnNext">&#8594;</button><button id="btnOverview">Overview (O)</button>
<button id="btnNotes">Notes (N)</button><button id="btnEdit">Edit (E)</button></div>
<script>{JS}</script>
</body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("deck")
    ap.add_argument("theme")
    ap.add_argument("-o", "--out", default="deck.html")
    a = ap.parse_args()
    spec, theme = load_json(a.deck), load_json(a.theme)
    out_dir = os.path.dirname(os.path.abspath(a.out))
    # copy image assets next to the HTML so file:// works
    asset_paths = [theme.get("photo_bg")]
    for s in spec.get("slides", []):
        asset_paths += [s.get("image"), s.get("photo")]
        asset_paths += list(s.get("orbs") or [])
        asset_paths += [a.get("src") for a in (s.get("art") or [])]
    for src in asset_paths:
        if src and not src.startswith(("http://", "https://", "data:")):
            p = src if os.path.isabs(src) else os.path.join(
                os.path.dirname(os.path.abspath(a.deck)), src)
            if os.path.isfile(p):
                dest_dir = os.path.join(out_dir, os.path.dirname(src))
                os.makedirs(dest_dir, exist_ok=True)
                dest = os.path.join(out_dir, src)
                if os.path.abspath(p) != os.path.abspath(dest):
                    shutil.copyfile(p, dest)
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(build(spec, theme))
    print(f"wrote {a.out} ({len(spec.get('slides', []))} slides, theme {theme['slug']})")


if __name__ == "__main__":
    main()
