---
name: deck-editable-visual-deck
description: Style deck "Editable Visual" cho hệ deck-studio — Deck 'mọi thứ đều sửa được': nền oải hương xám, lưới mảnh, mọi hình là shape gốc. Dùng khi làm deck mà mọi thành phần phải là shape/text gốc sửa được trong PowerPoint, không khóa thành ảnh. Theme có sẵn: ~/workspace/deck-studio/themes/editable-visual-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Editable Visual — Deck 'mọi thứ đều sửa được': nền oải hương xám, lưới mảnh, mọi hình là shape gốc

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Editable Visual Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/editable-visual-deck.json` (bg #ECEAF4, nhấn #F04E30).

## Khi nào dùng
- Deck bàn giao cho team vận hành tự cập nhật hằng tuần/tháng.
- Template nội bộ dùng lại nhiều lần (báo cáo, onboarding).
- Khách hàng yêu cầu file 'sửa được hết' theo hợp đồng.

## Nguyên lý cốt lõi
- Tiêu chí số một: người nhận mở PPTX và sửa được mọi chữ, mọi khối, mọi màu mà không cần tool khác.
- Không dùng ảnh trang trí không cần thiết; khi bắt buộc dùng ảnh, ghi rõ trong handoff note.
- Font phải là font phổ biến hoặc kèm ghi chú thay thế (fallback) trong handoff.

## Hệ hình ảnh
- Nền oải hương xám nhạt với lưới mô-đun mảnh (grid) — cảm giác như trang artboard.
- Màu tín hiệu đỏ cam cho điểm nhấn và số chính; tím nhạt cho khối phụ.
- Mọi sơ đồ/khung/biểu đồ đều dựng bằng shape đơn giản, không hiệu ứng ảnh.
- Có sẵn 3 phối màu trong bản gốc — ở đây nhân bản theme để đổi (xem Kỹ thuật).
- Trang trí của theme: decor `grid`, bo góc 0px, mật độ standard. Lavender-grey field, fine grid, red-orange signal colour; everything native shapes — editing is the feature.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/editable-visual-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/editable-visual-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Ba preset màu: nhân bản theme JSON, đổi palette (đỏ cam → xanh dương → xanh lá), giữ nguyên lưới + font.
- Sau export, kiểm tra bằng python-pptx: mọi shape phải là text/shape gốc; ảnh chỉ đến từ layout `image`.

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
- Deck + handoff note liệt kê: phần nào editable, phần nào là picture, font đã dùng và phương án thay thế.
- HTML studio chỉ để xem trước; PPTX là sản phẩm chính.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
