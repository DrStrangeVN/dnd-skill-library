---
name: deck-pastel-cutout-deck
description: Style deck "Pastel Cutout" cho hệ deck-studio — Cắt giấy pastel: nền hồng bụi, hình kem xếp lớp, điểm cam–vàng pop. Dùng khi làm deck collage cắt giấy pastel cho sản phẩm thủ công, nội dung trẻ em hoặc chiến dịch mềm mại. Theme có sẵn: ~/workspace/deck-studio/themes/pastel-cutout-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Pastel Cutout — Cắt giấy pastel: nền hồng bụi, hình kem xếp lớp, điểm cam–vàng pop

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Pastel Cutout Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/pastel-cutout-deck.json` (bg #EBCFD2, nhấn #F26722).

## Khi nào dùng
- Sản phẩm thủ công, đồ trẻ em, nội dung mềm mại.
- Chiến dịch cộng đồng cần sự dịu dàng.
- Lookbook nhỏ cho brand handmade.

## Nguyên lý cốt lõi
- Collage là thật: ảnh/hình phải có mép cắt và bóng lớp (drop shadow giữa các lớp giấy).
- Chữ luôn nằm trên mảng giấy kem, không in trực tiếp lên nền hồng.
- Một slide tối đa 3 lớp hình — nhiều hơn là rối.

## Hệ hình ảnh
- Nền hồng bụi (dusty pink); các hình cắt giấy màu kem xếp lớp (layered cutouts) làm bố cục chính.
- Điểm pop cam và vàng nắng ở chi tiết nhỏ: hoa, mặt trời, nhãn.
- Cạnh hình giữ vẻ xé/cắt tay — không bo tròn hoàn hảo kiểu UI.
- Chữ Anton đậm màu mực, đặt trên mảng kem để dễ đọc.
- Trang trí của theme: decor `none`, bo góc 18px, mật độ standard. Pastel paper cutouts: dusty-pink field, cream shapes, orange/yellow pop accents; collage-first deck.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/pastel-cutout-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/pastel-cutout-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Chuẩn bị ảnh collage đã compose (nền hồng + lớp kem) ở layout `image` cho các trang trưng bày.
- Trang chữ dùng surface kem của theme làm 'mảng giấy' chứa nội dung.

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
- Deck collage pastel có nhịp lớp giấy nhất quán.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
