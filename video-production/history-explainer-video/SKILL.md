---
name: history-explainer-video
description: Video dọc kể lịch sử Việt Nam với header cuộn thư, thẻ bản đồ/sơ đồ và ribbon phụ đề đỏ sẫm — dùng cho kênh Sử Việt, bài kể trận đánh/sự kiện lịch sử.
---

# Lịch sử Việt Nam (Vietnam History Explainer)

## Khi nào dùng
- Kể 1 sự kiện lịch sử Việt Nam trong 1–2 phút: trận đánh, nhân vật,
  mốc triều đại.
- Nội dung phải có diễn biến theo mốc để vẽ bản đồ/sơ đồ.
- Không dùng cho bài cảm nghĩ lịch sử không có sự kiện cụ thể.

## Mẫu gốc đã phân tích
- File: `bach-dang-938.mp4` (chủ đề mẫu: trận Bạch Đằng 938)
- Lưu tại: `~/workspace/reelcrew-analysis/videos/bach-dang-938.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~88 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/bach-dang-938.jpg`
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N → thẻ kết
  luận/CTA, bọc trong skin sử Việt.

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền kem `#F6EDD8` có viền khung trang trí cổ
  - Đỏ sẫm `#7A1F1F` cho ribbon phụ đề
  - Vàng kem `#F3DFA7` cho chữ trên ribbon
  - Mực nâu đen cho chữ thường
- Header: banner dạng CUỘN THƯ (scroll) chứa tiêu đề sự kiện + năm —
  thành phần nhận diện của skin.
- Thẻ nội dung: bản đồ/sơ đồ diễn biến (sông, bãi cọc, hướng tiến
  quân…) vẽ tối giản trên nền kem, cập nhật theo từng mốc.
- Ribbon phụ đề: dải đỏ sẫm cố định ở dưới, chữ vàng kem — MỌI phụ
  đề đều nằm trong ribbon này.
- Tem tròn "SỬ VIỆT": đóng ở góc như dấu triện của series, xuất hiện
  ở thẻ mở và thẻ kết.
- Mascot: không dùng mascot hoạt hình — skin này dùng tem + cuộn thư
  làm nhận diện.

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề trên cuộn thư): tên sự kiện + năm + 1 câu treo về
  kết cục bất ngờ.
- Thân: 3–5 bước diễn biến theo mốc thời gian/địa điểm; mỗi bước 1
  thẻ bản đồ hoặc sơ đồ (badge n/N nhỏ dạng tem).
- Kết (thẻ kết luận): kết quả sự kiện + 1 câu ý nghĩa lịch sử; tem
  SỬ VIỆT đóng chốt.
- Mỗi bước 35–50 từ; giọng kể trang trọng.

## Quy trình sản xuất
1. Kịch bản: dựng timeline sự kiện từ nguồn sử liệu tin cậy trước
   khi viết; năm tháng/địa danh kiểm chứng chéo 2 nguồn.
2. Voice: VieNeu local — preset v3 Turbo giọng nam trầm, speed 1.1,
   đọc rõ tên riêng và địa danh cổ.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `history-explainer-video`. Bản đồ/sơ đồ vẽ tối giản theo từng mốc
   và cập nhật dần qua các bước, không thay bản đồ mới mỗi bước.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/bach-dang-938.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `history-explainer-video__<chu-de>.mp4`.

## QA checklist
- [ ] Header cuộn thư có tên sự kiện + năm chính xác
- [ ] Mọi phụ đề nằm trong ribbon đỏ sẫm chữ vàng kem — không phụ đề trần ngoài ribbon
- [ ] Tem "SỬ VIỆT" xuất hiện ở thẻ mở và thẻ kết
- [ ] Bản đồ/sơ đồ mỗi bước khớp mốc diễn biến đang kể (hướng tiến quân, vị trí)
- [ ] Năm tháng, tên người, địa danh đã kiểm chứng 2 nguồn
- [ ] Viền khung trang trí giữ suốt video, không bị thẻ nội dung đè mất
