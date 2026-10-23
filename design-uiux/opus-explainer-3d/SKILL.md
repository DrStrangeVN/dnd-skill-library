---
name: opus-explainer-3d
description: Kỹ thuật explainer bằng 3D — Three.js/GLSL dựng mô hình vật thể và hiện tượng không gian để giải thích: cắt lớp, nổ tung (exploded view) có nhãn, tia sáng/quá trình chạy bên trong mô hình (19 mục threejs/shader trong kho opus5.5 Explainer). Dùng khi brief là "giải thích cấu tạo của X bằng 3D", "mô hình 3D dạy học", "exploded view có chú thích", "giải thích hiện tượng vật lý/không gian bằng three.js/shader", hoặc khái niệm mà sơ đồ 2D không tải nổi. Luôn đi cùng pipeline explainer chung của opus55-explainers (learning objective trước, reveal-on-cue, nhãn gắn liền vật).
---

# Opus Explainer — 3D (Mô hình không gian)

Khi khái niệm *là* một vật thể hoặc một hiện tượng không gian — thấu kính khúc xạ thế nào, động cơ quay ra sao, sóng lan trong không gian — sơ đồ 2D bắt người xem tự tưởng tượng phần khó nhất. Archetype này dựng mô hình 3D đủ thật để nhìn xuyên vào trong: cắt mở, nổ tung từng lớp có nhãn, cho quá trình (tia sáng, dòng chảy, trường) chạy qua mô hình, tất cả khóa vào `seek(t)` như mọi pipeline opus55.

Mẫu đại diện trong corpus (đọc trước khi làm — `~/workspace/opus55-videos/prompts/<slug>.md`):
- `aichrislee-408244` (Three.js+GLSL+SVG, full) — mẫu mực: ống kính máy ảnh dựng 3D "không dùng ảnh", cắt dọc để thấy chồng thấu kính bên trong, tia sáng màu bẻ cong và hội tụ trên sensor, nút Explode tách mọi bộ phận kèm nhãn + một dòng công dụng cho từng phần.
- `ajith-io-562538` (Three.js+Shader+Canvas, full) · `0xspikez-483865` (Three.js+Shader+SVG, full) — explainer 3D dùng shader cho hiệu ứng vật lý bên trong mô hình.
- `0xvalure-331584` (Three.js+Canvas, full) · `aichrislee-378670` (Three.js+Canvas+Audio, full) — mô hình 3D kết hợp lớp 2D/âm thanh dẫn giải.

## Khi nào dùng

- Giải thích cấu tạo/bên trong của vật thể: máy móc, cơ thể, thiết bị, kiến trúc — cần cắt lớp hoặc exploded view.
- Giải thích hiện tượng không gian/vật lý: khúc xạ, quỹ đạo, sóng, trường, dòng chảy — cần quá trình chạy *trong* không gian 3D.
- Khái niệm mà góc nhìn thay đổi là một phần của bài học (xoay quanh vật, bay từ ngoài vào trong).

Không dùng khi: khái niệm là quan hệ/luồng/số liệu (→ `opus-explainer-diagram` nhanh và rõ hơn), hoặc 3D chỉ để "cho đẹp" — 3D thừa trong explainer làm chậm hiểu.

## Nguyên lý cốt lõi

1. **Mô hình phục vụ một câu hỏi.** Trước khi dựng: bài học cần người xem thấy được điều gì mà 2D không cho thấy? Mọi chi tiết mô hình ngoài câu trả lời đó đều là nhiễu — dựng đơn giản hóa có chủ đích và ghi rõ đã đơn giản hóa gì.
2. **Bên trong quan trọng hơn bên ngoài.** Giá trị của archetype nằm ở phần không nhìn thấy ngoài đời: chồng thấu kính, lá khẩu, dòng chảy nội tại. Lên kế hoạch cắt lớp (section cut) hoặc làm mờ vỏ ngay từ storyboard, không phải xử lý hậu kỳ.
3. **Explode có kỷ luật:** các bộ phận tách dọc một trục logic duy nhất (trục lắp ráp thật), khoảng cách tách tỉ lệ đều, mỗi bộ phận có nhãn + đúng một dòng công dụng; lắp lại là chạy ngược cùng chuyển động. Nhãn gắn liền vật bằng leader line, không legend rời.
4. **Quá trình phải chạy đúng vật lý ở mức bài học tuyên bố:** tia sáng bẻ tại mặt khúc xạ và hội tụ đúng tiêu điểm mô hình; vật quay đúng chiều/chu kỳ tương đối. Sai vật lý trong video dạy = lỗi nghiêm trọng nhất.
5. **Camera là người thầy điềm tĩnh:** chuyển động camera chậm, có chủ đích (orbit nhẹ, dolly vào chi tiết đang nói), không bay lượn biểu diễn. Mọi vị trí camera là hàm của `t`; người xem không bao giờ bị mất phương hướng (giữ một trục tham chiếu cố định trong khung).
6. Kế thừa kỷ luật chung: `seek(t)` xác định thuần (vị trí explode, góc quay, pha quá trình đều tính từ `t`), reveal-on-cue (bộ phận sáng lên/được gọi tên đúng lúc lời nhắc), spring dạng đóng, cấm easing nảy.

