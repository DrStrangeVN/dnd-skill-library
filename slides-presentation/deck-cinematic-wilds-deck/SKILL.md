---
name: deck-cinematic-wilds-deck
description: Style deck "Cinematic Wilds" cho hệ deck-studio — Đen điện ảnh, tranh vẽ động vật/ phong cảnh khổ lớn, chữ trắng tối thiểu. Dùng khi làm deck kể chuyện thiên nhiên/phong cảnh điện ảnh: hình vẽ khổ lớn dẫn dắt, chữ chỉ là phụ đề. Theme có sẵn: ~/workspace/deck-studio/themes/cinematic-wilds-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Cinematic Wilds — Đen điện ảnh, tranh vẽ động vật/ phong cảnh khổ lớn, chữ trắng tối thiểu

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Cinematic Wilds Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/cinematic-wilds-deck.json` (bg #000000, nhấn #E8A33D).

## Khi nào dùng
- Workshop kể chuyện thiên nhiên.
- Pitch documentary hoặc chiến dịch môi trường.
- Diễn giả muốn khán giả 'xem' câu chuyện thay vì đọc slide.

## Nguyên lý cốt lõi
- Hình dẫn, chữ theo: không slide nào có quá ~15 từ trên màn hình.
- Nhịp điện ảnh: mở cảnh rộng → chi tiết → bước ngoặt → kết mở.
- Hình phải là hình gốc tự tạo/có licence; style này lộ ngay khi dùng stock rẻ tiền.

## Hệ hình ảnh
- Nền đen tuyền; hình vẽ painterly (động vật, phong cảnh kỳ ảo) chiếm trọn khung.
- Chữ trắng rất ít: một từ khóa lớn hoặc một câu ngắn mỗi slide.
- Chuyển nhịp xen kẽ trang hình toàn cảnh và trang biên tập đen–trắng (text page).
- Tiêu đề bản gốc là chữ brush trắng — bản house dùng Archivo black, giữ nguyên tắc 'chữ như nét cọ'.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ airy. Pure black cinema field; painterly animal/landscape artwork full-bleed; white brush-style display approximated by Archivo black.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/cinematic-wilds-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/cinematic-wilds-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Hầu hết slide dùng layout `image`; slide chữ dùng `quote` hoặc cover biến thể.
- Notes mang toàn bộ nội dung nói — bắt buộc viết notes đầy đủ cho từng cảnh.

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
- Deck điện ảnh ít chữ, notes đầy đủ từng cảnh.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
