---
name: deck-ochre-editorial-deck
description: Style deck "Ochre Editorial" cho hệ deck-studio — Biên tập đất son: kem và ochre, chân dung nghệ tây, chữ đậm như bìa tạp chí. Dùng khi làm deck biên tập/hồ sơ nhân vật với tông đất son–kem và ảnh chân dung nghệ tây ấm. Theme có sẵn: ~/workspace/deck-studio/themes/ochre-editorial-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Ochre Editorial — Biên tập đất son: kem và ochre, chân dung nghệ tây, chữ đậm như bìa tạp chí

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Ochre Editorial Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/ochre-editorial-deck.json` (bg #F6EFDD, nhấn #DE9A16).

## Khi nào dùng
- Hồ sơ nhân vật (nghệ nhân, đầu bếp, vận động viên, nhà sáng lập).
- Tạp chí nội bộ, ấn phẩm kỷ niệm.
- Câu chuyện nghề/thương hiệu cá nhân.

## Nguyên lý cốt lõi
- Mỗi nhân vật một chương: chân dung → câu chuyện → dấu mốc → câu nói.
- Giọng biên tập ấm và cụ thể; tránh văn phong thông cáo.
- Giữ tông ấm toàn deck — ảnh lệch tông lạnh phải xử lý lại trước khi build.

## Hệ hình ảnh
- Nền kem; ochre (đất son) là màu chủ đạo cho tiêu đề lớn và khối mở phần.
- Ảnh chân dung tông nghệ tây (saffron) ấm — con người là trung tâm của mọi trang mở.
- Điểm nhấn đỏ đất (burnt red) cho chi tiết nhỏ: số trang, đường kẻ, từ khóa.
- Chữ hiển thị đậm, chắc (Anton) theo tinh thần bìa tạp chí in.
- Trang trí của theme: decor `none`, bo góc 10px, mật độ standard. Ochre-and-cream editorial with a saffron portrait cover; display stands in heavy grotesk where the original uses expressive lettering.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/ochre-editorial-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/ochre-editorial-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `image` cho trang chân dung mở chương; `quote` cho câu nói của nhân vật.
- Ảnh xử lý warm grade thống nhất trước khi đưa vào spec.

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
- Deck biên tập theo chương nhân vật với nhịp tạp chí.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
