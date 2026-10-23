---
name: deck-learning-loop-deck
description: Style deck "Learning Loop" cho hệ deck-studio — Deck học theo vòng lặp: thẻ bạc hà, mỗi mô-đun kết bằng một hành động. Dùng khi làm deck dạy học theo vòng explain–engage–apply, có bài tập quyết định, phản hồi và cam kết hành động. Theme có sẵn: ~/workspace/deck-studio/themes/learning-loop-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Learning Loop — Deck học theo vòng lặp: thẻ bạc hà, mỗi mô-đun kết bằng một hành động

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Learning Loop Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/learning-loop-deck.json` (bg #F7F7F1, nhấn #1FA98C).

## Khi nào dùng
- Thiết kế khóa học/học phần có thực hành.
- Đào tạo nội bộ cần học viên hành động sau buổi học.
- Workshop kỹ năng có bài tập tình huống.

## Nguyên lý cốt lõi
- Vòng lặp khóa cứng: giải thích (explain) → tương tác (engage) → áp dụng (apply). Thiếu apply là deck chưa xong.
- Có ít nhất một bài tập dạng quyết định (decision practice) và một vòng phản hồi (feedback) trong deck.
- Mở đầu bằng kết quả: người học làm được gì sau buổi này — viết trước nội dung.

## Hệ hình ảnh
- Thẻ bo tròn xanh bạc hà (mint) là đơn vị nội dung; vòng lặp vẽ bằng mũi tên cong đơn giản.
- Chữ mực navy trầm; cam dành cho các điểm 'thực hành/quyết định'.
- Mỗi mô-đun mở bằng kết quả học tập (outcome) viết trên thẻ riêng.
- Bố cục lặp lại y hệt theo mô-đun — sự lặp lại là tính năng sư phạm.
- Trang trí của theme: decor `none`, bo góc 20px, mật độ standard. Loop-structured course deck: mint loop cards, navy ink, orange practice accents; every module ends in an action.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/learning-loop-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/learning-loop-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Mỗi mô-đun = section + cụm content/data; trang apply dùng `content` với bullets là nhiệm vụ đánh số.
- Trang chốt dùng layout `closing`, CTA = cam kết hành động cụ thể của học viên.

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
- Deck học theo mô-đun có vòng lặp đầy đủ và trang cam kết.
- Notes ghi đáp án/phản hồi mẫu cho giảng viên.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
