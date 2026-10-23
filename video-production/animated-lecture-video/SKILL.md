---
name: animated-lecture-video
description: Bài giảng ngang bằng hoạt hình vector phẳng với mascot robot dẫn dắt — dùng cho bài học, khoá học, giải thích kiến thức theo chương mục.
---

# Bài giảng hoạt hình 2D (Animated Lecture)

## Khi nào dùng
- Bài giảng/khoá học xem ngang: kiến thức học thuật, kỹ năng,
  onboarding nhân viên.
- Nội dung dài theo chương mục (1–10 phút), cần sơ đồ minh hoạ từng bước
  thay vì người thật đứng giảng.
- Không dùng cho nội dung cảm xúc/điện ảnh — skin này sáng, phẳng, học thuật.

## Mẫu gốc đã phân tích
- File: `sky-blue.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/sky-blue.mp4`
- Khổ/fps/thời lượng: 1280×720 @24fps, ~96 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/sky-blue.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Xanh trời `#7EC8E3`
  - Xanh lá `#7FB069`
  - Be `#F5EFE0` làm nền sáng; chữ tối dễ đọc
- Hình ảnh: hoạt hình vector phẳng (flat vector), nét đơn giản,
  không đổ bóng thật, không gradient nặng.
- Mascot robot: dẫn dắt xuyên suốt — chào mở bài, chỉ vào sơ đồ khi giảng,
  xuất hiện lại ở đoạn kết để tổng kết.
- Sơ đồ/biểu đồ: đơn giản, dựng ngay trên sân khấu (hình khối, mũi tên,
  biểu đồ cột). Mỗi mục học đúng 1 sơ đồ chính.
- Nhãn tiêu đề mục: nhỏ, cố định ở góc trên khi vào mục mới.
- Phụ đề: thanh tối bo tròn cố định dưới cùng, chữ trắng, ≤2 dòng.

## Cấu trúc kịch bản
- Mở: mascot đặt vấn đề/câu hỏi của bài trong 5 giây đầu.
- Thân: chia mục rõ ràng (Mục 1, 2, 3…); mỗi mục gồm 1 khái niệm +
  1 sơ đồ + 1 ví dụ ngắn.
- Kết: mascot quay lại tóm tắt tối đa 3 ý chính trong 1 khung tổng kết.
- Mỗi mục 40–60 từ lời đọc; có câu chuyển mục rõ ràng để khớp nhãn
  tiêu đề trên hình.

## Quy trình sản xuất
1. Kịch bản: viết theo mục trước, lời đọc sau; ghi rõ mục nào dùng
   sơ đồ nào trong ghi chú sản xuất.
2. Voice: VieNeu local — preset v3 Turbo giọng sáng, rõ chữ, speed 1.1.
   Giọng điệu giảng giải thân thiện, không đọc nhanh ở đoạn công thức.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `animated-lecture-video`. Mascot và sơ đồ là asset vector tái sử dụng
   giữa các bài trong series.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/sky-blue.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @24fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: ~60 giây (mở + 2 mục rút gọn + kết).
- Tên file xuất: `animated-lecture-video__<chu-de>.mp4`.

## QA checklist
- [ ] Mascot robot nhất quán (hình dạng, màu) và xuất hiện ở mở + kết
- [ ] Mỗi mục học có đúng 1 sơ đồ, sơ đồ khớp câu đang đọc
- [ ] Phụ đề nằm gọn trong thanh tối bo tròn, ≤2 dòng
- [ ] Nhãn tiêu đề mục ở góc trên khớp cấu trúc kịch bản
- [ ] Palette sáng trời/lá/be nhất quán, không lẫn màu nóng mạnh
- [ ] Glyph tiếng Việt đủ dấu trên mọi nhãn sơ đồ
