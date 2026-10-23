---
name: isometric-system-video
description: Video giải thích hệ thống bằng sơ đồ isometric line-art trong khung dashboard 60fps — dùng cho quy trình, nhà máy, kiến trúc phần mềm, luồng vận hành.
---

# Isometric giải thích hệ thống (Isometric System Explainer)

## Khi nào dùng
- Giải thích một HỆ THỐNG có nhiều thành phần nối nhau: dây chuyền
  sản xuất, kiến trúc phần mềm, luồng dữ liệu, quy trình vận hành.
- Khi người xem cần "nhìn toàn cảnh rồi đi từng bộ phận" thay vì
  đọc danh sách.
- Không dùng cho hệ thống chỉ có 1–2 thành phần — sơ đồ sẽ trống.

## Mẫu gốc đã phân tích
- File: `jev-factory.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/jev-factory.mp4`
- Khổ/fps/thời lượng: 1280×720 @60fps, ~70 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/jev-factory.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - UI sáng sạch trắng/xám nhạt `#F4F6F8`
  - Line-art xám `#5A6472`
  - Accent xanh lá `#35C759` — màu nhấn duy nhất
  - Chữ tối
- Khung dashboard cố định: header trên cùng ghi tên hệ thống; panel
  bên chứa legend/thông số; sân khấu isometric ở trung tâm.
- Sơ đồ: các khối isometric vẽ line-art; thành phần đang được nhắc
  tới SÁNG LÊN bằng accent xanh lá, các thành phần khác giữ xám.
- Luồng: mũi tên/đường ống animate cho thấy dữ liệu/vật liệu di
  chuyển giữa các khối.
- Chuyển động mượt ở 60fps: vẽ tuyến tính, highlight chuyển dần —
  không cắt cảnh rời rạc.

## Cấu trúc kịch bản
- Mở: toàn cảnh hệ thống (mọi khối đều xám) + 1 câu định nghĩa hệ
  thống làm gì.
- Thân: đi từng thành phần theo đúng thứ tự luồng; mỗi bước gồm khối
  sáng lên → 1–2 câu chức năng → luồng chạy sang khối kế tiếp.
- Kết: toàn hệ thống sáng đồng loạt, luồng chạy trọn 1 vòng từ đầu
  vào tới đầu ra.
- Mỗi khối 30–45 từ lời đọc.

## Quy trình sản xuất
1. Kịch bản: vẽ sơ đồ luồng (đầu vào → các khối → đầu ra) trước khi
   viết; lời đọc đi theo đúng thứ tự luồng thật của hệ thống.
2. Voice: VieNeu local — preset v3 Turbo giọng rõ ràng, trung tính,
   speed 1.1.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `isometric-system-video`, render ở 60fps. Highlight từng khối đồng
   bộ mốc thời gian của voice.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/jev-factory.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @60fps (đúng mẫu gốc — không hạ xuống 30fps).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `isometric-system-video__<chu-de>.mp4`.

## QA checklist
- [ ] File xuất đúng 60fps, chuyển động không giật khung
- [ ] Khối sáng lên khớp đúng thành phần đang được đọc (±0,3 giây)
- [ ] Khung dashboard (header + panel bên) cố định suốt video
- [ ] Accent chỉ là xanh lá; line-art còn lại giữ xám
- [ ] Thứ tự các khối trong video khớp luồng thật của hệ thống
- [ ] Cảnh kết: luồng chạy trọn từ đầu vào tới đầu ra, không đứt đoạn
