---
name: deck-prismatic-fashion-deck
description: Style deck "Prismatic Fashion" cho hệ deck-studio — Thời trang biên tập: ảnh vệt sáng lăng kính, serif, ghi chú màu cobalt–hồng. Dùng khi làm lookbook/hồ sơ thời trang với ảnh vệt sáng prismatic và bố cục tạp chí thưa. Theme có sẵn: ~/workspace/deck-studio/themes/prismatic-fashion-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Prismatic Fashion — Thời trang biên tập: ảnh vệt sáng lăng kính, serif, ghi chú màu cobalt–hồng

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Prismatic Fashion Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/prismatic-fashion-deck.json` (bg #F7F2EA, nhấn #1E40D8).

## Khi nào dùng
- Lookbook bộ sưu tập, hồ sơ nhà thiết kế.
- Ra mắt dòng sản phẩm thời trang/phụ kiện.
- Tài liệu gửi báo chí và buyer.

## Nguyên lý cốt lõi
- Ảnh là sản phẩm: ảnh nào không đạt chuẩn tạp chí (ánh sáng, styling) thì không vào deck.
- Chú thích ghi đúng tên thiết kế/chất liệu theo tài liệu của brand — sai tên mẫu là lỗi nghiêm trọng.
- Nhịp lookbook: mở toàn cảnh → chi tiết → bảng màu/chất liệu → thông tin mua/liên hệ báo chí.

## Hệ hình ảnh
- Nền kem biên tập; ảnh thời trang có vệt sáng lăng kính (prismatic streaks) là điểm nhận diện.
- Tiêu đề serif thanh; ghi chú màu (colour notes) nhỏ bằng mono cobalt/hồng ở lề.
- Bố cục tạp chí thưa: ảnh lớn, chữ ít, số trang như số tạp chí.
- Không màu ngoài kem–mực + hai màu ghi chú; vệt sáng trong ảnh là màu duy nhất được 'ồn'.
- Trang trí của theme: decor `none`, bo góc 6px, mật độ airy. Fashion editorial on cream: prismatic light streaks in photography, serif display, cobalt/pink colour notes.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/prismatic-fashion-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/prismatic-fashion-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `image` chủ đạo; ghi chú lề mô phỏng bằng caption + kicker mono.
- Ảnh xử lý giữ nguyên vệt sáng tự nhiên; tránh filter làm bệt màu vải.

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
- Lookbook biên tập thưa chữ, ảnh đạt chuẩn tạp chí.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
