---
name: deck-sunlit-structure-deck
description: Style deck "Sunlit Structure" cho hệ deck-studio — Panel mù tạt, lưới trắng–graphite, thẻ ảnh vát góc — deck dự án dày dữ kiện. Dùng khi làm deck dự án/đề án không gian với lưới dữ kiện dày, panel vàng mù tạt và ảnh mô hình. Theme có sẵn: ~/workspace/deck-studio/themes/sunlit-structure-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Sunlit Structure — Panel mù tạt, lưới trắng–graphite, thẻ ảnh vát góc — deck dự án dày dữ kiện

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Sunlit Structure Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/sunlit-structure-deck.json` (bg #FFFFFF, nhấn #E3A008).

## Khi nào dùng
- Đề án vườn đô thị/không gian công cộng.
- Báo cáo dự án thiết kế cho chủ đầu tư.
- Hồ sơ tham vấn cộng đồng về không gian sống.

## Nguyên lý cốt lõi
- Dày nhưng phải đọc được: mỗi ô lưới một dữ kiện có nhãn — ô nào cần giải thích dài là ô sai chỗ.
- Ảnh mô hình/phối cảnh luôn kèm trạng thái (concept/sơ bộ/đã duyệt) trong caption.
- Kết deck bằng cam kết tiếp theo có mốc thời gian, như mọi deck dự án nghiêm túc.

## Hệ hình ảnh
- Panel vàng mù tạt (mustard) xen lưới trắng/graphite — nhịp hai chất liệu chạy suốt deck.
- Thẻ ảnh vát góc (chamfered corners) chứa ảnh mô hình/phối cảnh/sơ đồ.
- Tiêu đề serif graphite chắc; nhãn mono viết hoa cho mã khu vực/hạng mục.
- Mật độ cao (dense): bảng dữ kiện, thông số, timeline nằm gọn trong lưới.
- Trang trí của theme: decor `grid`, bo góc 2px, mật độ dense. Mustard panels and white/graphite grids; chamfered photo cards; dense project-data deck.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/sunlit-structure-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/sunlit-structure-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Theme đặt density `dense` — cỡ chữ co theo hệ số của engine; vẫn phải screenshot QA vì chữ dễ tràn ở mật độ này.
- Ảnh vát góc: chuẩn bị ảnh đã vát sẵn (engine bo góc đều); ghi rõ khác biệt ở QA note.

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
- Deck dự án: bối cảnh → phân tích lưới → phương án → số liệu → lộ trình → cam kết.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
