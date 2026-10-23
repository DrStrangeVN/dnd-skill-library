---
name: deck-architectural-project-deck
description: Style deck "Architectural Project" cho hệ deck-studio — Bảng đen kiến trúc, serif ngà, một khối đỏ gạch — review dự án bằng bản vẽ. Dùng khi làm deck review dự án kiến trúc/nội thất cần trình bày bản vẽ, mặt bằng, phương án và kết ở một quyết định. Theme có sẵn: ~/workspace/deck-studio/themes/architectural-project-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Architectural Project — Bảng đen kiến trúc, serif ngà, một khối đỏ gạch — review dự án bằng bản vẽ

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Architectural Project Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/architectural-project-deck.json` (bg #181816, nhấn #C8431F).

## Khi nào dùng
- Kiến trúc sư/nội thất chuẩn bị review concept, design development hoặc gặp khách hàng.
- Team trình bày feasibility, đề án phát triển hoặc bài thi tuyển phương án.
- Project lead cần buổi review kết thúc bằng một quyết định rõ.

## Nguyên lý cốt lõi
- Mỗi slide chỉ mang MỘT bản vẽ hoặc một bằng chứng chính: site, khối, mặt bằng, mặt cắt, vật liệu, tiến độ.
- Đơn vị, trích dẫn, revision, giả định và ghi chú 'sơ bộ' phải nằm đúng chỗ reviewer tìm thấy.
- Deck luôn kết ở quyết định cần chốt + các câu hỏi còn mở — không kết bằng slide cảm ơn.

## Hệ hình ảnh
- Nền đen than như bàn vẽ; lưới tọa độ mảnh (grid) chạy dưới mọi slide.
- Tiêu đề serif ngà (Playfair) cỡ lớn, đối lập với nhãn mono viết hoa giãn chữ.
- Đúng một khối/mảng đỏ gạch (vermilion) mỗi slide làm điểm neo thị giác.
- Mã bản vẽ kiểu SK-01, thông số dự án (căn hộ, diện tích, giai đoạn) đặt ở góc cố định.
- Trang trí của theme: decor `grid`, bo góc 0px, mật độ airy. Near-black board, ivory serif display, one vermilion massing block; faint survey grid and mono drawing codes.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/architectural-project-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/architectural-project-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Bản vẽ xuất ra ảnh 16:9 nền tối trước khi đưa vào layout `image`; giữ mã bản vẽ trong `caption`.
- So sánh phương án dùng `two-col`, mỗi cột một phương án + cùng một bộ tiêu chí ở notes.

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
- Deck review: premise → site forces → massing → plan/section → vật liệu → chương trình → giai đoạn → so sánh phương án → quyết định.
- Notes ghi rõ giả định và điểm cần xác nhận của từng bản vẽ.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
