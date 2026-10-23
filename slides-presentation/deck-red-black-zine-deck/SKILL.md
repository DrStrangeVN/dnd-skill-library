---
name: deck-red-black-zine-deck
description: Style deck "Red Black Zine" cho hệ deck-studio — Zine ba bề mặt khóa cứng: giấy báo kem, đen tuyền, đỏ poster — nhịp bề mặt là luật. Dùng khi làm deck kiểu zine in độc lập với ba bề mặt kem–đen–đỏ và nhịp xen kẽ bắt buộc. Theme có sẵn: ~/workspace/deck-studio/themes/red-black-zine-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Red Black Zine — Zine ba bề mặt khóa cứng: giấy báo kem, đen tuyền, đỏ poster — nhịp bề mặt là luật

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Red Black Zine Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/red-black-zine-deck.json` (bg #EFE7D3, nhấn #D92323).

## Khi nào dùng
- Zine, tuyên ngôn, ấn phẩm văn hóa độc lập.
- Deck sự kiện underground/âm nhạc/nghệ thuật đường phố.
- Kỷ yếu nhóm sáng tạo có cá tính mạnh.

## Nguyên lý cốt lõi
- Nhịp bề mặt là luật của style: không hai trang cùng bề mặt liên tiếp quá 2 lần; lên lịch bề mặt trước khi viết nội dung.
- Giọng zine: thẳng, có thái độ, câu ngắn. Văn phong thông cáo sẽ phá style ngay.
- Chỉ ba màu mực: đen, kem, đỏ. Màu trong ảnh phải xử lý về gần hệ này.

## Hệ hình ảnh
- Hệ ba bề mặt KHÓA: trang giấy báo kem, trang đen tuyền, trang đỏ poster — không bề mặt thứ tư.
- Trang kem: serif hiển thị + thân bài mono như máy đánh chữ.
- Trang đen: chữ kem/đỏ lớn; trang đỏ: chữ đen/kem như poster dán tường.
- Ảnh xử lý tương phản gắt, hạt in (print grain), cắt cúp không bo góc.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ standard. Locked 3-surface zine: cream newsprint, full black, poster red; serif display with mono body.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/red-black-zine-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/red-black-zine-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Engine dùng một theme/deck: bề mặt đen và đỏ mô phỏng bằng slide `image` toàn khung màu đặc + chữ đặt trong spec, hoặc build 3 biến thể theme và ghép — ghi rõ cách làm trong QA note của deck.
- Validator tự chế: liệt kê chuỗi bề mặt của deck (K-Đ-Đỏ…) và kiểm tra luật nhịp trước khi bàn giao.

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
- Deck zine có bảng nhịp bề mặt kèm theo trong QA note.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
