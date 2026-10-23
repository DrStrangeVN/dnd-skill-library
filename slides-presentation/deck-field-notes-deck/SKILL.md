---
name: deck-field-notes-deck
description: Style deck "Field Notes" cho hệ deck-studio — Sổ tay hiện trường: bìa ảnh toàn khung, thẻ sage bo tròn, chữ tĩnh. Dùng khi làm deck nhật ký/báo cáo hiện trường với ảnh chụp thực địa toàn khung và thẻ ghi chép bo tròn. Theme có sẵn: ~/workspace/deck-studio/themes/field-notes-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Field Notes — Sổ tay hiện trường: bìa ảnh toàn khung, thẻ sage bo tròn, chữ tĩnh

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Field Notes Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/field-notes-deck.json` (bg #FFFFFF, nhấn #3E7CB1).

## Khi nào dùng
- Báo cáo thực địa môi trường/nông nghiệp/xây dựng.
- Nhật ký dự án cộng đồng tại hiện trường.
- Tổng kết chuyến khảo sát cho team văn phòng.

## Nguyên lý cốt lõi
- Ảnh hiện trường là dữ kiện: mỗi ảnh ghi ngày, nơi, điều kiện ngay trong caption.
- Ghi chép tách rõ quan sát (thấy gì) và diễn giải (nghĩa là gì) — hai cột hoặc hai đoạn riêng.
- Không làm đẹp số liệu hiện trường; số thô ghi kèm phương pháp đo.

## Hệ hình ảnh
- Bìa và các trang mở phần là ảnh hiện trường toàn khung (full-frame).
- Trang trong: thẻ trắng/xanh sage bo tròn lớn chứa ghi chép, như trang sổ tay.
- Tiêu đề grotesk trầm, không hiệu ứng; nhãn mono cho ngày/địa điểm/tọa độ.
- Bảng màu mượn từ hiện trường: sage, đất, trời nhạt.
- Trang trí của theme: decor `none`, bo góc 22px, mật độ airy. Notebook deck: full-frame field photography covers, sage-green rounded cards inside, quiet grotesk.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/field-notes-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/field-notes-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Layout `image` cho ảnh toàn khung kèm caption có metadata; `two-col` cho cặp quan sát–diễn giải.
- Ảnh giữ nguyên màu gốc; tránh filter làm sai lệch bằng chứng.

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
- Deck hiện trường: bản đồ/lộ trình → quan sát theo điểm → diễn giải → việc cần làm tiếp.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
