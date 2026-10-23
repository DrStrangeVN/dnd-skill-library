---
name: opus-3d-worlds
description: Kỹ thuật dựng thế giới/cảnh 3D bằng Three.js — môi trường, kiến trúc (archviz), thành phố, nội thất, sản phẩm trong bối cảnh, cỗ máy nhiều chi tiết (nhóm Three.js của kho opus5.5 3D: 46 video). Dùng khi brief cần một không gian 3D thật để camera đi vào: bay qua khu phố/dự án, showroom, exploded view có nhãn, cảnh môi trường bằng hạt. Luôn đi cùng pipeline chung của opus55-3d-scenes (storyboard bảng có vật gánh, master timeline seek(t), ánh sáng kiểu product shoot, nhãn HTML chiếu từ 3D).
---

# Opus 3D — Worlds (Three.js)

## Khi nào dùng

- Có **môi trường cụ thể**: khu phố, công trình, phòng, nhà máy, đảo/bãi biển — camera bay xuyên qua hoặc vòng quanh.
- Archviz giới thiệu dự án: mô hình kiến trúc premium, cần nhãn chú thích gắn đúng vị trí trong không gian.
- Sản phẩm/cỗ máy nhiều bộ phận trong bối cảnh: exploded view tách lớp có nhãn tên, hover/điểm nhấn từng phần.
- Không dùng khi: chỉ một vật thể 3D đơn lẻ làm nhân vật chính cho clip motion ngắn (→ `opus-motion-threejs`); cảnh trừu tượng tính bằng toán thuần, không asset (→ `opus-3d-shader`); chủ thể là chữ/ảnh phẳng cần cảm giác sâu (→ `opus-3d-canvas`).

## Nguyên lý cốt lõi

Kế thừa toàn bộ nguyên lý của `opus55-3d-scenes` (master timeline xác định, vật gánh, storyboard bảng, quality bar đo được), dịch sang dựng thế giới:

1. **Thế giới truy vết được về dữ kiện.** Cảnh dựng từ một file nguồn/facts file: mỗi công trình, bộ phận, con số đều có xuất xứ (bản đồ, số đo, ảnh tham chiếu) — dựng bằng **generator dùng chung** (một hàm sinh mặt tiền, một hàm sinh mái…) thay vì nặn từng cái một lần. Đây là mẫu của `alexalbert-274839`: cả con phố 1906 dựng lại từ bản đồ Sanborn + phim tư liệu, mọi tòa nhà truy về dữ kiện.
2. **Ánh sáng như buổi chụp sản phẩm:** một soft key từ một phía + rim light phía sau để tách chủ thể khỏi nền; không "đèn phẳng đều khắp" kiểu preview. Đo pixel nền sau render và chỉnh tới khi khớp màu brand.
3. **Camera là người kể chuyện:** góc nhìn giữ 35–55° so với mặt phẳng chính; không bao giờ nhìn thẳng xuống một mặt lớn, không kết cảnh cận trên mặt phẳng. Đường camera chốt trong storyboard trước khi trang trí cảnh.
4. **Nhãn sống ngoài 3D:** nhãn HTML được chiếu (project) từ tọa độ 3D mỗi frame — sắc nét, kiểm soát được tương phản, không vỡ glyph tiếng Việt.

## Quy trình sản xuất

1. Tra `~/workspace/opus55-videos/3D-INDEX.md` nhóm Three.js, đọc 1–2 prompt gốc (ưu tiên `full`).
2. Lập **file nguồn cảnh**: danh sách thực thể (tên, kích thước, vị trí, vật liệu, xuất xứ dữ kiện) — đây cũng là facts file của master skill.
3. Storyboard bảng theo `opus55-3d-scenes`: ghi rõ shot nào camera tĩnh/chuyển, vật gánh là gì, điểm handoff khớp pixel ở đâu.
4. Dựng theo thứ tự: generator + vật thể dùng chung → từng khu vực/cảnh con có trang test riêng → lắp vào master timeline.
5. Test render 5 giây (đo cả pixel nền so với brand), rồi render full theo pipeline chung: headless Chromium + `seek(t)`, supersample 1.5–2× rồi hạ cỡ bằng ffmpeg cho cạnh mịn; WebGL headless cần SwiftShader — probe frame thử trước.
6. QA theo quality bar của master + mục QA riêng dưới đây.

