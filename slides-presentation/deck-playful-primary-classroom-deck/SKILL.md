---
name: deck-playful-primary-classroom-deck
description: Style deck "Playful Primary Classroom" cho hệ deck-studio — Lớp học tiểu học: trời nhạt, thẻ màu gốc, chữ tròn — không một từ thuật ngữ. Dùng khi làm deck cho lớp học tiểu học/phụ huynh với thẻ màu gốc và ngôn ngữ không thuật ngữ. Theme có sẵn: ~/workspace/deck-studio/themes/playful-primary-classroom-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Playful Primary Classroom — Lớp học tiểu học: trời nhạt, thẻ màu gốc, chữ tròn — không một từ thuật ngữ

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Playful Primary Classroom Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/playful-primary-classroom-deck.json` (bg #EFF6FC, nhấn #FF6B5E).

## Khi nào dùng
- Bài giảng tiểu học trình chiếu trên lớp.
- Buổi họp phụ huynh cần trình bày thân thiện.
- Chương trình ngoại khóa cho trẻ em.

## Nguyên lý cốt lõi
- Không thuật ngữ là luật: từ nào trẻ 8 tuổi không hiểu thì viết lại.
- Một slide một hoạt động hoặc một thông điệp; có slide 'thử ngay' trong mỗi phần.
- Hướng dẫn cho người lớn (giáo viên/phụ huynh) để hết ở notes, không lẫn vào màn hình của trẻ.

## Hệ hình ảnh
- Nền trời nhạt; thẻ trắng bo tròn lớn viền màu gốc (đỏ, vàng, xanh).
- Chấm màu gốc rải như đồ dùng lớp học (decor dots).
- Chữ Baloo 2 tròn, rất lớn; mỗi slide tối đa ~20 từ.
- Hình minh họa phẳng, nhân vật trẻ em đa dạng, biểu cảm rõ.
- Trang trí của theme: decor `dots`, bo góc 22px, mật độ standard. Classroom deck: pale sky ground, primary-colour dots and cards, rounded heavy type, zero jargon.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/playful-primary-classroom-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/playful-primary-classroom-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `content` bullets tối đa 4 dòng ngắn; `image` cho trang hoạt động minh họa lớn.
- QA thêm: đọc to từng slide — câu nào vấp là câu phải sửa.

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
- Deck lớp học ít chữ, thẻ màu gốc, notes đầy đủ cho giáo viên.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
