---
name: deck-sorbet-window-deck
description: Style deck "Sorbet Window" cho hệ deck-studio — Khung cửa sổ sherbet: viền chanh, ảnh san hô, panel trắng để đọc. Dùng khi làm deck concept sản phẩm theo mùa (đồ uống, món ăn, bán lẻ) với khung cửa sổ màu sorbet. Theme có sẵn: ~/workspace/deck-studio/themes/sorbet-window-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Sorbet Window — Khung cửa sổ sherbet: viền chanh, ảnh san hô, panel trắng để đọc

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Sorbet Window Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/sorbet-window-deck.json` (bg #FFF6D8, nhấn #FFC81E).

## Khi nào dùng
- Concept đồ uống/món ăn theo mùa.
- Giới thiệu dòng sản phẩm mới cho nhà bán lẻ.
- Pitch menu/chiến dịch mùa cho đối tác F&B.

## Nguyên lý cốt lõi
- Một cửa sổ một vị/một sản phẩm — không nhồi nhiều sản phẩm vào một khung.
- Màu khung theo nhóm sản phẩm, nhất quán từ bìa tới trang giá/thông tin.
- Thông tin bán hàng (giá, điểm bán, thời gian) nằm trong panel trắng, không in lên ảnh.

## Hệ hình ảnh
- Mỗi trang là một 'cửa sổ' có khung (frame): viền chanh (lemon) hoặc san hô quanh nội dung.
- Ảnh sản phẩm tông san hô/cam hồng chiếm một ô cửa sổ; panel trắng chứa phần chữ đọc.
- Tiêu đề serif + italic xen kẽ (từ khóa để italic).
- Huy hiệu tròn viền mảnh (circular badge) cho mùa/vòng ra mắt (ví dụ 'Mùa 2').
- Trang trí của theme: decor `frame`, bo góc 8px, mật độ standard. Sherbet palette in window frames: lemon frame, coral photo fields, white reading panels, serif+italic titles.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/sorbet-window-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/sorbet-window-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Decor `frame` của engine tạo khung viền cho mọi trang — khớp sẵn với ý cửa sổ.
- Layout `two-col` cho cặp ảnh sản phẩm – mô tả vị; badge mùa đặt trong kicker.

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
- Deck concept theo mùa: bìa cửa sổ → từng vị/sản phẩm → bảng giá/thông tin bán → liên hệ đặt hàng.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
