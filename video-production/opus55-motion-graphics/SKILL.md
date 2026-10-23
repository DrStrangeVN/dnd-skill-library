---
name: opus55-motion-graphics
description: Router + pipeline chung cho video motion graphics học từ kho awesome-opus5-5-videos (nhóm Motion, 369 prompt). Dùng khi user nói "làm video motion graphics", "làm video kiểu opus55", "motion graphics theo prompt mẫu", "làm video giới thiệu sản phẩm chuyển động", "showreel motion", hoặc gửi brief motion mà chưa chốt kỹ thuật (canvas / SVG-GSAP / shader / three.js). Skill này chọn kỹ thuật, giao việc cho skill con tương ứng và sở hữu pipeline render + chuẩn đầu ra dùng chung.
---

# Opus55 Motion Graphics — Master (Router + Pipeline chung)

Học từ nhóm **Motion** của repo `awesome-opus5-5-videos` (703 video toàn repo, 369 mục motion).
Thư viện prompt gốc: `~/workspace/opus55-videos/prompts/<slug>.md`; catalogue đã xếp nhóm: `~/workspace/opus55-videos/MOTION-INDEX.md`.
Prompt thuộc về tác giả gốc — **chỉ học kỹ thuật và cấu trúc, nội dung luôn làm mới**, không sao chép nguyên văn brief của người khác thành sản phẩm của mình.

## Khi nào dùng

- User yêu cầu motion graphics dạng code-render (HTML/JS → MP4): product film, UI motion, kinetic type, logo/brand motion, showreel, loop cho social.
- User nhắc "kiểu opus5.5 / opus55", hoặc gửi một prompt mẫu trong repo và muốn làm tương tự với nội dung mới.
- Brief chưa rõ kỹ thuật → skill này phân loại rồi chuyển cho 1 trong 4 skill con:
  - `opus-motion-canvas` — Canvas 2D
  - `opus-motion-svg-gsap` — SVG morph + GSAP timeline
  - `opus-motion-shader` — GLSL shader / WebGL
  - `opus-motion-threejs` — Three.js 3D

## Chọn kỹ thuật theo brief (bảng router)

| Dấu hiệu trong brief | Chọn | Lý do |
|---|---|---|
| Cảnh vẽ tay/thủ tục, hạt (particles), hiệu ứng pixel, game-like, audio-reactive, vẽ liên tục không có "diễn viên" DOM | `opus-motion-canvas` | Canvas 2D vẽ lại toàn khung theo `t`, rẻ và xác định tuyệt đối |
| UI states, icon morph, chữ/đường vector biến hình, logo animation, infographic có timeline rõ từng beat | `opus-motion-svg-gsap` | SVG morph + spring theo thời gian; archetype mạnh nhất của corpus (120 mục) |
| Nền trừu tượng chảy/ phát sáng, liquid, psychedelic, distortion, màu là nhân vật chính | `opus-motion-shader` | Fragment shader GLSL chạy trên WebGL, mọi pixel là hàm của thời gian |
| Vật thể 3D thật, camera bay, portfolio/product 3D, chiều sâu và ánh sáng thật | `opus-motion-threejs` | Scene 3D với camera + lighting, vẫn khóa vào seek(t) |
| Brief trộn nhiều kỹ thuật | Lấy kỹ thuật của "nhân vật chính" làm skill chủ, mượn kỹ thuật phụ từ skill còn lại, ghi rõ trong brief | Tránh dàn trải |

Không chắc → mặc định `opus-motion-svg-gsap` cho nội dung UI/thương hiệu, `opus-motion-canvas` cho hiệu ứng tự do.

## Nguyên lý cốt lõi (áp dụng cho MỌI kỹ thuật — đây là "chất" của corpus)

1. **Animation là hàm thuần của thời gian.** Toàn bộ trạng thái tại thời điểm `t` tính từ `seek(t)` xác định (deterministic). Không CSS transition, không timer tích lũy, không physics state mang sang frame sau. Seek tới bất kỳ frame nào, theo bất kỳ thứ tự nào, kết quả phải giống hệt.
2. **Spring dạng đóng (closed-form).** Chuyển động dùng step response của spring tắt dần tới hạn (critically damped): `s(t) = 1 − (1 + ωt)·e^(−ωt)`. Một giá trị đổi đích nhiều lần = tổng của từng spring con cho mỗi lần đổi → vẫn là hàm thuần của `t`. Overshoot tối đa rất nhỏ.
3. **Mọi thứ nằm trên lưới nhịp ~120 BPM.** Phân tích nhạc bằng numpy lấy beat grid, bắt đầu ở downbeat; sự kiện hình ảnh rơi đúng beat; hiệu ứng âm thanh đặt theo peak đo được. Không có "dead time" — mỗi beat phải có chuyện xảy ra.
4. **Loop liền mạch (khi làm loop):** frame cuối ≡ frame đầu, kể cả vị trí/tốc độ của cursor và mọi phần tử phụ.
5. **Cấm:** easing nảy/đàn hồi (bouncy/elastic), particle burst vô cớ, glow rẻ tiền, gradient trang trí trên UI chrome, dead time, vẻ "template". Thà ít chuyển động mà chắc tay.

