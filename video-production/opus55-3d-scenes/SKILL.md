---
name: opus55-3d-scenes
description: Router + hệ thống sản xuất cho video cảnh 3D học từ kho awesome-opus5-5-videos (nhóm 3D scenes, 117 prompt). Dùng khi user nói "làm video 3D", "làm cảnh 3D kiểu opus55", "dựng thế giới 3D", "video kiến trúc 3D / archviz", "mô hình sản phẩm 3D chuyển động", "video không gian 3D", hoặc gửi brief cần cả một cảnh/thế giới 3D (không chỉ một vật thể). Skill này chọn kỹ thuật (three.js worlds / GLSL shader / canvas pseudo-3D), sở hữu quy trình brief + storyboard + critic QA và chuẩn đầu ra dùng chung.
---

# Opus55 3D Scenes — Master (Router + Hệ thống sản xuất)

Học từ nhóm **3D scenes** của repo `awesome-opus5-5-videos` (703 video toàn repo, 117 mục 3D: 79 prompt full, 38 partial).
Thư viện prompt gốc: `~/workspace/opus55-videos/prompts/<slug>.md`; catalogue đã xếp nhóm: `~/workspace/opus55-videos/3D-INDEX.md`.
Xương sống của nhóm là prompt hệ thống của **everestchris6-399895** — một quy trình sản xuất video 3D hoàn chỉnh (GSAP master timeline + three.js). Skill này chưng cất quy trình đó; **chỉ học kỹ thuật và kỷ luật sản xuất, nội dung luôn làm mới**, không sao chép brief của tác giả khác.

**Ranh giới với nhóm Motion:** `opus-motion-threejs` (nhóm Motion) lo **vật thể 3D ngắn** — một sản phẩm/logo/chữ 3D làm nhân vật chính trong clip motion graphics. Bộ skill này lo **cả cảnh / cả thế giới**: môi trường có chiều sâu, kiến trúc, nhiều vật thể phối hợp, đường camera đi xuyên không gian, nhãn HTML chiếu từ 3D. Brief "một vật thể 3D bay/xoay 10 giây" → Motion. Brief "bay qua một khu phố / một căn phòng / một cỗ máy" → bộ này.

## Khi nào dùng

- Video cần một **không gian 3D thật**: thành phố, nội thất, showroom, dây chuyền, cỗ máy nhiều chi tiết, cảnh thiên nhiên dựng bằng hạt/shader.
- Archviz / giới thiệu dự án: mô hình kiến trúc premium, bay quanh công trình, nhãn chú thích vị trí.
- Phim sản phẩm 3D có bối cảnh: sản phẩm đặt trong môi trường, ánh sáng kiểu chụp studio, exploded view có nhãn.
- Brief chưa rõ engine → skill này phân loại rồi chuyển cho 1 trong 3 skill con:
  - `opus-3d-worlds` — Three.js: thế giới, môi trường, kiến trúc, sản phẩm trong bối cảnh
  - `opus-3d-shader` — GLSL: cảnh 3D tính hoàn toàn trong fragment shader (raymarching, SDF)
  - `opus-3d-canvas` — Canvas: pseudo-3D / 2.5D khi không cần 3D thật

## Chọn kỹ thuật theo brief (bảng router)

| Dấu hiệu trong brief | Chọn | Lý do |
|---|---|---|
| Có môi trường/không gian cụ thể (phố, phòng, nhà máy, đảo), nhiều vật thể, camera di chuyển trong cảnh, nhãn chú thích gắn vào vị trí 3D | `opus-3d-worlds` | Three.js dựng cảnh thật, chiếu nhãn HTML từ tọa độ 3D mỗi frame |
| Cảnh trừu tượng/toán học thuần: hình SDF biến dạng, hành tinh/thể lỏng tính bằng raymarching, "một file shader là cả bộ phim", không có asset ngoài | `opus-3d-shader` | Fragment shader là hàm thuần của (pixel, t) — xác định tuyệt đối, không cần mô hình |
| Muốn cảm giác có chiều sâu nhưng chủ thể là chữ/ảnh/UI phẳng, hoặc cần liquid-glass/morph 2D liên tục một take, ngân sách render thấp | `opus-3d-canvas` | Canvas 2.5D: rẻ, sắc nét, vẫn có parallax/quỹ đạo/curve không gian |
| Một vật thể 3D đơn lẻ, clip ngắn kiểu motion graphics | `opus-motion-threejs` (nhóm Motion) | Ngoài phạm vi bộ này — xem ranh giới ở đầu file |

