---
name: deck-apricot-doodle-plan-deck
description: Style deck "Apricot Ink Plan" cho hệ deck-studio — Giấy kem, dải cam cháy, nhân vật vẽ mực — cho kế hoạch marketing gần gũi. Dùng khi làm kế hoạch marketing/launch cho doanh nghiệp nhỏ cần cảm giác thủ công, ấm, có hình vẽ mực. Theme có sẵn: ~/workspace/deck-studio/themes/apricot-doodle-plan-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Apricot Ink Plan — Giấy kem, dải cam cháy, nhân vật vẽ mực — cho kế hoạch marketing gần gũi

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Apricot Ink Marketing Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/apricot-doodle-plan-deck.json` (bg #F7F1E6, nhấn #E85D04).

## Khi nào dùng
- Kế hoạch ra mắt cho doanh nghiệp nhỏ/khu dân cư, brand địa phương.
- Trình bày ngân sách marketing và timeline chiến dịch.
- Workshop về khán giả và chiến lược cần không khí thân thiện.

## Nguyên lý cốt lõi
- Ấm nhưng phải có cấu trúc: kế hoạch vẫn đi đúng trình tự khán giả → mục tiêu → ngân sách → lịch ra mắt.
- Một slide một ý; hình vẽ minh họa đúng ý đó, không dùng hình trang trí chung chung.
- Cam chỉ xuất hiện ở dải băng, điểm nhấn và chi tiết trong hình — không tô nền toàn slide.

## Hệ hình ảnh
- Nền giấy kem ấm; dải cam cháy (apricot) chạy ngang đáy hoặc đầu slide như dải băng nhận diện.
- Minh họa nhân vật nét mực đen mảnh, điểm màu cam/nâu; ảnh vẽ là thành phần bắt buộc, không phải trang trí thêm.
- Tiêu đề grotesk đậm cỡ lớn màu mực gần đen; kicker mono viết hoa giãn chữ.
- Khung ảnh/vẽ có bóng đổ cứng lệch (offset shadow) kiểu cắt dán.
- Trang trí của theme: decor `band`, bo góc 4px, mật độ standard. Cream paper with a burnt-orange bottom band; ink-line character illustration carries the warmth, type stays heavy grotesk.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/apricot-doodle-plan-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/apricot-doodle-plan-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Chuẩn bị sẵn bộ hình vẽ mực (hoặc ảnh xử lý nét mực) trước khi viết spec; layout `image` cho slide mở từng phần.
- Theme có sẵn 1 accent cam — khi cần preset phụ, nhân bản theme và đổi accent sang nâu đất, giữ nguyên giấy kem.

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
- Deck kế hoạch ~9 trang mẫu: bìa, khán giả, mục tiêu, ngân sách, timeline, kênh, đo lường, rủi ro, bước tiếp theo.
- Speaker notes ngắn gọn từng trang; PPTX giữ text + notes editable, hình vẽ thành picture.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
