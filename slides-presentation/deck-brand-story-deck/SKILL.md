---
name: deck-brand-story-deck
description: Style deck "Brand Story" cho hệ deck-studio — Đen biên tập tương phản cao, chữ condensed kem + chanh acid — kể chuyện thương hiệu. Dùng khi kể câu chuyện thương hiệu/định vị dạng tạp chí: nguồn gốc, niềm tin, mã hình ảnh, tương lai. Theme có sẵn: ~/workspace/deck-studio/themes/brand-story-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Brand Story — Đen biên tập tương phản cao, chữ condensed kem + chanh acid — kể chuyện thương hiệu

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Brand Story Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/brand-story-deck.json` (bg #101010, nhấn #D8F526).

## Khi nào dùng
- Brand designer trình bày rationale của một hệ nhận diện.
- Marketer/product team dựng câu chuyện định vị hoặc launch narrative.
- Team muốn biến bài thuyết trình brand thường thành một chuỗi trang tạp chí.

## Nguyên lý cốt lõi
- Kể theo xương sống truyện: origin → friction → belief → visual codes → expression → future. Không nhảy cóc.
- Mỗi slide đúng một câu tuyên bố (one statement per slide); phần giải thích để ở notes.
- Màu/typography trên trang visual-codes phải khớp tuyệt đối với theme đang dùng.

## Hệ hình ảnh
- Nền đen; chữ condensed kem (Anton) cỡ tạp chí, một từ khóa nhuộm chanh acid (chartreuse).
- Thân bài serif dễ đọc (Playfair) — cặp condensed + serif là chữ ký của style.
- Một motif tem tròn đỏ (stamp) dùng tiết kiệm như dấu đóng của brand.
- Trang mã hình ảnh (visual codes) trình bày palette/type/motif như trang tạp chí.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ standard. Black editorial field, cream condensed display over acid chartreuse; one red stamp motif per deck.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/brand-story-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/brand-story-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `section` cho các chương của câu chuyện; `quote` cho trang manifesto.
- Tem đỏ là accent2 — chỉ xuất hiện tối đa 1 lần/deck, đặt ở slide tuyên ngôn hoặc closing.

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
- Deck câu chuyện thương hiệu có notes xuyên suốt, gồm trang manifesto và trang visual codes.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
