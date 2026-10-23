---
name: deck-article-brief-deck
description: Style deck "Article Brief" cho hệ deck-studio — Xanh slate trầm, một luận điểm mở đầu, bằng chứng truy được về bài gốc. Dùng khi biến một bài báo/báo cáo đã kiểm chứng thành deck brief có luận điểm, bằng chứng và câu hỏi thảo luận. Theme có sẵn: ~/workspace/deck-studio/themes/article-brief-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Article Brief — Xanh slate trầm, một luận điểm mở đầu, bằng chứng truy được về bài gốc

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Article Brief Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/article-brief-deck.json` (bg #222E44, nhấn #D97B5F).

## Khi nào dùng
- Giáo viên/người tạo khóa học dẫn lớp đi qua một bài báo và kết bằng thảo luận.
- Team brief đồng nghiệp về một bài báo/báo cáo trước khi ra quyết định.
- Người trình bày cần mọi khẳng định trên màn hình đều có nguồn đã duyệt.

## Nguyên lý cốt lõi
- Mở bằng thesis một câu; toàn deck là xương lập luận (argument spine) của bài gốc, không thêm ý ngoài bài.
- Mọi fact/trích dẫn trên slide phải truy được về đoạn tương ứng trong tài liệu đã duyệt.
- Thông tin chưa xác nhận phải để trạng thái pending hiển thị rõ, không viết như fact.

## Hệ hình ảnh
- Nền xanh slate đậm đồng nhất; chữ kem, không ảnh trang trí.
- Nhãn mono màu cá hồi (salmon) cho trạng thái tài liệu (ví dụ: bản đã duyệt / đang chờ xác nhận).
- Tiêu đề grotesk kem cỡ lớn; thông tin brief (số brief, tổng số trang) ở 4 góc bằng mono.
- Mật độ chữ thấp, khoảng trống lớn — deck để nói, không để đọc thay tài liệu.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ airy. Deep slate-navy field, cream grotesk, one salmon micro-label; mono furniture at the four corners.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/article-brief-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/article-brief-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Mỗi slide 3–5 talking points để trong `notes`; trên slide chỉ giữ luận điểm + bằng chứng ngắn.
- Slide kết dùng layout `closing` với 2–3 câu hỏi thảo luận thay cho CTA thông thường.

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
- Deck brief: thesis mở đầu → xương lập luận → các slide bằng chứng → câu hỏi thảo luận chốt.
- Notes chứa talking points và vị trí đoạn gốc tương ứng.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
