---
name: deck-yellow-sketchnote-deck
description: Style deck "Yellow Sketchnote" cho hệ deck-studio — Chữ đen–vàng khổ cực lớn, đảo chữ bất đối xứng, hình mực mảnh — sketchnote cho đội nhỏ. Dùng khi làm tài liệu hướng dẫn/thử nghiệm cho team nhỏ với chữ khổ lớn và hình vẽ mực kiểu sketchnote. Theme có sẵn: ~/workspace/deck-studio/themes/yellow-sketchnote-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Yellow Sketchnote — Chữ đen–vàng khổ cực lớn, đảo chữ bất đối xứng, hình mực mảnh — sketchnote cho đội nhỏ

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Yellow Sketchnote Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/yellow-sketchnote-deck.json` (bg #FFFFFF, nhấn #FFC81E).

## Khi nào dùng
- Hướng dẫn thử nghiệm (experiment guide) cho team nhỏ.
- Field guide nội bộ cho cách làm mới.
- Tài liệu học nhanh trong workshop.

## Nguyên lý cốt lõi
- Tài liệu để LÀM, không để ngắm: mỗi trang kết bằng một bước thử cụ thể, nhỏ, làm được ngay.
- Câu hỏi mở đầu là trục của deck — mọi trang sau trả lời hoặc kiểm chứng câu hỏi đó.
- Hình mực phải vẽ đúng tình huống của team; hình trang trí chung chung làm mất chất sketchnote.

## Hệ hình ảnh
- Nền trắng crisp; tiêu đề khổ cực lớn hai màu: một dòng vàng nắng, một dòng mực đen.
- Các 'đảo chữ' (copy islands) ngắn đặt bất đối xứng quanh hình vẽ trung tâm.
- Hình người/vật nét mực mảnh (fine ink) kèm dấu sao (asterisk) đen và vàng làm nhịp.
- Đoạn mở đầu nhỏ đặt trên đỉnh như lời dặn trước khi đọc.
- Trang trí của theme: decor `dots`, bo góc 0px, mật độ standard. Oversized black and yellow type, crisp white space, asymmetric copy islands, fine ink figures with star asterisks.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/yellow-sketchnote-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/yellow-sketchnote-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Tiêu đề hai màu: tách title thành 2 dòng và tô màu qua hai slide phần (cover + section) hoặc dùng **bold** + ghi chú màu ở QA; đơn giản nhất: giữ tiêu đề mực đen, dòng vàng chuyển thành kicker lớn.
- Hình mực chuẩn bị PNG nền trắng/trong; dấu sao mô phỏng bằng decor dots.

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
- Deck hướng dẫn: câu hỏi → nguyên tắc → các bước thử → cách đọc kết quả → bước tiếp theo duy nhất.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
