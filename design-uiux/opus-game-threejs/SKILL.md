---
name: opus-game-threejs
description: Làm game 3D chơi được bằng Three.js trong một file HTML — đua xe arcade, chase/survival 3D, khám phá 3D nhẹ. Dùng khi user nói "làm game 3d", "làm game đua xe web", "làm game three.js chơi được", "làm game rượt đuổi 3d", hoặc brief có camera 3D/vật thể 3D chơi được. Kỹ thuật lõi: hình học low-poly sinh bằng code (không asset ngoài), vật lý arcade 2.5D tự viết, entity data-driven dùng chung interface cho người chơi và AI, track/world là dữ liệu, bot-play quay demo.
---

# Opus Game Three.js — Game 3D playable trong 1 file HTML

Thuộc bộ `opus55-interactive` (master sở hữu workflow chung). Skill này sở hữu kỹ thuật Three.js playable.
Thư viện gốc: `~/workspace/opus55-videos/prompts/`; catalogue: `~/workspace/opus55-videos/INTERACTIVE-INDEX.md` (nhóm Three.js Playable: 40 mục — nhóm lớn nhất của Interactive).

**Prompt mẫu nên đọc trước khi build (prompt full, đã kiểm chứng):**
- `niegramotny-197521` — mẫu mực nhất: game đua lấy cảm hứng Ignition (1997) nhưng **nội dung gốc 100%**; low-poly sinh bằng code, vật lý 2.5D tự viết, xe data-driven, track là dữ liệu (spline + zones), AI dùng chung control interface, boost theo pin sạc, failsafe chống kẹt, acceptance criteria rõ. Đọc kỹ trước mọi dự án 3D.
- `froessell-562325` — PRD chase game đầy đủ nhất corpus: escalation wanted 5 cấp, AI đón đầu cố ý "hơi ngốc", juice stack, milestone có gate. Thiết kế của nó port thẳng sang bản three.js.
- `0xchuckstock-879327` — brief 1 câu (phi đội bắn hạm) cho thấy hướng ngược: brief càng ngắn, PRD rút gọn của mình càng phải làm việc nhiều trước khi code.
- `0xrathi-511319`, `gandamu-ml-220530` — mẫu threejs + physics/audio playable ngắn, tham khảo phạm vi MVP.

## Khi nào dùng

- Game 3D nhẹ trong browser: đua xe top-down/góc nghiêng, rượt đuổi, thu thập/tránh né trong không gian 3D, showroom có điều khiển được.
- Không dùng cho: scene 3D chỉ để xem (không gameplay → `opus-motion-threejs`), game 2D (→ `opus-game-canvas`), hay dự án cần engine thật (Unity/Godot) — bộ này chỉ làm bản web HTML.

## Nguyên lý cốt lõi

1. **Mọi hình học sinh bằng code.** Box/Cylinder/Sphere + màu đặc + vật liệu đơn giản (MeshLambert/Standard rẻ). Không model/texture ngoài — vừa giữ file single-file offline, vừa cho phong cách low-poly chunky đọc rõ silhouette như corpus.
2. **Vật lý arcade 2.5D tự viết, không engine vật lý.** Chuyển động trên mặt phẳng XZ (hoặc XY tùy game), chiều cao/bề mặt xử lý riêng; drift đến từ mô hình grip đơn giản (tốc độ càng cao, bám ngang càng giảm). Khó lường của engine vật lý là kẻ thù của game arcade — mẫu niegramotny cấm hẳn physics engine.
3. **Entity = dữ liệu + 1 class.** Xe/địch chỉ khác nhau ở config (mass, power, topSpeed, grip, steer, khả năng chịu va chạm, thông số boost: strength/duration/recharge). Thêm entity mới = thêm 1 dòng config.
4. **Người chơi và AI dùng chung control interface** (`throttle, brake, steer, boost`). AI là một "tay lái" khác cắm vào cùng interface → bot test, bot capture demo, và đối thủ đều từ một cơ chế.
5. **World là dữ liệu.** Track/arena định nghĩa bằng spline/centerline + bề rộng + danh sách zone (băng trơn, shortcut, chướng ngại) → mesh đường và waypoint AI sinh ra từ cùng dữ liệu đó, không lệch nhau.
6. **Single-file tuyệt đối.** Three.js phải **vendor vào trong file HTML** (inline) hoặc kèm theo như một phần của file giao — không CDN, vì output contract yêu cầu mở offline bằng `file://`. (Khác với demo motion threejs — ở đó file nguồn nhiều file được chấp nhận; game giao cho người chơi phải 1 file tự chứa.)

## Quy trình

