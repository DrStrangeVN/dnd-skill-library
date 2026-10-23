---
name: opus55-interactive
description: Router + workflow chung cho game & trải nghiệm tương tác học từ kho awesome-opus5-5-videos (nhóm Games & interactive, 101 prompt). Dùng khi user nói "làm game html", "làm game chơi được", "làm game kiểu opus55", "làm mini game", "làm game 2d", "làm game 3d chơi trên web", "viết prd game", "thiết kế game này giúp tôi", hoặc gửi ý tưởng game chưa chốt kỹ thuật (canvas 2D / three.js 3D / cần PRD trước). Skill này chọn hướng, giao việc cho skill con và sở hữu workflow brief → PRD rút gọn → greybox playable → juice → demo capture.
---

# Opus55 Interactive — Master (Router + Workflow chung)

Học từ nhóm **Games & interactive** của repo `awesome-opus5-5-videos` (703 video toàn repo, 101 mục interactive: 55 prompt full, 46 partial).
Thư viện prompt gốc: `~/workspace/opus55-videos/prompts/<slug>.md`; catalogue đã xếp nhóm: `~/workspace/opus55-videos/INTERACTIVE-INDEX.md`.
Prompt thuộc về tác giả gốc — **chỉ học kỹ thuật và cấu trúc, nội dung/game luôn làm mới** (tên game, nhân vật, track/arena, asset: tự sáng tạo, không clone IP của ai — mẫu `niegramotny-197521` ghi rõ nguyên tắc này).

## Điểm khác biệt cốt lõi so với nhóm Motion (phải nhớ)

- **Sản phẩm chính là file HTML CHƠI ĐƯỢC** — single-file, mở bằng `file://` chạy offline trong browser, không CDN, không network request, không asset ngoài. Người dùng cầm chơi được ngay.
- **Video demo gameplay chỉ là sản phẩm phụ để duyệt** — quay từ bản playable bằng bot-play/input script (xem mục Capture), không phải mục tiêu chính như nhóm Motion.
- Animation trong game **không** thuần `seek(t)` như motion graphics: game là mô phỏng thời gian thực. Nhưng sim phải **fixed-timestep + seed cố định** để (a) gameplay không phụ thuộc fps máy, (b) quay lại được đúng một run khi capture demo.

## Khi nào dùng

- User muốn một game/trải nghiệm tương tác chạy trong browser: mini game 2D, pixel game, game 3D nhẹ, prototype để test ý tưởng game.
- User có ý tưởng game nhưng chưa rõ thiết kế → đi qua `opus-game-prd` trước.
- Brief đã rõ kỹ thuật → chuyển thẳng skill con:
  - `opus-game-canvas` — game 2D Canvas: pixel art, arcade 2D, top-down/side-view phẳng
  - `opus-game-threejs` — game 3D Three.js chơi được: đua xe, chase, khám phá 3D nhẹ
  - `opus-game-prd` — biến ý tưởng thành PRD game build được, rồi greybox theo milestone

## Chọn hướng theo brief (bảng router)

| Dấu hiệu trong brief | Chọn | Lý do |
|---|---|---|
| 2D, pixel art, sprite, arcade cổ điển, game nhẹ chạy mọi máy, một nút/một ngón | `opus-game-canvas` | Canvas 2D + fixed timestep là đủ, file gọn, 60fps dễ đạt |
| Có chiều sâu 3D, camera bay/quay, xe/vật thể 3D, đua/chase 3D | `opus-game-threejs` | Three.js + vật lý arcade rút gọn (2.5D) là công thức corpus kiểm chứng |
| Ý tưởng còn mơ hồ ("làm game đuổi bắt đi"), chưa chốt core loop/điều khiển/phạm vi | `opus-game-prd` trước, build sau | PRD rút gọn 1 trang chốt loop + MVP + tiêu chí qua milestone; tránh build lan man |
| Chỉ cần hiệu ứng tương tác trang trí, không có thắng/thua/điểm | Không thuộc bộ này → cân nhắc nhóm Motion (`opus55-motion-graphics`) | Không có game loop thì không phải game |

Không chắc → mặc định `opus-game-canvas` cho game nhỏ; ý tưởng lớn hơn 1 buổi build → bắt buộc qua PRD rút gọn trước.

## Nguyên lý cốt lõi (chất của corpus — áp cho mọi game)

1. **Core loop trước, nội dung sau.** Vẽ được vòng lặp dạng sơ đồ chữ (hành động → phản ứng → phần thưởng → áp lực tăng → thua/thắng → restart) mới code. Mẫu chuẩn: `froessell-562325` — loop 13 bước mà bước nào cũng kiểm chứng được khi chơi.
2. **Greybox trước, đẹp sau.** Milestone 1 chỉ cần hình khối/sprite thô trong arena trống: "lái/chơi quanh sân trống đã thấy đã tay chưa" — chưa đạt thì không đi tiếp (nguyên tắc gate của froessell).
3. **Vật lý arcade, không mô phỏng.** Drift, nảy, trượt, va chạm kịch tính được ưu tiên hơn đúng vật lý. Mọi thông số (tốc độ, grip, lực va chạm…) để dạng biến chỉnh được (config object) để tune nhanh.
4. **Kẻ địch/AI là một phần của niềm vui, không phải bài toán tối ưu.** AI đuổi theo điểm đón đầu (`target = pos + vel × predictionTime`), cố ý có hạn chế (né vật cản kém, overshoot cua) để người chơi lừa được. AI và người chơi dùng **chung một interface điều khiển** (throttle/brake/steer/boost) — bot vừa là đối thủ vừa là công cụ test/capture.
5. **Escalation có thiết kế.** Độ khó tăng theo thời gian/điểm qua bảng cấp (số lượng địch, tốc độ, độ hung hăng, biến thể elite). Cuối run phải "khó tới mức gần như không thể" là chủ đích của thể loại survival — ghi rõ trong PRD.
6. **Juice là một milestone riêng, không rải rác.** Phản hồi va chạm = vật lý + particles + âm thanh + rung camera + hit-stop 50–100ms + popup điểm, đi thành chồng (stack) cố định. Screen shake liều lượng nhỏ; hit-stop chỉ cho sự kiện lớn.
7. **Restart < 2 giây, không menu thừa giữa các run.** Thua là bấm chơi lại ngay — nhịp "one more run" quyết định game có sống hay không.
8. **Hiệu năng là ngân sách, không phải hy vọng.** Chốt từ PRD: 60fps trên máy tầm trung; trần số entity đang hoạt động, trần particles; object pooling cho đạn/địch/mảnh vỡ (không cấp phát trong vòng lặp); ít real-time light/shadow đơn giản.

