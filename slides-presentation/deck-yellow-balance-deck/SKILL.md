---
name: deck-yellow-balance-deck
description: Style deck "Yellow Balance" cho hệ deck-studio — Trắng xám nhạt, thẻ vàng nắng bo tròn, chữ mảnh tĩnh — deck lập kế hoạch tập trung. Dùng khi làm deck về tập trung/kế hoạch (focus planning) với thẻ vàng nắng và bố cục rất thoáng. Theme có sẵn: ~/workspace/deck-studio/themes/yellow-balance-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Yellow Balance — Trắng xám nhạt, thẻ vàng nắng bo tròn, chữ mảnh tĩnh — deck lập kế hoạch tập trung

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Yellow Balance Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/yellow-balance-deck.json` (bg #F7F7F4, nhấn #FFC81E).

## Khi nào dùng
- Giới thiệu app lập kế hoạch/tập trung.
- Kế hoạch quý cá nhân/team nhỏ theo triết lý 'ít mà sâu'.
- Workshop quản lý sự chú ý/năng lượng.

## Nguyên lý cốt lõi
- Thông điệp là sự cân bằng: mỗi trang chỉ một quyết định về sự chú ý (giữ gì, bỏ gì).
- Không nhồi tính năng: trang tính năng tối đa 3 mục, mỗi mục một câu lợi ích.
- Giọng văn như người bạn điềm tĩnh — không FOMO, không thúc ép.

## Hệ hình ảnh
- Trường trắng và xám nhạt; thẻ vàng nắng bo tròn rất lớn là vùng chứa nội dung chính.
- Chữ grotesk mảnh, tĩnh; tiêu đề vừa phải — style này không hét.
- Hình minh họa 3D mềm (như tay cầm đồng hồ cát) hoặc ảnh sáng, ít chi tiết.
- Điểm navy rất nhỏ trong hình/kicker làm neo thị giác.
- Trang trí của theme: decor `none`, bo góc 26px, mật độ airy. White and pale-grey fields, sunny yellow rounded cards, delicate grotesk; calm focus-planning system.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/yellow-balance-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/yellow-balance-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `data` trên thẻ surface; ảnh 3D/ảnh sáng chuẩn bị nền trắng khớp bg.
- Mật độ airy của theme đã giảm cỡ chữ — kiểm tra độ đọc của chữ mảnh ở screenshot QA.

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
- Deck kế hoạch tập trung: vấn đề quá tải → nguyên tắc → cách dùng → nhịp ngày/tuần → bắt đầu nhỏ.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
