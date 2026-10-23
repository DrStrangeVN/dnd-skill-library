---
name: deck-mono-acid-deck
description: Style deck "Mono Acid" cho hệ deck-studio — Đen trắng nghiêm ngặt, một màu acid duy nhất phá vỡ — deck hệ thống tối giản gắt. Dùng khi làm deck đen trắng kỷ luật với đúng một màu acid làm điểm phá, cho manifesto/hệ thống/nguyên tắc. Theme có sẵn: ~/workspace/deck-studio/themes/mono-acid-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Mono Acid — Đen trắng nghiêm ngặt, một màu acid duy nhất phá vỡ — deck hệ thống tối giản gắt

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Mono Acid Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/mono-acid-deck.json` (bg #FAF8F5, nhấn #E4F51E).

## Khi nào dùng
- Manifesto/nguyên tắc thiết kế hoặc vận hành.
- Giới thiệu hệ thống sản phẩm/design system.
- Deck nội bộ cần sự dứt khoát, không trang trí.

## Nguyên lý cốt lõi
- Màu acid là tài nguyên khan hiếm: tối đa 1 phần tử mỗi slide, dành cho điều quan trọng nhất trang đó.
- Hệ thống phải tự giải thích bằng cấu trúc: đánh số, nhãn, lưới — không nhờ màu sắc cứu.
- Câu chữ ngắn, khẳng định, kiểu nguyên tắc (principles) — style này là để tuyên bố cách làm.

## Hệ hình ảnh
- Toàn deck chỉ đen, trắng, xám — cộng đúng một màu acid vàng chanh (acid yellow-green).
- Thẻ bo tròn mềm trên nền trắng/ghi; nhãn mono viết hoa cho mọi metadata.
- Chữ grotesk đen cỡ lớn, căn trái nghiêm ngặt, lưới cột rõ.
- Ảnh (nếu có) bắt buộc đen trắng.
- Trang trí của theme: decor `none`, bo góc 18px, mật độ standard. Black-and-white system broken by a single acid-yellow-green; rounded cards, strict mono labels.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/mono-acid-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/mono-acid-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Kiểm tra màu ở QA: chụp screenshot và rà — bất kỳ màu thứ ba nào ngoài acid đều là lỗi.
- Ảnh chuyển grayscale trước khi build.

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
- Deck manifesto/hệ thống đen trắng với điểm acid có kỷ luật.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
