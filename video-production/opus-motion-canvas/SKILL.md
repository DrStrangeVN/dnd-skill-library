---
name: opus-motion-canvas
description: Kỹ thuật motion graphics bằng Canvas 2D (nhóm Canvas trong kho opus5.5: 68 video xếp nhóm, 142 video gắn tag canvas). Dùng khi brief cần vẽ thủ tục bằng code — hạt/particles, cảnh minh họa vẽ theo thời gian, hiệu ứng pixel, audio-reactive visual, chuyển cảnh vẽ liên tục, visual trừu tượng không dùng DOM. Luôn đi cùng pipeline chung của opus55-motion-graphics (seek(t) xác định, spring dạng đóng, lưới nhịp 120 BPM, tmix motion blur).
---

# Opus Motion — Canvas 2D

## Khi nào dùng

- Brief mô tả một **cảnh được vẽ ra** chứ không phải giao diện: phong cảnh chuyển mùa, minh họa chuyển động, hiệu ứng hạt, mưa/tuyết/lửa, pixel art chuyển động.
- Audio-reactive: hình chạy theo sóng nhạc/beat (tag `audio` thường đi cùng canvas trong corpus).
- Cần toàn quyền kiểm soát từng pixel mà DOM/SVG quá nặng hoặc quá cứng.
- Không dùng khi: nội dung là UI states/icon morph (→ `opus-motion-svg-gsap`), nền shader chảy (→ `opus-motion-shader`), vật thể 3D (→ `opus-motion-threejs`).

## Nguyên lý cốt lõi

Kế thừa toàn bộ nguyên lý của `opus55-motion-graphics`, cộng thêm chất riêng của Canvas:

1. **Mỗi frame vẽ lại từ đầu theo `t`.** Hàm `draw(t)` xóa canvas và vẽ toàn cảnh từ các hàm thuần của `t`. Tuyệt đối không giữ state tích lũy kiểu `x += vx` qua frame — muốn có chuyển động tích lũy thì tích phân bằng công thức đóng theo `t`.
2. **Hạt cũng phải xác định:** hạt thứ `i` có seed cố định → vị trí/quỹ đạo là hàm đóng của `(seed_i, t)`. Cùng `t` luôn cho cùng một khung hình, kể cả khi seek ngược.
3. **Lớp vẽ tách bạch:** background → midground → foreground → foreground effects, mỗi lớp một hàm riêng để dễ QA và sửa.
4. **Tôn trọng devicePixelRatio** khi render xuất file: canvas nội bộ nhân tỉ lệ để nét vẽ không bị mềm khi phóng.

## Quy trình sản xuất

1. Tra catalogue `~/workspace/opus55-videos/MOTION-INDEX.md` nhóm Canvas 2D, đọc 1–2 prompt gốc cùng archetype (ưu tiên `full`).
2. Viết brief mới theo khung của master skill; chốt palette, nhịp (BPM), thời lượng, kích thước.
3. Dựng single-file HTML: `<canvas>` toàn khung + `seek(t)` đặt thời gian hiện tại + `draw(t)`; xuất frame qua Playwright theo pipeline chung (3–5 subframes + `tmix`).
4. Nếu có nhạc: phân tích beat grid trước, mọi sự kiện vẽ lớn (đổi cảnh, điểm nhấn) khóa vào beat.
5. Ghép MP4, QA theo checklist master, giao kèm HTML nguồn.

## Công thức & kỹ thuật đặc thù

- **Prompt gốc nên tham khảo (đều là prompt full, trong `~/workspace/opus55-videos/prompts/`):**
  - `itsolelehmann-762215` — cảnh thơ "4 mùa ngoài cửa sổ tàu" vẽ canvas: mẫu cho cảnh minh họa có không khí, chuyển mùa theo thời gian.
  - `kloss-xyz-941143` — canvas + Web Audio, khung dọc 9:16, motion + sound design đi đôi: mẫu cho audio-reactive và nhịp nhanh.
  - `ajith-io-615243` — canvas + particles: mẫu hệ hạt xác định theo seed.
  - `anabology-491441` — canvas kết hợp ảnh AI (ai-image): mẫu lai — ảnh tĩnh làm nền/tài sản, canvas lo chuyển động.
  - `1littlecoder-378066` — canvas thuần, gọn: mẫu tối giản cho hiệu ứng đơn chủ đề.
- Quỹ đạo hạt: `pos(i,t) = f(seed_i, t)` với `f` dùng sin/cos/noise-ngụy-tĩnh (value noise theo hàm băm của seed, không dùng `Math.random()` lúc render).
- Chuyển cảnh theo mùa/giai đoạn: nội suy tham số cảnh (màu trời, mật độ hạt, vị trí mặt trời) bằng spring dạng đóng giữa các mốc thời gian.
- Audio-reactive an toàn: biên độ tại `t` lấy từ envelope đã phân tích trước (offline), không đo live trong lúc render.

## Cạm bẫy (pitfalls)

- Dùng `Math.random()` hoặc `Date.now()` trong `draw()` → frame không tái lập được, seek vỡ, loop khựng. Mọi ngẫu nhiên phải từ seed cố định.
- Tích lũy state qua frame (biến toàn cục cộng dồn) → sai ngay khi Playwright chụp frame không theo thứ tự.
- Quên nhân devicePixelRatio → bản xuất bị nhòe dù xem preview thấy ổn.
- Vẽ quá nhiều hạt/phần tử mỗi frame trên máy yếu → render chậm; giảm mật độ hoặc pre-render lớp tĩnh thành offscreen canvas một lần.
- Text vẽ bằng `fillText` khổ lớn tiếng Việt: kiểm glyph và chọn font đã nạp xong (`document.fonts.ready`) trước khi chụp frame đầu.

## QA bắt buộc

- Toàn bộ checklist của `opus55-motion-graphics` (ffprobe, contact sheet, beat, loop, loudness).
- Riêng Canvas: seek ngẫu nhiên 5 thời điểm bất kỳ, chụp lại 2 lần — hai lần phải cho ảnh giống hệt nhau (bằng chứng tính xác định).
- Kiểm tra 3 frame ở đoạn mật độ hạt cao nhất: không vỡ hình, không tràn chi phí render bất thường.

## Output contract

MP4 cuối + HTML nguồn + ghi chú: archetype canvas đã theo, slug prompt gốc đã tham khảo, palette/BPM đã dùng. Không đăng khi chưa được user duyệt.
