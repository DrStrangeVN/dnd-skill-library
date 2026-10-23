---
name: deck-research-paper-deck
description: Style deck "Research Paper" cho hệ deck-studio — Bài báo nghiên cứu trên nền xanh sâu: hình là trung tâm, caption có trích dẫn. Dùng khi biến một bài báo nghiên cứu thành deck mà hình/biểu đồ là trung tâm và mọi hình đều có caption truy nguồn. Theme có sẵn: ~/workspace/deck-studio/themes/research-paper-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Research Paper — Bài báo nghiên cứu trên nền xanh sâu: hình là trung tâm, caption có trích dẫn

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Research Paper Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/research-paper-deck.json` (bg #0C3B2E, nhấn #E8A317).

## Khi nào dùng
- Journal club, seminar đọc paper.
- Trình bày lại nghiên cứu của nhóm khác một cách trung thực.
- Ôn tập tài liệu cho kỳ thi/hội đồng.

## Nguyên lý cốt lõi
- Figure-first: chọn 3–5 hình quyết định của paper trước, deck xây quanh chúng — không tóm tắt tuyến tính từ abstract.
- Dữ liệu minh họa (illustrative) phải ghi nhãn minh họa; số thật ghi rõ bảng/hình nguồn.
- Cuối deck có danh sách truy vết: mỗi claim trên slide ↔ đoạn/hình tương ứng trong paper.

## Hệ hình ảnh
- Nền xanh lá sâu như bìa tạp chí học thuật; chữ ngà serif.
- Trang hình (figure page): một hình chiếm phần lớn trang, panel nền bạc hà nhạt chứa hình gốc.
- Caption dưới MỌI hình: mô tả + trích dẫn (tác giả, năm, hình số mấy).
- Điểm nhấn hổ phách (amber) cho kết quả chính và số liệu khóa.
- Trang trí của theme: decor `none`, bo góc 0px, mật độ standard. Deep green paper deck: figure-first pages, amber highlights, captions with citations under every figure.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/research-paper-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/research-paper-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Hình cắt từ PDF paper ở độ phân giải cao; đặt trên surface nhạt mô phỏng panel bạc hà.
- Trang claim dùng `content`; trang hình dùng `image` với caption đầy đủ nguồn.

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
- Deck paper: câu hỏi → phương pháp (1 trang) → các trang hình → kết luận → giới hạn → danh sách truy vết.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
