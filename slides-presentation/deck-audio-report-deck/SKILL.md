---
name: deck-audio-report-deck
description: Style deck "Audio Report (Narrated)" cho hệ deck-studio — Deck có lời thuyết minh: mỗi trang một kịch bản đọc lưu trong speaker notes. Dùng khi biến báo cáo, tài liệu hoặc link thành deck có lời đọc (narration) từng trang để nghe thay vì đọc. Theme có sẵn: ~/workspace/deck-studio/themes/audio-report-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Audio Report (Narrated) — Deck có lời thuyết minh: mỗi trang một kịch bản đọc lưu trong speaker notes

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Narrated Report Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/audio-report-deck.json` (bg #F6F1E2, nhấn #1E8FB8).

## Khi nào dùng
- Biến báo cáo dài/paper thành bản nghe được khi di chuyển.
- Team chia sẻ update/review dạng deck tự chạy có thuyết minh.
- Người cần cùng một nội dung ở nhiều ngôn ngữ/giọng đọc.

## Nguyên lý cốt lõi
- Kịch bản đọc của mỗi trang lưu trong `notes`, viết để NÓI (câu ngắn, có câu chuyển), không sao chép nguyên văn chữ trên slide.
- Một trang một ý; trang nào cần đọc quá ~45 giây thì tách làm hai.
- Thứ tự nghe phải tuyến tính: không slide phụ thuộc vào việc quay lại slide trước.

## Hệ hình ảnh
- Style trung tính về hình: dùng BẤT KỲ theme deck-studio nào; theme mặc định ở đây là kem storybook (ảnh minh họa trung tâm, chữ grotesk đen, khối xanh nhỏ).
- Mỗi slide phải tự đứng vững khi chỉ nghe: tiêu đề nói đúng nội dung, không phụ thuộc chữ nhỏ trên hình.
- Nhãn READ / LISTEN hoặc tương đương ở bìa để người nhận biết định dạng.
- Trang trí của theme: decor `none`, bo góc 2px, mật độ standard. Cream storybook default theme; the style itself is theme-agnostic — narration script lives in speaker notes.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/audio-report-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/audio-report-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Quy trình: chốt theme (skill deck-* bất kỳ) → viết spec với `notes` = kịch bản đọc → build như deck thường → tổng hợp giọng đọc từ notes bằng pipeline TTS của máy (VieNeu) nếu cần file audio.
- Đặt tên file audio theo số slide (01.mp3, 02.mp3…) để ghép với bản trình chiếu.

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
- Deck editable kèm kịch bản đọc hoàn chỉnh trong notes của mọi trang.
- Danh sách trang + thời lượng đọc ước tính trong QA note khi bàn giao.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
