---
name: math-explainer-3b1b-video
description: Video giải thích toán/học sâu kiểu 3Blue1Brown bằng Manim trên nền đen — dùng khi cần dựng trực giác bằng đồ thị và công thức biến hình.
---

# Giải thích kiểu 3Blue1Brown (3B1B-style Math Explainer)

## Khi nào dùng
- Giải thích toán, xác suất, học sâu, thuật toán — nơi trực giác hình học
  quan trọng hơn lời nói.
- Chỉ dùng khi khái niệm VẼ ĐƯỢC: đồ thị, vector, ma trận, phân phối.
- Không dùng cho nội dung thuần chữ hoặc nhiều bảng số liệu.

## Mẫu gốc đã phân tích
- File: `resnet.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/resnet.mp4`
- Khổ/fps/thời lượng: 1280×720 @30fps, ~264 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/resnet.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền đen tuyền `#000000`
  - Chữ trắng
  - Highlight teal `#2EC4B6` và đỏ `#E63946` cho 2 phía đối lập của
    lập luận; màu phụ theo bảng màu Manim mặc định
- Công thức: render bằng LaTeX, font serif italic.
- Nhãn giải thích: sans trắng, ngắn, đặt cạnh đối tượng đang biến đổi.
- Chuyển động cốt lõi: đối tượng toán BIẾN HÌNH (morph) liên tục — đồ thị
  cong dần, vector xoay/kéo, công thức tách–gộp số hạng. Không cắt cảnh cứng.
- Tiêu đề mục: hiển thị trong vòng tròn đánh số ở góc khi vào mục mới.
- Phụ đề: không karaoke; có thể chèn phụ đề thường ≤2 dòng dưới cùng
  nếu cần bản có phụ đề.

## Cấu trúc kịch bản
- Mở: 1 câu hỏi trực giác + hình đơn giản nhất có thể.
- Thân: mỗi bước biến đổi đúng 1 đối tượng trên màn hình; xây trực giác
  hình học TRƯỚC, công thức tổng quát SAU.
- Kết: công thức đầy đủ hiện nguyên khung + 1 câu chốt ý nghĩa.
- Mỗi bước 30–50 từ lời đọc, chừa nhịp cho animation chạy hết trước
  khi chuyển ý.

## Quy trình sản xuất
1. Kịch bản: viết kèm chỉ dẫn hình cho từng câu (câu nào morph đối
   tượng nào, từ trạng thái nào sang trạng thái nào).
2. Voice: VieNeu local — preset v3 Turbo giọng nam trầm, speed 1.0.
   Thu voice TRƯỚC để lấy thời lượng từng câu làm mốc cho animation.
3. Dựng: Manim (venv `~/workspace/tools/manim-venv`) — viết scene Python
   theo kịch bản, render từng scene khớp thời lượng voice.
   Skill này KHÔNG dùng Remotion.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — ghép voice + nhạc
   nền warm pad ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/resnet.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây (1 khái niệm, 3–4 biến đổi).
- Tên file xuất: `math-explainer-3b1b-video__<chu-de>.mp4`.

## QA checklist
- [ ] Nền đen tuyền, không lẫn khung/nền xám của template khác
- [ ] Mọi biến đổi là morph liên tục, không nhảy hình giữa 2 trạng thái
- [ ] Công thức LaTeX render đúng (không lỗi ký tự, không vỡ layout)
- [ ] Highlight chỉ dùng teal/đỏ cho đúng 2 phía đối lập đã định
- [ ] Animation kết thúc khớp thời điểm câu đọc chuyển ý (lệch ≤0,5 giây)
- [ ] Số trong vòng tròn mục khớp cấu trúc kịch bản
