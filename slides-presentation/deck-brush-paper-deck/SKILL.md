---
name: deck-brush-paper-deck
description: Style deck "Brush Paper" cho hệ deck-studio — Giấy kem, vệt cọ khô ba màu gốc, tranh khắc mảnh — deck thủ công có học. Dùng khi làm deck thủ công trên giấy kem với vệt cọ màu gốc và minh họa khắc mảnh kiểu natural history. Theme có sẵn: ~/workspace/deck-studio/themes/brush-paper-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Brush Paper — Giấy kem, vệt cọ khô ba màu gốc, tranh khắc mảnh — deck thủ công có học

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Brush Paper Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/brush-paper-deck.json` (bg #FBF6E8, nhấn #123FA8).

## Khi nào dùng
- Dự án môi trường sống đô thị, thiên nhiên cộng đồng.
- Deck triển lãm/workshop cần cảm giác làm tay.
- Người sáng tạo có thông điệp rõ và muốn chất liệu giấy–cọ–mực.

## Nguyên lý cốt lõi
- Thủ công nhưng có kỷ luật: vệt cọ xuất hiện theo quy tắc (mở phần = cọ lớn, điểm nhấn = cọ nhỏ), không rải ngẫu nhiên.
- Mỗi slide một hình khắc chính; hình là nội dung khoa học/câu chuyện, không phải hoa văn.
- Ba màu gốc không pha thêm màu thứ tư.

## Hệ hình ảnh
- Nền giấy kem; vệt cọ khô (dry-brush) ba màu gốc: cobalt, đỏ, vàng — là trang trí duy nhất.
- Minh họa khắc đen mảnh kiểu natural-history (chim, cây, côn trùng) đặt trong mảng cọ cobalt.
- Tiêu đề bản gốc là script chảy — bản house dùng Playfair italic cho tiêu đề, giữ thân bài grotesk sạch.
- Đường mực đỏ uốn lượn mảnh nối các khối nội dung như nét bút dẫn mắt.
- Trang trí của theme: decor `dots`, bo góc 10px, mật độ airy. Cream paper, dry-brush primary marks (cobalt/red/yellow), fine black natural-history illustration; script headings approximated by Playfair italic.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/brush-paper-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/brush-paper-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Hình khắc chuẩn bị dạng PNG nền trong hoặc ảnh đã xử lý; layout `image` cho slide trưng bày hình.
- Accent chính của theme là cobalt (màu cọ chủ đạo); đỏ dùng accent2 cho điểm nhấn hiếm.

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
- Deck giấy kem với hệ vệt cọ nhất quán và hình khắc dẫn dắt.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
