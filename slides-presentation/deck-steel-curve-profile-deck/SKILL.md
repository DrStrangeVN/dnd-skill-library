---
name: deck-steel-curve-profile-deck
description: Style deck "Steel Curve Profile" cho hệ deck-studio — Trang băng trắng, panel thép xanh, khung ảnh cong, thẻ số liệu bo tròn. Dùng khi làm profile công ty kỹ thuật/công nghiệp với panel thép xanh và khung ảnh cong mềm. Theme có sẵn: ~/workspace/deck-studio/themes/steel-curve-profile-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Steel Curve Profile — Trang băng trắng, panel thép xanh, khung ảnh cong, thẻ số liệu bo tròn

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Steel Curve Profile Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/steel-curve-profile-deck.json` (bg #F2F6F8, nhấn #4A7188).

## Khi nào dùng
- Công ty công nghiệp, kỹ thuật, logistics giới thiệu năng lực.
- Cập nhật quý cho đối tác/nhà phân phối.
- Tài liệu đào tạo vận hành dùng chung giao diện.

## Nguyên lý cốt lõi
- Mềm ở hình, cứng ở số: ngôn ngữ cong thân thiện nhưng số liệu kỹ thuật phải chính xác, có đơn vị và chuẩn tham chiếu.
- Cấu trúc profile cố định như Blue Block (giới thiệu → dịch vụ → vận hành → số liệu → đội → liên hệ) nhưng giọng hiện đại hơn.
- Ảnh nhà máy/thiết bị/đội kỹ thuật thật; ảnh stock công nghiệp chung chung bị loại ở QA.

## Hệ hình ảnh
- Nền trắng băng (ice white); panel thép xanh (steel blue) cho các khối chính.
- Khung ảnh cong (curved frame): ảnh bo góc rất lớn, một cạnh cong mạnh như đường ống/kết cấu thép.
- Thẻ số liệu bo tròn trắng viền băng; dấu ba chấm (triple-dot) là mark lặp lại.
- Chữ grotesk mực thép trầm; kicker mono viết hoa.
- Trang trí của theme: decor `dots`, bo góc 24px, mật độ standard. Ice-white pages, steel-blue panels, curved image frames, rounded metric cards, triple-dot accent mark.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/steel-curve-profile-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/steel-curve-profile-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Có 4 preset accent trong bản gốc — nhân bản theme đổi dải thép (steel → slate → teal → navy) khi cần biến thể.
- Khung cong: engine bo góc đều (radius 24) — cong một cạnh là chi tiết ảnh, chuẩn bị ảnh đã bo cong sẵn nếu muốn giống bản gốc.

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
- Profile ~10 archetype trang với thẻ số liệu bo tròn và ảnh khung cong.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