## Quy trình sản xuất (pipeline chung — skill này sở hữu)

1. **Đọc prompt gốc để học:** tra `MOTION-INDEX.md`, mở 1–3 file `~/workspace/opus55-videos/prompts/<slug>.md` cùng archetype (ưu tiên prompt `full`). Rút ra: cấu trúc timeline, kỹ thuật chuyển động, gotchas — không copy nội dung.
2. **Adapt thành brief mới:** viết brief của user theo khung: deliverables (kích thước/fps/thời lượng) · art direction (màu, font, chất liệu) · timeline theo beat/ giây · audio · tiêu chí QA. Nội dung, thương hiệu, text: mới 100%.
3. **Dựng single-file HTML:** một file `.html` duy nhất chứa toàn bộ scene + hàm `seek(t)`; mọi transform/opacity/mask/UI state suy ra từ `t`. Theo đúng skill con đã chọn.
4. **Render frame-by-frame:** headless Chromium/Playwright mở file HTML, gọi `seek(t)` cho từng frame, chụp PNG. Mỗi frame render **3–5 temporal subframes** lệch nhau một phần nhỏ của 1 frame rồi trộn bằng ffmpeg `tmix` → motion blur tự nhiên, vật tĩnh vẫn sắc nét.
5. **Ghép MP4 + nhạc:** nhạc ~120 BPM bản quyền sạch (tự tổng hợp warm pad hoặc nguồn royalty-free), canh sự kiện hình theo beat grid, xuất loudness ≈ **−14 LUFS**. Không lồng tiếng trừ khi user yêu cầu.
6. **QA rồi mới giao** (xem mục QA bắt buộc). Chỉ báo "xong" sau khi render + QA thật đạt.

## Quy trình sản xuất — ghi chú máy này

- Máy đã có sẵn Node/Chromium headless qua hệ video-kit hiện hữu; render tuần tự, concurrency thấp (máy 2 core).
- Font chữ hiển thị tiếng Việt khổ lớn: **Be Vietnam Pro** (đã kiểm glyph). **Không** dùng Anton/Oswald cho chữ tiếng Việt lớn — dấu nặng (Ọ/Ị…) bị tách/sai vị trí.
- Mỗi dự án một thư mục riêng trong workspace, giữ lại: file HTML nguồn, thư mục frames, file nhạc, MP4 cuối, contact sheet QA.

## Công thức & kỹ thuật đặc thù

- Spring chuẩn nhà: `s(t) = 1 − (1 + ωt)·e^(−ωt)`, `ω` chỉnh theo độ "gắt" mong muốn (ω lớn = tới đích nhanh). Cộng dồn spring khi đổi đích giữa chừng.
- Stagger theo beat: phần tử thứ `i` bắt đầu tại `beat_i = i × (60/BPM)`, không dùng delay cảm tính.
- Motion blur: subframes tại `t + k/(fps × N)` với `N = 3–5`, trộn `tmix=frames=N:weights='1 1 1 ...'`.
- Match-cut theo vị trí: phần tử ra và phần tử vào dùng chung tâm/ tỉ lệ tại thời điểm chuyển để mắt không phải "tìm lại" chủ thể.

## QA bắt buộc

- ffprobe: đúng kích thước (1280×720 hoặc 1920×1080), đúng fps (30 hoặc 60), đúng thời lượng thiết kế.
- Contact sheet (ít nhất 3×2 frame dàn đều + các frame ở điểm chuyển cảnh nhanh): kiểm text không chồng nhau, không tràn khung, glyph tiếng Việt đúng.
- Kiểm frame tại các beat chính: sự kiện có rơi đúng nhịp không; có dead time > 1 beat không.
- Nếu là loop: so frame đầu và frame cuối — phải giống hệt.
- Loudness ≈ −14 LUFS, true peak ≤ −1 dBTP.
- Xem lại bản phát (không chỉ ảnh tĩnh) ít nhất 1 lượt trước khi giao.

## Output contract

Giao: **MP4 cuối** + **file HTML nguồn** (sửa được) + thông số (kích thước/fps/thời lượng/dung lượng) + ghi chú kỹ thuật đã dùng và prompt gốc đã tham khảo (slug). Không đăng công khai khi chưa có duyệt mới của user. Chưa render + QA xong thì không nói "xong".
