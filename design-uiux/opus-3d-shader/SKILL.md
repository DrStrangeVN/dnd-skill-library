---
name: opus-3d-shader
description: Kỹ thuật dựng cảnh 3D hoàn toàn bằng GLSL fragment shader — raymarching/SDF, thể lỏng, hành tinh và cảnh trừu tượng có chiều sâu tính theo pixel (nhóm Shader/WebGL của kho opus5.5 3D). Dùng khi brief muốn một thế giới 3D không cần mô hình/asset: hình khối biến dạng liên tục, bề mặt toán học, cảnh "một shader là cả bộ phim", hoặc vật liệu/hậu kỳ GLSL cho cảnh three.js. Luôn đi cùng pipeline chung của opus55-3d-scenes (seek(t) xác định, storyboard, quality bar đo được).
---

# Opus 3D — Shader (GLSL Raymarching & Frag 3D)

## Khi nào dùng

- Cảnh 3D **không có mô hình**: toàn bộ hình học là hàm khoảng cách (SDF) được raymarch trong fragment shader — khối uốn, thể lỏng metaball, địa hình/hành tinh thủ tục, tunnel, fractal.
- Brief một câu nhưng đòi độ phức tạp không gian cao (mẫu kinh điển của nhóm: "vẽ cảnh X phức tạp, tinh xảo nhất bằng bất kỳ kỹ thuật nào" — tác giả chọn GLSL thuần).
- Cần vật liệu/hậu kỳ cấp pixel cho cảnh three.js: DOF, glow có kiểm soát, biến dạng bề mặt — khi đó skill này hỗ trợ `opus-3d-worlds` làm chủ.
- Không dùng khi: cảnh có địa điểm/vật thể cụ thể phải nhận diện được (phố, phòng, sản phẩm thật → `opus-3d-worlds`); nền trừu tượng 2D chảy đơn giản không cần chiều sâu 3D (→ `opus-motion-shader` bên nhóm Motion lo nền/liquid 2D).

## Nguyên lý cốt lõi

Kế thừa nguyên lý của `opus55-3d-scenes`, với đặc thù shader:

1. **Cả thế giới là một hàm thuần `f(pixel, t)`.** Không state, không buffer tích lũy cho bản xuất (feedback buffer chỉ dùng nếu vẫn suy ra được từ `t`). Đây là archetype xác định tuyệt đối nhất của corpus: seek tới frame bất kỳ, thứ tự nào, cũng ra đúng hình đó.
2. **Hình học bằng SDF + phép biến đổi miền (domain warp/repeat/twist):** độ phức tạp đến từ toán — lặp miền có giới hạn, uốn không gian, trộn SDF bằng smooth-min — không đến từ số lượng asset.
3. **Camera vẫn là người kể chuyện:** dù không có scene graph, đường camera (vị trí + hướng nhìn theo `t`) phải được storyboard như mọi cảnh 3D khác; raymarch bay qua một thế giới đẹp mà không có ý đồ vẫn là video yếu.
4. **Ánh sáng tính trong shader nhưng theo cùng luật chụp sản phẩm:** một hướng sáng chính (key) + rim/back tách khối; normal suy từ gradient của SDF — ánh sáng phẳng đều là lỗi số một làm cảnh shader trông "rẻ".

## Quy trình sản xuất

1. Tra `~/workspace/opus55-videos/3D-INDEX.md` nhóm Shader/WebGL và các mục lai threejs+shader ở nhóm Three.js, đọc 1–2 prompt gốc (ưu tiên `full`).
2. Storyboard theo master: với shader, "vật gánh" thường là một hình khối SDF xuyên suốt hoặc chính đường camera; ghi rõ các pha biến dạng theo thời gian.
3. Single-file HTML: WebGL fullscreen quad + fragment shader; uniform chỉ gồm `u_time` (từ `seek(t)`), độ phân giải, và các tham số đã chốt. Viết SDF theo lớp: hình gốc → biến đổi miền → vật liệu/ánh sáng → hậu kỳ.
4. Render thử frame tại các mốc storyboard ở độ phân giải thấp để duyệt hình khối và đường camera (raymarch nặng — đừng render full mới phát hiện sai bố cục), test clip 5 giây, rồi mới render full. Trên máy này: SwiftShader render CPU rất chậm với raymarch — cân nhắc hạ độ phân giải nội bộ rồi upscale bằng ffmpeg, và render tuần tự qua đêm cho cảnh dài.
5. QA theo quality bar của master + mục QA riêng dưới đây.

## Công thức & kỹ thuật đặc thù

- **Prompt gốc nên tham khảo (prompt full, trong `~/workspace/opus55-videos/prompts/`):**
  - `axtonliu-290566` — GLSL/WebGL thuần: brief một dòng đòi cảnh có khớp nối và chuyển động không gian phức tạp nhất (bồ nông đạp xe — bài test năng lực không gian kinh điển), giải bằng shader. Mẫu cho tư duy "không asset, chỉ toán".
  - `ishuagra02-678129` — three.js + GLSL + particles: môi trường bãi biển bằng hạt phát sáng, shader lo chất liệu và dải chuyển động. Mẫu lai khi shader là lớp vật liệu của một thế giới three.js.
  - `alexalbert-274839` — dù là three.js là chính, các bề mặt/vật liệu tùy biến bằng shader là phần làm cảnh "có thật"; tham khảo cách khóa shader phục vụ dữ kiện thay vì trang trí.
  - `tanabe-fragm-322001` — hậu kỳ tự viết (DOF vòng bokeh theo độ sâu) cho cảnh three.js: mẫu khi cần hiệu ứng cấp pixel mà engine không có sẵn.
- **Raymarching khung chuẩn:** `ro/rd` từ camera theo `t`; vòng lặp bước tiến theo SDF (tối đa ~64–128 bước, epsilon theo khoảng cách); dừng sớm khi ra khỏi vùng cảnh. Normal = gradient trung tâm của SDF. Fog theo khoảng cách để có chiều sâu không khí.
- **Smooth-min (smin) cho metaball/thể lỏng:** hệ số `k` là thông số "độ dính" — khóa theo storyboard, không vặn theo cảm tính từng shot.
- **Domain repeat có kẹp chỉ số (cell clamping)** để tránh artefact ở xa; twist/bend áp trên miền trước khi tính SDF.
- **Chống vỡ hình khi render:** raymarch ở SwiftShader dễ timeout với vòng lặp dài — giữ step count vừa phải, dùng bounding volume đơn giản, và luôn probe frame nặng nhất (góc nhìn nhiều bề mặt nhất) trước khi render full.

## QA bắt buộc

- Toàn bộ quality bar của `opus55-3d-scenes`.
- Riêng Shader: không banding ở vùng gradient lớn (thêm dither hạt mịn nếu cần); không nhấp nháy (aliasing theo thời gian) khi camera chậm — kiểm bằng cách xem clip, không chỉ stills; frame ở góc nhìn "nặng" nhất render đúng, không đen/timeout; seek ngẫu nhiên nhiều thời điểm cho cùng một hình khi gọi lại.

## Output contract

MP4 cuối (+ music-only) + HTML nguồn (shader đọc/sửa được) + storyboard + ghi chú kỹ thuật SDF/ánh sáng đã dùng và slug prompt gốc đã tham khảo. Không đăng khi chưa được user duyệt.
