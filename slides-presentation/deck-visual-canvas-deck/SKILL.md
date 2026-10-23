---
name: deck-visual-canvas-deck
description: Style deck "Visual Canvas" cho hệ deck-studio — Mỗi slide một 'bảng' (board) bố cục riêng trên nền cobalt — deck khám phá thị giác. Dùng khi làm deck khám phá/creative direction mà mỗi trang là một bảng bố cục độc lập để duyệt hướng hình ảnh. Theme có sẵn: ~/workspace/deck-studio/themes/visual-canvas-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Visual Canvas — Mỗi slide một 'bảng' (board) bố cục riêng trên nền cobalt — deck khám phá thị giác

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Visual Canvas Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/visual-canvas-deck.json` (bg #1E3AF2, nhấn #B8F526).

## Khi nào dùng
- Creative director trình bày hướng hình ảnh.
- Workshop khám phá concept cho brand/dự án.
- Review nội bộ cần so sánh 2 hướng thị giác.

## Nguyên lý cốt lõi
- Quy trình plan-first: chốt tiêu đề, câu chuyện, thứ tự và hướng hình ảnh TRƯỚC khi build; có thể làm thêm một hướng thứ hai để so sánh.
- Board được duyệt là board có một ý tưởng thị giác duy nhất đọc được trong 3 giây.
- Sự ngẫu hứng có biên: font, lưới góc và dấu đăng ký không đổi giữa các board.

## Hệ hình ảnh
- Mỗi slide là một board riêng: nền cobalt (bảng mẫu), chữ condensed kem phủ gần kín mặt như tường type.
- Hai bảng phụ trợ: bảng đen và bảng xanh acid (acid green) đặt lệch, chồng lớp.
- Dấu đăng ký (registration marks) ở góc như bản in thử — decor corner của engine.
- Ba colorway trong bản gốc — theme này là Cobalt Registry; hai colorway còn lại nhân bản theme để đổi (xem Kỹ thuật).
- Trang trí của theme: decor `corner`, bo góc 0px, mật độ standard. Exploratory canvas boards: cobalt field, cream condensed walls of type, acid-green and black boards; each slide its own composition. Sample board shown; 3 colourways in notes.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/visual-canvas-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/visual-canvas-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Colorway phụ: nhân bản theme đổi bg/accent (đen–kem–đỏ; kem–đen–xanh lá) và build deck song song để so sánh ở contact sheet.
- Chữ phủ kín mặt dễ tràn — giữ tiêu đề ≤ 5 từ/dòng và screenshot QA từng board.

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
- Một (hoặc hai) deck hướng thị giác hoàn chỉnh kèm ghi chú hướng nào được chọn và vì sao (trong QA note).
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
