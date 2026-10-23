---
name: opus-game-canvas
description: Làm game 2D chơi được bằng Canvas 2D trong một file HTML duy nhất — pixel art, arcade 2D, top-down/side-view. Dùng khi user nói "làm game 2d", "làm game pixel", "làm mini game canvas", "làm game arcade đơn giản", "làm game chạy trong browser không cần cài", hoặc brief game phẳng không cần 3D. Kỹ thuật lõi: fixed-timestep sim, logical resolution + integer scaling cho pixel art, sprite vẽ thủ tục, particle pooling, bot-play để quay demo.
---

# Opus Game Canvas — Game 2D / pixel trong 1 file HTML

Thuộc bộ `opus55-interactive` (master sở hữu workflow chung: PRD rút gọn → greybox → juice → capture). Skill này sở hữu kỹ thuật Canvas 2D.
Thư viện gốc: `~/workspace/opus55-videos/prompts/`; catalogue: `~/workspace/opus55-videos/INTERACTIVE-INDEX.md` (nhóm Canvas Playable: 21 mục).

**Prompt mẫu nên đọc trước khi build (đều là prompt full, đã kiểm chứng trong videos.json):**
- `zacxbt-944604` — mẫu mực nhất cho pixel art: logical resolution 128×96, palette cố định ~24 màu, sprite vẽ thủ tục theo tham số pose, state machine IDLE→CHARGE→CAST→RECOVER, particle pooled allocation-free, fixed 60Hz timestep. Đọc kỹ file này trước mọi dự án pixel.
- `froessell-562325` — dù build 3D trong bản gốc, phần thiết kế arcade (điều khiển một ngón, AI đón đầu, escalation, juice stack) áp nguyên cho bản 2D top-down.
- `aisongman-461057`, `opener-ai-843891` — mẫu ngắn canvas + pixel + playable, xem cách brief gọn mà vẫn build được.
- `bilimfili1-459762` — canvas + svg playable, tham khảo khi game cần lớp DOM/SVG phụ (HUD, menu).

## Khi nào dùng

- Game 2D: platformer đơn giản, top-down chase/shooter, snake-like, dodger, puzzle hành động nhẹ, game pixel art hoài cổ.
- Trải nghiệm tương tác 2D có thắng/thua/điểm (không có game loop → quay về nhóm Motion).
- Không dùng khi brief cần chiều sâu/camera 3D thật → `opus-game-threejs`.

## Nguyên lý cốt lõi

1. **Sim cố định, render tự do.** Vòng lặp: rAF chỉ để vẽ; sim chạy bằng accumulator với `dt = 1/60` cố định. Tốc độ game không phụ thuộc fps hay máy mạnh/yếu — và đây là điều kiện để quay demo khớp từng frame.
2. **Vẽ lại toàn khung mỗi frame từ state.** Không giữ "vật thể DOM" cho gameplay; state là nguồn sự thật duy nhất, canvas là ảnh chụp của state.
3. **Không cấp phát trong vòng lặp.** Particle, đạn, địch dùng pool mảng cố định, tái sử dụng slot chết. Đây là quy tắc cứng của mẫu zacxbt ("zero object allocation inside the loop") và là lý do game canvas chạy ổn định lâu dài.
4. **Pixel art là một hệ thống, không phải style bôi lên.** Logical resolution cố định (ví dụ 128×96, 160×90, 320×180), scale lên bằng hệ số nguyên lớn nhất vừa màn hình, `imageSmoothingEnabled = false` + CSS `image-rendering: pixelated`, mọi tọa độ vẽ snap về lưới nguyên, palette đóng (~24 màu) — mọi pixel đều thuộc palette.
5. **Sprite thủ tục theo tham số.** Nhân vật dựng từ rect/run theo tham số pose (góc tay, độ nghiêng, sway) rồi lượng tử hóa về lưới pixel → chuyển động mượt ở tầng tham số nhưng đọc như animation 8–12fps đúng chất 16-bit.

## Quy trình

