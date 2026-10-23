---
name: office-skills-video
description: Video dọc dạy kỹ năng văn phòng (Excel, Word, công cụ số) bằng thẻ mock UI bảng tính — dùng cho kênh mẹo công sở, đào tạo nội bộ, series "1 hàm mỗi ngày".
---

# Kỹ năng văn phòng (Office Skills)

## Khi nào dùng
- Dạy 1 kỹ năng văn phòng cụ thể trong 1 video: 1 hàm Excel,
  1 phím tắt, 1 thao tác công cụ.
- Làm series đều đặn: mỗi video đúng 1 kỹ năng, cấu trúc lặp lại để
  khán giả quen nhịp.
- Không gộp 2 kỹ năng vào 1 video.

## Mẫu gốc đã phân tích
- File: `sumif-office.mp4` (chủ đề mẫu: hàm SUMIF)
- Lưu tại: `~/workspace/reelcrew-analysis/videos/sumif-office.mp4`
- Khổ/fps/thời lượng: 720×1280 @30fps, ~80 giây.
- Nguồn: https://reelcrew.io/#video
- Contact sheet đối chiếu: `~/workspace/reelcrew-analysis/sheets/sumif-office.jpg`
- Engine chung nhóm B: thẻ tiêu đề → các bước đánh số n/N → thẻ kết
  luận/CTA.

## Đặc tả thiết kế
- Palette (ước lượng từ mẫu):
  - Nền kem `#FAF5EA`
  - Navy `#1F3350` cho pill phụ đề
  - Cam `#F58220` highlight từ khoá/công thức
  - Vàng băng dính `#F5C542`
- Header: dải BĂNG DÍNH VÀNG (tape) dán trên đầu thẻ tiêu đề; tiêu đề
  nằm dưới dải tape — thành phần nhận diện của skin.
- Thẻ nội dung: thẻ trắng MOCK UI BẢNG TÍNH — lưới ô, thanh công
  thức, con trỏ — vẽ tối giản nhưng giống giao diện Excel thật.
- Mascot sticker theo chủ đề văn phòng xuất hiện ở góc thẻ.
- Phụ đề: pill navy chữ trắng ở dưới; từ khoá/công thức trong câu
  được highlight cam.
- Chấm tiến trình (dots) dưới cùng: số chấm = số bước, chấm sáng
  dần theo bước hiện tại.

## Cấu trúc kịch bản
- Mở (thẻ tiêu đề dưới băng dính vàng): tên kỹ năng + tình huống đau
  đầu nó giải quyết, trong 4 giây đầu.
- Thân: 3–5 bước — mỗi bước 1 thẻ mock bảng tính cho thấy thao tác/
  công thức tiến thêm 1 nấc (badge n/N).
- Kết (thẻ kết luận): công thức/thao tác hoàn chỉnh nguyên thẻ +
  CTA lưu video/theo dõi phần tiếp theo.
- Mỗi bước 30–45 từ; đọc rõ từng ký tự của công thức quan trọng.

## Quy trình sản xuất
1. Kịch bản: kiểm chứng công thức/thao tác chạy đúng trên phần mềm
   thật trước khi viết; chuẩn bị sẵn file dữ liệu ví dụ khớp video.
2. Voice: VieNeu local — preset v3 Turbo giọng rõ ràng, speed 1.1.
3. Dựng: Remotion tại `~/workspace/video-kit`, composition
   `office-skills-video`. Mock UI bảng tính là component dựng theo
   dữ liệu từng bước, không chụp màn hình thật.
4. Finish: `~/workspace/video-kit/tools/finish.sh` — nhạc nền warm pad
   ~−28dB dưới voice, loudnorm −14 LUFS.
5. QA: `tools/sheet.sh` trích contact sheet của bản dựng, đối chiếu
   `sheets/sumif-office.jpg` theo checklist bên dưới.

## Thông số xuất
- Khổ/fps: 720×1280 @30fps (đúng mẫu gốc).
- Video: H.264, yuv420p.
- Âm thanh: AAC stereo 48 kHz, loudnorm −14 LUFS, true peak ≤ −1 dBTP.
- Demo chuẩn: 30–45 giây.
- Tên file xuất: `office-skills-video__<chu-de>.mp4`.

## QA checklist
- [ ] Header có dải băng dính vàng đúng style, không thay bằng banner thường
- [ ] Mock UI đủ giống bảng tính thật (lưới ô + thanh công thức) để đối chiếu được
- [ ] Công thức/thao tác trong video chạy đúng khi gõ lại trên phần mềm thật
- [ ] Chấm tiến trình: số chấm = số bước, chấm hiện tại khớp badge n/N
- [ ] Highlight cam chỉ rơi vào từ khoá/công thức, không tô tràn lan
- [ ] Phụ đề pill navy không che hàng ô đang được minh hoạ
