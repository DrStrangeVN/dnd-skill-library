---
name: motion-comic-hype-video
description: Quảng cáo dọc kiểu truyện tranh chuyển động: sunburst, halftone, bong bóng starburst, caption trong hộp vàng — dùng cho ra mắt sản phẩm, ưu đãi, thông báo cần năng lượng hype.
---

# Quảng cáo kiểu truyện tranh (Motion Comic Hype)

## Khi nào dùng
- Ra mắt sản phẩm, mở bán, ưu đãi giới hạn — cần cảm giác poster
  truyện tranh siêu anh hùng, đập vào mắt trong 1 giây.
- Nội dung tiếng Anh hoặc song ngữ kiểu quảng cáo.
- Không dùng cho nội dung trang trọng/giải thích dài.

## Mẫu gốc đã phân tích
- File: `pantry-hype.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/pantry-hype.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~36 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/pantry-hype.jpg`
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N → thẻ kết
  luận/CTA, bọc trong skin comic.

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền sunburst tia nắng (đỏ/cam/vàng rực) + chấm halftone phủ nhẹ
  - Hộp caption vàng `#FFD23F`
  - Chữ đen condensed
- Khung bìa comic ở mở đầu: viền khung truyện + nhãn "ISSUE #01" như
  bìa tạp chí truyện tranh.
- Bong bóng starburst (viền răng cưa nổ): chứa giá/ưu đãi/từ khoá hét;
  chữ condensed khổ lớn nằm trong bong bóng.
- Font: Anton condensed, đổ bóng CỨNG lệch 1 hướng (hard shadow) —
  tuyệt đối không blur.
- Phụ đề/câu thoại: nằm trong HỘP CAPTION VÀNG kiểu comic ở dưới
  khung; không dùng karaoke trắng thông thường.
- Chuyển động: pop nảy mạnh, zoom giật theo nhịp; tia sunburst xoay
  chậm liên tục ở nền.

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề = bìa truyện): tên sản phẩm/sự kiện + "ISSUE #01" +
  1 câu hét ngắn.
- Thân: 3–4 bước — mỗi bước 1 tính năng/ưu đãi trong bong bóng
  starburst riêng; badge n/N thu nhỏ trong góc bong bóng.
- Kết (thẻ CTA): bong bóng starburst LỚN NHẤT chứa CTA + hạn chót
  ưu đãi.
- Câu cực ngắn kiểu quảng cáo: 3–6 từ/câu, viết tiếng Anh trước
  theo mẫu.

## Quy trình sản xuất
1. Kịch bản: viết theo bong bóng — mỗi bong bóng 1 ý hét duy nhất;
   kiểm tra độ dài chữ vừa khung starburst trước khi dựng.
2. Voice: VieNeu — giọng EN năng lượng cao (preset hỗ trợ EN hoặc
   giọng EN của API), speed 1.1, đọc kiểu "hét" quảng cáo.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `motion-comic-hype-video`. Sunburst + halftone là layer nền dùng
   chung; starburst là component theo nội dung.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/pantry-hype.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 20–36 giây.
- Tên file xuất: `motion-comic-hype-video__<chu-de>.mp4`.

## QA checklist
- [ ] Sunburst + halftone hiện diện suốt video, tia xoay đủ chậm không gây chóng mặt
- [ ] Mở đầu có khung bìa comic + nhãn "ISSUE #01"
- [ ] Mọi câu thoại/phụ đề nằm trong hộp caption vàng, chữ đen condensed
- [ ] Đổ bóng chữ là bóng cứng lệch 1 hướng — không có bóng blur
- [ ] Starburst không đè chữ trong hộp caption; CTA nằm trong bong bóng lớn nhất ở kết
- [ ] Badge n/N khớp số bước; glyph tiếng Việt (nếu có dòng VI) đủ dấu trên Anton
