---
name: deck-botanical-quiet-deck
description: Style deck "Botanical Quiet" cho hệ deck-studio — Giấy xanh phấn, lá teal phẳng, điểm hồng đào — deck tĩnh cho quan sát chậm. Dùng khi làm deck nhẹ, tĩnh, nhiều khoảng thở cho chủ đề thiên nhiên, quan sát, nhật ký hoặc workshop chậm. Theme có sẵn: ~/workspace/deck-studio/themes/botanical-quiet-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Botanical Quiet — Giấy xanh phấn, lá teal phẳng, điểm hồng đào — deck tĩnh cho quan sát chậm

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Botanical Quiet Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/botanical-quiet-deck.json` (bg #F7FAFB, nhấn #0A93B2).

## Khi nào dùng
- Nhật ký quan sát chậm, journal thiên nhiên.
- Workshop về chú ý/quan sát, nội dung chữa lành nhẹ.
- Người làm nội dung muốn deck như một cuốn sổ tay minh họa.

## Nguyên lý cốt lõi
- Ít chữ tối đa: một slide một quan sát, để khoảng trắng làm nhịp thở.
- Hình vẽ/minh họa tự làm mới hoặc có licence rõ — style này sống bằng hình.
- Không số liệu ồn ào; khi cần số, đặt nhỏ ở chân slide.

## Hệ hình ảnh
- Nền giấy xanh phấn (powder blue) hoặc trắng; tán lá teal phẳng (flat foliage) là họa tiết chính.
- Điểm nhấn hồng đào (peach) rất ít: một cành hoa, một chi tiết trong hình.
- Tiêu đề bản gốc là script tay mảnh — bản house dùng Playfair italic để giữ vẻ mềm và đọc được tiếng Việt.
- Nhân vật/vật thể vẽ nét nâu scratchy, mảnh; chữ thân bài nhỏ, thưa.
- Trang trí của theme: decor `none`, bo góc 6px, mật độ airy. Powder-blue paper, flat teal foliage, peach accents; display face stands in for the original delicate hand script.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/botanical-quiet-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/botanical-quiet-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Ưu tiên layout `image` và `quote`; tránh `data`/`chart` dày đặc.
- Script tay không có font tiếng Việt đầy đủ dấu trên máy — không ép dùng font script cho tiêu đề tiếng Việt.

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
- Deck tĩnh, thưa chữ, hình vẽ dẫn dắt; notes viết như lời dẫn chậm.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
