---
name: engraving-editorial-video
description: Video biên tập trang trọng với tranh khắc etching đen trắng và serif cổ điển — dùng cho triết lý, lịch sử tư tưởng, câu chuyện kinh điển cần chiều sâu.
---

# Phim tranh khắc biên tập (Engraving Editorial)

## Khi nào dùng
- Nội dung triết học, thần thoại, lịch sử tư tưởng, văn học kinh điển —
  cần không khí trang trọng như trang sách cổ.
- Khán giả xem ngang, chấp nhận nhịp chậm.
- Không dùng cho bán hàng, tin nhanh hay nội dung hài.

## Mẫu gốc đã phân tích
- File: `theseus.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/theseus.mp4`
- Khổ/fps/thời lượng: 1280×720 @30fps, ~156 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/theseus.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu) — CHỈ 3 màu trong toàn video:
  - Giấy kem `#F4EDDC`
  - Đen mực `#1A1714`
  - Đỏ `#A62B25` (con dấu sáp, quote)
- Font: Playfair Display (serif display) cho tiêu đề và trích dẫn;
  chữ thân bài serif cổ điển.
- Hình ảnh: tranh khắc etching đen trắng (nét hatching) — tuyệt đối
  không dùng ảnh màu hay ảnh AI màu.
- Thành phần đặc trưng:
  - Quote italic màu đỏ đặt trang trọng giữa trang
  - Con dấu sáp đỏ ở thẻ mở/kết chương
  - Bố cục biên tập kiểu trang sách: cột chữ, khoảng trắng rộng,
    drop cap ở đoạn mở chương
- Chuyển động: fade chậm, pan nhẹ trên tranh khắc; không hiệu ứng
  nảy/pop kiểu short-form.

## Cấu trúc kịch bản
- Mở: 1 trích dẫn hoặc 1 nghịch lý kinh điển đặt giữa trang (quote đỏ).
- Thân: các mục như chương sách — mỗi chương 1 tranh khắc + 1 đoạn
  luận ngắn.
- Kết: quay lại trích dẫn mở đầu (nay đã đổi nghĩa sau khi nghe hết)
  hoặc 1 quote kết đọng.
- Câu văn trau chuốt, nhịp chậm: ~50–70 từ cho 30 giây.

## Quy trình sản xuất
1. Kịch bản: trích dẫn phải đúng nguyên văn và ghi nguồn tác phẩm
   trong ghi chú sản xuất; tránh câu văn kiểu mạng xã hội.
2. Voice: VieNeu local — preset v3 Turbo giọng trầm trang trọng,
   speed 1.0.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `engraving-editorial-video`. Tranh khắc chọn/tạo theo bộ asset đen
   trắng, xử lý về đúng 2 tông đen–kem trước khi dựng.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/theseus.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `engraving-editorial-video__<chu-de>.mp4`.

## QA checklist
- [ ] Toàn video chỉ có 3 màu: kem, đen, đỏ — không lọt màu thứ tư
- [ ] Mọi hình đều là tranh khắc đen trắng, không ảnh màu
- [ ] Tiêu đề dùng Playfair Display; quote italic đỏ đúng vị trí trang trọng
- [ ] Con dấu sáp đỏ chỉ xuất hiện ở thẻ mở/kết chương
- [ ] Trích dẫn khớp nguyên văn nguồn, có ghi tác phẩm/tác giả
- [ ] Nhịp chuyển cảnh chậm (fade ≥0,8 giây), không hiệu ứng pop/nảy
