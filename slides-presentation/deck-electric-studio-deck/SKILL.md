---
name: deck-electric-studio-deck
description: Style deck "Electric Studio" cho hệ deck-studio — Tường studio xám sáng, khung panel, cặp tím–cam điện — portfolio/proposal sáng tạo. Dùng khi làm portfolio/proposal studio sáng tạo với khung panel xám và cặp màu tím điện–cam. Theme có sẵn: ~/workspace/deck-studio/themes/electric-studio-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Electric Studio — Tường studio xám sáng, khung panel, cặp tím–cam điện — portfolio/proposal sáng tạo

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Electric Studio Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/electric-studio-deck.json` (bg #ECECEC, nhấn #6C2BD9).

## Khi nào dùng
- Studio/agency trình bày portfolio.
- Proposal dự án sáng tạo cần trông 'có xưởng'.
- Showcase case study cho pitching.

## Nguyên lý cốt lõi
- Mỗi dự án một panel hoàn chỉnh: ảnh + vai trò + kết quả — không tách ảnh và chú thích ra hai slide.
- Tím = hệ thống/studio; cam = kết quả/điểm sáng của dự án. Giữ vai trò màu cố định.
- Giữ xám làm màu chính theo diện tích; tím/cam cộng lại dưới 20% bề mặt.

## Hệ hình ảnh
- Nền xám sáng như tường studio; nội dung nằm trong các panel có khung (frame) rõ.
- Cặp màu điện: tím violet chủ đạo, cam làm tia lửa điểm nhấn.
- Tiêu đề Anton condensed in hoa; thân bài grotesk xám đậm.
- Ảnh dự án đặt trong khung trắng bo góc lớn như khung trưng bày.
- Trang trí của theme: decor `frame`, bo góc 28px, mật độ standard. Light-grey studio wall, framed panels, violet-to-orange electric pairing; condensed display type.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/electric-studio-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/electric-studio-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `two-col` cho trang dự án (ảnh trái, mô tả phải) hoặc `image` cho trang trưng bày toàn khung.
- Style chị em với Neon Makers (cùng hệ khung + Anton) — Neon thiên về nhãn màu giấy, Electric thiên về cặp điện tím–cam.

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
- Deck portfolio có nhịp panel nhất quán và trang tổng kết năng lực.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
