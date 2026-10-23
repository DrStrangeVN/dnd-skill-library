---
name: property-location-video
description: Video dọc giới thiệu vị trí bất động sản: ảnh dự án + bản đồ tối với tuyến đường neon — dùng cho ra mắt dự án, vị trí đất/nền, điểm bán cần chứng minh tiện ích xung quanh.
---

# Video vị trí bất động sản (Property Location)

## Khi nào dùng
- Giới thiệu vị trí dự án BĐS: căn hộ, đất nền, shophouse — giá trị nằm
  ở "ở đâu, gần gì, bao nhiêu phút".
- Nội dung minh hoạ/tiếp thị: bắt buộc gắn nhãn demo minh hoạ như mẫu
  gốc; không khẳng định pháp lý/giá bán chưa kiểm chứng.

## Mẫu gốc đã phân tích
- File: `ho-tay.mp4` và `metro-2a.mp4` (2 mẫu cùng 1 template).
- Lưu tại: `~/workspace/reelcrew-analysis/videos/`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~37 giây mỗi mẫu.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/ho-tay.jpg`,
  `sheets/metro-2a.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Ảnh dự án sáng tự nhiên
  - Bản đồ tối (CARTO dark basemap trên dữ liệu OpenStreetMap)
  - Tuyến đường neon lime `#B4FF39`
  - Chữ trắng/lime đậm; pill badge số liệu nền trắng chữ đen hoặc
    nền đen chữ lime
- Phần 1 — ảnh: ảnh AI/render BĐS zoom chậm (Ken Burns) mở đầu.
- Phần 2 — bản đồ tối: tuyến đường VẼ CHẠY (draw-on animation) từ dự
  án tới từng tiện ích; điểm đến có ghim + nhãn tên.
- Pill badge: số liệu khoảng cách/thời gian bật lên theo từng điểm
  đến ("5 phút — chợ", "2 km — trường học"…).
- Nhãn cố định trên cùng: "VIDEO DEMO · DỰ ÁN MINH HỌA" — bắt buộc,
  hiện suốt video.
- Phụ đề: thanh tối dưới cùng, ≤2 dòng, không che ghim/nhãn bản đồ.

## Cấu trúc kịch bản
- Mở (0:00–0:03): hook bằng lợi thế vị trí mạnh nhất, trên ảnh dự án.
- Thân: 3–4 điểm tiện ích theo đúng thứ tự tuyến đường vẽ trên bản đồ;
  mỗi điểm 1 câu + 1 pill số liệu.
- Kết: quay về ảnh dự án + CTA mềm (xem vị trí thực tế/nhận thông tin).
  Không cam kết giá hay pháp lý.
- Tổng lời đọc: ~90–110 từ cho 37 giây.

## Quy trình sản xuất
1. Kịch bản: liệt kê tiện ích theo tuyến đường thật trước khi viết;
   mọi khoảng cách/thời gian phải ĐO từ bản đồ, không ước lượng miệng.
2. Voice: VieNeu local — giọng clone "Nhật Phong (Local Clone)",
   speed 1.1, giọng giới thiệu tự tin.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `property-location-video`. Tile bản đồ CARTO dark; tuyến đường
   draw-on theo mốc thời gian của voice.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/ho-tay.jpg` và `sheets/metro-2a.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–40 giây.
- Tên file xuất: `property-location-video__<chu-de>.mp4`.

## QA checklist
- [ ] Nhãn "VIDEO DEMO · DỰ ÁN MINH HỌA" hiện suốt video, dễ đọc
- [ ] Tuyến đường neon vẽ khớp thứ tự tiện ích trong lời đọc
- [ ] Mọi pill số liệu (phút/km) đã đo từ bản đồ thật, đúng đơn vị
- [ ] Bản đồ dùng bản tối — không lẫn tile sáng mặc định của OSM
- [ ] Phụ đề trong thanh tối, không che ghim/nhãn trên bản đồ
- [ ] Không có khẳng định giá bán/pháp lý chưa kiểm chứng trong lời và chữ trên hình
