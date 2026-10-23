---
name: deck-spectrum-brand-strategy-deck
description: Style deck "Spectrum Brand Strategy" cho hệ deck-studio — Nền đen chiến lược, gạch phổ màu (spectrum tiles) cho khán giả và kênh. Dùng khi làm deck chiến lược thương hiệu/định vị với lưới gạch màu phổ trên nền đen. Theme có sẵn: ~/workspace/deck-studio/themes/spectrum-brand-strategy-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Spectrum Brand Strategy — Nền đen chiến lược, gạch phổ màu (spectrum tiles) cho khán giả và kênh

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Spectrum Brand Strategy Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/spectrum-brand-strategy-deck.json` (bg #0C1210, nhấn #FFC81E).

## Khi nào dùng
- Deck định vị thương hiệu cho lãnh đạo duyệt.
- Chiến lược khán giả/kênh cho ra mắt sản phẩm.
- Tổng kết nghiên cứu thị trường thành kế hoạch hành động.

## Nguyên lý cốt lõi
- Màu gạch = thực thể: một nhóm khán giả/kênh giữ đúng một màu xuyên suốt deck, kể cả ở trang lộ trình.
- Chiến lược phải đi đủ: định vị → khán giả → thông điệp → kênh → lộ trình → thước đo.
- Mỗi gạch chỉ chứa dữ kiện quyết định được (quy mô, hành vi, chi phí) — gạch trang trí bị loại.

## Hệ hình ảnh
- Nền đen lục sẫm; tiêu đề kem grotesk rất đậm.
- Gạch phổ (spectrum tiles): các ô bo tròn màu xanh lá, xanh dương, cam, vàng — mỗi màu một nhóm khán giả hoặc kênh.
- Lưới gạch là ngôn ngữ chính cho trang phân khúc, kênh và lộ trình.
- Chữ trong gạch luôn là mực đen hoặc trắng tùy độ sáng của gạch — kiểm tra ở QA.
- Trang trí của theme: decor `none`, bo góc 18px, mật độ standard. Black strategy field; spectrum tiles (green/blue/orange/yellow) form the audience and channel grids.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/spectrum-brand-strategy-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/spectrum-brand-strategy-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Lưới gạch mô phỏng bằng layout `data` (4 ô) hoặc `content` có bullets tô màu qua **bold** + kicker; lưới lớn hơn 4 ô thì dùng ảnh sơ đồ riêng ở layout `image`.
- Giữ bảng màu gạch trong decor_note của theme để các deck sau dùng lại đúng hex.

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
- Deck chiến lược ~9 trang: bối cảnh → định vị → khán giả (gạch) → thông điệp → kênh (gạch) → lộ trình → KPI.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