## Quy trình sản xuất (workflow chung — skill này sở hữu)

1. **Học mẫu:** tra `INTERACTIVE-INDEX.md`, mở 1–3 prompt cùng archetype (ưu tiên `full`). Rút: core loop, sơ đồ điều khiển, cấu trúc milestone, gotchas.
2. **PRD rút gọn (luôn làm, kể cả game nhỏ — tối đa 1 trang):** tên tạm · thể loại/nền tảng/hướng màn hình · fantasy 1 câu · core loop dạng sơ đồ · điều khiển (kèm 1 phương án dự phòng để test) · MVP scope (gồm gì / KHÔNG gồm gì) · bảng escalation · bảng điểm · ngân sách hiệu năng · milestone kèm tiêu chí qua từng mốc. Ý tưởng lớn hoặc user yêu cầu tài liệu đầy đủ → dùng `opus-game-prd`.
3. **Greybox playable:** build milestone 1 trong 1 file HTML duy nhất: sim fixed-timestep (accumulator, dt = 1/60), render tách khỏi sim, hình khối thô, điều khiển chạy được, camera bám. Tự chơi thử: điều khiển có "đã" chưa — chưa thì tune biến, không thêm tính năng.
4. **Thêm hệ thống theo milestone:** địch/AI → va chạm & phá hủy → escalation → điểm/game over/restart. Mỗi mốc tự kiểm tiêu chí trước khi sang mốc sau.
5. **Juice pass:** áp chồng phản hồi (mục Nguyên lý 6), particles pooled, âm thanh tổng hợp bằng WebAudio (không file ngoài), popup, hit-stop.
6. **Demo capture (sản phẩm phụ để user duyệt):** lái game bằng bot/input script với seed cố định, quay bằng headless Chromium → MP4 ngắn 20–45s cho thấy trọn core loop (xem mục Capture). Ghép nhạc/tiếng nếu cần, ≈ −14 LUFS.
7. **QA rồi mới giao** (mục QA bắt buộc). Giao file HTML playable trước, video demo kèm sau.

## Capture demo gameplay (chuẩn máy này)

- Cách ưu tiên: nhúng vào game một chế độ `?demo=1` — input lấy từ script timeline (mảng sự kiện phím/chạm theo thời gian) + seed RNG cố định → run quay lại giống hệt mỗi lần.
- Quay bằng puppeteer-core lái Chrome Headless Shell của Remotion (puppeteer-core **không** có sẵn trong `video-kit/node_modules` — cài cục bộ vào thư mục dự án). WebGL (bản three.js) cần cờ `--use-angle=swiftshader --enable-unsafe-swiftshader`; **probe 1 frame trước** (không đen) mới render hàng loạt; tắt autoplay/rAF tự do khi đang step frame.
- Vì sim fixed-timestep: step sim theo số frame cần quay thay vì thời gian thực → video mượt đúng 30fps dù máy chậm.
- Bot-play thay script khi game là survival/chase: dùng chính AI interface cho nhân vật chính với độ khó vừa phải, vẫn seed cố định.

## QA bắt buộc

- Mở file HTML bằng `file://` khi **offline**: chạy được, không lỗi console, không request mạng nào (grep nguồn: không `http://`/`https://` trong src/href/fetch).
- Chơi tay hết vòng đời: start → chơi → thắng/thua → restart (đo restart ≤ 2s) → chơi lại.
- Fixed-timestep thật: ép rAF chậm/nhanh (throttle CPU trong DevTools hoặc sửa fps render) — tốc độ game không đổi.
- Bot/demo mode chạy liền ít nhất 3 run hoặc 3 phút không kẹt (có failsafe chống kẹt: đứng yên quá lâu → reset về checkpoint/trung tâm).
- FPS: hiển thị counter trong lúc dev, đạt ~60fps trên máy này ở scene nặng nhất của MVP.
- Điều khiển: chơi được bằng keyboard; nếu game hướng mobile thì có touch control hoạt động (ít nhất qua emulate) và nút bấm đủ lớn.
- Chữ tiếng Việt trong game (nếu có): font Be Vietnam Pro hoặc font pixel có glyph Việt; không dùng Anton/Oswald cho chữ Việt khổ lớn.

## Output contract

Giao: **file HTML playable** (sản phẩm chính) + **PRD rút gọn** đã dùng + **video demo gameplay** (kèm thông số) + ghi chú prompt gốc đã tham khảo (slug) và cách mở chơi (phím/touch). Không đăng công khai khi chưa có duyệt mới của user. Chưa chơi thử đạt QA thì không nói "xong".
