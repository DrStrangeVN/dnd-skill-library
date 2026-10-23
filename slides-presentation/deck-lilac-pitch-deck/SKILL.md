---
name: deck-lilac-pitch-deck
description: Style deck "Lilac Pitch" cho hệ deck-studio — Pitch oải hương thoáng: trang tím nhạt thưa chữ, bìa kính tím sâu. Dùng khi làm pitch deck tông oải hương nhẹ, nhiều khoảng thở cho sản phẩm tiêu dùng/wellness/sáng tạo. Theme có sẵn: ~/workspace/deck-studio/themes/lilac-pitch-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Lilac Pitch — Pitch oải hương thoáng: trang tím nhạt thưa chữ, bìa kính tím sâu

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Lilac Glass Pitch Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/lilac-pitch-deck.json` (bg #ECE7FA, nhấn #7B3FE4).

## Khi nào dùng
- Startup sản phẩm tiêu dùng, wellness, giáo dục, sáng tạo.
- Pitch vòng sớm cho nhà đầu tư thiên về brand.
- Giới thiệu sản phẩm cần cảm giác 'dễ thở' khác biệt với pitch đen–xanh thông thường.

## Nguyên lý cốt lõi
- Nhẹ là chiến lược: pitch này thuyết phục bằng sự dễ chịu và rõ ràng, không bằng áp lực thị giác.
- Số liệu vẫn phải cứng: traction, doanh thu, giữ chân — trình bày trên thẻ trắng để đọc rõ.
- Một deck một tông tím; không trộn thêm màu nóng ngoài ảnh sản phẩm thật.

## Hệ hình ảnh
- Trang nội dung tím oải hương rất nhạt, chữ tím than, khoảng trắng lớn.
- Bìa bản gốc là kính tím sâu (deep-violet glass) — tương đương ở đây: dùng bìa ảnh gradient tím đậm qua layout `image` hoặc nhân bản theme đảo nền (xem Kỹ thuật).
- Thẻ trắng bo tròn mềm chứa số liệu; bóng đổ tím rất nhẹ.
- Chuyển sắc (gradient) tím nhạt dùng ở trang section như hơi thở giữa các phần.
- Trang trí của theme: decor `none`, bo góc 22px, mật độ airy. Spacious lilac pages, deep-violet glass cover in the original; airy grotesk, soft gradients between sections.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/lilac-pitch-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/lilac-pitch-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Bìa kính tím: hoặc (a) dùng theme này với ảnh bìa gradient tím đậm ở slide cover dạng `image`, hoặc (b) copy theme thành biến thể đảo nền #1B0B33 cho riêng bìa/closing bằng hai lần build — ghi rõ lựa chọn trong QA note.
- Layout `data` trên thẻ surface trắng cho trang traction.

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
- Pitch ~9 trang: bìa, vấn đề, sản phẩm, thị trường, traction, mô hình, đội, ask, liên hệ.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
