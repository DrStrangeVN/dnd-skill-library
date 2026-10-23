---
name: deck-blue-lime-ledger-deck
description: Style deck "Blue Lime Ledger" cho hệ deck-studio — Thẻ ảnh cao bo tròn, nhãn xanh điện và chanh — deck phân tích mà vẫn có người. Dùng khi làm deck phân tích (ledger/báo cáo) cần thẻ ảnh chân dung cao, nhãn màu điện và biểu đồ thanh mảnh. Theme có sẵn: ~/workspace/deck-studio/themes/blue-lime-ledger-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Blue Lime Ledger — Thẻ ảnh cao bo tròn, nhãn xanh điện và chanh — deck phân tích mà vẫn có người

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Blue Lime Ledger Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/blue-lime-ledger-deck.json` (bg #FFFFFF, nhấn #2B50E0).

## Khi nào dùng
- Deck phân tích cho dự án cộng đồng/dịch vụ (ví dụ thư viện cho mượn, dịch vụ dùng chung).
- Team cần ngôn ngữ hình ảnh nhất quán giữa trang kể chuyện và trang số.
- Người có thông điệp rõ và muốn deck trông hiện đại, đáng tin.

## Nguyên lý cốt lõi
- Mỗi thẻ ảnh phải gắn với một nhu cầu/kết quả cụ thể — ảnh là bằng chứng, không phải lấp chỗ.
- Số liệu trình bày dạng ledger: hàng rõ, nhãn rõ, một điểm nhấn màu mỗi trang.
- Xanh điện = hệ thống/dữ liệu; chanh = con người/kết quả. Không hoán đổi vai trò màu.

## Hệ hình ảnh
- Thẻ ảnh chân dung khổ cao, bo tròn lớn (~26px), xếp hàng ngang như các cột sổ cái.
- Nhãn pill xanh điện cho mục dữ/quy trình; đúng một pill chanh (lime) dành cho kết quả con người.
- Chữ grotesk đen đậm trên nền trắng; biểu đồ thanh mảnh bo tròn khi vào slide số liệu.
- Mũi tên ↗ mảnh ở góc như dấu điều hướng xuyên suốt.
- Trang trí của theme: decor `none`, bo góc 26px, mật độ standard. Tall rounded editorial photo cards; electric-blue pills, one lime pill for the human outcome; bold black grotesk.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/blue-lime-ledger-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/blue-lime-ledger-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Ảnh chân dung crop dọc 3:4 trước; layout `image` của engine là full-bleed 16:9 nên thẻ dọc mô phỏng bằng ảnh đã compose sẵn nền trắng.
- Biểu đồ dùng layout `chart` — thanh cuối (kết quả) tự được highlight, khớp vai trò màu chanh/xanh.

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
- Deck phân tích kể chuyện bằng thẻ ảnh + trang số liệu ledger, notes đầy đủ.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
