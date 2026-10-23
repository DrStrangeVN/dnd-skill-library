---
name: law-explainer-video
description: Video dọc giải thích văn bản luật mới trên nền navy viền vàng với con dấu hiệu lực — dùng cho kênh pháp luật, phổ biến nghị định/thông tư mới tới người dân và doanh nghiệp.
---

# Giải thích luật mới (Law Explainer)

## Khi nào dùng
- Phổ biến 1 văn bản pháp luật mới (nghị định, thông tư, luật) ảnh
  hưởng trực tiếp tới người dân/doanh nghiệp.
- Yêu cầu chính xác tuyệt đối về số hiệu, điều khoản, ngày hiệu lực —
  sai một con số là sai cả video.
- Không dùng để tư vấn pháp lý cho trường hợp cá nhân cụ thể.

## Mẫu gốc đã phân tích
- File: `nd-356-du-lieu.mp4` (chủ đề mẫu: nghị định về dữ liệu)
- Lưu tại: `~/workspace/reelcrew-analysis/videos/nd-356-du-lieu.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~65 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/nd-356-du-lieu.jpg`
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N → thẻ kết
  luận/CTA, bọc trong skin pháp luật.

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền navy tối `#0E1B30`, viền vàng `#C9A227`
  - Chữ trắng/vàng
  - Giấy văn bản sáng đặt trong khung vàng
- Font: Playfair Display (serif) cho tiêu đề và số điều — tạo cảm
  giác văn bản chính thống.
- Thẻ văn bản: trích điều luật đặt như trang văn bản; đoạn đang
  giảng được đánh dấu trong thẻ.
- Con dấu "CÓ HIỆU LỰC": stamp đỏ đóng lên thẻ khi nói tới hiệu
  lực/ngày áp dụng — thành phần nhận diện của skin, không dùng
  trang trí ở thẻ khác.
- Mascot: cú học giả (đeo kính) ở góc thẻ.
- Phụ đề: bar đen chữ vàng ở dưới, có GẠCH VÀNG ở mép trái của bar.

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề): tên văn bản + số hiệu + 1 câu "ai bị ảnh hưởng"
  trong 5 giây đầu.
- Thân: 3–4 bước — mỗi bước 1 quy định/điều cụ thể theo mạch: nội
  dung điều → dịch sang ngôn ngữ thường → ai phải làm gì (badge n/N).
- Kết (thẻ kết luận): ngày hiệu lực (đóng dấu "CÓ HIỆU LỰC") + danh
  sách việc cần làm ngắn gọn.
- Phần trích dẫn và phần diễn giải phải tách bạch trong kịch bản.

## Quy trình sản xuất
1. Kịch bản: đọc văn bản gốc (PDF/cổng thông tin chính phủ) trước
   khi viết; trích điều phải nguyên văn, ghi rõ số điều/khoản nguồn
   trong ghi chú sản xuất.
2. Voice: VieNeu local — preset v3 Turbo giọng trầm trang trọng,
   speed 1.0.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `law-explainer-video`. Thẻ văn bản dựng từ đúng điều luật được
   trích; stamp hiệu lực animate đóng dấu tại thẻ kết.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/nd-356-du-lieu.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `law-explainer-video__<chu-de>.mp4`.

## QA checklist
- [ ] Số hiệu văn bản, số điều, ngày hiệu lực khớp 100% văn bản gốc (đối chiếu từng ký tự)
- [ ] Con dấu "CÓ HIỆU LỰC" chỉ đóng ở thẻ nói về hiệu lực — không dùng trang trí
- [ ] Phụ đề bar đen chữ vàng + gạch vàng mép trái ở mọi câu
- [ ] Tiêu đề/số điều dùng Playfair Display; trích dẫn tách rõ với diễn giải trong lời đọc
- [ ] Mascot cú học giả nhất quán, không đổi nhân vật giữa video
- [ ] Không có lời khuyên pháp lý cá nhân hoá — chỉ phổ biến nội dung văn bản
