---
name: english-listening-video
description: Video luyện nghe tiếng Anh dọc: câu chuyện EN có highlight theo câu và từ đang đọc, kèm dịch Việt — dùng cho kênh học tiếng Anh, luyện nghe cho người mới bắt đầu.
---

# Luyện nghe tiếng Anh (English Listening)

## Khi nào dùng
- Bài luyện nghe ngắn cho người học EN trình độ đầu: câu chuyện đơn
  giản, nghe–đọc đồng thời.
- Không dùng cho nội dung ngữ pháp khô — skill này là nghe theo câu
  chuyện có minh hoạ.

## Mẫu gốc đã phân tích
- File: `a-small-step.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/a-small-step.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~26 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/a-small-step.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền kem `#FAF3E3`
  - Thẻ trắng
  - Dải highlight xanh nhạt `#CDE7D8` sau câu đang đọc
  - Chữ EN đen đậm; dịch VI xám nhỏ
- Thẻ minh hoạ: hình stick-figure đơn giản ở đầu câu chuyện, nét vẽ
  tay tối giản.
- Bố cục câu: các câu EN in đậm xếp dọc trong khung.
  - Câu đang đọc: phủ dải xanh nhạt toàn dòng
  - Từ đang phát âm: có Ô VIỀN quanh riêng từ đó
  - Dịch VI: in nhỏ ngay bên dưới từng câu EN, luôn hiện
- Không mascot, không thẻ bước n/N — tiến trình chính là dải highlight
  chạy xuống theo câu.

## Cấu trúc kịch bản
- Mở: tiêu đề câu chuyện + thẻ minh hoạ; câu đầu tiên bắt đầu ngay,
  không dẫn nhập dài.
- Thân: câu chuyện 5–8 câu EN đơn giản (thì hiện tại/quá khứ đơn,
  từ vựng A1–A2); mỗi câu là 1 nhịp highlight trọn câu.
- Kết: hết câu chuyện; có thể lặp lại 1 câu khó nhất ở tốc độ chậm
  hơn hoặc đặt 1 câu hỏi hiểu bài bằng VI.
- Mỗi câu EN ≤10 từ để người mới theo kịp.

## Quy trình sản xuất
1. Kịch bản: viết truyện EN trước; kiểm tra ngữ pháp và độ khó từ
   vựng; dịch VI sát nghĩa từng câu. Giọng điệu kể chuyện ấm áp.
2. Voice: VieNeu — giọng EN (preset v3 Turbo hỗ trợ EN hoặc giọng EN
   của API), speed 1.0, đọc chậm rõ từng từ để ô highlight bám kịp.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `english-listening-video`. Highlight câu + ô từ theo word-timing
   của file voice EN.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   rất nhẹ ~−28dB dưới voice (không lấn tiếng đọc), loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/a-small-step.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 20–30 giây.
- Tên file xuất: `english-listening-video__<chu-de>.mp4`.

## QA checklist
- [ ] Dải highlight phủ đúng câu đang đọc, chuyển câu khớp thời điểm đọc (±0,2 giây)
- [ ] Ô viền bám đúng từ đang phát âm, không nhảy trước/sau
- [ ] Dịch VI khớp nghĩa từng câu EN và luôn hiển thị dưới câu
- [ ] Câu EN đúng ngữ pháp, từ vựng đúng trình độ đã định (A1–A2)
- [ ] Giọng EN phát âm rõ, tốc độ chậm — nghe kịp không cần tua lại
- [ ] Nền kem + thẻ stick-figure nhất quán, không lẫn skin của template khác
