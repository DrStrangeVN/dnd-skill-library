---
name: deck-cobalt-dark-pitch-deck
description: Style deck "Cobalt Ribbon Pitch" cho hệ deck-studio — pitch đen–cobalt: dải ruy-băng kính cobalt phát sáng trên nền đen, panel xanh nhạt chỉ dành cho phần bằng chứng, một slide sáng đảo nền ở cuối. Cấu trúc gốc 8 slide (bìa / vấn đề / bức tranh chung / phương pháp / bằng chứng / mở rộng / đội ngũ / đề nghị). Dùng khi làm pitch sản phẩm/vận hành cần quyết định nhanh, nhịp vấn đề → giải pháp → bằng chứng → ask. Theme: ~/workspace/deck-studio/themes/cobalt-dark-pitch-deck.json. Engine + quy trình: skill deck-studio (master); demo chuẩn: ~/workspace/skillry-slides/demos/cobalt-dark-pitch-deck/ (deck.json + PREVIEW-MAP.md + FIDELITY.md).
---

# Deck Cobalt Ribbon Pitch — Đen–cobalt điện, ribbon kính, bằng chứng xanh nhạt

Style house của deck-studio, chưng cất từ mô tả + preview công khai của skill "Cobalt Ribbon Pitch Deck" (Skillry, gói trả phí) và rà sát lại theo previews ngày 23/10/2026 — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh, cấu trúc và công dụng. Theme: `themes/cobalt-dark-pitch-deck.json` (bg #04060A, accent #2E6BFF, accent2 #A9C6FF).

## Cấu trúc gốc (8 slide — khóa cứng, không dùng spec 9 slide chung)
1. **Bìa** — ribbon full-bleed từ phải, logo góc trái trên, kicker caps, headline grotesk ~90–100px, subtitle 2 dòng. Vùng chữ trái phải nằm trên đen sạch (dùng biến thể ribbon đã làm tối phía trái).
2. **Vấn đề** — headline nhỏ (~35px) + lede trái; hai chỉ số lớn (số trắng, số thứ hai xanh nhạt) trên gạch hairline ở dưới trái; ảnh dọc bên phải ~38%.
3. **Bức tranh chung** — ảnh lớn trái (~43%), headline + lede phải, hai cột mini 01/02 có hairline phía trên.
4. **Phương pháp** — headline + lede CĂN GIỮA trên cùng; một dải ảnh ngang ở giữa; ba thẻ xanh nhạt (#BDD3F8, chữ navy) ở hàng dưới.
5. **Bằng chứng** — panel biểu đồ tối bên trái (cột cuối xanh nhạt #9CC2F7, nhãn giá trị trên cột, footnote số liệu minh họa); headline + ba chỉ số trên hairline bên phải.
6. **Mở rộng** — SLIDE SÁNG duy nhất (nền #EDF2FA): kicker xanh, headline sẫm, ba thẻ — thẻ đầu xanh nhạt chứa số lớn, hai thẻ sau trắng.
7. **Đội ngũ** — headline + lede trái; ba thẻ chân dung cao bên phải, tên đậm + vai trò dưới ảnh.
8. **Đề nghị (ask)** — quay lại ngữ pháp bìa: ribbon, headline lớn là lời đề nghị, một dòng lede, một dòng meta.

## Hệ hình ảnh
- Nền gần đen #04060A; ribbon kính cobalt là motif duy nhất — chuẩn bị 3 biến thể từ 1 artwork: full (bìa/kết), dim ~42% (slide nội dung), left-darkened (bìa/kết, giữ vùng chữ sạch).
- Xanh nhạt chỉ dành cho bằng chứng — không dùng trang trí chỗ khác.
- Chrome: logo (ô vuông cobalt + wordmark caps) góc trái trên mọi slide; KHÔNG footer, KHÔNG số trang.
- Chữ grotesk đậm, tracking chặt, sentence case có dấu chấm cuối headline. Micro-label caps dùng Be Vietnam Pro bold (IBM Plex Mono vỡ dấu tiếng Việt ở cỡ ≤12px khi render headless).
- Ảnh bo góc ~14px: pre-mask alpha bằng Pillow (PPTX không bo góc ảnh được).

## Quy trình
1. Viết spec bằng layout `free` (deckkit): phần tử rect/roundrect/oval/text/image/art/gradient/scrim với tọa độ stage 1280×720 — sao chép deck.json của demo chuẩn rồi thay nội dung. Mọi slide có `notes`; slide 1 field `title` = dòng đầu của headline bìa.
2. Ảnh: sinh artwork/ảnh gốc (không sao chép preview), pre-crop đúng tỉ lệ khung đặt, ghi `assets/CREDITS.txt`.
3. Build + verify + chụp toàn bộ slide:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/cobalt-dark-pitch-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/cobalt-dark-pitch-deck.json -o <thư-mục-ra>/deck.pptx
   ~/workspace/tools/deck-venv/bin/python verify.py <deck.json> <thư-mục-ra>/deck.pptx   # phải ALL PASS
   node screenshot.js <thư-mục-ra>/deck.html <thư-mục-ra>/shots 0,1,2,3,4,5,6,7
   ```
4. Đọc sheet bằng mắt: dấu tiếng Việt, tràn chữ, ribbon có lấn vùng chữ không, slide sáng có đúng là điểm đảo duy nhất không. Đọc lại PPTX bằng python-pptx (số slide / text frames / pictures / notes).

## Giới hạn cần nhớ
- Engine không auto-fit chữ: headline tiếng Việt dài hơn tiếng Anh — giảm cỡ chữ trước, đừng để tràn.
- Thứ tự phần tử trong spec `free` = thứ tự lớp vẽ (cả HTML lẫn PPTX).
- Số liệu trên slide bằng chứng luôn ghi rõ minh họa nếu là số demo.
