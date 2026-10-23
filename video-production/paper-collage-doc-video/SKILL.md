---
name: paper-collage-doc-video
description: Video tư liệu kiểu cắt dán giấy: sticker ảnh tư liệu trên nền giấy cổ — dùng cho lịch sử, khám phá, câu chuyện tư liệu cần chất liệu thủ công.
---

# Tư liệu cắt dán giấy (Paper Collage Documentary)

## Khi nào dùng
- Câu chuyện tư liệu/lịch sử/khám phá có ảnh tư liệu thật: hiện vật,
  bản đồ cổ, chân dung nhân vật lịch sử.
- Khi muốn cảm giác "hồ sơ giấy" thủ công thay vì đồ hoạ số sạch bóng.
- Không dùng cho nội dung số liệu hiện đại — skin giấy cổ sẽ lệch tông.

## Mẫu gốc đã phân tích
- File: `rosetta.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/rosetta.mp4`
- Khổ/fps/thời lượng: 1280×720 @24fps, ~105 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/rosetta.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Giấy cổ/papyrus `#E8DCC0`
  - Mực nâu đen `#2E241A`
  - Đỏ `#B3392E` — dành riêng cho ô năm/số liệu
- Nền: giấy cổ xé mép không đều; riêng phần sơ đồ dùng nền giấy kẻ ô
  (graph paper).
- Sticker: ảnh tư liệu cắt theo viền trắng dày (sticker style), dán hơi
  chéo, bóng đổ nhẹ như giấy thật.
- Nhãn: chữ condensed đậm (Anton/Oswald) cho tiêu đề.
- Ô đỏ: đóng dấu chứa năm/số liệu trọng yếu — đỏ chỉ xuất hiện ở đây.
- Từ khoá đặc biệt: xếp bằng chữ ô rời kiểu ransom-note (mỗi chữ 1 ô
  giấy khác tông), tối đa 1–2 từ khoá mỗi video.
- Chuyển động: sticker pop-in như được dán xuống; ô đỏ đóng stamp kèm
  rung nhẹ; nhịp vừa, chất tư liệu.

## Cấu trúc kịch bản
- Mở: 1 hiện vật/câu hỏi bí ẩn dán lên giữa khung + ô đỏ chứa năm
  xuất phát.
- Thân: các bước là các mốc tư liệu nối tiếp — mỗi mốc gồm 1 sticker
  ảnh + 1 nhãn + 1 ô số liệu khi có.
- Kết: sticker hiện vật mở đầu quay lại + 1 câu về ý nghĩa của phát
  hiện/câu chuyện.
- Mỗi mốc 40–60 từ lời đọc; giọng kể chuyện khám phá.

## Quy trình sản xuất
1. Kịch bản: viết theo mốc tư liệu; kiểm chứng niên đại/tên riêng từ
   nguồn tư liệu trước khi viết.
2. Voice: VieNeu local — preset v3 Turbo giọng kể chuyện trầm ấm,
   speed 1.0.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `paper-collage-doc-video`. Chuẩn bị sticker trước: cắt ảnh tư liệu +
   thêm viền trắng + bóng đổ, rồi mới đưa vào composition.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/rosetta.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @24fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `paper-collage-doc-video__<chu-de>.mp4`.

## QA checklist
- [ ] Viền trắng sticker đều và đủ dày ở mọi ảnh tư liệu
- [ ] Ô đỏ chỉ chứa năm/số liệu — không dùng đỏ cho chữ thường
- [ ] Hiệu ứng dán/stamp khớp nhịp câu đọc nhắc tới mốc đó
- [ ] Chữ ransom-note chỉ cho 1–2 từ khoá, không lạm dụng
- [ ] Nền giấy (cổ hoặc kẻ ô) nhất quán theo cảnh, mép xé không lặp pattern lộ liễu
- [ ] Glyph tiếng Việt đủ dấu trên font condensed của nhãn
