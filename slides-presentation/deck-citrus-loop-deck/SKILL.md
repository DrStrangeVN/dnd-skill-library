---
name: deck-citrus-loop-deck
description: Style deck "Citrus Loop" cho hệ deck-studio — Trắng mô-đun, nhãn capsule cam–chanh–oải hương, motif vòng lặp xám. Dùng khi làm deck về vật liệu tuần hoàn/kinh tế vòng tròn với nhãn capsule màu và bố cục mô-đun sạch. Theme có sẵn: ~/workspace/deck-studio/themes/citrus-loop-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Citrus Loop — Trắng mô-đun, nhãn capsule cam–chanh–oải hương, motif vòng lặp xám

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Citrus Loop Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/citrus-loop-deck.json` (bg #FFFFFF, nhấn #FF7A1A).

## Khi nào dùng
- Dự án vật liệu tuần hoàn, sửa chữa, tái sử dụng.
- Team trình bày quy trình vòng tròn cho đối tác/cộng đồng.
- Người cần deck sáng, sạch, thân thiện cho chủ đề kỹ thuật.

## Nguyên lý cốt lõi
- Màu capsule = chương: một chương một màu, dùng nhất quán từ mục lục tới từng slide.
- Trình bày theo vòng đời vật liệu: cơ hội → vật liệu đang dùng → kế hoạch → con người/quy trình → thử nghiệm đầu tiên.
- Mọi khẳng định về tái chế/tuần hoàn phải có số liệu hoặc ghi rõ là mục tiêu.

## Hệ hình ảnh
- Nền trắng mô-đun; nhãn capsule (pill bo tròn đầy) ba màu: cam, chanh, oải hương — mỗi màu một chương.
- Motif vòng lặp (loop) xám rất nhạt chạy nền, chỉ thấy khi nhìn kỹ.
- Mục lục dạng danh sách đánh số với hairline, mỗi hàng một mô tả ngắn.
- Ảnh sản phẩm/vật liệu cắt vignette tròn hoặc bo góc lớn trên thẻ xám nhạt.
- Trang trí của theme: decor `none`, bo góc 20px, mật độ standard. White modular grid; capsules in orange, lime and lavender label the chapters; one pale grey loop motif behind.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/citrus-loop-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/citrus-loop-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `content` với bullets đánh số hợp cho trang mục lục/quy trình; màu chương thể hiện qua kicker text.
- Ảnh vật liệu chuẩn bị nền trắng/xám nhạt để hòa với surface của theme.

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
- Deck tuần hoàn có mục lục màu theo chương và nhịp vòng đời rõ ràng.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
