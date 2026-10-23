---
name: deck-image-narrative-deck
description: Style deck "Image Narrative" cho hệ deck-studio — Mỗi trang một cảnh toàn khung, chú thích trực tiếp ngắn, câu chuyện nằm trong notes. Dùng khi làm deck kể chuyện mà mỗi trang là một cảnh hình toàn khung và lời kể nằm trong ghi chú thuyết trình. Theme có sẵn: ~/workspace/deck-studio/themes/image-narrative-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Image Narrative — Mỗi trang một cảnh toàn khung, chú thích trực tiếp ngắn, câu chuyện nằm trong notes

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Image Narrative Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/image-narrative-deck.json` (bg #081C20, nhấn #E8A33D).

## Khi nào dùng
- Kể chuyện hành trình/địa điểm cho đối tác hoặc nhà tài trợ.
- Hồ sơ địa điểm (site story) cho dự án cộng đồng/du lịch.
- Bài nói truyền cảm hứng dựa trên trải nghiệm thật.

## Nguyên lý cốt lõi
- Bỏ slide nào không có cảnh đủ mạnh — style này không có chỗ cho slide chữ lấp chỗ trống.
- Caption viết như lời thì thầm tại hiện trường: thời gian, nơi chốn, một chi tiết cảm quan.
- Câu chuyện đầy đủ sống trong notes: mỗi cảnh 3–5 ý nói (talking points).

## Hệ hình ảnh
- Một cảnh toàn khung (full-frame) cho mỗi slide — ảnh hoặc tranh sơn dầu phong cảnh.
- Chú thích trực tiếp (live caption) rất ngắn đặt trên cảnh: 1 dòng, tối đa ~10 từ.
- Trang nghỉ đen/xanh rêu đậm xen giữa các cảnh để nhịp thở.
- Tiêu đề serif chỉ xuất hiện ở bìa và các trang nghỉ.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ airy. Dark expedition field; one full-frame painted/photographic scene per slide, short live captions, story in the notes.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/image-narrative-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/image-narrative-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Toàn bộ slide nội dung dùng layout `image`; kiểm tra caption tương phản trên từng ảnh ở bước screenshot QA.
- Chuỗi ảnh phải cùng một gam màu (ấm/lạnh nhất quán) — lệch gam là lỗi QA.

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
- Deck cảnh nối cảnh có trang nghỉ, notes 3–5 talking points mỗi cảnh.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