Không chắc → mặc định `opus-3d-worlds` cho cảnh có chủ thể thật; `opus-3d-shader` khi brief nhấn mạnh "trừu tượng, phát sáng, biến dạng liên tục".

## Nguyên lý cốt lõi (hệ thống everestchris6, chưng cất)

1. **Mọi giá trị hoạt họa là hàm của thời gian trên MỘT master timeline.** Không timer, không animation thời gian thực, không random không seed. Bất kỳ frame nào render lại cũng phải giống hệt (deterministic `seek(t)` — kế thừa nguyên lý của `opus55-motion-graphics`, gồm spring dạng đóng `1 − (1 + ωt)·e^(−ωt)` và lưới nhịp).
2. **Một vật thể "gánh" câu chuyện xuyên suốt các shot (carry object).** Vật ở tiền cảnh trở thành cú chuyển cảnh; vật gánh giữ nguyên danh tính và **hạ cánh đúng cùng tọa độ pixel ở hai phía của cut**. Cắt chỉ được phép khi kích thước, hướng và chủ thể khớp nhau ở cả hai phía.
3. **Một chuyển động chính dẫn, các chuyển động phụ xếp lớp bên dưới, tất cả chồng lấp nhau.** Khung hình không bao giờ dừng–chạy đồng loạt. Tốc độ luôn biến thiên: đến thì chậm đủ để đọc, rời thì nhanh, vật tiếp theo chậm dần khi tới. Không chuyển động tuyến tính.
4. **Mỗi hành động phải sinh ra kết quả nhìn thấy được** (quét → hiện kết quả, chạm → đổi trạng thái, yêu cầu → có xác nhận). Không chuyển động trang trí vô nghĩa.
5. **Đa dạng tỉ lệ khung hình có chủ đích:** cận → toàn → overhead → chữ full-frame; không lặp lại cùng một bố cục (kiểu "tiêu đề trên ba thẻ") hai lần.
6. **Frame 1 là một bức tranh hoàn chỉnh** — không bao giờ là chữ/vật đang bay dở vào khung.
7. **3D chỉ dùng khi nó giải thích được điều vật lý/không gian** (lớp, bộ phận, vị trí, tỉ lệ). Ánh sáng như chụp sản phẩm: **soft key một phía + rim light phía sau**; góc camera giữ trong khoảng **35–55°**, không nhìn thẳng xuống mặt phẳng lớn, không kết thúc cận trên mặt phẳng. Kiến trúc kiểu mô hình premium: vật liệu thật, có đế, không chi tiết lơ lửng, không khe hở ở chỗ nối, không kính đen phẳng, không texture lặp lộ liễu.
8. **Nhãn là HTML chiếu từ cảnh 3D mỗi frame** — không bao giờ nướng chữ vào trong 3D (chữ trong 3D vỡ glyph tiếng Việt và không kiểm soát được tương phản).

## Quy trình sản xuất (pipeline chung — skill này sở hữu)

