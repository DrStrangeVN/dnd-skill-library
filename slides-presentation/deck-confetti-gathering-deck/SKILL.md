---
name: deck-confetti-gathering-deck
description: Style deck "Confetti Gathering" cho hệ deck-studio — Poster lễ hội hồng rắc confetti, panel kem để đọc, pill hành động teal/vàng. Dùng khi làm deck sự kiện/ngày hội cộng đồng cần poster hồng vui, confetti và thông tin sự kiện rõ ràng. Theme có sẵn: ~/workspace/deck-studio/themes/confetti-gathering-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Confetti Gathering — Poster lễ hội hồng rắc confetti, panel kem để đọc, pill hành động teal/vàng

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Confetti Gathering Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/confetti-gathering-deck.json` (bg #F8B4C6, nhấn #12A5E8).

## Khi nào dùng
- Ngày hội, sự kiện cộng đồng, buổi gặp gỡ/gathering.
- Chương trình cho gia đình, tình nguyện viên, câu lạc bộ.
- Kickoff hoạt động cần không khí lễ hội.

## Nguyên lý cốt lõi
- Vui nhưng phải trả lời đủ 5W của sự kiện: ai, cái gì, khi nào, ở đâu, tham gia thế nào — thiếu một là deck chưa xong.
- Chữ quan trọng (giờ, địa điểm) luôn nằm trong panel kem, không đặt trực tiếp lên nền hồng rắc confetti.
- Một pill hành động duy nhất mỗi slide.

## Hệ hình ảnh
- Nền hồng poster; confetti là các chấm tròn nhiều màu rải có nhịp (decor dots của engine).
- Panel kem (cream) bo tròn lớn chứa phần chữ cần đọc: lịch trình, địa điểm, lưu ý.
- Pill hành động hai màu: teal cho thông tin, vàng cho kêu gọi (đăng ký/tham gia).
- Tiêu đề Baloo 2 đậm, thân thiện; ảnh sự kiện/người tham gia cắt bo tròn.
- Trang trí của theme: decor `dots`, bo góc 24px, mật độ standard. Pink gathering-poster field with confetti dots; cream reading panels; teal and yellow action pills.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/confetti-gathering-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/confetti-gathering-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `data` cho cụm thông tin (giờ/địa điểm/số người), `closing` cho pill đăng ký.
- Ảnh sự kiện chuẩn bị tông sáng; tránh ảnh tối vì nền hồng sẽ làm ảnh trông bẩn.

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
- Deck sự kiện: bìa poster → điểm nhấn chương trình → lịch trình → địa điểm → đăng ký/CTA.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
