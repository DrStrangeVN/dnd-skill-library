---
name: deck-academic-argument-deck
description: Style deck "Academic Argument" cho hệ deck-studio — Trắng học thuật, tiêu đề là câu luận điểm, trích dẫn nằm ngay trên slide bằng chứng. Dùng khi làm deck bảo vệ luận văn, bài nói hội thảo khoa học, seminar/lab meeting cần lập luận chặt và trích dẫn rõ. Theme có sẵn: ~/workspace/deck-studio/themes/academic-argument-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Academic Argument — Trắng học thuật, tiêu đề là câu luận điểm, trích dẫn nằm ngay trên slide bằng chứng

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Academic Argument Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/academic-argument-deck.json` (bg #FFFFFF, nhấn #2F7D6B).

## Khi nào dùng
- Nhà nghiên cứu chuẩn bị talk hội thảo, seminar, lab meeting hoặc brief xin tài trợ.
- Nghiên cứu sinh sắp bảo vệ, nơi hội đồng sẽ chất vấn mạch lập luận.
- Người trình bày đã có số liệu + trích dẫn đã kiểm chứng và phải khớp khung thời gian cố định.

## Nguyên lý cốt lõi
- Đọc riêng dãy tiêu đề phải thấy trọn lập luận: câu hỏi → bằng chứng → kết luận. Tiêu đề nào chỉ nêu chủ đề là chưa đạt.
- Mỗi slide kết quả chỉ chứa MỘT biểu đồ/hình bằng chứng, phát hiện ghi ngay trên hình, trích dẫn để cùng slide.
- Giới hạn (limitations) và phụ lục được gắn nhãn rõ, không giấu ở cuối.

## Hệ hình ảnh
- Nền trắng tuyệt đối, không trang trí — khoảng trắng là hệ hình ảnh.
- Tiêu đề grotesk đậm cỡ lớn viết như câu khẳng định (action title), không phải nhãn chủ đề.
- Nhãn mono viết hoa giãn chữ màu gỉ sắt ở góc trên phải; dấu chấm đầu dòng màu teal.
- Chân slide: một dòng ghi chú nguồn/minh họa mảnh, tách bằng hairline.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ airy. Bare white field, one rust mono micro-label top-right, teal bullet dots; the argument is the decoration.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/academic-argument-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/academic-argument-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Dùng layout `content` cho các slide luận điểm, `chart`/`data` cho slide bằng chứng — một hình một slide.
- Số liệu minh họa hay số chưa công bố phải ghi nhãn ngay trên slide (footer hoặc dòng `meta`).

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
- Deck mà dãy tiêu đề tự nó kể được câu chuyện nghiên cứu, kết ở conclusions + references + appendix có nhãn.
- Slide kết quả: biểu đồ vẽ lại ở cỡ trình chiếu, nhãn phát hiện trên biểu đồ, citation cùng trang.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
