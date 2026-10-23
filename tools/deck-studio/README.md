# deck-studio — shared slide engine (one engine, many style themes)

deck-studio is the production engine behind the house slide-style skills
(the Skillry-equivalent pack). A **style skill only ships a `theme.json`**
(+ its SKILL.md guidance); this engine turns a deck spec + theme into:

1. **`deck.html`** — a single-file studio deck: 16:9 slides (1280×720 stage,
   auto-scaled), keyboard/click navigation, overview grid (**O**),
   speaker-notes panel (**N**), in-browser text editing (**E** toggles
   `contenteditable`), print stylesheet (one slide per page). Runs offline
   via `file://`; Google Fonts load when online and degrade gracefully.
2. **`.pptx`** — editable PowerPoint, 16:9 (13.333×7.5 in). **All text is
   native text boxes** mirroring the HTML geometry; decorations are native
   shapes; charts are native bars + labels; speaker notes are written to
   the notes slides. Fonts are *named*, not embedded.

Both outputs are compiled from **one geometry model** (`deckkit.py`:
a 1280×720 stage, 9525 EMU/px), so HTML and PPTX never drift apart.

## Quick start

```bash
cd ~/workspace/deck-studio
# studio HTML (system python3, stdlib only)
python3 build_deck.py samples/sample-deck.json themes/test-cobalt-dark.json -o /tmp/deck.html
# editable PPTX (venv python with python-pptx)
~/workspace/tools/deck-venv/bin/python export_pptx.py samples/sample-deck.json \
    themes/test-cobalt-dark.json -o /tmp/deck.pptx
# read-back verification of any export
~/workspace/tools/deck-venv/bin/python verify.py samples/sample-deck.json /tmp/deck.pptx
# slide screenshots (needs node + the video-kit puppeteer-core / Chrome shell)
node screenshot.js /tmp/deck.html /tmp/shots 0,4,5
```

## Deck spec (`deck.json`)

```json
{ "title": "Deck title (footer + <title>)",
  "theme": "<theme-slug>",
  "slides": [ { "layout": "cover", "notes": "speaker notes…", ...fields } ] }
```

| layout    | fields |
|-----------|--------|
| `cover`   | `kicker`, `title` (`\n` = line break), `subtitle`, `meta` |
| `section` | `number`, `title`, `lede` |
| `content` | `title`, `lede` (optional), `bullets[]` |
| `two-col` | `title`, `left{heading, body}`, `right{heading, body}` |
| `data`    | `title`, `stats[{value, label}]` (max 4), `takeaway` |
| `chart`   | `title`, `bars[{label, value}]`, `takeaway` — native bar chart, last bar highlighted |
| `quote`   | `quote`, `attribution` |
| `image`   | `image` (local path relative to the deck.json), `title`, `caption` — full-bleed + overlay band |
| `closing` | `title`, `cta`, `contact` |

Inline emphasis: `**bold**` works in any text field (both renderers).
Every slide may carry `notes`. The footer (deck title + `NN / TT`) is
added automatically except on full-bleed `image` slides.

## Theme (`theme.json`) — how a style skill plugs in

```json
{ "slug": "my-style", "name": "My Style",
  "palette": { "bg": "#0B1226", "surface": "#131C3A", "ink": "#F2F4FA",
               "muted": "#97A1BC", "accent": "#2E5BFF", "accent2": "#7D97FF",
               "line": "#26335F" },
  "fonts":   { "display": "Space Grotesk", "body": "Be Vietnam Pro",
               "mono": "IBM Plex Mono" },
  "radius": 14,
  "decor": "corner",
  "decor_note": "free-text description of the decorative language",
  "density": "standard" }
```

- `palette` — exactly the 7 keys above (hex). `surface` = card/panel fill,
  `line` = hairlines/borders, `accent2` = secondary highlight.
- `fonts` — Google Fonts family names for the roles `display` / `body` /
  `mono`. For Vietnamese decks prefer families with full VN subsets
  (Be Vietnam Pro, Space Grotesk, Playfair Display, IBM Plex Mono…).
- `decor` — one of `none | frame | corner | band | grid | dots`
  (frame = inset border, corner = accent L-corners, band = top accent bar,
  grid = faint graph grid, dots = accent dot cluster).
