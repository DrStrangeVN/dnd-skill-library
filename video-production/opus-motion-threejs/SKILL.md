---
name: opus-motion-threejs
description: Kỹ thuật motion graphics bằng Three.js — scene 3D thật với camera, ánh sáng, vật thể (nhóm Three.js của kho opus5.5: 24 video). Dùng khi brief cần không gian 3D: portfolio/showreel 3D, sản phẩm xoay/bay trong không gian, chữ 3D, cảnh có chiều sâu và chuyển động camera. Luôn đi cùng pipeline chung của opus55-motion-graphics (seek(t) xác định — camera và vật thể đều là hàm của thời gian, lưới nhịp 120 BPM, tmix motion blur).
---

# Opus Motion — Three.js (3D)

## Khi nào dùng

- Chủ thể là **vật thể 3D thật**: sản phẩm, logo khối, chữ 3D, kiến trúc, nhân vật đơn giản — cần xoay, lật, bay, va chạm có chiều sâu.
- Portfolio/showreel: dựng video từ các tác phẩm/hình ảnh đưa vào không gian 3D (thẻ, panel bay, gallery 3D).
- Cần chuyển động camera điện ảnh: dolly, orbit, crane, rack-focus giả.
- Không dùng khi: hiệu ứng phẳng là đủ (2D rẻ và sắc hơn — `opus-motion-canvas` / `opus-motion-svg-gsap`), hoặc chỉ cần nền trừu tượng chảy (→ `opus-motion-shader`; nhiều scene threejs trong corpus vẫn gắn shader cho vật liệu phát sáng — khi đó skill này làm chủ, shader làm vật liệu).

## Nguyên lý cốt lõi

Kế thừa nguyên lý của `opus55-motion-graphics`, dịch sang 3D:

1. **Scene là hàm của `t`, kể cả camera.** Mọi position/rotation/scale của vật thể và camera tại thời điểm `t` tính bằng công thức đóng (spring đóng, nội suy theo keyframe đặt trên beat grid). CẤM dùng clock tích lũy của Three.js (`clock.getElapsedTime()` cộng dồn qua vòng lặp render tự do) cho bản xuất.
2. **Choreography trước, mô hình sau:** chốt đường đi của camera và các "điệu nhảy" chính theo beat trước khi trang trí scene; 3D dễ sa vào đẹp-từng-frame mà rối toàn cục.
3. **Ánh sáng nhất quán:** một key light chủ đạo + fill/rim tiết chế; đổi ánh sáng giữa cảnh phải có lý do theo nhịp, không nhấp nháy ngẫu nhiên.
4. **Antialias + độ phân giải render cao hơn khung xuất** (render 1.5–2× rồi hạ xuống bằng ffmpeg) để cạnh 3D mịn, chữ trong scene không răng cưa.

## Quy trình sản xuất

1. Tra `~/workspace/opus55-videos/MOTION-INDEX.md` nhóm Three.js, đọc 1–2 prompt gốc (ưu tiên `full`).
2. Brief chốt: danh sách vật thể, 3–5 góc camera chính, đường camera theo beat, palette vật liệu/ánh sáng, đoạn nào cần text (text quan trọng để ở lớp DOM phủ lên, không nướng vào 3D).
3. Single-file HTML: Three.js scene + `seek(t)` đặt toàn bộ trạng thái (vật thể + camera + light intensity) từ `t`.
4. Render thử các frame tại beat chính để duyệt choreography trước khi render full; sau đó chạy pipeline chung (subframes + `tmix` — quan trọng vì camera di chuyển liên tục).
5. QA, giao kèm HTML nguồn và ghi chú đường camera.

## Công thức & kỹ thuật đặc thù

- **Prompt gốc nên tham khảo (prompt full, trong `~/workspace/opus55-videos/prompts/`):**
  - `heyiammallik-293397` — threejs + canvas, ~30s showreel từ portfolio: mẫu cho tư duy "mỗi frame đều quan trọng", tự phê bình và làm lại nếu chưa đạt chất pro.
  - `itisrazak-332386` — threejs + canvas: biến thể showreel 3D để đối chiếu cấu trúc.
  - `spearwtf-029058` — threejs + canvas: mẫu nhịp nhanh, nhiều vật thể.
  - `felipemoller-936736` — threejs + svg + gsap: mẫu lai — 3D làm sân khấu, SVG/GSAP lo chữ và UI phủ trên.
  - `onewaysidewalks-440008` — threejs + canvas + svg + css: mẫu composition nhiều lớp đầy đủ nhất của nhóm.
- Đường camera: keyframe vị trí + lookAt trên beat grid, nội suy bằng spring đóng theo từng đoạn; tránh nội suy tuyến tính (góc gãy lộ rõ trong 3D).
- Vật thể vào cảnh: bay từ ngoài frustum + spring tới vị trí đích + quay nhẹ theo trục — cùng một "ngữ pháp" vào cảnh cho mọi vật thể để video có chất riêng.
- Vật liệu: MeshStandardMaterial với 1–2 đèn chính cho sản phẩm; phát sáng (emissive/bloom giả bằng sprite glow tiết chế) chỉ cho điểm nhấn — corpus cấm glow tràn lan.
- Chữ 3D: chỉ dùng cho từ khóa ngắn; đoạn chữ dài/chữ tiếng Việt nhiều dấu luôn để DOM 2D phủ trên (font Be Vietnam Pro), tránh font 3D thiếu glyph tiếng Việt.

## Cạm bẫy (pitfalls)

- Dùng vòng lặp render tự do + thời gian tích lũy → seek không tái lập, frame chụp bởi Playwright lệch nhau. Mọi thứ phải từ `seek(t)`.
- Render đúng độ phân giải xuất + không antialias → cạnh răng cưa, moiré khi camera lướt.
- Quên khóa tỉ lệ khung hình (aspect) và FOV giữa các lần xuất thử → bản cuối khác hẳn preview.
- Nạp model/texture ngoài nặng, không cần thiết: corpus chủ yếu dùng hình học nguyên thủy + vật liệu tốt. Ưu tiên primitive + bố cục hơn asset nặng.
- Text 3D tiếng Việt thiếu glyph hoặc dấu vỡ — chuyển sang lớp DOM như quy tắc trên.

## QA bắt buộc

- Toàn bộ checklist của `opus55-motion-graphics`.
- Riêng Three.js: kiểm frame ở tốc độ camera nhanh nhất (motion blur + răng cưa); seek ngẫu nhiên 5 thời điểm chụp 2 lần phải giống hệt; kiểm tra không vật thể nào "pop" xuất hiện/biến mất ngoài ý đồ tại các beat chuyển đoạn.

## Output contract

MP4 cuối + HTML nguồn + ghi chú: danh sách góc camera/beat chính, archetype đã theo, slug prompt gốc đã tham khảo. Không đăng khi chưa được user duyệt.
