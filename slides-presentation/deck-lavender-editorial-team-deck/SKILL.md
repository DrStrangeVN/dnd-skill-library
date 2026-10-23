---
name: deck-lavender-editorial-team-deck
description: Style deck "Lavender Editorial Team" cho hệ deck-studio — Phòng tin oải hương: chân dung halftone, thẻ trích dẫn, nhịp như ấn phẩm in. Dùng khi làm deck giới thiệu đội ngũ/báo cáo nhóm với chân dung halftone và mỗi hồ sơ một thẻ trích dẫn. Theme có sẵn: ~/workspace/deck-studio/themes/lavender-editorial-team-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Lavender Editorial Team — Phòng tin oải hương: chân dung halftone, thẻ trích dẫn, nhịp như ấn phẩm in

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Violet Editorial Team Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/lavender-editorial-team-deck.json` (bg #F4F4F2, nhấn #6D28F5).

## Khi nào dùng
- Hồ sơ đội nhóm gửi đối tác/khách hàng.
- Báo cáo năm của team (team annual).
- Giới thiệu ban tổ chức, diễn giả, mentor.

## Nguyên lý cốt lõi
- Người thật, câu thật: trích dẫn phải là câu người đó đã nói/viết, không bịa lời hay cho nhân vật.
- Mỗi hồ sơ đủ 4 phần: chân dung, vai trò, đóng góp cụ thể, thẻ trích dẫn.
- Giữ nhịp ấn phẩm: độ dài các trang hồ sơ tương đương nhau để không ai bị 'nhẹ' hơn.

## Hệ hình ảnh
- Nền trắng giấy; dấu góc (corner marks) tím oải hương ở các trang hồ sơ.
- Chân dung xử lý halftone đen trắng (chấm in) — motif nhận diện của style.
- Mỗi hồ sơ có đúng một thẻ trích dẫn (quote card): một câu nói thật của người đó.
- Lưới biên tập cứng kiểu báo in: cột đều, hairline xám, kicker mono.
- Trang trí của theme: decor `corner`, bo góc 0px, mật độ standard. Newsroom deck: paper-white ground, violet corner marks, halftone team portraits, one quote card per profile.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/lavender-editorial-team-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/lavender-editorial-team-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Chân dung xử lý halftone trước khi build (grayscale + chấm) để đồng nhất cả đội.
- Trang hồ sơ dùng `two-col` (chân dung–thông tin) và `quote` cho thẻ trích dẫn.

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
- Deck đội nhóm ~10 trang mẫu: bìa, tổng quan team, các hồ sơ, đóng góp chung, liên hệ.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
