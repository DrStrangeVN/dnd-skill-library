---
name: farm-product-promo-video
description: Video dọc quảng bá nông sản/trang trại bằng ảnh thật, tem sticker và thẻ giá — dùng cho nông trại, đặc sản địa phương, sản phẩm thủ công bán qua tin nhắn.
---

# Quảng bá nông sản/trang trại (Farm Product Promo)

## Khi nào dùng
- Bán nông sản/đặc sản: mật ong, cà phê, trái cây, sản phẩm trang
  trại — kênh bán chính là nhắn tin đặt hàng.
- Bắt buộc dùng ẢNH THẬT của sản phẩm/trang trại; ảnh AI làm mất
  niềm tin với nhóm sản phẩm này.

## Mẫu gốc đã phân tích
- File: `honey-farm.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/honey-farm.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~43 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/honey-farm.jpg`
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N → thẻ kết
  luận/CTA, bọc trong skin nông trại.

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu) — tông ấm nông sản trên ảnh thật:
  - Kem `#FFF6E9`
  - Nâu `#6B4226`
  - Cam `#F59E0B`
- Hình ảnh: ảnh thật sản phẩm/trang trại full-bleed, ánh sáng tự nhiên.
- Typography: Baloo 2 tròn trịa cho mọi tiêu đề/giá — không dùng
  font góc cạnh trong skin này.
- Tem sticker tròn: giá, chứng nhận, "100% tự nhiên"… dán ở góc ảnh,
  hơi xoay nhẹ như tem giấy thật.
- Badge bước n/N thu nhỏ thành dạng tem tròn theo skin.
- Caption karaoke TIẾNG ANH theo từ, chữ trắng/nâu đậm trên dải mờ
  dưới ảnh.
- Thẻ kết: thẻ giá rõ ràng + nút CTA "Message to order" trông như
  nút bấm được, giữ đủ lâu ở cuối video.

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề): ảnh sản phẩm đẹp nhất + tên sản phẩm + 1 tem tròn
  chứa điểm khác biệt lớn nhất.
- Thân: 3–4 bước theo mạch: nguồn gốc/quy trình → lợi ích → cách
  dùng/bảo quản. Mỗi bước 1 ảnh thật + tem thông tin.
- Kết (thẻ CTA): thẻ giá + nút "Message to order", giữ tối thiểu
  2 giây cuối.
- Viết tiếng Anh theo mẫu (cả caption lẫn voice); câu ngắn, thân thiện.

## Quy trình sản xuất
1. Kịch bản: mọi tuyên bố về sản phẩm (nguồn gốc, chứng nhận, thành
   phần) phải đúng sự thật của sản phẩm thật — ghi nguồn kiểm chứng
   vào ghi chú sản xuất.
2. Voice: VieNeu — giọng EN thân thiện (preset hỗ trợ EN hoặc giọng
   EN của API), speed 1.1.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `farm-product-promo-video`. Ảnh thật crop dọc giữ chủ thể; tem
   sticker là component tái sử dụng.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/honey-farm.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–43 giây.
- Tên file xuất: `farm-product-promo-video__<chu-de>.mp4`.

## QA checklist
- [ ] 100% ảnh là ảnh thật của sản phẩm/trang trại — không ảnh AI, không stock lạ
- [ ] Mọi typo dùng Baloo 2, tông kem/nâu/cam nhất quán
- [ ] Tem sticker tròn, hơi xoay, không che phần chính của sản phẩm trong ảnh
- [ ] Thẻ kết có giá + nút "Message to order" rõ ràng, giữ ≥2 giây
- [ ] Caption karaoke tiếng Anh khớp từ đang đọc
- [ ] Tuyên bố sản phẩm (chứng nhận, nguồn gốc) đúng sự thật, không phóng đại
