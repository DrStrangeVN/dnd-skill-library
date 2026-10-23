# Style System v2.3 — distilled from 4 Beeknoee + 2 Cường it + 2 Kiến Thức Số (2026-10-09)

Reference analyses: `/tmp/fb_sample/` (Paperclip 94.7K) + `/tmp/fb_new/`
(3 videos: Agent Reach 93K★, Impeccable 78K★, Brigade 11K★) + `/tmp/fb_comp/`
(2 Cường it tutorial reels) + `/tmp/fb_comp2/` (2 Kiến Thức Số analyst reels,
one at 32K views). Learn pacing, edit density, visual hierarchy,
layout — never copy copyrighted assets.
Four renderable variants: see `style-variants.md` + `assets/style-demos/`.

## Canvas
- 1080x1920 vertical. Dark navy/black gradient + ambient particles/stars
  drifting continuously + faint blueprint grid. Two parallax layers, different rates.

## Typography — font system v2.1 (đã verify 0 lỗi tiếng Việt)
Font bundle sẵn tại `assets/fonts/` (mỗi font gồm 2 subset `latin` +
`vietnamese`, dùng kèm `unicode-range` — xem `pipeline.md`). Tất cả đã
verify bằng fontTools + render thử headless Chromium: dấu Ư/Ơ/Ă/Â/Đ chuẩn,
không tofu, không fallback.

| Vai trò | Font | Dùng cho |
|---|---|---|
| Display | **Anton** (400) | Hero 1-3 từ, poster condensed: "SƯ TỬ THẬT" |
| Display alt | **Archivo** (800) | Hero grotesque đậm: "NHANH CHƯA CHẮC ĐÚNG." |
| Tech label | **Space Grotesk** (500/700) | Kicker, stat numbers, eyebrow labels |
| Tech alt | **Chakra Petch** (600/700) | Terminal, command chips, cảnh báo kỹ thuật |
| Body | **Plus Jakarta Sans** (500/600/700/800) | Captions karaoke, card body — premium, tròn đầy |
| Body VN-first | Be Vietnam Pro (400-900) | Dự phòng khi cần nét Việt truyền thống |

Quy tắc phối: 1 video dùng tối đa **3 họ font** (Display + Tech + Body).
Caption karaoke: Plus Jakarta Sans 600, 42-58px; màu highlight từ đang đọc
là tham số theo variant — vàng #FFC531 (Editorial) hoặc cam #FF9A3C
(Tutorial). Không dùng font không có vietnamese subset (vd Sora) —
sẽ dính lỗi fallback như bài học v1.

## Color semantics
- Orange/amber: money, warnings, heat, CTA.
- Teal/green: positive, OK, "system" states. **Teal-dominant theme** (variant D):
  teal becomes the primary accent over dark navy-teal gradient.
- Red: danger, alerts, "R.I.P" moments; also punchline keyword (variant D).
- Purple/blue: info, mystery, "secret" beats.
- Yellow: keyword highlight inside captions (variant B); yellow-box punchlines (D).

## Scene archetypes (each scene = 1 idea, 8-15s)
1. **Hero statement** — giant display type + floating icon.
2. **Pill title + stat cards** — pill slides from left (+ slight blur);
   cards slide from right, stagger 0.15-0.3s.
3. **Data cards** — stat pills ($215/tháng, 403, 77,8K★), terminal windows,
   progress bars, checklist pills, comparison rows.
4. **Diagrams** — network graph (nodes around a central eye), org chart
   (You → Ledger/Audit/Research/Ops), flowcharts with arrows.
5. **Phase compare** — two side-by-side cards (PHE 1 vs PHE 2), color-coded.
6. **Stamps/badges** — rotated warning stamps ("KHÓA NICK", "CẢNH BÁO"),
   "R.I.P" cards, "GỐC #1" tags. Pop-in with back.out.
7. **Charts** — star-history line chart, growth bars; animate stroke/draw.
8. **Quote card** — Hacker News / tweet style quote.
9. **Chat mock** — chat bubbles for dialogue beats.
10. **Command chip** — `$ command --flag` mono chip, typing effect.
11. **Verdict** — verdict pill + 3 takeaway chips + repo/source CTA.

