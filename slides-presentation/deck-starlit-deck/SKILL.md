---
name: deck-starlit-deck
description: Style deck "Starlit" cho hệ deck-studio — Đêm xanh sâu đầy sao, serif vàng — deck trang trọng cho thư và tổng kết. Dùng khi làm deck trang trọng nền đêm sao với serif vàng cho thư thường niên, tổng kết năm hoặc bài nói cá nhân. Theme có sẵn: ~/workspace/deck-studio/themes/starlit-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Starlit — Đêm xanh sâu đầy sao, serif vàng — deck trang trọng cho thư và tổng kết

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Starlit Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/starlit-deck.json` (bg #081426, nhấn #E9C46A).

## Khi nào dùng
- Thư nhà sáng lập cuối năm.
- Tổng kết năm (year in review) của tổ chức/cá nhân.
- Bài nói cá nhân tại lễ, kỷ niệm, tốt nghiệp.

## Nguyên lý cốt lõi
- Giọng văn thư tín: viết cho một người đọc cụ thể, không hô hào đám đông.
- Nhịp nền sao là nhịp cảm xúc: trang cao trào nền sao dày, trang thông tin nền sao thưa — ghi vào kế hoạch trước khi build.
- Một deck một preset sao/màu; không trộn Midnight Gold với Aurora trong cùng deck.

## Hệ hình ảnh
- Nền navy sâu; trường sao là các chấm nhỏ rải (decor dots) với mật độ thay đổi như bầu trời thật.
- Tiêu đề serif vàng (gold) — preset 'Midnight Gold'; hai preset phụ: Aurora Teal (ngọc), Dawn Rose (hồng) — xem Kỹ thuật.
- Chữ thân màu ngà nhạt, thưa dòng; mỗi trang rất ít chữ.
- Số trang và nhãn phần nhỏ, đặt thấp, như ghi chú chân trang sách.
- Trang trí của theme: decor `dots`, bo góc 0px, mật độ airy. Deep navy with procedural starfield dots; gold serif for the Midnight Gold preset. Variants: Aurora Teal, Dawn Rose (clone theme to switch).

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/starlit-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/starlit-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Preset phụ: nhân bản theme — Aurora Teal: accent #7FD1C0; Dawn Rose: accent #E8A0B4, ink giữ ngà. Ghi preset đã dùng vào QA note.
- Validator cấu trúc của bản gốc → tương đương: verify.py + kiểm tra số trang/liền mạch nền ở contact sheet.

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
- Deck đêm sao trang trọng, notes viết như bản thảo bài nói.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
