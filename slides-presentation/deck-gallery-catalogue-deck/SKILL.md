---
name: deck-gallery-catalogue-deck
description: Style deck "Gallery Catalogue" cho hệ deck-studio — Catalogue triển lãm: nền trắng, ảnh tĩnh vật, serif, nhãn chú thích như nhãn treo tường. Dùng khi làm catalogue triển lãm/bộ sưu tập với ảnh tĩnh vật lớn và chú thích kiểu nhãn treo tường bảo tàng. Theme có sẵn: ~/workspace/deck-studio/themes/gallery-catalogue-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Gallery Catalogue — Catalogue triển lãm: nền trắng, ảnh tĩnh vật, serif, nhãn chú thích như nhãn treo tường

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Gallery Catalogue Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/gallery-catalogue-deck.json` (bg #FFFFFF, nhấn #D9A404).

## Khi nào dùng
- Catalogue triển lãm/bộ sưu tập nghệ thuật, thủ công, thiết kế.
- Hồ sơ sản phẩm thủ công cao cấp (ceramics, đồ gỗ, trang sức).
- Tài liệu kèm triển lãm để gửi đối tác/báo chí.

## Nguyên lý cốt lõi
- Một trang một tác phẩm; không gộp nhiều tác phẩm nhỏ vào một trang như bảng liên hệ (contact sheet).
- Chú thích tuân đúng định dạng nhãn treo tường, không viết như quảng cáo.
- Thứ tự trang = thứ tự xem triển lãm (curatorial order), không phải thứ tự thời gian tùy tiện.

## Hệ hình ảnh
- Nền trắng gallery; khoảng trắng quanh tác phẩm rộng như phòng triển lãm.
- Ảnh tĩnh vật (still-life) hoặc ảnh tác phẩm khổ lớn, một tác phẩm một trang.
- Chú thích kiểu wall label: tên tác phẩm, chất liệu, năm, một câu giới thiệu — đặt thấp, nhỏ, serif italic cho tên.
- Đường kẻ mảnh màu mù tạt (mustard) và số thứ tự tác phẩm là chi tiết nhận diện duy nhất.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ standard. Gallery catalogue on white: still-life photography, serif display, mustard rules and captions set like wall labels.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/gallery-catalogue-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/gallery-catalogue-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `image` cho trang tác phẩm, caption chứa wall label đầy đủ; trang mở dùng cover với ảnh hero duy nhất.
- Ảnh chuẩn bị nền sáng/trắng; tránh ảnh nền tối phá nhịp gallery.

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
- Catalogue: bìa → lời curator → các trang tác phẩm theo thứ tự xem → thông tin triển lãm/liên hệ.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
