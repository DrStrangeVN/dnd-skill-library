# PIL Signal Deck — build your own local dashboard (v1.2.0)

The Signal Deck is the visual front-end for your Personal Instagram Library:
a topic-ring hero over your saved posts, with search → synthesis (The Brief),
a sources rail, a sticky index, and a full archive grid.

**Code is shared, data stays home.** Everything runs from one self-contained
HTML file you build locally. Nothing is uploaded, and the page never phones
home (the only network call it makes is the opt-in "Check for updates" button).

## Prerequisites

- The PIL skill installed and your Instagram saves ingested into a local
  SQLite database (see the repo README).
- Python 3.8+
- Optional: `node` + `npm` (for the QA suite), Pillow (to regenerate icons).

## Build

```bash
cd dashboard
PIL_DB=/path/to/your/pil.sqlite python3 build-signal.py
# writes pil-signal-deck.html (~27MB for ~5k posts)
```

If `PIL_DB` is unset, the builder falls back to
`~/workspace/instagram-kb/instakb.sqlite`.

Open `pil-signal-deck.html` in Chrome or Safari (open the file directly —
the Muse in-app file preview sandbox blocks popups and the install prompt).

## What's in here

| File | Purpose |
|---|---|
| `build-signal.py` | Signal Deck builder. Reads your PIL database, computes the topic graph, emits the self-contained HTML. Version lives in `DASHBOARD_VERSION`. |
| `build.py` | Topic-graph computation shared by the builder (140-node filtered tag graph). |
| `ring-component/pil-ring.js` | Reusable topic-ring component (ECharts-free canvas renderer): themes, hover, click-to-arm rotation, `setMatches()` highlight API. |
| `vendor/echarts.min.js` | Vendored ECharts (Apache-2.0), inlined into the built page. |
| `qa-signal.js` | 127 automated checks (structure, component, full-page jsdom integration). Run with `node qa-signal.js` after `npm install jsdom`. |
| `pil-logo.svg` | Master logo — bookmark mark with PIL, safety orange `#FF5A1F`. |
| `make-logo-pngs.py` | Rasterizes the SVG into PWA/app icons (needs Pillow). |
| `pil-icon-512.png`, `pil-icon-192.png` | PWA icons. |
| `pil-apple-touch-180.png` | iOS home-screen icon. |
| `pil-favicon-32.png`, `pil-favicon-16.png` | Favicons. |

## PWA

The built page ships PWA metadata (manifest via data URI, theme-color,
apple-touch-icon, install button that appears on `beforeinstallprompt`).
A true installable/offline PWA needs HTTPS hosting plus a service worker —
a single downloaded file can't provide that. Host it yourself to get the
full install experience.

## Updates

The deck is stamped with its version (`SIGNAL DECK vX.Y.Z` in the footer).
The **CHECK FOR UPDATES** button compares it against the latest GitHub
release tag — that's the whole update mechanism. A downloaded HTML file
cannot update itself; download the new release's builder and rebuild.

## Privacy

Never commit your built `pil-signal-deck.html`: it contains your private
saved posts. The `.gitignore` in this directory blocks it.
