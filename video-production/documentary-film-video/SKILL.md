---
name: documentary-film-video
description: Phim tư liệu ngang dài hơi với thẻ chương, số năm khổ lớn và tư liệu thật — dùng cho hành trình lịch sử, hồ sơ sự kiện, câu chuyện nhiều giai đoạn.
---

# Phim tư liệu (Documentary Film)

## Khi nào dùng
- Câu chuyện dài nhiều giai đoạn: lịch sử một ngành/một nơi, hồ sơ
  sự kiện, hành trình phát triển theo năm tháng.
- Thời lượng từ vài phút trở lên; khán giả xem ngang.
- Ưu tiên độ tin cậy tư liệu hơn tốc độ; không dùng cho tin nhanh.

## Mẫu gốc đã phân tích
- File: `internet-vietnam.mp4`
- Lưu tại: `~/workspace/reelcrew-analysis/videos/internet-vietnam.mp4`
- Khổ/fps/thời lượng: 1280×720 @24fps, ~292 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/internet-vietnam.jpg`

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền tối trung tính `#101216`
  - Chữ trắng
  - Màu theo tư liệu gốc — ảnh lưu trữ giữ nguyên màu thời kỳ,
    không ép về một tông
- Tư liệu: ảnh/video LƯU TRỮ THẬT là chính, có ghi nguồn; không thay
  bằng ảnh AI.
- Thẻ chương: toàn khung nền tối, chữ "CHƯƠNG n — <mốc thời gian>" mở
  đầu mỗi giai đoạn.
- Số năm khổ lớn: typography chiếm khung khi chuyển mốc thời gian
  quan trọng.
- Biểu đồ: trình bày trên nền tối khi cần số liệu.
- Thẻ trích dẫn (quote card): cho phát biểu của nhân vật/tài liệu gốc.
- Phụ đề: thanh tối dưới cùng, ≤2 dòng. Nhịp chậm — mỗi cảnh tư liệu
  giữ đủ lâu để xem.

## Cấu trúc kịch bản
- Mở: mốc năm đầu tiên + 1 tư liệu tiêu biểu + câu hỏi xuyên suốt phim.
- Thân: mỗi chương 1 giai đoạn, theo trình tự: thẻ chương → chuỗi tư
  liệu → biểu đồ/trích dẫn (khi có) → câu chuyển giai đoạn.
- Kết: thẻ trích dẫn tổng kết hoặc đối chiếu mốc năm đầu–cuối.
  Không CTA bán hàng.
- Mỗi chương 150–250 từ lời đọc cho bản đầy đủ.

## Quy trình sản xuất
1. Kịch bản: dựng timeline niên biểu trước khi viết lời; mọi mốc
   ngày/tháng/năm kiểm chứng từ ít nhất 1 nguồn tư liệu tin cậy và
   ghi nguồn vào ghi chú sản xuất.
2. Voice: VieNeu local — preset v3 Turbo giọng trầm, speed 1.0.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `documentary-film-video`. Tư liệu sắp theo chương; thẻ chương và
   số năm khổ lớn là component tái sử dụng.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/internet-vietnam.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 1280×720 @24fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: ~60 giây (mở + 1 chương rút gọn).
- Tên file xuất: `documentary-film-video__<chu-de>.mp4`.

## QA checklist
- [ ] Thẻ chương đúng format "CHƯƠNG n — <mốc>" ở đầu mỗi giai đoạn
- [ ] Số năm khổ lớn xuất hiện ở mọi mốc thời gian trọng yếu
- [ ] Mọi tư liệu có ghi nguồn; không dùng ảnh AI đóng vai tư liệu thật
- [ ] Niên biểu trong lời đọc không mâu thuẫn giữa các chương
- [ ] Biểu đồ trên nền tối, số liệu khớp nguồn đã kiểm chứng
- [ ] Nhịp cắt chậm kiểu tư liệu — không chèn hiệu ứng short-form
