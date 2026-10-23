---
name: deck-research-talk-deck
description: Style deck "Research Talk (Beamer-style)" cho hệ deck-studio — Bài nói nghiên cứu kiểu Beamer: dải phân đoạn teal, thanh tiến trình, mỗi trang một thông điệp. Dùng khi làm bài nói học thuật kiểu Beamer/metropolis: một thông điệp mỗi trang, có thanh tiến trình và công thức kèm cách đọc thường. Theme có sẵn: ~/workspace/deck-studio/themes/research-talk-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Research Talk (Beamer-style) — Bài nói nghiên cứu kiểu Beamer: dải phân đoạn teal, thanh tiến trình, mỗi trang một thông điệp

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Research Talk Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/research-talk-deck.json` (bg #0A6B5E, nhấn #F5A623).

## Khi nào dùng
- Talk hội thảo học thuật có giới hạn phút nghiêm ngặt.
- Bài giảng nghiên cứu cho sinh viên sau đại học.
- Báo cáo tiến độ đề tài trước hội đồng.

## Nguyên lý cốt lõi
- Một trang một thông điệp — thông điệp viết thành tiêu đề đầy đủ.
- Công thức không bao giờ đứng một mình: luôn có dòng đọc thường và một ví dụ số.
- Nhịp talk phải khớp thời gian: ghi thời lượng dự kiến cho từng phần trong notes.

## Hệ hình ảnh
- Dải band teal ở các trang phân đoạn (section) và đầu trang nội dung chính.
- Thanh tiến trình (progress) + số trang hiện diện xuyên suốt như Beamer thật.
- Phương trình/công thức luôn đi kèm một dòng 'đọc là:' bằng ngôn ngữ thường.
- Chữ grotesk trắng trên teal ở trang section; trang nội dung nền sáng biến thể qua nhân bản theme (xem Kỹ thuật).
- Trang trí của theme: decor `band`, bo góc 0px, mật độ standard. Beamer/metropolis homage: teal section bands, progress bar, page numbers, equations with plain readings.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/research-talk-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/research-talk-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Thanh tiến trình là chi tiết của bản gốc — trong engine, thay bằng footer số trang + nhãn section nhất quán (ghi rõ khác biệt ở QA note).
- Công thức render thành ảnh (PNG nền trong) từ LaTeX/MathJax bên ngoài rồi chèn như hình; không gõ công thức bằng text thường.

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
- Deck talk: bìa → outline → các section (mỗi section: 1 thông điệp/trang) → kết luận → tài liệu tham khảo.
- Notes có thời lượng từng phần; HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
