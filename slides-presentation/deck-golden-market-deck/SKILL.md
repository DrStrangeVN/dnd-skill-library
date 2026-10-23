---
name: deck-golden-market-deck
description: Style deck "Golden Market" cho hệ deck-studio — Kem nắng, dải vàng, điểm teal — deck chợ/thương mại địa phương đầy sức sống. Dùng khi làm deck về chợ/sản phẩm địa phương/thương mại cộng đồng với tông vàng nắng và nhãn kiểu thẻ giá. Theme có sẵn: ~/workspace/deck-studio/themes/golden-market-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Golden Market — Kem nắng, dải vàng, điểm teal — deck chợ/thương mại địa phương đầy sức sống

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Golden Market Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/golden-market-deck.json` (bg #FFF9EE, nhấn #F5A800).

## Khi nào dùng
- Giới thiệu chợ/OCOP/sản phẩm địa phương.
- Chương trình xúc tiến thương mại cộng đồng.
- Pitch gian hàng, hội chợ, tuần lễ sản phẩm.

## Nguyên lý cốt lõi
- Con người của chợ là nhân vật chính: người bán, sản phẩm, câu chuyện — theo thứ tự đó.
- Thông tin thực dụng (giờ, địa điểm, cách mua) có trang riêng rõ ràng, không chôn trong lời kể.
- Giá/số liệu ghi kèm ngày cập nhật; thị trường thay đổi nhanh, số không ngày là số chết.

## Hệ hình ảnh
- Nền kem nắng; dải band vàng chạy chân/trang bìa như mái hiên chợ.
- Nhãn kiểu thẻ giá (price tag): chữ mono trong khung nhỏ gắn vào ảnh/gian hàng.
- Điểm nhấn teal tiết kiệm cho thông tin thực dụng (giờ mở cửa, bản đồ).
- Ảnh gian hàng/người bán bão hòa ấm; tiêu đề grotesk nâu đậm.
- Trang trí của theme: decor `band`, bo góc 14px, mật độ standard. Sun-warm market field: cream ground, golden bands, teal counter-accent; stall photography and price-tag labels.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/golden-market-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/golden-market-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `image` cho trang gian hàng tiêu biểu; `data` cho số liệu thương mại có ngày cập nhật trong takeaway.
- Teal là accent2 — chỉ dùng cho chi tiết thông tin, không dùng cho tiêu đề.

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
- Deck thị trường: mở đầu không khí chợ → người bán/sản phẩm → số liệu → thông tin tham quan/mua bán.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
