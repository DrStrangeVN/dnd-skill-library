---
name: deck-chromatic-futures-deck
description: Style deck "Chromatic Futures" cho hệ deck-studio — Đen ấm, dải collage giấy nhiều màu, mỗi trang một bố cục riêng — cho workshop tương lai. Dùng khi biến ý tưởng workshop thành deck có dải collage giấy màu và bố cục biến hóa từng trang. Theme có sẵn: ~/workspace/deck-studio/themes/chromatic-futures-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Chromatic Futures — Đen ấm, dải collage giấy nhiều màu, mỗi trang một bố cục riêng — cho workshop tương lai

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Chromatic Futures Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/chromatic-futures-deck.json` (bg #171512, nhấn #CDBCF2).

## Khi nào dùng
- Facilitator futures lab / workshop tầm nhìn.
- Team tổng kết một buổi ideation thành câu chuyện trình bày được.
- Dự án cộng đồng cần không khí lạc quan, thủ công.

## Nguyên lý cốt lõi
- Collage là chất liệu thật: dùng ảnh giấy xé/cắt thật hoặc ảnh tự tạo, không dùng gradient thay thế.
- Dù bố cục thay đổi từng trang, dải collage đáy + hệ màu + font phải không đổi.
- Nội dung workshop phải đi từ tưởng tượng → ý tưởng → cam kết cụ thể; trang cuối luôn là bước làm được.

## Hệ hình ảnh
- Nền đen ấm; dọc đáy slide là dải 'đồi' collage giấy xé: hồng sọc, bạc hà sóng, tím vẽ tay.
- Chữ grotesk kem, căn giữa ở các trang mở; chip CTA oải hương (lavender).
- Hình khối giấy cắt (trứng oải hương, vòng than, điểm cam) làm motif lặp.
- Mỗi trang một bố cục khác nhau — sự đa dạng có kiểm soát là bản sắc của style.
- Trang trí của theme: decor `band`, bo góc 12px, mật độ standard. Tactile paper-collage hills (pink/mint/violet) along the bottom of a near-black field; cream grotesk, lavender CTA chip.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/chromatic-futures-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/chromatic-futures-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Chuẩn bị 2–3 ảnh dải collage 16:9 dùng lặp ở layout `image`/cover; các slide chữ dùng nền đen của theme.
- Layout `two-col` cho so sánh kịch bản (scenario A/B).

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
- Deck workshop có nhịp tưởng tượng → lựa chọn → cam kết, hình collage xuyên suốt.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
