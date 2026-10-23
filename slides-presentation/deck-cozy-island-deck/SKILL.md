---
name: deck-cozy-island-deck
description: Style deck "Cozy Island" cho hệ deck-studio — Kem ấm, thẻ du lịch bo tròn, biển cyan nắng amber — deck khám phá thư giãn. Dùng khi làm deck du lịch/trải nghiệm ấm áp với thẻ bo tròn, motif bản đồ đảo và nhãn như thẻ hành lý. Theme có sẵn: ~/workspace/deck-studio/themes/cozy-island-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Cozy Island — Kem ấm, thẻ du lịch bo tròn, biển cyan nắng amber — deck khám phá thư giãn

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Cozy Island Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/cozy-island-deck.json` (bg #FBF3DC, nhấn #12B5C9).

## Khi nào dùng
- Giới thiệu tour/trải nghiệm/điểm đến.
- Hành trình retreat, company trip, fam trip.
- Cẩm nang điểm đến cho đối tác bán tour.

## Nguyên lý cốt lõi
- Mỗi thẻ là một điểm dừng; thứ tự thẻ = thứ tự hành trình, không sắp xếp ngẫu nhiên.
- Thông tin thực dụng (giờ, giá, di chuyển) nằm ngay trong thẻ của điểm dừng đó.
- Giọng văn mời gọi nhưng cụ thể — tránh tính từ du lịch sáo rỗng.

## Hệ hình ảnh
- Nền kem ấm; thẻ nội dung bo tròn rất lớn, bóng mềm như thẻ giấy du lịch.
- Hai màu biển–nắng: cyan cho biển/thông tin, amber cho điểm nhấn ấm.
- Motif bản đồ đảo đơn giản và nhãn kiểu luggage tag (thẻ hành lý) cho tên điểm đến.
- Chữ Baloo 2 tròn; ảnh phong cảnh bão hòa vừa, tông ấm.
- Trang trí của theme: decor `none`, bo góc 26px, mật độ airy. Warm cream, rounded travel cards, cyan sea and amber sun; island-map motifs and luggage-tag labels.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/cozy-island-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/cozy-island-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `two-col` cho cặp điểm đến; `image` full-bleed cho trang mở mỗi chặng.
- Ảnh phong cảnh crop 16:9 tông ấm trước khi build.

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
- Deck hành trình theo chặng với thẻ điểm dừng và thông tin thực dụng.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
