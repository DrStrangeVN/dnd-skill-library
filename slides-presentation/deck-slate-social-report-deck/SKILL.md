---
name: deck-slate-social-report-deck
description: Style deck "Slate Social Report" cho hệ deck-studio — Báo cáo xám lạnh, tiêu đề xanh cobalt khổng lồ, ảnh đội ngũ cắt nền đen trắng. Dùng khi làm báo cáo social media/content theo quý với ảnh team cắt nền và nhãn pill nghiêng vui nhộn. Theme có sẵn: ~/workspace/deck-studio/themes/slate-social-report-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Slate Social Report — Báo cáo xám lạnh, tiêu đề xanh cobalt khổng lồ, ảnh đội ngũ cắt nền đen trắng

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Slate Social Report Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/slate-social-report-deck.json` (bg #F1F1EF, nhấn #4C54F2).

## Khi nào dùng
- Báo cáo social/content quý cho sếp hoặc khách hàng.
- Tổng kết chiến dịch nhiều kênh.
- Review team content định kỳ.

## Nguyên lý cốt lõi
- Báo cáo quý phải trả lời: kênh nào tạo giá trị, kênh nào ngốn sức — và đề xuất cắt/thêm rõ ràng ở trang cuối.
- Số liệu luôn so với quý trước (QoQ) và ghi rõ nguồn export; không số 'ước lượng cảm tính'.
- Pill nghiêng là gia vị: tối đa 2 pill/trang, nội dung pill phải là thông tin thật (trạng thái, deadline).

## Hệ hình ảnh
- Nền xám lạnh phẳng; tiêu đề xanh cobalt (electric blue) cỡ rất lớn mở mỗi phần.
- Ảnh người cắt nền (cut-out) đen trắng — cả đội cùng một xử lý.
- Nhãn pill nhỏ đặt NGHIÊNG vài độ chứa trạng thái/hài hước nội bộ (kiểu 'vẫn đang load…').
- Bảng số liệu xám–trắng sạch, một cột highlight xanh mỗi bảng.
- Trang trí của theme: decor `none`, bo góc 12px, mật độ standard. Cool grey report field, oversized blue display, B/W cut-out team photos, tilted pill labels.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/slate-social-report-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/slate-social-report-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Ảnh team xử lý grayscale + cắt nền trước; layout `chart` cho biểu đồ tăng trưởng kênh.
- Pill nghiêng là chi tiết ảnh gốc — trong engine thay bằng kicker pill thẳng, ghi rõ khác biệt ở QA note.

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
- Báo cáo ~9 trang: bìa quý → tổng quan → từng kênh → nội dung nổi bật → bài học → kế hoạch quý sau.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
