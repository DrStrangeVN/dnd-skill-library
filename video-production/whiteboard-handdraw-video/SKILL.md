---
name: whiteboard-handdraw-video
description: Video vẽ tay trên nền giấy kem: bàn tay cầm bút vẽ line-art dần theo lời đọc — dùng cho giải thích khái niệm, bài học, kể chuyện cần cảm giác gần gũi thủ công.
---

# Vẽ tay bảng trắng (Whiteboard Hand-drawn)

## Khi nào dùng
- Giải thích khái niệm, bài học ngắn, quy trình đơn giản — khi hình
  vẽ tay tạo cảm giác gần gũi hơn đồ hoạ số.
- Nội dung phải vẽ được thành chuỗi hình đơn giản.
- Không dùng cho nội dung nhiều số liệu/bảng biểu.

## Mẫu gốc đã phân tích
- File: `cau-vong.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/cau-vong.mp4`
- Khổ/fps/thời lượng: 1280×720 @30fps, ~54 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/cau-vong.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền giấy kem `#F8F1DE`
  - Line-art đen/nâu `#33302A`
  - Màu tô: chỉ ở yếu tố chính của hình (ví dụ cầu vồng nhiều màu);
    phần còn lại giữ nét đen
- Thành phần cốt lõi: bàn tay cầm bút (lớp phủ) di chuyển theo đúng
  đường nét đang được vẽ.
- Vẽ dần (stroke reveal): từng nét hiện ra theo thứ tự vẽ tự nhiên,
  tốc độ khớp lời đọc đang mô tả chi tiết đó.
- Chữ trong hình: font tròn thân thiện hoặc chữ viết tay-style; tiêu
  đề được "viết" trực tiếp lên bảng như các nét vẽ khác.
- Phụ đề: chữ có viền (outline) ở dưới cùng, đọc rõ trên cả nền kem
  lẫn vùng đã vẽ dày.
- Cách tạo hình: line-art tạo bằng AI (ảnh đường nét sạch) rồi tách
  stroke để reveal; tay là lớp phủ PNG/video, không phải tay quay thật.

## Cấu trúc kịch bản
- Mở: câu hỏi gợi mở + nét vẽ đầu tiên xuất hiện ngay trong 3 giây đầu.
- Thân: mỗi ý = 1 hình vẽ hoàn chỉnh; lời đọc mô tả đúng chi tiết
  đang được vẽ tại thời điểm đó.
- Kết: "camera" lui ra thấy toàn bộ bức tranh tổng hợp + 1 câu chốt.
- Mỗi hình 40–60 từ lời đọc.

## Quy trình sản xuất
1. Kịch bản: viết theo hình — mỗi câu gắn với 1 chi tiết sẽ vẽ; ghi
   thứ tự nét cho từng hình. Giọng điệu thân thiện như thầy cô giảng bài.
2. Voice: VieNeu local — preset v3 Turbo giọng thân thiện, speed 1.1.
   Thu voice trước để lấy mốc thời gian cho từng nét vẽ.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `whiteboard-handdraw-video`. Stroke reveal bằng mask theo path của
   line-art; tay phủ di chuyển dọc path đang reveal.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/cau-vong.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `whiteboard-handdraw-video__<chu-de>.mp4`.

## QA checklist
- [ ] Đầu bút của tay khớp đúng đầu nét đang reveal, không "vẽ trước" tay
- [ ] Thứ tự nét tự nhiên như người thật vẽ (khung → chi tiết), không hiện nguyên hình cùng lúc
- [ ] Lời đọc mô tả đúng chi tiết đang vẽ tại thời điểm đó
- [ ] Phụ đề outline đọc rõ trên cả nền kem trống lẫn vùng nhiều nét
- [ ] Màu tô chỉ ở yếu tố chính; phần còn lại giữ line-art đen/nâu
- [ ] Không lộ cạnh mask/vệt xám quanh đường reveal khi trích frame kiểm tra
