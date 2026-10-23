---
name: deck-orbital-workshop-deck
description: Style deck "Orbital Workshop" cho hệ deck-studio — Sân vàng quỹ đạo: vòng chấm quỹ đạo, chip mô-đun cam–xanh, năng lượng xưởng vũ trụ. Dùng khi làm deck workshop khoa học/không gian với nền vàng, vòng quỹ đạo chấm và chip mô-đun màu. Theme có sẵn: ~/workspace/deck-studio/themes/orbital-workshop-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Orbital Workshop — Sân vàng quỹ đạo: vòng chấm quỹ đạo, chip mô-đun cam–xanh, năng lượng xưởng vũ trụ

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Orbital Workshop Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/orbital-workshop-deck.json` (bg #FFCE54, nhấn #FF7A33).

## Khi nào dùng
- Workshop STEM, trại khoa học, ngày hội không gian.
- Chương trình khoa học cho học sinh/người trẻ.
- Tổng kết dự án khoa học cộng đồng.

## Nguyên lý cốt lõi
- Mỗi mô-đun là một 'trạm' (station): mục tiêu → thử thách → vật liệu → sản phẩm mang về.
- Khoa học phải đúng: số liệu không gian ghi nguồn (NASA/ESA/tài liệu mở) trong caption.
- Năng lượng cao nhưng hướng dẫn an toàn/thao tác luôn ở chip riêng, chữ rõ nhất trang.

## Hệ hình ảnh
- Nền vàng nắng (golden field) phủ toàn slide.
- Vòng quỹ đạo vẽ bằng chấm (decor dots của engine gợi vòng tròn quỹ đạo) và hành tinh nhỏ ở góc.
- Chip mô-đun bo tròn: cam cho hoạt động, xanh dương cho kiến thức.
- Chữ mực navy đậm; nhãn mono cho mã mô-đun (MOD-01…).
- Trang trí của theme: decor `dots`, bo góc 24px, mật độ standard. Golden orbital field: dotted orbit rings, navy ink, orange/blue module chips; space-workshop energy.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/orbital-workshop-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/orbital-workshop-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `content`/`two-col` theo trạm; mã mô-đun đặt trong kicker.
- Ảnh hoạt động chuẩn bị tông sáng để nổi trên nền vàng.

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
- Deck workshop theo trạm với chip mô-đun nhất quán.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