## Tutorial archetypes (Cường it style — variant A)
12. **Channel header bar** — persistent top bar: channel name left, topic tag
    right (pill). Present on every frame of tutorial videos.
13. **Numbered step cards** — 01/02/03 with colored number badges
    (orange/teal/purple), title + one-line description; stagger in.
14. **Checklist card** — rows with animated green checkmarks drawing in
    (stroke-dashoffset), one row per beat.
15. **Tag pill cluster** — tech-stack pills (Claude Code, Codex, Cursor…),
    color-coded, wrap to 2 rows max.
16. **Browser mockup** — window frame (traffic lights, URL bar) containing
    app UI screenshot/illustration; subtle screen-tilt on entry.
17. **Progress bar card** — labeled bar (e.g. "Ngân sách theo tháng") with
    gradient fill animating width.
18. **Hand-drawn illustration card** — cream/beige card with sketch-style
    illustration; warm human contrast to dark bg.
19. **Social end card** — Follow / Like / Save button row + repo URL.

## Analyst archetypes (Kiến Thức Số style — variant D)
20. **Section nav bar** — persistent top bar: channel name left, CURRENT
    SECTION right (MỞ ĐẦU → REPO → CHỈ SỐ → … → KẾT LUẬN). Update the section
    label per scene; viewers always know where they are (retention device).
21. **Punchline caption** — 2–4 word phrases, red #FF3B5C or yellow-box
    keyword ("NGHÌN LƯỢT FORK.", "TẠO. ARTCRAFT"). Replaces word-by-word
    karaoke in variant D; punchier, less cluttered.
22. **Radial org chart** — center node with satellite nodes + connecting lines;
    satellites pop in with stagger.
23. **Labeled flow nodes** — boxes with arrows between them, each node labeled
    (e.g. THAM CHIẾU 2D → KHÔNG GIAN 3D); arrows draw via stroke animation.
24. **Isometric layer cube** — stacked layers (ẢNH / VIDEO / CẢNH 3D), subtle
    3D tilt, layers separate on entry.
25. **Repo card (refined)** — dark card: repo name, star count, file tree
    (mono, indented), license pill.

## Caption modes (per-video parameter)
- **Karaoke** (A/B/C): full sentence, word-by-word highlight (orange/yellow/chip).
- **Punchline** (D): 2–4 word phrase per scene, red or yellow-box keyword.
  Choose per variant; never mix both in one video.

## Motion vocabulary (HyperFrames + GSAP)
- Pill: x -600 → 0 + blur(8px)→0, 0.45s power3.out.
- Cards: x +600 → 0 stagger, blur dissolve on scene change
  (out: blur 12-22px + scale 0.94-1.1, 0.3-0.35s; in: blur 22px → 0).
- Camera push: every scene entry, scale 1.07 → 1, 0.55s.
- Masking wipe: clip-path inset wipe on 1-2 transitions per video.
- Numbers: count-up power2.out. Words: stagger rise. CTA: scale pop back.out(1.6).
- Typing: per-char stagger 0.03-0.05s. Floating micro-icons: y ±16 yoyo.
- Glowlines: 3px gradient strokes, scaleX 0→1 under heroes.
- Progress bar: bottom, scaleX 0→1 across full duration.
- No flash/glitch abuse; motion follows voice rhythm.

## Pacing
- Deep dives: 150-180s, scene per idea. Short explainers: 60-70s.
- Tutorials: 30-45s, 6-10s per scene, denser cuts.
- Karaoke captions run through the whole video, never static slides.

## Narrative arcs
- **Editorial deep-dive** (variant B, see narrative.md):
  Hook → Pain → Data proof → Community hype → Hidden cost →
  Two-sided clash → Verdict → Source/repo CTA.
- **Tutorial** (variant A):
  Hook (result promise) → Steps 01-N (numbered cards) → Demo/proof
  (browser mockup) → Checklist recap → CTA (Follow + repo).
- **Think-piece** (variant C):
  Provocative question → One killer stat (tension) → Verdict.
