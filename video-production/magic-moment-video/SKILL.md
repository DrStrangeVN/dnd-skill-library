---
name: magic-moment-video
description: Biến clip talking-head/selfie của Trí thành video dọc kể lại một câu chuyện công việc thật mà trợ lý AI đã làm — lời thoại gốc giữ nguyên, câu chuyện tái hiện đồng bộ bằng bong bóng chat, gõ chữ, reaction, widget/app thật, âm thanh tin nhắn, kết bằng lockup. Dùng khi Trí có clip quay mặt nói chuyện và muốn dựng thành clip ngắn chia sẻ được về việc AI đã làm gì cho mình.
---

# Magic-Moment Video

> Chưng cất từ thiết kế workflow của skill `magic-moment` trong bản lưu trữ
> không chính thức https://github.com/win4r/MuseAI-Skills
> (`opt/hatch/skills/magic-moment/`, HEAD 6c12bde, 26/11/2026).
> Repo nguồn KHÔNG CÓ LICENSE và là snapshot skill hệ thống của Muse — skill
> này viết lại hoàn toàn bằng lời của mình, KHÔNG chép nguyên văn, KHÔNG copy
> file hay component từ nguồn. Tool render gốc (`mm`) không có trong snapshot
> nên pipeline dưới đây thay bằng công cụ sẵn có của Trí: Remotion + giọng
> VieNeu API + QA frame.

## Mục đích

Một video "magic moment" không phải video giới thiệu tính năng. Nó kể một
câu chuyện có thật, đã xảy ra: Trí nói một câu, trợ lý làm một việc, kết quả
hiện ra trên màn hình — và người xem thấy đúng việc đó tái hiện đồng bộ với
lời kể. Giá trị nằm ở tính thật: mọi beat trong video phải bám vào công việc
máy đã làm, không dựng chuyện.

## Khi nào dùng / không dùng

Dùng khi:
- Trí có clip talking-head hoặc selfie (quay bằng điện thoại cũng được) kể
  về một việc AI đã làm cho mình.
- Có artifact thật để khoe: file, deck, web, app, bảng số liệu, tin nhắn.
- Muốn clip dọc 9:16 đăng Shorts/Reels/TikTok.

Không dùng khi:
- Không có clip gốc có lời thoại thật (không bịa lời kể).
- Câu chuyện chưa có bằng chứng (không có file/log/artifact thật để đối chiếu).
- Chỉ muốn video giải thích chung chung — dùng skill video explainer khác.

## Quy trình 6 bước (có cổng review trước render)

### 1. Transcript + fact sheet

- Lấy transcript đầy đủ của clip gốc (nghe và gõ lại, hoặc dùng công cụ
  transcribe sẵn có). Giữ nguyên lời Trí nói — không viết lại lời thoại.
- Lập fact sheet: liệt kê từng việc AI đã làm trong câu chuyện, đối chiếu với
  bằng chứng thật (file đã tạo, log chạy, link artifact, tin nhắn đã gửi).
  Beat nào không có bằng chứng thì bỏ khỏi kịch bản, không bịa.

### 2. Chọn beat hội thoại và artifact reveal

- Từ fact sheet, chọn 3–5 beat đắt nhất: mỗi beat = một hành động AI làm +
  một thứ hiện ra trên màn hình (file card, slide, web, widget, kết quả).
- Mỗi beat trả lời được: "người xem thấy gì thay đổi trên màn hình ở giây
  này?" Nếu không có gì để thấy thì đó không phải beat hình ảnh — cắt.

### 3. Lên visuals

- Kiểu hiển thị theo đúng thứ đang kể: bong bóng chat khi kể về trao đổi,
  hiệu ứng gõ chữ khi kể về viết, reaction khi kể về phản hồi, widget/app
  thật khi kể về sản phẩm đã dựng.
- Artifact thật được cho đủ không gian: hiện nguyên màn hình hoặc khung lớn,
  không nhét vào góc nhỏ. Dùng ảnh chụp màn hình thật của artifact, không
  dựng lại giao diện giả.
- Nền và chữ theo chuẩn kênh: video dọc 1080×1920@30, chữ lớn tiếng Việt
  dùng Be Vietnam Pro Black 900 (font Anton/Oswald lỗi dấu nặng ở khổ lớn).

### 4. Screenplay + timeline

- Viết screenplay: mỗi beat gồm thời gian bắt đầu/kết thúc, lời thoại gốc
  (trích đúng transcript), visual hiện ra, âm thanh (ting tin nhắn, pop khi
  chữ hiện).
- Timeline bám giọng đọc: chữ và artifact xuất hiện đồng bộ với lời thoại,
  không chạy trước/sau quá 0,3 giây.
- Chuẩn kênh Học Bóng Rổ: video dọc tối thiểu 60 giây (mục tiêu 60–90 giây).

### 5. Review gate — BẮT BUỘC trước render

- Đọc lại screenplay đối chiếu fact sheet: beat nào không có bằng chứng thì
  cắt. Kiểm tra từng artifact trong timeline có đúng file thật không.
- Xem thử timeline tĩnh (contact sheet hoặc storyboard): chữ không tràn,
  không đè nhau, dấu tiếng Việt đúng vị trí.
- Chỉ render khi gate này pass. Sửa tối đa 3 vòng; quá 3 vòng chưa pass thì
  báo lại và hỏi hướng, không render mù.

### 6. Render + QA

- Render bằng Remotion (project riêng tại
  `~/workspace/video-kit/demos/<slug>/`), giọng kể là giọng trong clip gốc
  (tách audio gốc khỏi clip bằng ffmpeg, giữ nguyên làm narration track —
  không thu lại giọng khác), nhạc nền warm pad nhẹ ~28 dB dưới giọng đọc nếu cần.
- QA đo thật trên file cuối: thời lượng, loudness mục tiêu −14 LUFS (±0,5),
  0 đoạn đen, xem khung hình thật để chắc chữ không cắt/tràn.
- Chỉ báo xong khi render + QA thật sự xong. Không đăng công khai nếu chưa
  có duyệt (trừ kênh Học Bóng Rổ đã có ủy quyền tự đăng theo plan đã duyệt).

## Ví dụ beat (ngắn)

Transcript: "Tôi gửi cho nó một cái reel, nó phân tích xong dựng lại cho tôi
một video mới trong một buổi sáng."
→ Beat: [Trí gửi link reel] → [rea-video phân tích: "100% motion graphics
vẽ bằng code"] → [demo mới 70 giây hiện lên, Trí duyệt]. Bằng chứng: file
reel gốc + báo cáo phân tích + file demo đã render.

## Output

- Video dọc 1080×1920@30, H.264 + AAC, −14 LUFS.
- `scripts/script.md`: transcript gốc + fact sheet + screenplay.
- `QA.md`: số đo thật (thời lượng, LUFS, TP, đoạn đen, lỗi đã sửa).

## Giới hạn

- Không bịa lời thoại, không bịa kết quả công việc.
- Không dùng ảnh/video AI thay cho artifact thật trong câu chuyện.
- Tool `mm` (transcribe/validate/preview/render/inspect/publish) của nguồn
  gốc không tồn tại trong môi trường này — không tìm, không cài, không giả
  vờ có nó. Pipeline trên đã thay bằng Remotion + VieNeu + QA frame.
- Nhạc nền chỉ dùng nhạc có giấy phép rõ ràng.

## Nguồn

- Thiết kế workflow: skill `magic-moment` trong
  https://github.com/win4r/MuseAI-Skills (không license, snapshot skill hệ
  thống Muse, HEAD 6c12bde). Skill này chưng cất lại bằng lời của mình.
