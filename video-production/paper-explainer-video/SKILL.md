---
name: paper-explainer-video
description: Video giải thích bài báo khoa học trên nền giấy kem học thuật — dùng để tóm tắt paper, nghiên cứu mới cho khán giả không chuyên.
---

# Giải thích bài báo khoa học (Paper Explainer)

## Khi nào dùng
- Tóm tắt 1 paper/nghiên cứu cụ thể (AI, y học, kinh tế…) cho khán giả
  phổ thông hoặc cộng đồng chuyên môn.
- Giá trị nằm ở độ tin cậy học thuật: phải dẫn đúng tên paper, tác giả,
  năm và số liệu gốc.
- Không dùng cho bài tổng hợp nhiều nguồn — template này bám theo
  cấu trúc của đúng 1 paper.

## Mẫu gốc đã phân tích
- File: `attention.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/attention.mp4`
- Khổ/fps/thời lượng: 1280×720 @30fps, ~174 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/attention.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền giấy kem `#F7F3E9`
  - Mực đen/xám `#22252A`
  - Accent đỏ gạch chân `#B3392E` cho thuật ngữ/số liệu trọng yếu
- Header: nhỏ ở trên cùng, ghi "Tên paper — Tác giả, Năm", hiện suốt video.
- Nội dung chính: tái hiện bảng, hình và công thức TRÍCH TỪ paper
  (chụp từ PDF hoặc vẽ lại trung thành); vùng đang giảng được phóng to
  hoặc đánh dấu.
- Đánh số mục: ký hiệu tiết §1, §2, §3… hiển thị khi chuyển mục, khớp
  cấu trúc bài giảng.
- Phụ đề: dưới cùng, ≤2 dòng, style trung tính — không karaoke loè loẹt.
- Chuyển động: chậm, học thuật; zoom vào chi tiết bảng/công thức thay vì
  hiệu ứng nảy.

## Cấu trúc kịch bản
- Mở: vấn đề paper giải quyết + vì sao nó quan trọng — trước khi nhắc
  tên paper.
- Thân theo §:
  - §1 Bối cảnh
  - §2 Phương pháp (kèm hình/công thức gốc)
  - §3 Kết quả (kèm bảng số liệu gốc)
  - §4 Ý nghĩa và giới hạn
- Kết: 1 câu takeaway duy nhất + trích dẫn đầy đủ của paper.
- Mỗi § 60–90 từ lời đọc.

## Quy trình sản xuất
1. Kịch bản: đọc paper trước khi viết; mọi số liệu chép nguyên văn từ
   paper và ghi rõ trang/bảng nguồn trong ghi chú sản xuất. Tách rõ câu
   nào là kết quả của paper, câu nào là diễn giải.
2. Voice: VieNeu local — preset v3 Turbo giọng trung tính, rõ chữ,
   speed 1.0 (nội dung học thuật dày, cần chậm để kịp nhìn công thức).
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `paper-explainer-video`. Trích hình/bảng từ PDF của paper, highlight
   vùng đang giảng theo mốc voice.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/attention.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây (1–2 mục §).
- Tên file xuất: `paper-explainer-video__<chu-de>.mp4`.

## QA checklist
- [ ] Header "Tên paper — Tác giả, Năm" chính xác và hiện suốt video
- [ ] Số § trên hình khớp thứ tự cấu trúc kịch bản
- [ ] Bảng/công thức trích từ paper đọc rõ ở 720p, không mờ, không mất cột/hàng
- [ ] Mọi số liệu khớp nguyên văn paper (đối chiếu lại bản gốc)
- [ ] Nền giấy kem nhất quán, accent đỏ chỉ cho điểm trọng yếu
- [ ] Lời đọc phân biệt rõ: kết quả của paper vs. diễn giải của người làm video