- `density` — `airy | standard | dense` (scales type/spacing ±6–8%).

**A new style skill = write `theme.json` from the style's visual system,
keep this engine unchanged, run the two commands, screenshot-QA 3 slides,
export + `verify.py` the PPTX.** Two reference themes ship in `themes/`:
`test-cobalt-dark` (dark product deck) and `test-paper-editorial`
(cream editorial) — same sample deck rendered both ways lives in
`samples/<theme>/` (deck.html, demo.pptx, shots/).

## Glass / photo mode (v2, for photographic styles like Sky Glass)

Themes may add three **optional** keys (all 61 existing themes omit them
and render exactly as before):

```json
"glass":    { "fill_alpha": 0.12, "border_alpha": 0.45, "blur_px": 14 },
"gradient": { "from": "#081F33", "to": "#3E84BE", "angle": 180 },
"photo_bg": "assets/sky-main.jpg"
```

- `glass` — how translucent panels render. **HTML:** real glass —
  `rgba(255,255,255,fill_alpha)` fill, 1px white border at
  `border_alpha`, `backdrop-filter: blur(blur_px)`, plus a soft
  `box-shadow` on cover/data/two-col/panel/closing glass. **PPTX
  (v3):** *baked frost* — see "Frosted glass in PPTX" below; the v2
  translucent-fill behaviour remains as the automatic fallback if
  baking fails for a panel.
- `gradient` — deep-panel gradient (`angle` = CSS degrees). HTML uses a
  CSS `linear-gradient`; PPTX pre-renders the gradient to a PNG with
  Pillow and places editable text on top.
