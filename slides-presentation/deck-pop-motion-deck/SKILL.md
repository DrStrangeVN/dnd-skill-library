---
name: deck-pop-motion-deck
description: Style deck "Pop Motion" cho hệ deck-studio — Pop xanh trời, sticker và tia bùng vàng–hồng — năng lượng chiến dịch chuyển động. Dùng khi làm deck chiến dịch/ra mắt cần năng lượng pop, màu trời và điểm bùng nổ như sticker. Theme có sẵn: ~/workspace/deck-studio/themes/pop-motion-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Pop Motion — Pop xanh trời, sticker và tia bùng vàng–hồng — năng lượng chiến dịch chuyển động

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Pop Motion Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/pop-motion-deck.json` (bg #2BB3E6, nhấn #FFC81E).

## Khi nào dùng
- Chiến dịch social/ra mắt sản phẩm cho giới trẻ.
- Deck ý tưởng viral, thử thách, trend.
- Tổng kết chiến dịch cần khoe số liệu tăng trưởng.

## Nguyên lý cốt lõi
- Ba giây đầu quyết định: bìa phải đọc như thumbnail — một câu, một hình, một màu bùng.
- Mỗi slide một thông điệp shareable; câu nào không đăng lên social được thì viết lại.
- CTA xuất hiện ít nhất 2 lần: giữa deck và trang cuối.

## Hệ hình ảnh
- Nền xanh trời (sky) tươi; chấm sticker trắng/màu rải theo nhịp (decor dots).
- Điểm bùng (burst) vàng và hồng ở từ khóa/CTA như sticker dán.
- Chữ Baloo 2 đậm màu mực navy; thẻ trắng bo tròn cực lớn cho nội dung chính.
- Ảnh sản phẩm/người dùng cắt sticker (viền trắng dày) khi có thể.
- Trang trí của theme: decor `dots`, bo góc 26px, mật độ standard. Pop sky-blue field, sticker dots, yellow/pink burst accents; campaign-motion energy in stills.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/pop-motion-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/pop-motion-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `data` cho trang số liệu chiến dịch; thanh cuối highlight = chỉ số bùng nổ nhất.
- Ảnh cắt sticker chuẩn bị trước (viền trắng) để giữ ngôn ngữ.

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
- Deck chiến dịch pop: hook → ý tưởng → cơ chế → số liệu/kỳ vọng → CTA.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
