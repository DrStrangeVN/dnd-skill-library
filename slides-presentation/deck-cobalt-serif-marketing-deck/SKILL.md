---
name: deck-cobalt-serif-marketing-deck
description: Style deck "Cobalt Serif Marketing" cho hệ deck-studio — Nửa đêm + serif ngà + đường kẻ cobalt mảnh — marketing tĩnh lặng, cao cấp. Dùng khi làm deck marketing/ra mắt sản phẩm cao cấp cần serif sang, nền tối và nhịp thưa như lookbook. Theme có sẵn: ~/workspace/deck-studio/themes/cobalt-serif-marketing-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Cobalt Serif Marketing — Nửa đêm + serif ngà + đường kẻ cobalt mảnh — marketing tĩnh lặng, cao cấp

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Cobalt Serif Marketing Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/cobalt-serif-marketing-deck.json` (bg #101014, nhấn #4453E8).

## Khi nào dùng
- Ra mắt sản phẩm/dịch vụ cao cấp.
- Thư nhà sáng lập, tổng kết năm dạng biên tập.
- Tài liệu định vị thương hiệu premium.

## Nguyên lý cốt lõi
- Thưa là sang: mỗi slide tối đa 1 ảnh + 1 câu + 1 chi tiết hỗ trợ.
- Giọng văn viết như thư, không hô khẩu hiệu; bán bằng sự điềm tĩnh.
- Cobalt chỉ xuất hiện ở đường kẻ và chi tiết nhỏ — diện tích màu luôn dưới 5%.

## Hệ hình ảnh
- Nền đen nửa đêm (midnight); tiêu đề serif ngà cỡ lớn, thưa dòng.
- Đường kẻ (rule) cobalt mảnh chia các khối; số trang/số chương dạng ghost numeral rất nhạt.
- Ảnh sản phẩm như ảnh thời trang: ít, lớn, nhiều khoảng đen quanh.
- Không icon, không pill — typography và ảnh làm toàn bộ công việc.
- Trang trí của theme: decor `none`, bo góc 8px, mật độ airy. Midnight field, ivory serif display, slim cobalt rules and ghost numerals; whisper-quiet marketing deck.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/cobalt-serif-marketing-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/cobalt-serif-marketing-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Ưu tiên layout `image`, `quote`, `section` thưa; tránh `data` dày — khi cần số, trình bày như dòng chữ serif.
- Ảnh chuẩn bị tông tối (dark editorial) để không phá nền midnight.

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
- Deck marketing biên tập thưa chữ, ảnh dẫn dắt.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
