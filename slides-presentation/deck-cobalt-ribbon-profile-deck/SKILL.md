---
name: deck-cobalt-ribbon-profile-deck
description: Style deck "Cobalt Ribbon Profile" cho hệ deck-studio — Hồ sơ cobalt với dải ruy-băng xanh chạy xuyên suốt và các chồng số liệu căn giữa. Dùng khi làm company profile/hồ sơ năng lực xanh cobalt với ribbon chạy suốt và số liệu căn giữa trang trọng. Theme có sẵn: ~/workspace/deck-studio/themes/cobalt-ribbon-profile-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Cobalt Ribbon Profile — Hồ sơ cobalt với dải ruy-băng xanh chạy xuyên suốt và các chồng số liệu căn giữa

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Cobalt Ribbon Profile Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/cobalt-ribbon-profile-deck.json` (bg #0B3D91, nhấn #66A3FF).

## Khi nào dùng
- Hồ sơ studio/công ty sáng tạo số (digital studio profile).
- Giới thiệu năng lực cho đối tác doanh nghiệp.
- Cập nhật quý dạng profile ngắn.

## Nguyên lý cốt lõi
- Đối xứng và tĩnh tại là thông điệp: hồ sơ này nói 'ổn định, đáng tin'.
- Số liệu xếp chồng theo thứ tự quan trọng giảm dần; tối đa 4 số/trang.
- Ribbon không bao giờ cắt qua chữ — luôn chạy ở biên hoặc nền sau panel.

## Hệ hình ảnh
- Nền cobalt sâu; một dải ruy-băng (ribbon) đồ họa chạy xuyên các slide như sợi chỉ liên kết.
- Bố cục căn giữa đối xứng: kicker → tiêu đề → cụm số liệu xếp chồng.
- Mark/logo chỉ dùng glyph hình học (không chữ) ở góc cố định.
- Chữ trắng và xanh nhạt hai tông; không màu ngoài phổ xanh.
- Trang trí của theme: decor `band`, bo góc 0px, mật độ standard. Deep cobalt pages with a continuous blue ribbon graphic; centered kicker/title/stat stacks; glyph-only marks.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/cobalt-ribbon-profile-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/cobalt-ribbon-profile-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Có 4 preset accent trong bản gốc — tương đương: nhân bản theme đổi dải xanh (royal → sky → navy → ice), giữ bố cục.
- Trang số liệu dùng layout `data` căn giữa sẵn có của engine.

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
- Profile ~10 archetype trang: bìa, giới thiệu, dịch vụ, số liệu, quy trình, đội, dự án, đối tác, cam kết, liên hệ.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
