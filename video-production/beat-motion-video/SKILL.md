---
name: beat-motion-video
description: Video kinetic typography chạy theo nhịp beat trên nền tối, accent lime — dùng cho promo, intro kênh, thông báo ngắn cần năng lượng cao.
---

# Chữ & hiệu ứng chuyển động (Beat Motion)

## Khi nào dùng
- Promo sản phẩm/kênh, intro/outro, thông báo ra mắt, đếm ngược sự kiện.
- Nội dung rất ngắn (15–45 giây), ít chữ, cần cảm giác "đã mắt, bắt tai"
  thay vì giải thích dài.
- Không dùng khi nội dung cần giải thích chi tiết — template này không có
  thẻ nội dung để chứa thông tin dày.

## Mẫu gốc đã phân tích
- File: `promo.mp4` — video promo giới thiệu chính ReelCrew, dùng làm
  tham chiếu style (không phải output khách hàng).
- Lưu tại: `~/workspace/reelcrew-analysis/videos/promo.mp4`
- Khổ/fps/thời lượng: 1280×720 @30fps, ~30 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/promo.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền đen/xám than `#0A0A0B`
  - Accent lime `#B4FF39` — màu nhấn DUY NHẤT của template
  - Chữ trắng `#FFFFFF`, xám phụ `#8A8A8A` cho nhãn nhỏ
- Font chữ:
  - Space Grotesk cho chữ chính
  - Anton/condensed bold cho cụm từ khoá khổ lớn
  - IBM Plex Mono cho nhãn kiểu terminal
- Layout: chữ lớn chiếm trung tâm khung hình; motif cửa sổ terminal và
  clapper board làm đồ hoạ phụ; không thẻ nội dung, không mascot.
- Chữ trên màn hình CHÍNH là nội dung — không chạy phụ đề karaoke riêng.
  Mỗi cụm chữ xuất hiện đúng nhịp beat.
- Chuyển động: cắt cứng theo beat nhạc; hiệu ứng glitch, slide, scale-pop;
  chữ vào theo từng từ/cụm, không fade mềm.
- Vùng an toàn: cụm chữ chính giữ trong 80% khung giữa, không sát mép.

## Cấu trúc kịch bản
- Mở (0:00–0:02): 1 câu hook ≤6 từ, xuất hiện kèm cú hit âm thanh.
- Thân: 5–8 cụm chữ chính, mỗi cụm 1 ý duy nhất (tính năng, con số, lợi ích).
- Kết (3 giây cuối): logo/tên kênh khổ lớn + 1 CTA ngắn (đăng ký, xem ngay,
  link ở mô tả).
- Không có thẻ bước n/N — nhịp beat thay cho cấu trúc bước.
- Tổng chữ trên màn hình cả video: không quá ~60 từ.

## Quy trình sản xuất
1. Kịch bản: viết theo cụm chữ trước (mỗi cụm ≤4 từ); voice chỉ đọc đúng
   các cụm đó. Giọng điệu dồn dập, tự tin.
2. Voice: VieNeu local — giọng clone "Nhật Phong (Local Clone)",
   speed 1.1. Câu ngắn, ngắt đúng nhịp cụm chữ; xuất WAV 48 kHz mono và
   lấy mốc thời gian từng cụm làm beat map phụ.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `beat-motion-video`. Đồng bộ frame chữ với beat của nhạc nền; glitch/slide
   là preset chuyển động dùng chung.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/promo.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 20–30 giây.
- Tên file xuất: `beat-motion-video__<chu-de>.mp4`.

## QA checklist
- [ ] Accent chỉ dùng lime `#B4FF39`, không lẫn màu nhấn khác
- [ ] Mọi cú xuất hiện chữ khớp beat nhạc (lệch tối đa 1 frame)
- [ ] Chữ không tràn khung, không bị hiệu ứng glitch làm mất dấu tiếng Việt
- [ ] Kiểm glyph tiếng Việt trên Space Grotesk/Anton trước khi render
- [ ] Hook xuất hiện trong 2 giây đầu
- [ ] CTA + logo ở cụm cuối, giữ tối thiểu 1,5 giây
