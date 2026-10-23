---
name: deck-primary-doodle-deck
description: Style deck "Primary Doodle" cho hệ deck-studio — Trang vở trắng, doodle màu gốc, mũi tên vẽ tay — giải thích thân thiện. Dùng khi làm deck giải thích khái niệm kiểu doodle màu gốc trên trang vở trắng, thân thiện với người mới bắt đầu. Theme có sẵn: ~/workspace/deck-studio/themes/primary-doodle-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Primary Doodle — Trang vở trắng, doodle màu gốc, mũi tên vẽ tay — giải thích thân thiện

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Primary Doodle Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/primary-doodle-deck.json` (bg #FFFFFF, nhấn #0B4BD6).

## Khi nào dùng
- Onboarding nhân viên mới, hướng dẫn sử dụng.
- Bài giảng nhập môn, chuỗi '101'.
- Giải thích quy trình cho khách hàng không chuyên.

## Nguyên lý cốt lõi
- Giải thích như cho bạn mới vào nghề: mỗi khái niệm một ví dụ đời thường.
- Doodle phải minh họa đúng nội dung trang — doodle trang trí vô nghĩa bị loại ở QA.
- Kết mỗi phần bằng một câu 'nhớ một điều này' (one takeaway).

## Hệ hình ảnh
- Nền trắng như trang vở; doodle nét tay ba màu gốc (xanh dương, đỏ, vàng) quanh nội dung.
- Mũi tên vẽ tay nối các bước — là hệ điều hướng của style.
- Chữ Baloo 2 tròn mực đen; từ khóa khoanh tròn bằng nét doodle.
- Không ảnh stock; hình là doodle hoặc sơ đồ vẽ tay đơn giản.
- Trang trí của theme: decor `none`, bo góc 16px, mật độ standard. White notebook field, primary-colour doodles, hand-drawn arrows; friendly explainer system.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/primary-doodle-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/primary-doodle-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Doodle chuẩn bị dạng ảnh PNG nét tay nền trong/trắng; layout `two-col` cho cặp khái niệm–ví dụ.
- Giữ số doodle ≤ 3 mỗi slide để trang vở không thành bãi chiến trường.

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
- Deck giải thích có nhịp khái niệm → ví dụ → takeaway từng phần.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