1. **PRD rút gọn** theo master (core loop, điều khiển, MVP scope, bảng điểm/escalation nếu có, ngân sách hiệu năng).
2. **Khung file:** 1 HTML — CSS căn giữa canvas, JS gồm các khối: `CONFIG` (mọi thông số tune được) · input · sim (update theo dt) · render · audio (WebAudio tổng hợp) · demo mode (`?demo=1` + seed).
3. **Greybox:** hình khối màu đặc + arena, điều khiển chạy, va chạm cơ bản. Chơi thử: di chuyển đã tay chưa.
4. **Hệ thống game:** địch/AI (đón đầu + sai số cố ý), va chạm, điểm, escalation, game over + restart ≤ 2s.
5. **Hình ảnh:** thay khối thô bằng sprite thủ tục/pixel art theo hệ thống ở Nguyên lý 4–5; state machine cho nhân vật (idle/move/attack/hurt…) kèm easing giữa keyframe pose.
6. **Juice:** particles pooled (vòng đời theo palette index: sáng → màu chủ → tối → despawn), screen shake 1–2px cho sự kiện vừa, hit-stop chỉ cho sự kiện lớn, popup điểm.
7. **Capture demo:** chạy `?demo=1` với input script/bot + seed cố định, step sim theo frame, chụp bằng headless Chromium → MP4 (chi tiết ở master).

## Công thức & kỹ thuật đặc thù

- **Fixed timestep:** `acc += min(frameDelta, 0.1); while (acc >= DT) { update(DT); acc -= DT } render(interpolation không bắt buộc với game pixel — snap lưới đã đủ)`.
- **Integer scaling:** `scale = max(1, floor(min(winW/logW, winH/logH)))`; canvas hiển thị = logW×scale; vẽ lên offscreen ở logical resolution rồi blit.
- **State machine nhân vật:** trạng thái là hàm của timer + sự kiện; chuyển trạng thái reset timer; pose params nội suy (ease) rồi mới quantize — đừng nội suy trực tiếp trên pixel.
- **AI đón đầu:** `target = player.pos + player.vel × tPredict` (tPredict 0.3–0.8s tùy độ khó); thêm nhiễu/overshoot cố ý theo cấp escalation.
- **Va chạm rẻ:** AABB hoặc khoảng cách bình phương; broad-phase bằng lưới ô (grid) khi entity nhiều. Không dùng thư viện vật lý cho arcade 2D trừ khi brief đòi.
- **RNG có seed:** mulberry32/LCG tự viết, seed đặt trong CONFIG → run quay lại giống hệt khi capture; cấm `Math.random()` trong sim (chỉ dùng cho hiệu ứng thuần thị giác không ảnh hưởng gameplay — mà tốt nhất cũng qua RNG seed).
- **Âm thanh:** WebAudio oscillator/noise buffer tổng hợp (beep, nổ, nhặt điểm); tạo khi có tương tác đầu tiên (chính sách autoplay của browser); mute bằng phím M.

## QA bắt buộc

- Kế thừa QA của master (offline file://, không request mạng, chơi hết vòng đời, restart ≤ 2s, bot chạy không kẹt).
- Riêng canvas: kiểm tra ở 2–3 kích thước cửa sổ — pixel vẫn crisp, scale nguyên, không vỡ lưới; FPS counter ~60 ở cảnh đông nhất; throttle CPU 4× — tốc độ sim không đổi; chơi liên tục 5 phút không tụt fps (dấu hiệu rò pool/cấp phát trong loop).
- Nếu có chữ tiếng Việt: dùng font hệ thống/Be Vietnam Pro cho HUD (đừng vẽ chữ bằng pixel font tự chế thiếu glyph Việt).

## Output contract

Theo master: file HTML playable là sản phẩm chính + PRD rút gọn + video demo bot-play (20–45s thấy trọn core loop) + ghi chú slug mẫu. Nêu rõ trong ghi chú: logical resolution, palette (nếu pixel art), phím/touch điều khiển.
