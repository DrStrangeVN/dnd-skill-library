---
name: opus-3d-canvas
description: Kỹ thuật pseudo-3D / 2.5D bằng Canvas 2D — cảnh có chiều sâu, quỹ đạo không gian, chữ và vật thể di chuyển trong "không gian" mà không cần engine 3D thật (nhóm Canvas của kho opus5.5 3D). Dùng khi brief muốn cảm giác 3D nhưng chủ thể là chữ/ảnh/UI phẳng: phim ra mắt sản phẩm một-take liên tục, kinetic type trên quỹ đạo cong, parallax nhiều lớp, liquid glass trên canvas. Luôn đi cùng pipeline chung của opus55-3d-scenes (seek(t) xác định, storyboard bảng, beat grid, quality bar đo được).
---

# Opus 3D — Canvas (Pseudo-3D / 2.5D)

## Khi nào dùng

- Muốn **cảm giác không gian** (bay tới, vòng quanh, đường cong quỹ đạo, lớp trước–sau) nhưng chủ thể thật là chữ, ảnh, UI — dựng 3D thật sẽ nặng và kém sắc.
- Phim một take liên tục kiểu keynote: mọi cảnh sinh ra từ cảnh trước bằng biến hình (morph), không cắt/fade — mẫu mạnh nhất của nhóm là `twoclipping-496100`.
- Kinetic typography có "vật lý không gian": chữ chạy trên ellipse/quỹ đạo, camera kéo lùi/lăn (roll) quanh cụm chữ.
- Không dùng khi: cần vật thể 3D thật với vật liệu/ánh sáng đúng (→ `opus-3d-worlds`), hoặc hình học toán thuần cấp pixel (→ `opus-3d-shader`). Nhóm này đánh đổi "3D thật" lấy tốc độ, độ sắc và khả năng morph liên tục.

## Nguyên lý cốt lõi

Kế thừa nguyên lý của `opus55-3d-scenes` và `opus55-motion-graphics` (hàm thuần của `t`, spring đóng, beat grid), với đặc thù 2.5D:

1. **Chiều sâu là quy ước vẽ, không phải engine:** thứ tự lớp (painter's order), tỉ lệ theo khoảng cách giả, parallax khi "camera" di chuyển, và đường cong phân tích (ellipse, bezier, quỹ đạo) tạo cảm giác không gian. Mọi vị trí tính bằng công thức đóng từ `t` — cấm tích lũy vật lý.
2. **Camera tách khỏi hướng chữ/vật:** biến đổi camera (pull-back, roll, bám vận tốc) áp lên toàn cảnh; hướng của chủ thể đang đọc phải được bù trừ để luôn đọc được (counter-rotate). Mẫu chuẩn: `gdgtify-989608` — camera lăn 70° nhưng cụm chữ đang đọc được counter-rotate giữ ngang.
3. **Một take liên tục bằng morph, không bằng cắt:** hình ở tiền cảnh phình ra nuốt khung rồi co lại thành cảnh sau; hình đen flood toàn khung phải overscale qua cả bốn góc và mất ~0.3 giây, nếu không nửa màn hình đổi trong một frame trông như lỗi.
4. **Nội dung đang đọc không bao giờ bị hiệu ứng đè:** chữ đang trong "reading hold" thì đứng yên và sắc nét; motion blur chỉ chạm vào hình học trang trí phía sau, không chạm chữ đang đọc.

## Quy trình sản xuất

1. Tra `~/workspace/opus55-videos/3D-INDEX.md` (nhóm Canvas nhỏ — phần lớn mục pseudo-3D nằm rải ở nhóm Khác do không gắn tag; tìm thêm bằng tech tag `canvas` trong `data/videos.json`), đọc 1–2 prompt gốc (ưu tiên `full`).
2. Storyboard bảng theo master; với nhóm này phải ghi thêm: đường cong/quỹ đạo của từng pha và phép biến đổi camera của từng đoạn (chỉ dùng ít phép nhưng mỗi phép có lý do kể chuyện).
3. Single-file HTML: Canvas 2D + `seek(t)`; cache glyph và hình học tĩnh (chữ render một lần ra offscreen canvas rồi tái dùng), lấy mẫu theo **arc-length** để khoảng cách dọc đường cong đều nhau.
4. Kiểm frame tại các mốc chất lượng đã chốt trong brief (ví dụ 0 / 3 / 5 / 7.5 / 10.5 / 13 / 16 / 19 giây cho phim 20 giây như mẫu `gdgtify-989608`) trước khi render full; rồi pipeline chung: subframes + `tmix`, nhạc theo beat grid, −14 LUFS.
5. QA theo quality bar của master + mục QA riêng dưới đây.

## Công thức & kỹ thuật đặc thù

- **Prompt gốc nên tham khảo (prompt full, trong `~/workspace/opus55-videos/prompts/`):**
  - `twoclipping-496100` — canvas thuần, phim ra mắt kiểu Apple keynote: một take liên tục, mọi cảnh morph từ cảnh trước; liquid glass dựng bằng distance field trên canvas (mỗi glyph một distance field cho displacement/mask/highlight) thay vì `backdrop-filter` (Chromium đọc sai displacement map qua `url()` — phải clone cảnh ra sau rồi lọc); iris 6 lá, wordmark "accordion" nén vào dấu chấm. Kho gotchas dày nhất của nhóm.
  - `gdgtify-989608` — kinetic type trên quỹ đạo ellipse phân tích: đường baseline của câu là quỹ đạo; chỉ 3 phép camera (pull-back, roll, velocity-match), mỗi phép có lý do tu từ; blend vị trí + tiếp tuyến liên tục tại điểm "thoát quỹ đạo", không teleport; quality gate liệt kê sẵn các mốc giây phải soi.
- **Quỹ đạo phân tích:** ellipse/path biểu diễn bằng tham số; vị trí và tiếp tuyến tại `t` tính trực tiếp; khi đổi đường (ví dụ thoát ellipse sang đường thẳng) phải blend cả vị trí lẫn tiếp tuyến ở điểm nối để không gãy góc.
- **Velocity match:** khi camera bám theo chủ thể đang chạy, trừ vận tốc chủ thể khỏi nền — chủ thể đứng yên tương đối, thế giới/quỹ đạo cũ trôi lùi phía dưới; cảm giác tăng tốc thể hiện bằng khoảng giãn giữa các vệt theo sau, **không** rung camera.
- **Liquid glass trên canvas:** mỗi phần tử kính giữ một bản clone của cảnh phía sau, lọc qua displacement map (SVG feDisplacementMap ở vài tỉ lệ lệch nhau cho viền sắc sai màu) + rim light; hiệu ứng goo bằng blur + alpha threshold rồi composite nguồn lên trên để kính vẫn sắc bên trong.
- **Footage nhúng trong canvas:** re-encode all-intra (`ffmpeg -g 1`), nạp qua blob URL, chờ sự kiện `seeked` rồi mới vẽ frame — máy chủ tĩnh thường không range-seek được video.

## QA bắt buộc

- Toàn bộ quality bar của `opus55-3d-scenes` (frozen time — trừ các reading hold có chủ đích và ghi trong storyboard, frame 1 hoàn chỉnh, tương phản 4.5:1, hiểu khi tắt tiếng).
- Riêng Canvas 2.5D: soi frame-difference tìm "pop" một frame (đỉnh chênh lệch gấp ~3 lần các frame kề) — dấu hiệu morph/flood lỗi; chữ đang đọc không được mờ vì motion blur; tại điểm nối quỹ đạo không gãy góc nhìn thấy được; flood nuốt khung phải phủ kín bốn góc.

## Output contract

MP4 cuối (+ music-only) + HTML nguồn + storyboard (kèm đường cong/phép camera từng đoạn) + ghi chú slug prompt gốc đã tham khảo. Không đăng khi chưa được user duyệt.