1. **PRD rút gọn** theo master: core loop, điều khiển (phím WASD/mũi tên + touch), MVP scope, bảng escalation, ngân sách hiệu năng (trần xe/entity, trần particles ~100, 1–2 light, shadow đơn giản hoặc tắt).
2. **Greybox milestone 1:** mặt phẳng + 1 entity điều khiển được + camera bám. Tiêu chí gate: lái quanh sân trống đã đã tay (drift/grip tune bằng CONFIG).
3. **World:** dựng track/arena từ dữ liệu, zone đặc biệt, chướng ngại; failsafe: entity kẹt > ~4s → đưa về checkpoint gần nhất (cấm kẹt vĩnh viễn, kể cả bot).
4. **AI + va chạm:** đối thủ cùng interface, waypoint + đón đầu, rubber-banding nhẹ, va chạm entity–entity và entity–world có impulse + phản hồi.
5. **Hệ thống game:** boost/kỹ năng theo config, vòng đua/checkpoint hoặc escalation sinh địch, điểm, HUD DOM/CSS (vị trí, vòng, đồng hồ "pin" cho boost: đỏ→vàng→xanh, đầy thì nhấp nháy), màn hình chọn chế độ → chơi → kết quả → restart.
6. **Juice:** trail khói/bụi, tia lửa va chạm, rung camera theo cấp sự kiện, hit-stop cho phá hủy lớn, popup điểm; particles pooled, không cấp phát trong loop.
7. **Capture demo:** bot lái nhân vật chính (cùng AI interface) + seed cố định, quay headless (xem mục Capture ở master và ghi chú máy bên dưới).

## Công thức & kỹ thuật đặc thù

- **Mô hình xe arcade:** vận tốc tách thành phần dọc (theo hướng xe) và ngang; mỗi tick: phần ngang *= gripFactor(dt, speed, zone) → drift tự sinh, không cần nút handbrake. Thông số mẫu cần có: mass, power, topSpeed, grip, steering, collisionResistance + boost{strength, duration, recharge}.
- **Boost kiểu "pin":** chỉ kích hoạt ở 100%, dùng xong về 0 và sạc lại; mỗi entity một bộ số riêng (kẻ nhanh: boost mạnh-ngắn-sạc lâu; kẻ chậm: yếu-nhanh) để cân bằng — và AI cũng dùng boost theo luật (chỉ đường thẳng, không trước cua gấp/không trên băng).
- **AI waypoint + đón đầu:** lái tới waypoint phía trước trên spline; khi truy đuổi thì target = vị trí + vận tốc × tPredict của con mồi; độ bám waypoint và tPredict thay đổi theo cấp escalation. Né chướng ngại ở mức "vừa đủ kém" để người chơi lừa được.
- **Camera:** góc nghiêng ~50–70° (top-down lệch), bám với smoothing (lerp theo dt của render), nhìn lệch về hướng di chuyển (look-ahead), tốc độ cao thì pull-back nhẹ; rung camera cộng riêng một lớp offset, không ghi vào vị trí gốc.
- **Pooling:** enemy/particles/mảnh vỡ lấy từ pool; trần entity hoạt động ghi trong CONFIG theo ngân sách PRD (mẫu froessell: ~12 xe, ~100 debris).
- **Fixed timestep:** sim dt = 1/60 như canvas; render nội suy nhẹ nếu cần nhưng vị trí logic chỉ đổi trong sim step.

## Ghi chú máy này (render/capture)

- WebGL headless cần cờ `--use-angle=swiftshader --enable-unsafe-swiftshader` và **probe 1 frame thử** (kiểm không đen) trước khi render hàng loạt; lái bằng puppeteer-core cài cục bộ trong thư mục dự án (không có sẵn trong `video-kit/node_modules`).
- Khi capture phải tắt vòng rAF tự do và step sim thủ công theo số frame (giống lỗi đã gặp ở bộ Motion: rAF ghi đè seek/step).
- Chơi thử hiệu năng: bản three.js chạy SwiftShader khi capture sẽ chậm — đó là tốc độ render demo, không phải tốc độ chơi thật trên máy user; đừng kết luận game chậm từ thời gian capture.

## QA bắt buộc

- Kế thừa QA của master. Riêng three.js: bot tự lái hoàn thành được một vòng/một run đầy đủ (đua: hết số vòng; chase: tới game over); mọi entity đều qua được failsafe chống kẹt; đổi từng entity trong config đều chơi được và cảm giác lái khác nhau rõ (gate của mẫu niegramotny); HUD đọc được ở 1280×720; không rò WebGL context khi restart nhiều lần.

## Output contract

Theo master: 1 file HTML tự chứa (three.js inline) + PRD rút gọn + video demo bot-play + ghi chú slug mẫu. Ghi rõ: số entity, thông số boost từng loại, phím điều khiển, cách thêm entity/track mới bằng config (người dùng sau này tự mở rộng được).