## Quy trình sản xuất

1. Từ pipeline master: chốt learning objective + câu hỏi mà 3D phải trả lời + danh sách bộ phận/quá trình sẽ xuất hiện (mỗi cái một dòng công dụng — đây cũng là nội dung nhãn).
2. Storyboard theo beat: trạng thái mô hình (nguyên/cắt/nổ) · camera ở đâu · quá trình nào chạy · nhãn nào hiện — khớp mốc từ khóa script.
3. Dựng mô hình bằng code (Three.js primitives + lathe/extrude; shader GLSL cho hiệu ứng trong suốt/trường/sóng). Không ảnh ngoài, không model tải sẵn không rõ nguồn. Vỏ ngoài có chế độ section/fade sẵn trong code.
4. Dựng hệ nhãn: SVG/HTML overlay chiếu từ tọa độ 3D của bộ phận (project mỗi frame theo `t`) — nhãn đi theo vật khi explode/camera di chuyển, leader line cập nhật cùng frame.
5. Kiểm chứng tĩnh trước: render frame ở các trạng thái chốt (nguyên, cắt, nổ tối đa, quá trình giữa chừng) thành contact sheet; kiểm vật lý hình học (tia hội tụ đúng điểm, thứ tự lớp đúng cấu tạo thật) trước khi render full.
6. Render frame-by-frame (headless Chromium, WebGL qua SwiftShader — probe frame thử không đen trước khi chạy hàng loạt) + ghép voice/phụ đề/nhạc, QA theo pipeline master + mục riêng dưới đây.

## Công thức & kỹ thuật đặc thù

- **Explode tham số hóa:** mỗi bộ phận có vector tách `d_i` (dọc trục lắp ráp) và hệ số `k_i`; vị trí = vị trí gốc + `d_i × k_i × E(t)` với `E(t)` là spring dạng đóng theo cửa sổ beat — một tham số duy nhất điều khiển toàn cảnh nổ/lắp.
- **Section cut:** clipping plane theo trục mô hình (Three.js `clippingPlanes`) hoặc vỏ dùng material trong suốt có fresnel nhẹ; mặt cắt tô accent phẳng để mắt phân biệt "đang nhìn vào trong".
- **Quá trình bằng shader/đường cong tham số:** tia sáng = line/tube theo đường gãy khúc tính hình học thật (điểm vào → điểm khúc xạ → tiêu điểm), vẽ dần bằng dash tỉ lệ theo `t`; sóng/trường = fragment shader với pha là hàm của `t` (uniform duy nhất là thời gian).
- **Nhãn bám vật:** `vector.project(camera)` mỗi frame → tọa độ màn hình; ẩn nhãn khi bộ phận bị che (dot product với hướng nhìn) hoặc khi chưa tới beat của nó.
- **Ánh sáng dạy học:** 1 key light + rim để đọc khối; tránh vật liệu "quá thật" gây nhiễu — bề mặt bán mờ (matte) + accent chỉ dành cho bộ phận đang được nói tới.

## QA bắt buộc

- Kiểm vật lý/hình học ở frame tĩnh: tia sáng hội tụ đúng tiêu điểm, thứ tự các lớp khi nổ khớp cấu tạo thật, chiều quay đúng.
- Nhãn: mọi bộ phận xuất hiện đều có nhãn + đúng một dòng công dụng; nhãn bám vật không lệch khi camera/explode di chuyển, không chồng nhau ở trạng thái nổ tối đa.
- Định hướng: xem trọn bản phát — có khoảnh khắc nào không biết mình đang nhìn từ phía nào không; camera không được "nhảy" giữa các beat.
- Đơn giản hóa đã tuyên bố: đối chiếu mô hình với danh sách đơn giản hóa ở bước 1 — không được có chi tiết dựng sai mà không ghi.
- Frame probe WebGL không đen + thêm các mục QA chung của `opus55-explainers` (ffprobe, contact sheet, sound-off test, loudness, xem trọn bản phát).

## Output contract

Theo output contract của `opus55-explainers`, cộng: danh sách bộ phận + dòng công dụng đã dùng làm nhãn, và danh sách các đơn giản hóa của mô hình so với vật thật.
