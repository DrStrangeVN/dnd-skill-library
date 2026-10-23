---
name: talking-head-highlight-video
description: Cắt highlight dọc từ video nói chuyện dài (podcast, talk, webinar) — dùng để tái chế nội dung dài thành clip ngắn có hook, jump-cut và caption karaoke.
---

# Cắt highlight video nói chuyện (Talking Head Highlight)

## Khi nào dùng
- Có sẵn video nói chuyện dài (podcast, phỏng vấn, livestream, webinar)
  và cần rút các đoạn hay thành clip dọc đăng short.
- Đây là hậu kỳ cắt dựng — không sản xuất từ kịch bản.
- Không dùng khi chưa có footage gốc.

## Mẫu gốc đã phân tích
- Không có file mẫu trên site — đặc tả theo mô tả sản phẩm ReelCrew
  + changelog 0.2.34.
- Nguồn mô tả: https://reelcrew.io/#video (mục Talking Head Highlight).
- Không có file tương ứng trong `~/workspace/reelcrew-analysis/videos/`
  và không có contact sheet mẫu để đối chiếu.
- Khổ đầu ra theo mô tả sản phẩm: 720×1280 @30fps.

## Đặc tả thiết kế
- Nguồn vào: video nói chuyện ngang hoặc dọc; đầu ra cắt dọc 720×1280,
  mặt người nói ở nửa trên khung.
- Hook: câu mạnh nhất của đoạn được đưa lên 2 giây đầu (có thể đảo thứ
  tự so với bản gốc).
- Jump-cut: cắt bỏ khoảng lặng, tiếng ừm/à, đoạn lạc đề; nhịp nói
  liền mạch từ đầu đến cuối.
- Zoom punch-in: phóng nhẹ 110–130% ở câu nhấn mạnh, thu lại ở câu thường.
- Caption karaoke đậm: chữ trắng viền tối, từ đang đọc tô màu nhấn
  (vàng/cam — ước lượng theo mô tả sản phẩm), ≤2 dòng, đặt giữa–dưới
  khung, không che miệng người nói.
- B-roll: chèn ảnh/video minh hoạ toàn khung hoặc nửa khung đúng lúc
  người nói nhắc tới đối tượng.
- Palette: theo footage gốc; chỉ caption và đồ hoạ chèn dùng màu nhấn
  cố định của kênh.

## Cấu trúc kịch bản (chọn đoạn)
- Tiêu chí chọn đoạn 20–60 giây: có 1 câu hook đứng độc lập được +
  1 ý trọn vẹn + 1 câu kết gọn.
- Sắp xếp lại: hook (2 giây) → thân ý → câu kết.
- Cắt bỏ mọi dẫn nhập kiểu "ờ thì…", "như mình đã nói…" ở đầu đoạn.
- Mỗi clip đúng 1 ý; 1 video dài thường rút được 3–6 clip độc lập.

## Quy trình sản xuất
1. Chọn đoạn: transcribe video gốc lấy word-timing; chấm các câu ứng
   viên hook; đánh dấu khoảng lặng và tiếng đệm cần cắt.
2. Voice: GIỮ NGUYÊN giọng người nói trong footage — không dùng TTS.
   Chỉ khử ồn nhẹ và cân bằng âm lượng trước khi dựng.
3. Dựng: ffmpeg (skill này KHÔNG dùng Remotion) — cắt/jump-cut theo mốc
   thời gian, crop dọc theo vị trí khuôn mặt, punch-in zoom, burn
   caption từ word-timing, chèn B-roll theo điểm nhắc.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice (chỉ khi clip cần nhạc), loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng và đối chiếu
   checklist đặc tả ở trên (không có sheet mẫu gốc).

## Thông số xuất
- Khổ/fps: 720×1280 @30fps.
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 20–45 giây, cắt từ 1 đoạn nói có sẵn.
- Tên file xuất: `talking-head-highlight-video__<chu-de>.mp4`.

## QA checklist
- [ ] Câu hook xuất hiện trong 2 giây đầu, nghe hiểu độc lập không cần ngữ cảnh
- [ ] Không còn khoảng lặng >0,5 giây và tiếng ừm/à trong bản cắt
- [ ] Caption karaoke khớp từng từ, ≤2 dòng, không che miệng/mặt
- [ ] Punch-in chỉ ở câu nhấn, biên zoom không làm vỡ nét mặt
- [ ] B-roll xuất hiện đúng điểm người nói nhắc tới đối tượng (±0,5 giây)
- [ ] Khuôn mặt không bị crop mất trán/cằm ở mọi mức zoom
