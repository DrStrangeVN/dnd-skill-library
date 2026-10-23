---
name: deck-cobalt-growth-deck
description: Style deck "Cobalt Growth" cho hệ deck-studio — Nền cobalt phủ kín, chữ ma (ghost word) khổng lồ, ảnh người trong thẻ bo tròn cực lớn. Dùng khi làm deck chương trình tăng trưởng/học thực hành trên nền cobalt với chữ ghost và ảnh người khổ lớn. Theme có sẵn: ~/workspace/deck-studio/themes/cobalt-growth-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Cobalt Growth — Nền cobalt phủ kín, chữ ma (ghost word) khổng lồ, ảnh người trong thẻ bo tròn cực lớn

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Cobalt Growth Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/cobalt-growth-deck.json` (bg #2542D8, nhấn #D9F45C).

## Khi nào dùng
- Chương trình thực hành/tăng trưởng dựa trên bằng chứng (evidence-based).
- Đội ngũ huấn luyện, cộng đồng học tập, chương trình nghề.
- Người muốn deck năng lượng cao nhưng vẫn nghiêm túc.

## Nguyên lý cốt lõi
- Cobalt là sân khấu, con người là diễn viên: ảnh người thật chiếm diện tích lớn nhất có thể.
- Ghost word chỉ dùng cho 1–2 từ khóa của chương trình — dùng nhiều sẽ thành nhiễu.
- Mạch nội dung: niềm tin thực hành → bằng chứng từng buổi → ai làm được → tham gia thế nào.

## Hệ hình ảnh
- Toàn bộ deck chìm trong nền cobalt bão hòa; không có slide nền trắng.
- Một 'ghost word' xanh nhạt cực lớn chạy nền một vài slide chủ chốt.
- Ảnh con người trong thẻ bo tròn cực lớn (~28px), đặt lệch lưới.
- Pill trắng và pill chanh (lime) làm nhãn; chữ trắng grotesk đậm.
- Trang trí của theme: decor `none`, bo góc 28px, mật độ standard. Full cobalt field; one huge pale ghost word per deck; pills in white/lime; people photography in oversized rounded cards.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/cobalt-growth-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/cobalt-growth-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Ảnh người cắt sẵn trên nền cobalt hoặc nền trong suốt; layout `image` cho trang người học tiêu biểu.
- Ghost word mô phỏng bằng tiêu đề kicker cỡ lớn trong spec — đọc QA để tránh tràn chữ.

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
- Deck chương trình cobalt toàn phần với trang bằng chứng và trang kêu gọi tham gia.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
