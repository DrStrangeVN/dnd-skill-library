---
name: deck-lime-endurance-deck
description: Style deck "Lime Endurance" cho hệ deck-studio — Xanh rừng sâu, chanh tín hiệu, khung ảnh địa hình — deck cho nỗ lực đường dài. Dùng khi làm deck thể thao sức bền/hành trình dài với nền xanh rừng, tín hiệu chanh và ảnh địa hình trong khung. Theme có sẵn: ~/workspace/deck-studio/themes/lime-endurance-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Lime Endurance — Xanh rừng sâu, chanh tín hiệu, khung ảnh địa hình — deck cho nỗ lực đường dài

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Lime Endurance Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/lime-endurance-deck.json` (bg #0E2417, nhấn #CDE94A).

## Khi nào dùng
- Sự kiện endurance: chạy trail, đạp xe đường dài, bơi mở.
- Hành trình expedition nhiều ngày.
- Chương trình huấn luyện sức bền theo chu kỳ.

## Nguyên lý cốt lõi
- Trình bày theo chặng: deck phải đọc như bản đồ hành trình, mỗi phần là một leg có số đo riêng.
- Mọi con số (km, độ cao, thời gian) ghi kèm nguồn đo (GPX, thiết bị, bản đồ) — số endurance sai là nguy hiểm thật.
- Kế hoạch an toàn/tiếp tế có trang riêng, không gộp vào ghi chú.

## Hệ hình ảnh
- Nền xanh rừng sâu (forest); khung viền mảnh (frame) quanh trang như cửa sổ lều trại.
- Chanh (lime) là màu tín hiệu duy nhất cho số quãng đường, mốc thời gian, điểm tiếp tế.
- Ảnh địa hình/tuyến đường đặt trong khung bo tròn rất lớn.
- Chữ trắng grotesk chắc; nhãn mono cho chặng (LEG 01, CP-2…).
- Trang trí của theme: decor `frame`, bo góc 30px, mật độ standard. Deep forest-green field, lime signal colour, framed route/terrain photography; built for long efforts.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/lime-endurance-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/lime-endurance-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `data` cho số liệu chặng (tối đa 4: km, gain, thời gian, điểm tiếp tế).
- Ảnh địa hình tông tối/xanh để hợp nền; ảnh quá sáng sẽ phá nhịp — giảm exposure khi chuẩn bị.

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
- Deck hành trình theo chặng với trang an toàn riêng và số liệu có nguồn.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
