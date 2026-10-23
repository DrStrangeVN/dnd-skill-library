---
name: travel-itinerary-video
description: Video dọc trình bày lịch trình du lịch theo giờ: thẻ vé, timeline, bản đồ tuyến chấm và bảng ngân sách — dùng cho kênh du lịch, review hành trình, gợi ý chuyến đi cuối tuần.
---

# Lịch trình du lịch (Travel Itinerary)

## Khi nào dùng
- Chia sẻ lịch trình chuyến đi có khung giờ cụ thể (24h/48h/2 ngày
  1 đêm) để người xem làm theo được.
- Cần số liệu thật: giờ mở cửa, giá vé, quãng đường.
- Đây là "cẩm nang dùng được" — không phải clip cảm xúc du lịch.

## Mẫu gốc đã phân tích
- File: `da-lat-48h.mp4` (chủ đề mẫu: Đà Lạt 48 giờ)
- Lưu tại: `~/workspace/reelcrew-analysis/videos/da-lat-48h.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~63 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/da-lat-48h.jpg`
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N (mỗi bước
  = 1 mốc giờ/điểm đến) → thẻ kết luận (ngân sách) + CTA.

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền kem đốm pastel `#FBF3E4`
  - Navy `#1F3350` + cam `#F58220` làm cặp màu chính
  - Chữ navy trên thẻ trắng
- Thẻ vé (ticket card): mép răng cưa 2 bên, chứa điểm đến + giờ —
  thành phần nhận diện của skin.
- Timeline giờ: trục dọc bên trái nối các mốc giờ tăng dần; mỗi bước
  gắn vào đúng mốc giờ của nó.
- Bản đồ tuyến chấm: các điểm đến nối bằng đường chấm; xuất hiện ở
  bước di chuyển hoặc thẻ tổng quan đầu/cuối.
- Bảng ngân sách: thẻ cuối dạng bảng cộng dồn từng khoản.
- Mascot: máy ảnh sticker.
- Phụ đề: thẻ trắng GHIM (pin) ở dưới, từ khoá highlight cam.

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề): điểm đến + tổng thời gian ("Đà Lạt 48 giờ") +
  lời hứa lịch trình trọn gói, trong 4 giây đầu.
- Thân: 4–6 bước theo mốc giờ thật (07:00 ăn sáng → 09:00 điểm A →
  …); mỗi bước 1 thẻ vé: giờ + điểm đến + 1 mẹo ngắn.
- Kết (thẻ kết luận): bảng ngân sách cộng tổng + CTA lưu lịch trình.
- Mỗi bước 25–40 từ; giọng vui tươi.

## Quy trình sản xuất
1. Kịch bản: dựng lịch trình giờ thật trước — giờ mở cửa và thời
   gian di chuyển giữa các điểm phải khả thi; giá vé/chi phí ghi
   nguồn và thời điểm kiểm tra vào ghi chú sản xuất.
2. Voice: VieNeu local — preset v3 Turbo giọng vui tươi, speed 1.1.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `travel-itinerary-video`. Timeline và thẻ vé là component theo dữ
   liệu mốc giờ; bản đồ tuyến chấm vẽ theo vị trí tương đối các điểm.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/da-lat-48h.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `travel-itinerary-video__<chu-de>.mp4`.

## QA checklist
- [ ] Timeline giờ tăng dần, không mốc nào chồng giờ hoặc thiếu thời gian di chuyển
- [ ] Thẻ vé có mép răng cưa 2 bên ở mọi điểm đến
- [ ] Bảng ngân sách cộng đúng tổng của từng khoản hiển thị
- [ ] Bản đồ tuyến chấm nối đúng thứ tự các điểm trong lịch trình
- [ ] Phụ đề dạng thẻ trắng ghim, highlight cam ở tên điểm đến/giờ
- [ ] Giá vé/giờ mở cửa có ghi thời điểm kiểm tra trong ghi chú sản xuất
