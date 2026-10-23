---
name: english-mistakes-video
description: Video dọc sửa lỗi tiếng Anh bằng flashcard SAI/ĐÚNG trên nền giấy kẻ — dùng cho kênh dạy tiếng Anh, series "lỗi người Việt hay mắc".
---

# Sửa lỗi tiếng Anh (English Mistakes Fix)

## Khi nào dùng
- Chỉ ra và sửa các lỗi tiếng Anh phổ biến: ngữ pháp, từ vựng, dịch
  word-by-word từ tiếng Việt.
- Mỗi video 1 nhóm lỗi nhỏ (mẫu gốc: 3 lỗi).
- Không nhồi nhiều lỗi vào 1 video — người xem chỉ nhớ được 2–3 lỗi.

## Mẫu gốc đã phân tích
- File: `english-3-loi.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/english-3-loi.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~63 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/english-3-loi.jpg`
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N (mỗi bước
  = 1 lỗi) → thẻ kết luận/CTA.

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền giấy kẻ (ruled paper) trắng–kem
  - Mực xanh/đen
  - Đỏ `#D93A2B` cho gạch lỗi
  - Vàng `#FFD94D` highlight phụ đề
  - Xanh lá cho dấu ĐÚNG
- Header: ghi chú vàng (sticky note) dán ở đầu, chứa tiêu đề kiểu
  viết tay "3 lỗi tiếng Anh…".
- Flashcard là thành phần chính, 2 trạng thái nối tiếp trong 1 thẻ:
  - SAI: câu sai có gạch đỏ + dấu ✗
  - ĐÚNG: câu đúng được highlight + dấu ✓
- Mascot: vẹt hoặc cú sticker, xuất hiện phản ứng ở mỗi flashcard —
  chọn 1 nhân vật cho cả series.
- Phụ đề: highlight vàng theo từ đang đọc, ở dưới khung.

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề trên sticky note): nêu số lỗi + hứa sửa xong trong
  video, 4 giây đầu.
- Thân: mỗi lỗi 1 bước (badge n/N):
  1. Đọc câu SAI — gạch đỏ hiện
  2. Giải thích ngắn bằng VI vì sao sai
  3. Câu ĐÚNG — highlight + ✓, đọc chậm 1 lần
- Kết (thẻ kết luận): liệt kê lại tất cả câu đúng trong 1 khung tổng
  kết + CTA lưu video.
- Giải thích VI phải ngắn, tránh thuật ngữ ngữ pháp nặng.

## Quy trình sản xuất
1. Kịch bản: chọn lỗi có thật người Việt hay mắc; câu ĐÚNG phải
   chuẩn ngữ pháp — kiểm chứng bằng từ điển/nguồn học thuật trước
   khi viết.
2. Voice: VieNeu — preset hỗ trợ EN–VI (câu EN đọc chuẩn, giải thích
   bằng VI), speed 1.1. Câu ĐÚNG đọc chậm và rõ hơn câu sai.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `english-mistakes-video`. Flashcard SAI/ĐÚNG là 1 component 2
   trạng thái; gạch đỏ/highlight animate theo mốc voice.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/english-3-loi.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây (2–3 lỗi).
- Tên file xuất: `english-mistakes-video__<chu-de>.mp4`.

## QA checklist
- [ ] Gạch đỏ + ✗ chỉ ở câu SAI; highlight + ✓ chỉ ở câu ĐÚNG — không nhầm phía
- [ ] Câu ĐÚNG chuẩn ngữ pháp 100% (đã kiểm chứng nguồn)
- [ ] Sticky note vàng làm header, nền giấy kẻ giữ suốt video
- [ ] Mascot xuất hiện ở mỗi flashcard, cùng 1 nhân vật cả video
- [ ] Phụ đề highlight vàng khớp từ đang đọc, không che flashcard
- [ ] Khung kết liệt kê đủ các câu đúng đã dạy, khớp thứ tự các bước
