---
name: deck-ink-landscape-deck
description: Style deck "Ink Landscape" cho hệ deck-studio — Giấy gạo, tranh mực phong cảnh, một con dấu đỏ — deck như cuốn họa tập. Dùng khi làm deck phong cách thủy mặc: giấy gạo, tranh núi nét mực và các chương đặt tên theo thuật ngữ phong cảnh. Theme có sẵn: ~/workspace/deck-studio/themes/ink-landscape-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Ink Landscape — Giấy gạo, tranh mực phong cảnh, một con dấu đỏ — deck như cuốn họa tập

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Ink Landscape Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/ink-landscape-deck.json` (bg #F5F0E4, nhấn #C8431F).

## Khi nào dùng
- Dự án văn hóa/nghệ thuật lấy cảm hứng Á Đông.
- Hành trình phong cảnh, retreat, triển lãm tranh.
- Thư ngỏ/năm mới dạng họa tập cho đối tác thân thiết.

## Nguyên lý cốt lõi
- Ít chữ như thơ: slide nào cũng viết được thành đoạn văn dài là slide sai style.
- Tranh mực phải là tranh gốc/có licence; tuyệt đối không dùng ảnh phong cảnh stock thay tranh.
- Con dấu đỏ là điểm màu duy nhất ngoài đen–ngà–xám mực.

## Hệ hình ảnh
- Nền giấy gạo (rice paper) ngà; tranh phong cảnh nét mực đen là thành phần chính.
- Đúng một con dấu đỏ (seal) nhỏ mỗi deck — đặt ở bìa hoặc trang kết như triện của họa sĩ.
- Tên các chương mượn thuật ngữ phong cảnh (sơn, thủy, vân, vụ…) thay cho 'Phần 1/2/3'.
- Tiêu đề Space Grotesk mảnh, khoảng cách dòng rộng; chữ ít và thưa.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ airy. Ink-painting deck: rice-paper field, one vermilion seal, mountain/line artwork, chapters named like landscape terms.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/ink-landscape-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/ink-landscape-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `image` và `section` là chủ lực; tên chương đặt trong kicker của section.
- Màu xanh đá (slate) accent2 chỉ dùng cho chú thích nhỏ về địa danh/lộ trình.

## QA bắt buộc (không bỏ qua)
1. `~/workspace/tools/deck-venv/bin/python verify.py <deck.json> <deck.pptx>` — phải đạt: đủ số slide, tiêu đề bìa khớp, mọi slide có text, notes đầy đủ.
2. Chụp ít nhất 3 slide (bìa, một slide data/chart, closing) và ghép contact sheet:
   ```bash
   cd ~/workspace/deck-studio
   node screenshot.js <thư-mục-ra>/deck.html <thư-mục-ra>/shots 0,5,8
   ```
   Đọc sheet bằng mắt: dấu tiếng Việt, tràn chữ, tương phản, đúng vai trò màu của style.
3. Đọc lại PPTX bằng python-pptx (số slide, số text shapes, notes) khi bàn giao deck quan trọng.

## Sản phẩm bàn giao (output contract)
- Deck họa tập: mở cảnh → các chương phong cảnh → trang kết có triện.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
