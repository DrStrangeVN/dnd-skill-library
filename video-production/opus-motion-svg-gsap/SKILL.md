---
name: opus-motion-svg-gsap
description: Kỹ thuật motion graphics bằng SVG morph + GSAP/spring theo thời gian (nhóm lớn nhất của kho opus5.5: 120 video xếp nhóm SVG+GSAP). Dùng khi brief là UI motion, một hình biến hình qua nhiều trạng thái, icon/logo animation, kinetic typography, infographic/chart tự vẽ, product film kiểu giao diện. Luôn đi cùng pipeline chung của opus55-motion-graphics (seek(t) xác định, spring dạng đóng, lưới nhịp ~120 BPM, tmix motion blur, cấm easing nảy).
---

# Opus Motion — SVG + GSAP

## Khi nào dùng

- **Một phần tử biến hình liên tục qua nhiều trạng thái** (button → loader → player → slider → chart…): archetype "one shape, never cut" kinh điển của corpus.
- UI/product motion: mockup giao diện chuyển động, tính năng app được "diễn" bằng morph và cursor.
- Logo/icon animation, đường vector tự vẽ (stroke draw), chart tự dựng, chữ chuyển động theo nhịp.
- Không dùng khi: cảnh vẽ tự do/hạt (→ `opus-motion-canvas`), nền shader (→ `opus-motion-shader`), 3D (→ `opus-motion-threejs`).

## Nguyên lý cốt lõi

Kế thừa nguyên lý của `opus55-motion-graphics`, nhấn mạnh thêm:

1. **GSAP chỉ là công cụ soạn timeline — khi xuất file, timeline phải "nướng" được thành hàm của `t`.** Mọi tween quy về giá trị tại thời điểm `t` (dùng easing dạng đóng hoặc spring dạng đóng), không phụ thuộc trạng thái chơi thực tế của trình duyệt lúc render.
2. **Morph là thay đổi thuộc tính của CÙNG một phần tử** (size, radius, path `d`, màu), nội dung bên trong hoán đổi bằng blur/mask ngắn — không cắt cảnh, không thay node đột ngột.
3. **Cursor là diễn viên:** click/drag thật điều khiển thay đổi; khi kéo, giá trị bám theo vị trí con trỏ (direct manipulation), thả ra thì spring về từ đúng vị trí đó.
4. **Hai cạnh, hai spring khác nhau:** phần tử kéo giãn (tab indicator, toggle knob) cho cạnh dẫn đi spring nhanh hơn cạnh theo → hiệu ứng "kéo dãn như chất lỏng" đặc trưng.

## Quy trình sản xuất

1. Tra `~/workspace/opus55-videos/MOTION-INDEX.md` nhóm SVG + GSAP, đọc prompt gốc cùng archetype (ưu tiên `full`).
2. **Trước khi code: lập danh sách trạng thái và đặt lên beat grid** (trạng thái nào ở bar/beat nào, sự kiện gì ở mỗi beat) — trình user xem nếu brief phức tạp.
3. Dựng single-file HTML: SVG/DOM + hàm `seek(t)` tính mọi thuộc tính từ `t`; spring đóng cho các giá trị đổi đích nhiều lần (cộng dồn từng spring con).
4. Render thử **một frame cho mỗi beat** trước; sửa mọi điểm lệch nhịp, chật, khó đọc rồi mới render full theo pipeline chung.
5. Ghép nhạc ~120 BPM, QA, giao kèm nguồn.

## Công thức & kỹ thuật đặc thù

- **Prompt gốc nên tham khảo (prompt full, trong `~/workspace/opus55-videos/prompts/`):**
  - `hicallmechai-878304` — **prompt mẫu mực nhất của cả corpus**: một hình morph qua 11 trạng thái UI trên lưới 120 BPM/7 bars, spring đóng cộng dồn, drag trực tiếp, loop frame cuối ≡ frame đầu, danh sách cấm rõ ràng. Đọc kỹ file này trước mọi dự án SVG/GSAP nghiêm túc.
  - `moritzkremb-466494` — SVG + GSAP gọn, mẫu cho morph đơn chủ đề.
  - `daniel-mac8-306214` — SVG + GSAP, mẫu timeline trạng thái rõ ràng.
  - `melvynx-638493` — canvas + svg + gsap lai: SVG lo hình chính, canvas hỗ trợ hiệu ứng phụ.
  - `miskinho-956105` — SVG + GSAP, thêm một biến thể nhịp/tiết tấu để đối chiếu.
- Spring cộng dồn: giá trị đổi đích tại các thời điểm `t₁…tₙ` → `x(t) = Σ spring_k(t − t_k)`; mỗi spring con là step response `1 − (1 + ω(t−t_k))·e^(−ω(t−t_k))` nhân với độ lệch đích của lần đổi đó.
- Stroke tự vẽ: `stroke-dashoffset` là hàm tuyến tính/spring theo `t`; chart "tự dựng" từng đoạn theo beat.
- Text trong container đang morph: text ra/vào có timing riêng (fade+blur ngắn) lệch pha với container, tránh chồng chữ giữa hai trạng thái.
- Camera zoom giả: scale wrapper quanh điểm neo của trạng thái hiện tại để mỗi trạng thái "lấp đầy khung"; **không** đặt `will-change` lên phần tử bị camera scale (chữ sẽ nhòe).

## Cạm bẫy (pitfalls)

- Để GSAP/CSS transition chạy theo đồng hồ thật khi render → frame chụp lệch, không tái lập. Mọi thứ phải suy ra từ `seek(t)`.
- Easing nảy (elastic/back mạnh) cho cảm giác rẻ tiền — corpus cấm; chỉ dùng spring tới hạn hoặc overshoot cực nhỏ.
- Chữ của hai trạng thái chồng lên nhau giữa morph vì dùng chung một timing.
- Loop khựng vì quên đưa cursor (vị trí + trạng thái) về đúng điểm bắt đầu ở frame cuối.
- Nét icon không đồng nhất (stroke width khác nhau giữa các trạng thái) làm vỡ cảm giác "cùng một phần tử".

## QA bắt buộc

- Toàn bộ checklist của `opus55-motion-graphics`.
- Riêng SVG/GSAP: render 1 frame/beat và đối chiếu beat grid; kiểm tra frame giữa mỗi lần morph (khoảnh khắc dễ chồng chữ nhất); kiểm tra loop point (frame đầu/cuối, gồm cả cursor).

## Output contract

MP4 cuối + HTML nguồn + bảng trạng thái trên beat grid đã thực hiện + slug prompt gốc đã tham khảo. Không đăng khi chưa được user duyệt.
