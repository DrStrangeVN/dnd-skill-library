---
name: deck-neon-makers-deck
description: Style deck "Neon Makers" cho hệ deck-studio — Poster hội chợ maker: khung panel, nhãn neon tím–cam, chữ condensed. Dùng khi làm deck sự kiện maker/hội chợ STEM với khung panel và nhãn màu neon như poster dán tường. Theme có sẵn: ~/workspace/deck-studio/themes/neon-makers-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Neon Makers — Poster hội chợ maker: khung panel, nhãn neon tím–cam, chữ condensed

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Neon Makers Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/neon-makers-deck.json` (bg #EFEDEA, nhấn #7B3FE4).

## Khi nào dùng
- Hội chợ maker, ngày hội STEM trường học.
- Chương trình chế tạo/xưởng mở cho cộng đồng.
- Tổng kết trại hè sáng chế.

## Nguyên lý cốt lõi
- Mỗi hoạt động một panel đầy đủ: làm gì, ai hướng dẫn, cần mang gì, ra sản phẩm gì.
- Thông tin an toàn/dụng cụ có panel riêng màu cam — nhìn thấy từ xa.
- Nhịp poster: trang bìa phải đọc được từ khoảng cách 3 mét (chữ lớn, ít chữ).

## Hệ hình ảnh
- Các panel có khung rõ trên nền ghi sáng như poster hội chợ.
- Nhãn màu neon: tím cho chương trình, cam cho hoạt động/điểm nóng.
- Tiêu đề Anton condensed in hoa; thẻ ảnh bo tròn lớn ở góc.
- Chi tiết kỹ thuật nhỏ (mono) rải như ghi chú trên bản vẽ chế tạo.
- Trang trí của theme: decor `frame`, bo góc 28px, mật độ standard. Maker fair poster system: framed panels, neon label colours (violet/orange), condensed display, photo cards.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/neon-makers-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/neon-makers-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Trang hoạt động dùng `two-col` (mô tả–dụng cụ/sản phẩm); bìa dùng cover với tiêu đề rút tối đa 4–5 từ.
- Style chị em với Electric Studio — khác ở nhãn giấy neon và tinh thần poster dán tường.

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
- Deck sự kiện maker: bìa poster → hoạt động → an toàn → lịch → đăng ký.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
