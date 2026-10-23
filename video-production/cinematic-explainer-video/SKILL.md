---
name: cinematic-explainer-video
description: Clip giải thích bằng tranh minh hoạ AI phong cách điện ảnh, nhịp chậm — dùng cho câu chuyện thương hiệu, giải thích khái niệm cần cảm xúc và chiều sâu hình ảnh.
---

# Clip giải thích điện ảnh (Cinematic Explainer)

## Khi nào dùng
- Giải thích khái niệm/sản phẩm cần không khí điện ảnh: câu chuyện
  thương hiệu, tầm nhìn, "vì sao" của một vấn đề.
- Khán giả xem ngang (YouTube), thời lượng 30 giây – vài phút.
- Ưu tiên cảm xúc hơn mật độ thông tin; không dùng cho tin nhanh hay
  nội dung cần nhiều số liệu chi tiết.

## Mẫu gốc đã phân tích
- File: `paper-fold.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/paper-fold.mp4`
- Khổ/fps/thời lượng: 1280×720 @24fps, ~29 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/paper-fold.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Navy đêm `#0B1626` làm tông chủ đạo
  - Xanh biển sâu cho vùng bóng
  - Điểm sáng cyan/trắng cho số liệu và chữ phát sáng
- Hình ảnh: tranh minh hoạ AI chất điện ảnh (ánh sáng có hướng, chiều sâu
  trường ảnh).
- Nhân vật: MỘT nhân vật nhất quán xuất hiện qua nhiều cảnh — khoá bảng mô
  tả nhân vật (khuôn mặt, tóc, trang phục, tuổi) cố định khi tạo ảnh.
- Typography: số liệu khổ lớn phát sáng nhẹ (glow) là điểm nhấn chính;
  chữ giải thích sans mảnh, ít chữ trên mỗi cảnh.
- Phụ đề: tối giản dưới cùng, tối đa 2 dòng, không karaoke theo từ.
- Chuyển động: nhịp chậm, dissolve mềm giữa cảnh, camera đẩy nhẹ
  (slow push-in). Tuyệt đối không cắt nhanh kiểu short.

## Cấu trúc kịch bản
- Mở: 1 cảnh hook — nhân vật đối diện vấn đề + 1 câu hỏi treo.
- Thân: 3–4 cảnh chính, mỗi cảnh 1 ý; số liệu quan trọng được "đọng" lại
  thành typography phát sáng riêng 1 nhịp.
- Kết: cảnh vấn đề được giải quyết + 1 câu kết đọng, không CTA gắt.
- Mỗi cảnh 12–20 từ lời đọc để chừa khoảng thở cho hình ảnh.

## Quy trình sản xuất
1. Kịch bản: 60–90 từ cho 30 giây; giọng điệu trầm, kể chuyện, câu ngắn.
   Viết kèm chỉ dẫn cảnh cho từng câu.
2. Voice: VieNeu local — preset nam trầm v3 Turbo (hoặc API
   "Nam - Nhật Phong"), speed 1.0. Thu voice trước để khoá thời lượng cảnh.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `cinematic-explainer-video`. Tạo ảnh AI theo bảng mô tả nhân vật cố
   định; slow push-in + dissolve bằng Remotion.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/paper-fold.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @24fps (đúng mẫu gốc — giữ 24fps cho cảm giác
  điện ảnh, không nâng 30fps).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `cinematic-explainer-video__<chu-de>.mp4`.

## QA checklist
- [ ] Nhân vật nhất quán (khuôn mặt, trang phục) qua mọi cảnh
- [ ] Palette navy đêm nhất quán, không cảnh nào lệch tông sáng
- [ ] Số liệu phát sáng đọc rõ, hiệu ứng glow không cháy sáng
- [ ] Nhịp cắt chậm — không có cú cắt dưới 2 giây
- [ ] Phụ đề ≤2 dòng, không che chi tiết chính của cảnh
- [ ] Glyph tiếng Việt đủ dấu trên font chữ phát sáng
