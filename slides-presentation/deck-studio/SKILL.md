---
name: deck-studio
description: Hệ dựng deck thuyết trình của nhà (master/router): một spec JSON + một theme = deck HTML studio (xem/sửa/in) + PPTX sửa được, dùng chung một mô hình hình học nên hai bản không lệch nhau. Dùng khi cần làm slide/PPTX theo một phong cách có sẵn (61 style deck-*), chọn style, hoặc bảo trì engine. Catalogue style: ~/workspace/skillry-slides/SLIDES-INDEX.md. Engine: ~/workspace/deck-studio/.
---

# Deck Studio — Master

Hệ dựng deck gồm: **engine** (`~/workspace/deck-studio/`: `deckkit.py` mô hình hình học dùng chung, `build_deck.py` → HTML, `export_pptx.py` → PPTX, `verify.py`, `screenshot.js`), **61 theme** (`themes/*.json`), **61 skill style** (`deck-*`). Một style = một file theme + một SKILL.md hướng dẫn; hình học do engine lo.

## Khi nào dùng
- Cần làm deck/PPTX có phong cách nhất quán và bản PPTX sửa được → chọn 1 style `deck-*` rồi làm theo skill đó.
- Cần deck gấp chưa rõ style → tra catalogue (dưới), chọn theo "Việc hợp nhất".
- Cần theme mới → tạo thêm 1 file JSON trong `themes/` theo schema, không sửa engine.

## Chọn style
1. Mở catalogue: `~/workspace/skillry-slides/SLIDES-INDEX.md` — 61 dòng: tên skill, phong cách một dòng, việc hợp nhất, file theme.
2. Lọc theo bối cảnh: pitch (cobalt-dark-pitch, lilac-pitch…), biên tập (gallery-catalogue, ochre-editorial, lavender-editorial-team…), dữ liệu (cobalt-system, slate-social-report…), học thuật (academic-argument, research-paper, research-talk…), sự kiện/vui (confetti-gathering, pop-motion, orbital-workshop…), bàn giao sửa lâu dài (editable-visual).
3. Vào skill `deck-<tên>` để lấy nguyên lý + kỹ thuật đặc thù của style đó; file này (master) chỉ lo engine và quy trình chung.

## Định dạng spec (tóm tắt)
File JSON: `{deck_title, slides: [...]}`. Mỗi slide có `layout` + `notes` (speaker notes, hiện trong cả HTML lẫn PPTX). 9 layout:

| Layout | Trường chính |
|---|---|
| cover | kicker, title, subtitle, meta |
| section | number, title, lede |
| content | title, lede, bullets[] |
| two-col | title, left{heading, body}, right{heading, body} |
| data | title, stats[{value, label}] (tối đa 4), takeaway |
| chart | title, bars[{label, value}], takeaway (bar cuối tự highlight) |
| quote | quote, attribution |
| image | image (đường dẫn file local, tương đối so với spec), title, caption |
| closing | title, cta, contact |

- Inline `**bold**` hoạt động ở cả hai renderer.
- Footer (tên deck + số trang) tự thêm, trừ slide `image`.
- Mẫu đầy đủ: `~/workspace/deck-studio/samples/sample-deck.json`.

## Theme (schema)
```json
{"slug": "...", "name": "...",
 "palette": {"bg","surface","ink","muted","accent","accent2","line"},  // hex
 "fonts": {"display","body","mono"},
 "radius": 0-30, "decor": "none|frame|corner|band|grid|dots",
 "density": "airy|standard|dense", "decor_note": "ghi chú tự do"}
```
Font an toàn trên máy này: Be Vietnam Pro, Playfair Display, Space Grotesk, Oswald, Anton, Baloo 2, IBM Plex Mono, Archivo (cảnh báo: Anton/Oswald lỗi dấu nặng tiếng Việt ở khổ lớn — chữ hiển thị lớn tiếng Việt ưu tiên Be Vietnam Pro Black hoặc Archivo/Playfair).

## Lệnh chuẩn
```bash
cd ~/workspace/deck-studio
python3 build_deck.py <deck.json> themes/<style>.json -o <out>/deck.html
~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/<style>.json -o <out>/deck.pptx
~/workspace/tools/deck-venv/bin/python verify.py <deck.json> <out>/deck.pptx
node screenshot.js <out>/deck.html <out>/shots 0,4,5   # chụp slide chỉ định
```
- Python cho export/verify bắt buộc dùng venv `~/workspace/tools/deck-venv` (có python-pptx + Pillow); build HTML dùng python3 thường.
- HTML studio: mở bằng file:// — phím ←/→/Space chuyển slide, **O** overview, **N** notes, **E** sửa chữ trực tiếp, có print stylesheet 1 slide/trang.
- Cài mới trên máy khác: xem `~/workspace/deck-studio/README.md` (venv + python-pptx/Pillow; screenshot cần puppeteer-core + Chrome Headless Shell).

## QA chuẩn cho mọi deck
1. `verify.py` đạt cả 4 kiểm tra (số slide, tiêu đề bìa, mọi slide có text, notes đủ).
2. Screenshot ≥3 slide → contact sheet → đọc bằng mắt: dấu tiếng Việt, tràn chữ (engine KHÔNG có auto-fit), tương phản, khớp vai trò màu của style.
3. Deck quan trọng: đọc lại PPTX bằng python-pptx (đếm slide / text shapes / notes).

## Giới hạn engine (nói thẳng khi bàn giao)
- Không auto-fit: chữ quá dài sẽ tràn — sửa ở spec (rút chữ), không sửa tay file xuất.
- Layout `image`: chỉ file local, kéo phủ đầy 16:9 (chuẩn bị ảnh đúng tỉ lệ trước).
- PPTX khớp hình học với HTML, không pixel-perfect (PowerPoint tự reflow nhẹ).
- Sửa chữ trong studio (E) không chảy ngược về spec — spec là nguồn sự thật duy nhất.
- Style đặc thù vượt engine (bề mặt zine 3 màu, gradient, khung cong một cạnh…) được ghi rõ cách mô phỏng + khác biệt trong SKILL.md của từng style.