1. **Brief + facts file trước tiên.** Chốt: video để làm gì, ai xem, hành động cuối (CTA), độ dài + các kích thước xuất, brand (màu/font/logo), tài sản có sẵn. Mọi **con số, tên, tuyên bố** xuất hiện trên màn hình chỉ được lấy từ **một facts file duy nhất** — không bịa số liệu. Thiếu thông tin thì tự quyết theo chuẩn nhà và ghi lại giả định, không hỏi vòng vo.
2. **Học mẫu:** tra `3D-INDEX.md`, đọc 1–3 prompt gốc cùng archetype (ưu tiên `full`). Nếu user đưa video tham chiếu: phân tích số (frame-difference tìm cut/điểm nhanh, độ sáng, chi tiết cạnh), làm contact sheet tổng quan + sheet dày 16–20fps quanh mỗi transition, ghi chú quy tắc chuyển động rút ra. Tham chiếu chỉ để học — không copy hình ảnh/logo/bố cục/nhạc của họ.
3. **Storyboard dạng bảng — bắt buộc trước khi code:** cột **thời gian · trên màn hình có gì · khoảnh khắc này để làm gì · nó rời đi bằng cách nào · vật nào gánh sang shot sau**. Mật độ chuẩn: ~12–15 bố cục mỗi 30 giây, mỗi bố cục 1.4–3.5 giây; chủ thể chính chiếm phần lớn khung (không thẻ nhỏ lơ lửng giữa khoảng trống); đặt tên **3 khoảnh khắc "signature"** mô tả được mà không cần dùng tên hiệu ứng; video phải hiểu được khi tắt tiếng. Gửi storyboard cho một vòng critic (xem mục QA) và sửa trước khi dựng.
4. **Dựng các mảnh dùng chung trước:** bảng màu, font, model 3D dùng chung, và tọa độ pixel chính xác của mọi điểm bàn giao (handoff) giữa các cảnh.
5. **Mỗi cảnh là một component có trang test riêng**, render stills + clip ngắn, qua critic rồi mới nhập vào phim. Có thể dựng song song nhiều cảnh khi các mảnh chung đã xong.
6. **Test render 5 giây trước** để xác nhận pipeline (seek, render, encode) chạy đúng, rồi mới render full. Trên máy này render headless Chromium tuần tự, concurrency thấp (2 core); WebGL cần SwiftShader và probe frame thử không đen trước khi chạy hàng loạt.
7. **Âm thanh:** nhạc khớp năng lượng hình và người xem, để nhỏ dưới nội dung; whoosh ngắn mềm cho mỗi chuyển cảnh thật, click/pop nhỏ chỉ cho hành động thật trên màn hình; cắt cảnh rơi trên beat; loudness ≈ **−14 LUFS**, và luôn xuất kèm bản music-only.
8. **Critic loop tới khi đạt quality bar đo được** (mục QA) — builder không tự chấm bài của mình.

## Công thức & kỹ thuật đặc thù

- Master timeline: một timeline GSAP (hoặc hàm `seek(t)` tương đương) điều khiển cả DOM, canvas và three.js; camera path và vật gánh đều khóa vào cùng trục thời gian này.
- Handoff khớp pixel: tính vị trí/kích thước của vật gánh tại thời điểm cut ở cả hai scene trong lúc viết storyboard — không "ước lượng bằng mắt" ở khâu dựng.
- Pixel nền của render 3D phải đo và chỉnh tới khi **khớp đúng mã màu brand** (đo pixel thật trong frame xuất, không tin thông số khai báo vì encoding/ánh sáng làm lệch màu).
- Vật chuyển động "như sản phẩm thật" thì đo đường cong từ footage thật theo từng frame; số đo đó là curve — không tự chế easing cảm tính cho chuyển động cơ khí.
- Ảnh/clip AI tạo chỉ dùng cho shot phụ và phải ghi nhãn concept; không bao giờ tạo kết quả/công trình/khách hàng giả.

## QA bắt buộc (quality bar — đo được, lấy từ hệ thống gốc)

- **Frozen time:** tổng thời gian màn hình "đứng yên" ≤ ~1 giây mỗi 30 giây; không đoạn đứng nào dài hơn ~0.5 giây (đo bằng frame-difference, không cảm tính).
- **Frame 1** là bố cục hoàn chỉnh.
- **Tương phản chữ ≥ 4.5:1** ở mọi frame chữ xuất hiện; không chữ nào va chạm hay bay xuyên qua chữ khác; chữ luôn có nền đỡ khi nằm trên hình bận.
- Màu brand trong render 3D khớp giá trị brand (đo pixel nền/chủ thể).
- Loudness ổn định ≈ −14 LUFS, không clipping, hiệu ứng không bao giờ át nhạc.
- Người xem lần đầu **hiểu được video khi tắt tiếng**.
- Critic loop: sau storyboard, sau từng component và sau mỗi bản full render — gửi render + brief cho một critic "sạch" (chưa thấy quá trình dựng, không được mớm kết luận), nhận danh sách vấn đề xếp hạng kèm timestamp + phán quyết ship / thêm một vòng; sửa vấn đề lớn nhất trước; giữ ledger từng vòng (thấy gì · đã sửa gì · số đo trước/sau).
- Phẩm chất đối sánh: đặt cạnh video tham chiếu, bản làm không được trông yếu hơn. "Không có bug" khác với "hay".

## Output contract

Giao: **MP4 cuối** (+ bản music-only) + **HTML nguồn** + **storyboard** + **facts file** + thông số (kích thước/fps/thời lượng/dung lượng) + ghi chú kỹ thuật và slug prompt gốc đã tham khảo. Không đăng công khai khi chưa có duyệt mới của user. Chưa qua critic loop và quality bar thì không nói "xong".
