---
name: opus-motion-shader
description: Kỹ thuật motion graphics bằng GLSL fragment shader trên WebGL (nhóm Shader/WebGL của kho opus5.5: 11 video xếp nhóm, 19 video gắn tag shader). Dùng khi brief cần nền/hiệu ứng trừu tượng theo pixel — chất lỏng chảy, psychedelic/hypnotic, distortion, hào quang màu, visual theo nhạc — hoặc product film cần lớp artwork shader bên dưới UI. Luôn đi cùng pipeline chung của opus55-motion-graphics (seek(t) xác định, lưới nhịp 120 BPM, tmix motion blur).
---

# Opus Motion — Shader / WebGL (GLSL)

## Khi nào dùng

- Màu sắc và chất liệu là nhân vật chính: liquid silk, molten glass, khói, lửa, nhiễu động, kaleidoscope, "hypnotic showreel".
- Cần một lớp nền sống (ambient background) cho product film, title sequence, loop sự kiện.
- Hiệu ứng cấp pixel: warp, ripple, chromatic aberration, grain, glow có kiểm soát.
- Không dùng khi: nội dung chính là UI/text cần sắc nét và đọc lâu (shader chỉ làm nền — chữ và UI để DOM/SVG lo, xem `opus-motion-svg-gsap`), hoặc cần vật thể 3D có hình khối thật (→ `opus-motion-threejs`).

## Nguyên lý cốt lõi

Kế thừa nguyên lý của `opus55-motion-graphics`, với chất riêng:

1. **Mỗi pixel là hàm thuần `(uv, t)`:** fragment shader nhận `uniform float u_time` do `seek(t)` đặt — cùng `t` cho cùng ảnh, không tích lũy buffer qua frame (trừ khi hiệu ứng feedback được thiết kế xác định ngay từ đầu).
2. **Shader lo chất liệu, DOM lo thông tin:** text, logo, UI luôn là lớp HTML/SVG phía trên, render sắc nét; shader chỉ ở dưới hoặc trong khung artwork được clip gọn.
3. **Chuyển động chậm mà chắc:** shader đẹp ở biên độ nhỏ và tốc độ vừa; tham số thời gian thường scale 0.05–0.3, tránh "sôi" loạn.
4. **Khớp nhịp bằng tham số, không bằng mắt:** các xung năng lượng (pulse, đổi pha màu) đặt tại beat grid 120 BPM giống mọi kỹ thuật khác.

## Quy trình sản xuất

1. Tra `~/workspace/opus55-videos/MOTION-INDEX.md` nhóm Shader / WebGL, đọc 1–2 prompt gốc (ưu tiên `full`).
2. Brief chốt: palette (tối đa ~5 màu có vai trò rõ), chất liệu (liquid/smoke/fire/geo), mức năng lượng theo từng đoạn timeline, lớp UI/text phủ trên.
3. Single-file HTML: WebGL canvas fullscreen (hoặc trong stage có bo góc/clip rõ ràng) + lớp DOM phía trên; `seek(t)` set `u_time` và mọi uniform khác.
4. Render subframes + `tmix` theo pipeline chung — với shader, motion blur chủ yếu cứu các đoạn warp/zoom nhanh.
5. QA kỹ độ sắc nét của lớp chữ phủ trên và độ "sôi" của nền ở các frame tĩnh.

## Công thức & kỹ thuật đặc thù

- **Prompt gốc nên tham khảo (prompt full, trong `~/workspace/opus55-videos/prompts/`):**
  - `brainextends-606193` — **mẫu product film hoàn chỉnh nhất**: GLSL + SVG, 18s 1920×1080@60, timeline chi tiết từng 0.1s, artwork "liquid silk" dùng nhất quán suốt phim, quy tắc motion quality và validation rất chặt. Học cấu trúc brief và cách giữ nhất quán artwork, không chỉ học shader.
  - `monokern-832979` — GLSL/WebGL psychedelic hypnotic showreel: mẫu cho visual trừu tượng toàn khung, năng lượng cao.
  - `zheke-622583` — shader + webgl + canvas + particles: mẫu lai nhiều lớp hiệu ứng.
  - `miaai-lab-774895` — shader + webgl + canvas: biến thể cân bằng giữa hiệu ứng và bố cục.
  - `prasenx-693512` — shader + canvas + audio: mẫu shader chạy theo nhạc.
- Bộ khung shader chuẩn: `uv` chuẩn hóa theo aspect, domain warp bằng fbm 2–3 octave (đủ mượt, rẻ), palette nội suy cos (cosine palette) để màu chuyển liền mạch.
- Liquid silk kiểu `brainextends-606193`: folds lớn bằng warp tần số thấp + highlight specular giả từ gradient của trường nhiễu; giữ cùng seed/tham số suốt phim để artwork "là cùng một vật" ở mọi cảnh.
- Pulse theo beat: `energy(t) = exp(-frac(t / beat_len) * k)` cộng vào biên độ warp/độ sáng tại các beat chính.
- Grain + vignette cuối pipeline (trong shader hoặc ffmpeg) để phá banding trên nền tối gradient.

## Cạm bẫy (pitfalls)

- Quên sửa aspect ratio → hình bị kéo giãn khi xuất 16:9 khác với lúc xem thử 1:1.
- fbm quá nhiều octave / vòng lặp nặng → render frame cực chậm trên máy 2 core; pre-render đoạn shader thuần thành video nền rồi mới phủ UI nếu timeline cho phép.
- Nền "sôi" quá mức làm chữ phủ trên khó đọc — luôn QA bằng frame có chữ thật, giảm biên độ warp ở vùng đặt chữ.
- Banding trên gradient tối: thêm grain/dither, tránh nén CRF quá cao ở bản cuối.
- Hiệu ứng feedback buffer (vẽ lại frame trước) phá tính xác định nếu không cố định số bước và seed — tránh dùng cho bản xuất chính thức.

## QA bắt buộc

- Toàn bộ checklist của `opus55-motion-graphics`.
- Riêng shader: kiểm 3 frame liên tiếp ở đoạn chuyển động nhanh nhất (motion blur có tự nhiên không); kiểm frame tĩnh có chữ phủ trên (độ đọc được); kiểm banding ở vùng tối nhất.

## Output contract

MP4 cuối + HTML nguồn (gồm toàn bộ GLSL) + ghi chú palette/chất liệu và slug prompt gốc đã tham khảo. Không đăng khi chưa được user duyệt.
