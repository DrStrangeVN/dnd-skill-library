# Style Variants — 3 demo directions (rendered 2026-10-09)

See `assets/style-demos/styles_compare.png` (left→right: A, B, C).
HTML sources: `demoA_tutorial.html`, `demoB_editorial.html`, `demoC_minimal.html`
— open in Chromium at 1080×1920 to preview, all fonts from `assets/fonts/`.

## A — Tutorial (Cường it style)
Best for: how-to, tool walkthroughs, "3 bước" explainers, 30–45s.
- Persistent channel header bar (name left, topic tag right) on every frame.
- Numbered step cards 01/02/03 with colored number badges, stagger in.
- Checklist cards with animated green checkmarks.
- Tag pill clusters (tech stack), progress bars.
- Karaoke highlight: **orange #FF9A3C**.
- Narrative: Hook → Steps (numbered) → Demo/proof → Checklist → CTA/Follow.
- Pacing: fast, 6–10s per scene.

## B — Editorial (Beeknoee style, skill baseline)
Best for: deep dives, repo analysis, data stories, 60–180s.
- Pill scene titles, giant Anton/Archivo heroes, glass stat cards, glowlines.
- Charts, diagrams, stamps, phase-compare cards.
- Karaoke highlight: **yellow #FFC531**.
- Narrative: 8-beat arc in `narrative.md`.

## C — Minimal Premium (think-piece)
Best for: verdicts, opinion pieces, "sư tử thật hay gầm to?" angles.
- Generous whitespace, eyebrow labels (letterspaced), huge Anton hero,
  thin accent rule, muted sub copy.
- Caption style: keyword inside rounded highlight chip (not plain color).
- No progress bar noise; quiet meta line ("AI 60 GIÂY — REPO RADAR").
- Narrative: Question → Tension (one killer stat) → Verdict.

## D — Analyst (Kiến Thức Số style)
Best for: repo/data analysis with authority, 55–100s.
- Section-tracking nav bar: channel name left, CURRENT SECTION right
  (MỞ ĐẦU → GITHUB REPO → CHỈ SỐ → PHÒNG BAN → … → KẾT LUẬN). Strong retention device.
- Teal-dominant palette (#2DD4BF) instead of orange; dark navy-teal gradient bg.
- Punchline captions: 2–4 word phrases, red #FF3B5C or yellow-box keyword
  ("NGHÌN LƯỢT FORK.", "TẠO. ARTCRAFT") — not word-by-word karaoke.
- Diagram-heavy: radial org charts, labeled flow nodes with arrows,
  isometric layer cubes, refined GitHub repo cards (name, stars, file tree).
- Stat grids 2×2 with teal numbers.
- Demo: `assets/style-demos/demoD_analyst.html` / `.png`.
| Content | Variant |
|---|---|
| Hướng dẫn tool, steps | A |
| Phân tích repo/số liệu, drama | B |
| Góc nhìn, verdict, opinion | C |
| Phân tích repo kiểu analyst, số liệu uy tín | D |
| Tin AI nhanh, sub 1 dòng kiểu escbase | E |

## E — Punchline (escbase style, 2026-10-10)
Best for: tin AI nhanh 60–120s, một ý tưởng/scene, cần gọn nhẹ dễ xem.
Chọn E khi nội dung là tin nhanh/khám phá tool — không phải mặc định cho mọi video.
Học từ video đối thủ @escbase (115s, 1080×1920/30fps — phân tích frame 2026-10-10):
- **Sub tối đa 1 dòng** (2 dòng chỉ khi bất khả kháng): punchline 6–10 từ/dòng,
  KHÔNG karaoke nguyên câu dài. Vị trí ~70% chiều cao màn hình.
- Keyword highlight **đỏ #FF3B5C** cho từ đang đọc; từ đã đọc trắng, từ sắp đọc xám.
- Section pill top-center mỗi scene: icon + label ngắn ("Một câu lệnh", "Ví dụ: code review"),
  nền kính tối — thay cho pill title trượt từ trái.
- Một ý tưởng/scene, bố cục giữa màn hình, nhiều khoảng thở (nền tối + particles).
- Progress bar gradient ở mép trên; watermark logo + handle 2 góc (trên-trái, dưới-phải).
- Intro: icon card (rounded square kính) + tag pill + title gradient cực lớn + value pill
  ("1 câu lệnh → team agent").
- Caption highlight color is a per-video parameter: A=orange, B=yellow, C=chip, D=punchline (red/yellow keyword), E=red keyword on 1-line punchline.
- Kỹ thuật bổ sung từ video @escbase thứ hai (AIHawk, 150s — phân tích 2026-10-10):
  stat constellation (logo trung tâm + pills số liệu bay quanh + vòng orbit),
  headline keyword gradient (peach→teal), visual strikethrough chuyển đổi
  (cũ gạch ngang → mới), mockup UI thật (GitHub repo header), warning pill đỏ,
  social-proof strip (stars/forks/stack). Video dài 150s vẫn giữ retention nhờ
  mỗi scene một ý tưởng + mật độ visual cao.
Max 3 font families per video (see font system v2.1 in style-system.md).
