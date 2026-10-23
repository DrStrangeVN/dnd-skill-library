---
name: deck-mint-marker-deck
description: Style deck "Mint Marker" cho hệ deck-studio — Vệt bút dạ bạc hà trên giấy kem — deck workshop như trang bảng chụp lại. Dùng khi làm deck tổng kết workshop/playbook với vệt highlight dạ quang bạc hà và ảnh chụp buổi làm việc. Theme có sẵn: ~/workspace/deck-studio/themes/mint-marker-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Mint Marker — Vệt bút dạ bạc hà trên giấy kem — deck workshop như trang bảng chụp lại

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Mint Marker Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/mint-marker-deck.json` (bg #F7F4EC, nhấn #2FA89A).

## Khi nào dùng
- Tổng kết workshop/sprint cho người vắng mặt.
- Playbook cách làm việc của team.
- Tài liệu onboarding mộc, gần gũi.

## Nguyên lý cốt lõi
- Deck phải giữ được chất 'vừa làm xong workshop': trích đúng câu chữ từ bảng/giấy note của buổi làm việc.
- Mỗi trang một quyết định hoặc một bài học — trang nào chỉ 'không khí' thì cắt.
- Highlight chỉ quét từ khóa thật quan trọng; quét nhiều = không còn điểm nhấn.

## Hệ hình ảnh
- Nền giấy kem; vệt highlight bút dạ bạc hà (mint marker) quét dưới các từ khóa — trang trí duy nhất.
- Ảnh chụp workshop thật (bảng, giấy note, tay người) xen kẽ trang chữ.
- Chữ grotesk đen mộc, không hiệu ứng; mũi tên vẽ tay mảnh nối ý.
- Số trang và nhãn phần viết kiểu ghi chú lề sổ.
- Trang trí của theme: decor `none`, bo góc 8px, mật độ airy. Hand-drawn marker system on cream: mint highlighter strokes, workshop photographs, plain grotesk.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/mint-marker-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/mint-marker-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Highlight mô phỏng bằng accent bạc hà trên thẻ/kicker; khi cần giống bản gốc hơn, chèn ảnh chụp bảng thật ở layout `image`.
- Layout `content` với bullets là các câu nguyên văn từ workshop (ghi rõ nguồn trong notes).

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
- Deck tổng kết ~8–10 trang: mục tiêu buổi → diễn biến → quyết định → bài học → việc tiếp theo.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