- `photo_bg` — default photographic background, resolved relative to the
  deck spec (a slide's own `photo` field wins).

Glass-era layouts & fields:

| layout / variant | fields |
|---|---|
| `cover` + `"variant": "split-glass"` | `photo`, `headline` (serif, over photo), `card_label`, `card_title`, `card_sub`, `chip_label`, `chip_text`, `kicker`, `title` (mixed type), `body`, `buttons[{label, style: light\|accent}]`, `footer_note`, `scrim` (see below), `glass_blur` (per-slide frost override), + chrome below |
| `statement` (light concept slide) | `bg_color` (default `#F4F6F7`), `kicker`, `title`, `subline`, `button`, `orbs: [src, …]` (up to 7 alpha-PNG artworks on a fixed arc — v3; preferred), or legacy `spheres: true` (3 CSS glass spheres; PPTX: translucent ovals — approximation), `footer_note` |
| `glass-panel` (full gradient) | `kicker`, `title`, `body`, `card_label`, `card_items[{n, text}]`, `footer_note` |
| `data` / `two-col` + `"bg": "photo"` | cards become glass panels over the photo (`photo` or theme `photo_bg`) |
| `closing` + `"bg": "gradient"` | gradient ground + centred glass card + CTA pill inside |

Mixed-type headlines: inside any text field, wrap a segment in `~…~`
to set it in the theme's serif (`display`) font, non-bold — e.g.
`"Một góc nhìn\nrõ hơn về\n~thế giới quanh ta.~"`. `**bold**` still
works as before.

Chrome: a slide may carry `header` (bold caps, top-left) and
`counter` + `counter_label` (top-right, e.g. `"02 / 06"` /
`"Khái niệm thực địa"`). Such slides — and all glass/photo/gradient
slides — skip the default footer/decor.

### Art assets (v3)

A slide may place real artwork — images with alpha — via
`"art": [{"src", "x", "y", "w", "h"}]` on any layout (inserted above
backgrounds/shapes, below text), and the `statement` layout takes
`"orbs": [src, …]` for its arc. Both renderers draw the same files
(HTML: `object-fit: contain`; PPTX: native picture), so artwork is
identical across formats. House method for producing orbs: generate
one strip of motifs on a clean ground, then cut each piece with a
fitted circular alpha matte in Pillow (see the Sky Glass v3 demo,
`assets/CREDITS.txt`, for prompts). Always record generated/photo
sources in a `CREDITS.txt` beside the assets.

### Scrim (v3)

The split-glass cover accepts `"scrim": true` (or
`"scrim": {"a0": 42, "a1": 4}`): a vertical dark gradient
(`#041E38`, alpha a0→a1) laid over the photo under the glass zones so
white caps labels and serif headlines stay legible over bright cloud.
HTML renders a CSS gradient; PPTX pre-renders the same gradient to a
PNG. Also a quick fix for any too-bright cover photo: deepen the
photo itself in Pillow (saturation/contrast/blue lift) before use —
the v3 demo's `cover-person.jpg` carries a light grade.

### Frosted glass in PPTX — baked blur (v3)

PowerPoint has no backdrop blur, and a merely translucent fill reads
cheap over photography (the v2 gap). The PPTX exporter therefore
keeps a running Pillow composite of each slide (`SlideCanvas`):
photos, gradients, scrims, art and shapes are composited in element
order; when a glass panel is reached, its fill is *baked* — the
composite region under the panel is cropped, Gaussian-blurred by the
panel's blur (theme `blur_px`, or the element's `blur` override from
a slide's `glass_blur`), saturation-lifted, tinted toward white by
`fill_alpha`, corner-masked, and — for shadowed panels — composited
over a baked soft shadow on a padded transparent canvas. The baked
PNG is placed as a picture; a native no-fill rounded rectangle on
top carries the crisp alpha border, and all text stays native.
Panels bake in order, so an overlapping panel frosts the panel
beneath it, like real glass. If baking throws for a panel, the
exporter falls back to the v2 translucent fill for that panel only.
Verified by rendering the exported PPTX (LibreOffice → PDF → PNG)
and comparing frost inside vs outside panels; see the Sky Glass v3
`QA.md`. An external-engine evaluation (PptxGenJS) and the decision
to stay on python-pptx are recorded in `ENGINE-NOTES.md`.

## Dependencies & fresh-machine setup

- **HTML build:** Python 3.10+ (stdlib only).
- **PPTX export:** `python3 -m venv ~/workspace/tools/deck-venv &&
  ~/workspace/tools/deck-venv/bin/pip install python-pptx Pillow`
  (this machine: `~/workspace/tools/deck-venv`, python-pptx 1.0.2).
- **Screenshots (QA only):** Node 20+, `puppeteer-core`, and a Chrome
  Headless Shell. On this machine both come from the video-kit install —
  paths are constants at the top of `screenshot.js`
  (`.../video-kit/opus55/explainer-kinetic/node_modules/puppeteer-core`,
  `.../video-kit/node_modules/.remotion/chrome-headless-shell/...`).
  Point them elsewhere on another machine.
- **Fonts:** fetched from Google Fonts by the HTML at view time; the PPTX
  only *names* fonts — install the named families on the presenting
  machine for pixel-faithful rendering.

## Files

```
deckkit.py       shared core: spec/theme compile -> element list (single source of truth)
build_deck.py    deck.json + theme.json -> deck.html (studio)
export_pptx.py   deck.json + theme.json -> editable .pptx
verify.py        PPTX read-back checks vs spec
screenshot.js    headless slide screenshots for QA
ENGINE-NOTES.md  external exporter evaluation (PptxGenJS test) + decision
vendor-test/     the PptxGenJS cover test that decision rests on
themes/          theme.json files (2 test themes)
samples/         sample-deck.json (VN, DEMO-labelled) + built outputs per theme
```

## Known limitations

- **PPTX glass is a translucent fill, not a live blur** (see Glass /
  photo mode above). Over a busy photo the HTML (real backdrop blur)
  will look softer than the PPTX; keep glass-panel text short and
  high-contrast.
- No text auto-fit: sizes are fixed per layout; very long titles/bullets
  can overflow their boxes — keep copy within the sample deck's lengths
  and screenshot-QA before shipping.
- `image` layout needs a **local** image file (no remote URLs in PPTX);
  the picture is stretched to full bleed (design/crop at 16:9).
- PPTX parity is geometric, not pixel-perfect: PowerPoint reflows text
  with its own metrics, and the `grid` decor renders at reduced opacity.
- HTML edits made in the studio (E mode) live in the browser only —
  export to PPTX from the spec, not from edited HTML.
