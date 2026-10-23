---
name: deck-storybook-margin-deck
description: Style deck "Storybook Margin" cho hệ deck-studio — Sách truyện ngà: chân dung gouache, số chương khổng lồ, nhãn dọc ở lề. Dùng khi làm deck kể chuyện/sách truyện với số chương lớn và chân dung vẽ gouache cho chương trình đọc trẻ em. Theme có sẵn: ~/workspace/deck-studio/themes/storybook-margin-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Storybook Margin — Sách truyện ngà: chân dung gouache, số chương khổng lồ, nhãn dọc ở lề

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Storybook Margin Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/storybook-margin-deck.json` (bg #F7F1DF, nhấn #1E6FA8).

## Khi nào dùng
- Chương trình đọc sách/s kể chuyện cho trẻ em.
- Hồ sơ nhân vật dạng truyện (nhà văn, họa sĩ minh họa).
- Tài liệu giới thiệu bộ sách/truyện cho trường học và phụ huynh.

## Nguyên lý cốt lõi
- Mỗi chương một nhân vật hoặc một câu chuyện hoàn chỉnh; không cắt chuyện giữa chừng để 'tạo tò mò'.
- Chữ kể chuyện ngắn, đọc to được; phần giải thích cho người lớn để ở notes.
- Số chương là hệ điều hướng: mục lục và từng chương phải khớp số tuyệt đối.

## Hệ hình ảnh
- Nền giấy ngà (ivory); chân dung nhân vật vẽ gouache là thành phần trung tâm.
- Số chương (chapter numeral) mực đen khổ cực lớn ở lề trái — chi tiết nhận diện mạnh nhất.
- Nhãn dọc (vertical label) chạy ở mép trang ghi tên phần.
- Một khối xanh nhỏ (blue block) duy nhất mỗi chương làm điểm neo — họ hàng màu với style Audio Report.
- Trang trí của theme: decor `none`, bo góc 2px, mật độ airy. Ivory storybook: gouache portraits, oversized chapter numerals, vertical marginal labels, one small blue block.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/storybook-margin-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/storybook-margin-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `section` dùng trường number làm số chương; `image` cho trang chân dung toàn trang.
- Nhãn dọc là chi tiết ảnh gốc — mô phỏng bằng kicker trong spec và ghi rõ khác biệt ở QA note.

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
- Deck truyện theo chương có mục lục khớp số và notes cho người kể.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