## Công thức & kỹ thuật đặc thù

- **Prompt gốc nên tham khảo (prompt full, trong `~/workspace/opus55-videos/prompts/`):**
  - `everestchris6-399895` — prompt hệ thống cấp master: GSAP master timeline + three.js, storyboard bảng, luật ánh sáng/camera 35–55°, nhãn HTML chiếu từ 3D, quality bar đo được. (File không gắn tech tag nên nằm ở nhóm "Khác" trong `3D-INDEX.md`, nhưng đây là khung quy trình của cả nhóm 3D.)
  - `alexalbert-274839` — archviz lịch sử: dựng cả tuyến phố từ file nguồn có độ tin cậy từng dữ kiện, generator tái dùng cho mặt tiền/mái/đèn/xe. Mẫu cho mọi dự án "dựng lại một nơi có thật".
  - `aichrislee-476025` — sản phẩm cơ khí chi tiết (đồng hồ cơ): vật liệu kim loại/kính thuyết phục, exploded view tách lớp kèm nhãn tên từng bộ phận, nhãn giải thích một dòng khi điểm nhấn. Mẫu cho product 3D có chú thích.
  - `tanabe-fragm-322001` — sản xuất quy mô lớn: ~190.000 instance gạch mosaic (InstancedMesh), mỗi viên một instance riêng biến vị trí/hướng/độ dày/màu; hậu kỳ depth-of-field tự viết; frame cuối khớp ảnh đích (đo màu/độ phơi sáng đối chiếu). Mẫu cho cảnh "hàng vạn chi tiết" và kỹ thuật giấu–hiện (reveal) bằng chính vật liệu của cảnh.
  - `ishuagra02-678129` — môi trường bằng **particle illustration**: hàng nghìn điểm sáng thay cho mặt đặc + dải ribbon chảy phía sau nhân vật gợi chuyển động; môi trường đổi theo giờ trong ngày. Mẫu cho cảnh thiên nhiên/đám đông không cần mô hình nặng.
- **Instancing là mặc định cho chi tiết lặp:** cây, gạch, đèn, ghế, người — một InstancedMesh với biến thể theo instance (vị trí/xoay/tỉ lệ/màu), không copy mesh rời (sập hiệu năng render frame-by-frame).
- **Đường camera:** keyframe vị trí + lookAt trên lưới thời gian của storyboard, nội suy spring đóng theo đoạn; thêm "velocity match" khi cần bám theo vật đang di chuyển (camera khớp vận tốc vật → vật đứng yên tương đối, thế giới trôi qua).
- **Exploded view:** mỗi bộ phận trượt ra theo trục/lớp đã định trong file nguồn, nhãn HTML bám theo tọa độ chiếu của bộ phận; lắp lại phải khớp vị trí ban đầu tuyệt đối (snap-back không lệch pixel).
- **Trời/giờ trong cảnh:** đổi ánh sáng theo thời gian là thay key light + màu nền theo curve đã chốt trong storyboard — không đổi đột ngột giữa hai frame kề.

## QA bắt buộc

- Toàn bộ quality bar của `opus55-3d-scenes` (frozen time, frame 1, tương phản 4.5:1, màu brand đo pixel, hiểu khi tắt tiếng, critic loop).
- Riêng Worlds: không chi tiết lơ lửng/khe hở ở chỗ nối/kính đen phẳng/texture lặp lộ; nhãn chiếu không trôi lệch khỏi vật khi camera ở tốc độ nhanh nhất; seek ngẫu nhiên 5 thời điểm, chụp 2 lần phải giống hệt; kiểm frame ở đoạn camera nhanh nhất về răng cưa và moiré.

## Output contract

MP4 cuối (+ music-only) + HTML nguồn + file nguồn cảnh/facts file + storyboard + ghi chú đường camera và slug prompt gốc đã tham khảo. Không đăng khi chưa được user duyệt.
