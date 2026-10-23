---
name: vertical-photo-news-video
description: Bản tin dọc dùng ảnh thật full-bleed và caption karaoke — dùng cho tin nóng, sự kiện, cập nhật nhanh cần đăng trong ngày.
---

# Bản tin ảnh dọc — tin nóng (Vertical Photo News)

## Khi nào dùng
- Tin nóng/sự kiện cần sản xuất nhanh trong ngày: thể thao, thời sự
  địa phương, thông báo chính thức.
- Chỉ dùng khi có ảnh thật (tự chụp hoặc stock có credit).
- Không dùng ảnh AI thay ảnh tin — mất độ tin cậy của thể loại bản tin.

## Mẫu gốc đã phân tích
- File: `roman-news.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/roman-news.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~45 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/roman-news.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Màu chủ đạo theo ảnh thật
  - Đỏ pill `#D92323` cho nhãn "TIN NÓNG"
  - Dải đáy olive `#5A6236`
  - Highlight karaoke vàng `#FFD94D` trên chữ trắng
- Layout: ảnh thật full-bleed toàn khung, dòng credit ảnh nhỏ ở góc.
- Pill đỏ "TIN NÓNG": cố định góc trên, chữ trắng viết hoa, hiện suốt video.
- Caption karaoke: trắng đậm, đặt giữa–dưới ảnh; từ đang đọc tô vàng,
  đồng bộ theo từng từ (word-by-word).
- Dải đáy olive: CỐ ĐỊNH suốt video, chứa tag chuyên mục + headline
  condensed viết hoa (Oswald/Anton). Dải này không đổi nội dung theo cảnh.
- Chuyển động: chuyển ảnh bằng cắt + Ken Burns nhẹ; caption là yếu tố
  động chính, ảnh chỉ dịch chuyển rất chậm.

## Cấu trúc kịch bản
- Mở (0:00–0:02): headline chứa số liệu/cú sốc chính — đúng dòng headline
  đang hiện ở dải đáy.
- Thân: 3–5 ý chính, mỗi ý 1 ảnh; câu ngắn kiểu bản tin, một câu một
  dữ kiện, không bình luận.
- Kết: nhắc lại tag chuyên mục + nguồn tin; không CTA bán hàng.
- Tổng lời đọc: 90–120 từ cho ~45 giây.

## Quy trình sản xuất
1. Kịch bản: kiểm chứng mọi số liệu/dữ kiện từ nguồn tin trước khi viết;
   ghi nguồn vào ghi chú sản xuất.
2. Voice: VieNeu local — giọng clone "Nhật Phong (Local Clone)",
   speed 1.1, đọc dứt khoát kiểu phát thanh viên. Xuất WAV 48 kHz mono
   kèm word-timing cho karaoke.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `vertical-photo-news-video`. Ảnh crop dọc giữ chủ thể, gắn credit,
   karaoke theo word-timing.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/roman-news.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `vertical-photo-news-video__<chu-de>.mp4`.

## QA checklist
- [ ] Mọi ảnh đều là ảnh thật và có credit ở góc
- [ ] Pill "TIN NÓNG" đỏ, đúng vị trí góc trên, hiện suốt video
- [ ] Dải đáy olive cố định, headline condensed viết hoa, không đổi giữa chừng
- [ ] Karaoke tô vàng đúng từ đang đọc, caption không tràn xuống dải đáy
- [ ] Số liệu trong kịch bản đã kiểm chứng nguồn
- [ ] Glyph tiếng Việt đủ dấu trên Oswald/Anton
