# Pipeline — HyperFrames + GSAP + ffmpeg

## Project layout
```
~/workspace/<slug>/
  index.html            # composition (template: ~/workspace/skills-video/index.html)
  fonts/                # Be Vietnam Pro subsets (see Font lesson)
  voice_seg*.wav        # narration segments
  music_bed.wav sfx_*.wav
  final_audio.m4a
  renders/  qa/
```

## Font lesson (critical, 2026-10-09; upgraded v2.1)
Google Fonts splits fonts into `latin` / `latin-ext` / `vietnamese` subsets.
The `vietnamese` subset alone has only ~115 glyphs **and lacks basic ASCII**
— using it solo makes the browser silently fall back to system fonts for
normal letters ("font lỗi", phát hiện ở video v1). Fix: **always declare
both subsets with `unicode-range`**. Bundled, pre-verified fonts live in
`assets/fonts/` (Anton, Archivo, Space Grotesk, Plus Jakarta Sans,
Chakra Petch — each in needed weights × latin/vietnamese).
Template projects also carry Be Vietnam Pro subsets.

Pattern per weight:
```css
@font-face{font-family:'Plus Jakarta Sans';font-weight:700;
 src:url('fonts/PlusJakartaSans-700-latin.woff2') format('woff2');
 unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD;}
@font-face{font-family:'Plus Jakarta Sans';font-weight:700;
 src:url('fonts/PlusJakartaSans-700-vietnamese.woff2') format('woff2');
 unicode-range:U+0102-0103,U+0110-0111,U+0128-0129,U+0168-0169,U+01A0-01A1,U+01AF-01B0,U+0300-0301,U+0303-0304,U+0308-0309,U+0323,U+0329,U+1EA0-1EF9,U+20AB;}
```
Verify with fontTools: every character used must exist in the combined cmap.
Before adding any new font: (1) check Google Fonts serves a `vietnamese`
subset (Sora doesn't — rejected); (2) download both subsets; (3) fontTools
cmap check; (4) headless-Chromium screenshot proof with real Vietnamese text.

## Render
```bash
cd ~/workspace/<slug>
TMPDIR=$PWD/tmprender npx hyperframes@0.8.127 check   # before render
TMPDIR=$PWD/tmprender npx hyperframes@0.8.127 render  # ~19 min for 62s
```
- `/tmp` is a 512MB tmpfs — always set TMPDIR to the project dir.
- If the VM is replaced mid-render, the process dies silently: re-run from scratch.
- Never `opacity:0` on `[data-start]` clips (stays invisible); animate inner wrappers.
- `backdrop-filter` crashes headless Chromium — fake glass with gradients.
  Regular `filter: blur()` is safe.
- `page.evaluate(() => timeline.seek(t))` must return string/void, not the timeline.

## Audio mix
```bash
# voice segments at exact offsets -> [voice]; music bed -> sidechain duck under voice
ffmpeg -i seg1.wav ... -filter_complex "
[0:a]adelay=250|250[v0]; ... amix=inputs=N:normalize=0[voice];
[voice]asplit=2[vsc][vmix];
[music][vsc]sidechaincompress=threshold=0.02:ratio=6:attack=20:release=400[ducked];
[ducked][vmix][sfx]amix=inputs=3:normalize=0,alimiter=limit=0.95[aout]"
```
- Music/SFX: synthesize with numpy (pad: detuned sines through lowpass;
  whoosh: filtered noise sweep; click/pop: decaying sine bursts). No copyrighted audio.
- SFX placement: whoosh at scene transitions, tick/pop at card reveals.

## QA checklist (all mandatory)
1. `ffprobe`: 1080x1920, 30fps, h264 + aac, expected duration ±0.5s.
2. Loudness: `ebur128` + `volumedetect`/`astats` — voice clear, peak < 0 dBFS.
3. Screenshots: 8 scenes + 10 midpoints → contact sheet; check Vietnamese
   diacritics, no clipped text, karaoke highlight visible.
4. Glyph check: fontTools cmap over all on-screen text → 0 missing.
5. Karaoke: word timestamps derived from real segment durations.
6. Voice identity: the exact `Nam - Nhật Phong` voice, stated speed applied.

## Deliver
```bash
/opt/hatch/bin/remote-storage upload-file --path renders/<final>.mp4
```
Report: URL + expiry, duration, size, version, changelog, project path,
contact sheet. Upload links expire (~48h); note the expiry.
