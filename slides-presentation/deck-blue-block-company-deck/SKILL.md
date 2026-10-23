---
name: deck-blue-block-company-deck
description: Style deck "Blue Block Company" cho hệ deck-studio — Khung xanh dương đậm, ảnh kiến trúc, số liệu viền đôi — hồ sơ công ty chắc chắn. Dùng khi làm hồ sơ công ty/profile doanh nghiệp cần khung xanh trang trọng, ảnh kiến trúc và trang số liệu rõ. Theme có sẵn: ~/workspace/deck-studio/themes/blue-block-company-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Blue Block Company — Khung xanh dương đậm, ảnh kiến trúc, số liệu viền đôi — hồ sơ công ty chắc chắn

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Blue Block Company Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/blue-block-company-deck.json` (bg #FFFFFF, nhấn #1D4E7E).

## Khi nào dùng
- Giới thiệu công ty và cập nhật cho đối tác/khách hàng.
- Team giải thích dịch vụ và mô hình vận hành.
- Tài liệu đào tạo và chuẩn vận hành dùng chung.

## Nguyên lý cốt lõi
- Cấu trúc hồ sơ cố định: giới thiệu → dịch vụ → mô hình vận hành → số liệu → đội ngũ → liên hệ.
- Số liệu phải là số công ty công bố được; metric nào chưa chốt thì bỏ, không để placeholder số.
- Ảnh kiến trúc/trụ sở thật của công ty ưu tiên tuyệt đối so với ảnh stock.

## Hệ hình ảnh
- Khối xanh dương đậm dạng khung chữ nhật lệch (offset block) ôm ảnh kiến trúc khổ rộng.
- Tiêu đề serif lớn; kicker viết hoa toàn bộ, giãn chữ nhẹ.
- Trang số liệu dùng khung viền đôi (double outline) quanh từng metric.
- Bảng màu chỉ có xanh dương + xám kiến trúc + trắng — không màu thứ ba.
- Trang trí của theme: decor `frame`, bo góc 0px, mật độ standard. Rectangular deep-blue framing blocks offset against architectural photography; all-caps kickers, serif display.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/blue-block-company-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/blue-block-company-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Có sẵn 4 biến thể phối màu trong bản gốc — tương đương ở đây: nhân bản theme, đổi accent theo dải xanh (navy → steel → sky), giữ serif + khung.
- Trang metric dùng layout `data` (tối đa 4 chỉ số); nhiều hơn thì tách hai slide.

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
- Deck hồ sơ ~10 archetype trang: bìa, tổng quan, dịch vụ, mô hình, số liệu, quy trình, đội ngũ, đối tác, chứng nhận, liên hệ.
- PPTX editable cho text + notes; nền/khung phức tạp có thể thành picture.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
