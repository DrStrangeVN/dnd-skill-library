---
name: profile-showreel-video
description: Showreel hồ sơ cá nhân khổ ngang phong cách ghi hình: kinetic type, mindmap thành tựu, overlay máy quay — dùng cho portfolio cá nhân, hồ sơ ứng tuyển, giới thiệu chuyên gia.
---

# Showreel hồ sơ cá nhân (Profile Showreel)

## Khi nào dùng
- Giới thiệu 1 con người: ứng tuyển, portfolio freelancer/chuyên gia,
  hồ sơ diễn giả/đối tác.
- Khổ ngang để gửi kèm hồ sơ hoặc đăng YouTube/LinkedIn.
- Không phải short dọc câu view — đừng ép template này vào khổ dọc.

## Mẫu gốc đã phân tích
- File: `showreel-ho-so.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/showreel-ho-so.mp4`
- Khổ/fps/thời lượng: 1280×720 @30fps (khổ ngang — ngoại lệ trong
  nhóm AgentVid), ~36 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/showreel-ho-so.jpg`
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N → thẻ kết
  luận/CTA.

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền navy tối `#0D1B2E`
  - Accent cam `#FF8A3D`
  - Chữ trắng đậm
- Kinetic type đậm: tên, vai trò, con số thành tựu chạy chữ lớn theo nhịp.
- Ảnh chân dung nhân vật chính đặt trong khung cố định.
- Mindmap: các nhánh kỹ năng/dự án mở dần từ trung tâm, khớp từng bước.
- Overlay kiểu máy quay: khung ngắm ở 4 góc + chấm REC + timecode chạy
  liên tục ở góc khung — hiện SUỐT video, không tắt ở thẻ nào.
- Thẻ bước: mỗi dự án/thành tựu 1 thẻ, có badge số bước n/N theo
  engine chung.

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề): tên + vai trò + 1 con số ấn tượng nhất, kinetic
  type trong 3 giây đầu.
- Thân: 3–4 bước — mỗi bước 1 dự án/thành tựu (badge n/N); mindmap mở
  thêm nhánh tương ứng và giữ các nhánh đã mở.
- Kết (thẻ CTA): tổng hợp thế mạnh + cách liên hệ.
- Mỗi bước 25–35 từ; giọng điệu tự tin, không khoe khoang.

## Quy trình sản xuất
1. Kịch bản: chắt lọc hồ sơ thành 3–4 thành tựu CÓ CON SỐ; mọi con số
   phải khớp hồ sơ thật của nhân vật.
2. Voice: VieNeu local — giọng clone "Nhật Phong (Local Clone)",
   speed 1.1 (hoặc giọng của chính nhân vật nếu được phép dùng).
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `profile-showreel-video`. Timecode chạy bằng đồng hồ frame thật
   của composition, không dùng số tĩnh.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/showreel-ho-so.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–40 giây.
- Tên file xuất: `profile-showreel-video__<chu-de>.mp4`.

## QA checklist
- [ ] Timecode chạy liên tục, không đứng/nhảy ngược ở các điểm cắt
- [ ] Overlay khung ngắm + REC đủ 4 góc, hiện suốt video
- [ ] Mindmap mở nhánh khớp bước đang đọc; nhánh đã mở giữ nguyên đến cuối
- [ ] Badge n/N đúng thứ tự và khớp tổng số bước của kịch bản
- [ ] Accent cam nhất quán trên nền navy; overlay không che mặt trong ảnh chân dung
- [ ] Mọi con số thành tựu khớp hồ sơ thật của nhân vật (không bịa số)
