---
name: deck-acid-agency-deck
description: Style deck "Acid Agency" cho hệ deck-studio — Năng lượng agency: trường màu acid chanh–cam–tím, chữ condensed khổng lồ, ảnh retro desktop. Dùng khi làm proposal/deck sáng tạo cần năng lượng cao, chữ condensed cực lớn và ảnh retro. Theme có sẵn: ~/workspace/deck-studio/themes/acid-agency-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Acid Agency — Năng lượng agency: trường màu acid chanh–cam–tím, chữ condensed khổng lồ, ảnh retro desktop

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Acid Agency Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/acid-agency-deck.json` (bg #F4F1EA, nhấn #FF6A00).

## Khi nào dùng
- Team làm proposal cho product discovery sprint hoặc pitch ý tưởng sáng tạo.
- Nhóm muốn một ngôn ngữ hình ảnh nhất quán, nổi bật qua nhiều trang.
- Người có thông điệp và khán giả rõ ràng, cần deck gây ấn tượng ngay trang đầu.

## Nguyên lý cốt lõi
- Mỗi slide một trường màu — nhịp màu là cấu trúc điều hướng của deck.
- Chữ phải thắng ảnh: tiêu đề condensed luôn đè lên hoặc cắt ngang khung ảnh.
- Giữ tối đa 3 màu acid; thêm màu thứ tư là vỡ hệ.

## Hệ hình ảnh
- Ba trường màu acid thay nhau làm nền từng slide: chanh (lime), cam cháy, tím điện.
- Chữ condensed (Anton) cỡ khổng lồ, thường đặt trong khối trắng cắt ngang ảnh.
- Ảnh phong cách retro desktop/still-life bão hòa, khung bo tròn lớn.
- Nhãn pill nhỏ viền đen ở góc, chữ mono viết hoa cho metadata.
- Trang trí của theme: decor `band`, bo góc 18px, mật độ standard. Acid fields (lime/orange/violet) behind oversized condensed type; retro desktop photography in big rounded frames.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/acid-agency-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/acid-agency-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Ảnh dùng layout `image` full-bleed hoặc chèn vào spec như ảnh minh họa cỡ lớn; crop sẵn 16:9.
- Đổi trường màu theo slide bằng cách tách deck thành các section — theme giữ một accent chính (cam), lime dùng cho khối nhấn.

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
- Bộ layout tái dùng được (cover, section, content, data, closing) trong cùng hệ acid.
- Deck HTML studio + PPTX editable, notes đầy đủ từng slide.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
