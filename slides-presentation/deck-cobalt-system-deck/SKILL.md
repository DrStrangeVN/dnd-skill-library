---
name: deck-cobalt-system-deck
description: Style deck "Cobalt System" cho hệ deck-studio — Cobalt chia đôi: chữ trái, trực quan dữ liệu phải; vàng chỉ dành cho tín hiệu. Dùng khi làm deck dữ liệu/hệ thống với bố cục chia đôi cobalt và màu vàng làm tín hiệu duy nhất. Theme có sẵn: ~/workspace/deck-studio/themes/cobalt-system-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Cobalt System — Cobalt chia đôi: chữ trái, trực quan dữ liệu phải; vàng chỉ dành cho tín hiệu

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Cobalt System Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/cobalt-system-deck.json` (bg #0A48D2, nhấn #FFD81E).

## Khi nào dùng
- Báo cáo dữ liệu/quý cho team vận hành.
- Giải thích hệ thống bằng sơ đồ + số.
- Tổng kết thử nghiệm A/B, funnel, hiệu năng.

## Nguyên lý cốt lõi
- Một slide một câu hỏi dữ liệu; viz trả lời đúng câu hỏi đó, không trưng bày thêm.
- Vàng xuất hiện quá 2 lần/trang là mất tác dụng tín hiệu — rà soát ở QA.
- Nguồn và đơn vị ghi ngay dưới viz, không gộp vào phụ lục.

## Hệ hình ảnh
- Khung cobalt; lưới mô-đun mảnh (grid) hiện rõ trên nền.
- Bố cục chia đôi mặc định: cột chữ trái, cột trực quan (viz) phải có texture chấm li ti (speckle).
- Vàng tín hiệu (signal yellow) CHỈ dùng cho giá trị cần chú ý: đỉnh, ngưỡng, cảnh báo.
- Nhãn mono trắng viết hoa cho trục, đơn vị, nguồn dữ liệu.
- Trang trí của theme: decor `grid`, bo góc 0px, mật độ standard. Cobalt divided layout: text left, speckled data-viz right; yellow reserved for signal values on blue.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/cobalt-system-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/cobalt-system-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `chart` cho viz chính; `two-col` khi cần giải thích dài bên trái, biểu đồ bên phải.
- Speckle texture là phần ảnh — chuẩn bị ảnh viz có texture sẵn nếu cần giống bản gốc.

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
- Deck dữ liệu cobalt với nhịp câu hỏi → viz → kết luận từng trang.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
