---
name: ecommerce-explainer-video
description: Video dọc giải thích TMĐT/bán lẻ với 2 skin (biển gỗ nền be / hoá đơn kraft mono) — dùng cho chủ shop, seller: tính lãi, quy trình bán hàng, công cụ AI cho shop.
---

# TMĐT & bán lẻ (Ecommerce Explainer)

## Khi nào dùng
- Nội dung cho chủ shop/seller: tính lãi từng đơn, phí sàn, quy
  trình xử lý đơn, công cụ hỗ trợ bán hàng.
- Chọn 1 trong 2 skin theo tính chất nội dung:
  - Skin gỗ/be: hướng dẫn thân thiện, quy trình, công cụ
  - Skin hoá đơn kraft: nội dung tiền bạc, số liệu, tính lãi

## Mẫu gốc đã phân tích
- File: `ai-inbox-shop.mp4` (skin A — biển gỗ/be, ~68 giây) và
  `lai-that-moi-don.mp4` (skin B — hoá đơn kraft, ~59 giây).
- Lưu tại: `~/workspace/reelcrew-analysis/videos/`
- Khổ/fps/thời lượng: 720×1280 @30fps cho cả 2 mẫu.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/ai-inbox-shop.jpg`
  (skin A), `sheets/lai-that-moi-don.jpg` (skin B).
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N → thẻ kết
  luận/CTA.

## Đặc tả thiết kế
- Skin A (gỗ/be):
  - Header là BIỂN GỖ khắc chữ; nền be `#EFE6D8`
  - Thẻ trắng mock UI inbox/chat khách hàng
  - Tông ấm, thân thiện
- Skin B (hoá đơn kraft):
  - Thẻ là HOÁ ĐƠN giấy kraft, mép răng cưa trên/dưới
  - Font mono IBM Plex Mono cho toàn bộ số liệu
  - Mascot hộp hàng sticker
  - Highlight teal `#0E7C7B` — chỉ ở con số chính (lãi/tổng)
- Quy tắc chung cả 2 skin:
  - Số tiền/số liệu là "nhân vật chính": mỗi bước có ít nhất 1 con
    số cụ thể trên thẻ
  - Một video CHỈ dùng 1 skin duy nhất từ đầu tới cuối
  - Phụ đề theo skin: A dùng pill tối trên nền be; B dùng dòng chữ
    mono trên dải hoá đơn ở dưới

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề): vấn đề tiền bạc cụ thể của shop ("lãi thật mỗi
  đơn còn bao nhiêu?") trong 4 giây đầu.
- Thân: 3–5 bước — mỗi bước bóc tách 1 khoản (doanh thu → phí sàn →
  ship → quảng cáo → lãi) hoặc 1 khâu quy trình; số trên thẻ
  cộng/trừ chạy theo lời đọc.
- Kết (thẻ kết luận): con số tổng kết (lãi thật/tỉ lệ %) khổ lớn +
  CTA áp dụng cho shop của mình.
- Mỗi bước 30–45 từ; giọng thực tế kiểu người bán nói với người bán.

## Quy trình sản xuất
1. Kịch bản: dựng bảng tính số liệu mẫu trước; mọi con số trong
   video phải cộng/trừ khớp nhau tuyệt đối. Ghi rõ số liệu là ví dụ
   minh hoạ trong ghi chú sản xuất.
2. Voice: VieNeu local — giọng clone "Nhật Phong (Local Clone)",
   speed 1.1.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `ecommerce-explainer-video` với tham số skin `wood` hoặc
   `receipt` chọn từ đầu. Số liệu animate cộng dồn theo voice.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   sheet của skin tương ứng theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây cho mỗi skin.
- Tên file xuất: `ecommerce-explainer-video__<chu-de>.mp4`.

## QA checklist
- [ ] Chỉ 1 skin trong toàn video (gỗ/be HOẶC hoá đơn kraft) — không trộn yếu tố 2 skin
- [ ] Mọi con số cộng/trừ khớp nhau giữa các bước và khớp con số kết luận
- [ ] Skin B: mép răng cưa hoá đơn + font mono cho mọi số liệu; highlight teal chỉ ở con số chính
- [ ] Skin A: header biển gỗ ở thẻ mở; mock UI inbox giống ứng dụng chat thật
- [ ] Badge n/N khớp số bước; mascot hộp hàng (skin B) nhất quán
- [ ] Không khẳng định doanh thu/lợi nhuận như cam kết — số liệu ghi rõ là ví dụ minh hoạ
