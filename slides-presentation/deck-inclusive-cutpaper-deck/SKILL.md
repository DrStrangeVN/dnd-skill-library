---
name: deck-inclusive-cutpaper-deck
description: Style deck "Inclusive Cut-paper" cho hệ deck-studio — Giấy cắt nhiều màu, hình người đa dạng, ngôn ngữ dễ hiểu — deck hòa nhập. Dùng khi làm deck hòa nhập/dễ tiếp cận với hình người cắt giấy đa dạng và ngôn ngữ đơn giản, tương phản cao. Theme có sẵn: ~/workspace/deck-studio/themes/inclusive-cutpaper-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Inclusive Cut-paper — Giấy cắt nhiều màu, hình người đa dạng, ngôn ngữ dễ hiểu — deck hòa nhập

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Inclusive Cutpaper Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/inclusive-cutpaper-deck.json` (bg #FBF4E4, nhấn #12A150).

## Khi nào dùng
- Chương trình hòa nhập, giáo dục đặc biệt, cộng đồng đa dạng.
- Tài liệu hướng dẫn cho nhiều đối tượng đọc khác nhau.
- Workshop về tiếp cận (accessibility) và ngôn ngữ dễ hiểu.

## Nguyên lý cốt lõi
- Ngôn ngữ đơn giản là yêu cầu cứng: câu ngắn, từ phổ thông, một ý một slide.
- Tương phản chữ/nền luôn đạt mức dễ đọc; không đặt chữ lên hình cắt giấy.
- Hình người phải đa dạng thật (tuổi, giới, khả năng) — đa dạng là nội dung, không phải trang trí.

## Hệ hình ảnh
- Nền kem; hình người cắt giấy với nhiều tông da, trang phục màu gốc tươi (đỏ, vàng, xanh dương, xanh lá).
- Hình khối lớn, rõ, không chi tiết nhỏ — đọc được từ xa và với thị lực yếu.
- Chữ grotesk đậm, cỡ lớn; mỗi slide rất ít chữ.
- Chấm tròn màu (confetti dots) trang trí nhẹ quanh hình người.
- Trang trí của theme: decor `dots`, bo góc 18px, mật độ standard. Cream ground, cut-paper people shapes in many skin tones and bright primaries+green; plain-language deck.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/inclusive-cutpaper-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/inclusive-cutpaper-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Hình người chuẩn bị dạng ảnh cắt giấy/flat illustration nền trong hoặc nền kem khớp theme.
- QA bắt buộc thêm một lượt: đọc thử từng slide ở khoảng cách xa (thu nhỏ 50%) để kiểm tra độ rõ.

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
- Deck dễ hiểu, ít chữ, hình người đa dạng dẫn dắt.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
