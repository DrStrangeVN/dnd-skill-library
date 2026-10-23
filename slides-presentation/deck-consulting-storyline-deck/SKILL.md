---
name: deck-consulting-storyline-deck
description: Style deck "Consulting Storyline" cho hệ deck-studio — Giấy kem, dải hồng bụi chạy dọc, tiêu đề là câu kết luận — deck tư vấn kết ở quyết định. Dùng khi làm deck tư vấn/báo cáo lãnh đạo với tiêu đề dạng câu kết luận, bằng chứng, khuyến nghị và kết ở quyết định cần chốt. Theme có sẵn: ~/workspace/deck-studio/themes/consulting-storyline-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Consulting Storyline — Giấy kem, dải hồng bụi chạy dọc, tiêu đề là câu kết luận — deck tư vấn kết ở quyết định

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Consulting Storyline Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/consulting-storyline-deck.json` (bg #F7F3EC, nhấn #B3242E).

## Khi nào dùng
- Tư vấn trình bày cho steering committee/ban giám đốc.
- Báo cáo chiến lược cần chốt ngân sách hoặc lộ trình.
- Tổng kết dự án có khuyến nghị hành động.

## Nguyên lý cốt lõi
- Chuỗi khóa cứng: phát hiện → bằng chứng → khuyến nghị → roadmap → quyết định của ban điều hành.
- Giả định và cổng quyết định (decision gates) phải ghi tường minh, không để trong đầu người trình bày.
- Slide cuối là quyết định cần chốt kèm phương án dự phòng — không phải slide cảm ơn.

## Hệ hình ảnh
- Nền giấy kem; một dải (sidebar) hồng bụi chạy dọc mép slide xuyên suốt deck.
- Tiêu đề lớn dạng câu đầy đủ (action title) chứa kết luận của trang.
- Điểm nhấn đỏ crimson rất tiết kiệm: số quyết định, mốc roadmap, dòng takeaway.
- Bảng/biểu đồ nhỏ, sạch, nhiều khoảng trắng kiểu báo cáo in.
- Trang trí của theme: decor `none`, bo góc 2px, mật độ standard. Cream paper, dusty-pink sidebar washing down the deck, crimson display serif approximated by Archivo; deck ends on a decision.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/consulting-storyline-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/consulting-storyline-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Trang roadmap mô phỏng bằng `content` bullets có mốc thời gian đậm (**bold**) đầu dòng.
- Dải sidebar là đặc trưng của ảnh gốc; trong engine, thay bằng dải band trang trí + kicker nhất quán (ghi rõ khác biệt này ở QA note).

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
- Deck storyline: tình huống → phát hiện → bằng chứng → khuyến nghị → roadmap → quyết định.
- Notes ghi giả định + câu hỏi dự phòng của lãnh đạo.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
