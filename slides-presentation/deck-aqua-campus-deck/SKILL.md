---
name: deck-aqua-campus-deck
description: Style deck "Aqua Campus" cho hệ deck-studio — Trắng sáng, xanh trời và vàng nắng, chữ tròn nặng — cho chương trình học tập. Dùng khi làm deck chương trình đào tạo/học tập cần tươi sáng, chữ tròn thân thiện, ảnh học viên. Theme có sẵn: ~/workspace/deck-studio/themes/aqua-campus-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Aqua Campus — Trắng sáng, xanh trời và vàng nắng, chữ tròn nặng — cho chương trình học tập

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Aqua Campus Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/aqua-campus-deck.json` (bg #FFFFFF, nhấn #2E9BE6).

## Khi nào dùng
- Người giới thiệu chương trình học mở, khóa học, trại học tập.
- Team muốn ngôn ngữ hình ảnh nhất quán, tươi sáng cho nhiều bài giảng.
- Giảng viên/facilitator có thông điệp và đối tượng học rõ ràng.

## Nguyên lý cốt lõi
- Mỗi trang mở bằng một câu hỏi hoặc một trải nghiệm thực hành — học bằng làm, không thuyết giảng.
- Ảnh người học thật (hoặc minh họa rõ nhãn) chiếm tối thiểu 1/3 số slide.
- Giữ khoảng trắng rộng; mật độ chữ thấp hơn deck doanh nghiệp thông thường.

## Hệ hình ảnh
- Nền trắng thoáng; khối hình học xanh trời (cyan) và vàng nắng cắt góc slide.
- Tiêu đề Baloo 2 tròn, nặng; chân dung cắt tròn là motif lặp lại.
- Lưới chấm (dot grid) xanh nhạt ở góc làm nền trang trí nhẹ.
- Thẻ trắng bo tròn lớn chứa trích dẫn/nguyên tắc, đổ bóng mềm.
- Trang trí của theme: decor `dots`, bo góc 24px, mật độ airy. Sky-cyan fields and yellow geometry on white; circular portraits, dot grids, heavy rounded headings.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/aqua-campus-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/aqua-campus-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `quote` hợp cho thẻ nguyên tắc học tập; `two-col` cho cặp khái niệm–thực hành.
- Ảnh chân dung chuẩn bị dạng vuông, engine cắt full-bleed ở layout `image` — crop 16:9 trước.

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
- Deck chương trình học với nhịp: mở đầu tò mò → trải nghiệm → nguyên tắc → hoạt động tiếp theo.
- HTML studio + PPTX editable kèm notes cho facilitator.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
