---
name: opus-game-prd
description: Biến ý tưởng game thành PRD build được rồi greybox theo milestone — core loop, điều khiển, escalation, MVP scope, milestone kèm tiêu chí qua, juice list, ngân sách hiệu năng. Dùng khi user nói "viết prd game", "thiết kế game giúp tôi", "lên ý tưởng game này thành bản build được", "làm spec game", "game này nên làm thế nào", hoặc ý tưởng game còn mơ hồ chưa chốt loop/điều khiển/phạm vi. Sau PRD, build greybox bằng opus-game-canvas hoặc opus-game-threejs.
---

# Opus Game PRD — Từ ý tưởng tới bản build được

Thuộc bộ `opus55-interactive`. Skill này sở hữu **tài liệu thiết kế**; việc build thuộc `opus-game-canvas` / `opus-game-threejs` theo workflow của master.
Thư viện gốc: `~/workspace/opus55-videos/prompts/`; catalogue: `~/workspace/opus55-videos/INTERACTIVE-INDEX.md` (nhóm PRD/Spec).

**Thực tế corpus (nói thẳng):** trong 101 prompt Interactive chỉ có **2 tài liệu đạt chuẩn PRD đúng nghĩa** theo quét tín hiệu (PRD/MVP/milestone/core loop/acceptance criteria…) — nhưng chúng là 2 mẫu có giá trị phương pháp cao nhất cả nhóm:
- `froessell-562325` — PRD game chase "Heatwave": đủ mọi thành phần ở khung dưới, milestone có success criterion và gate "không đạt không đi tiếp", câu hỏi kiểm chứng sau prototype. **Đây là archetype gốc của skill này — đọc kỹ trước khi viết PRD.**
- `niegramotny-197521` — spec đua xe dạng kỹ thuật: stack, kiến trúc thư mục, workflow theo giai đoạn (a–e), out-of-scope tường minh, acceptance criteria kiểm chứng được, unit test cho logic (boost/lap).
- `zacxbt-944604` — spec cấp component: không phải PRD sản phẩm nhưng là mẫu viết đặc tả kỹ thuật (RENDERING / ANIMATION / QUALITY BAR) chặt tới mức build không cần hỏi lại — học cách viết mục "đặc tả" từ file này.

## Khi nào dùng

- User có ý tưởng game (dù chỉ 1 câu) và muốn làm thật: cần chốt thiết kế trước khi code.
- Dự án game lớn hơn 1 buổi build, hoặc user muốn tài liệu để giao người khác/agents khác build.
- Không dùng khi: brief đã là spec rõ ràng (build thẳng qua skill kỹ thuật), hoặc game nhỏ làm trong 1 lần (master đã có PRD rút gọn 1 trang — skill này là bản đầy đủ).

## Nguyên lý cốt lõi

1. **PRD trả lời "chơi có vui không, biết vui bằng cách nào" trước "có tính năng gì".** Mọi mục thiết kế phải truy được về core loop; tính năng không phục vụ loop thì vào danh sách Phase 2 (parking lot), không vào MVP.
2. **MVP scope là một danh sách cắt bỏ, không phải danh sách mơ ước.** Ghi tường minh cả phần KHÔNG làm (progression, monetization, nhiều arena, save…) — mẫu froessell mở đầu milestone 1 bằng câu lệnh cấm build những thứ đó.
3. **Mỗi milestone có đúng 1 success criterion kiểm chứng bằng chơi thử**, và milestone "cảm giác điều khiển" (greybox) là gate cứng: chưa đã tay thì dừng, tune tiếp, không chất thêm hệ thống.
4. **Thông số là biến, không phải hằng số chôn trong code.** Mọi giá trị gameplay (tốc độ, điểm, thời gian, số địch mỗi cấp) nằm trong bảng CONFIG của PRD — build và tune đều theo bảng này.
5. **Thất bại phải công bằng và dễ hiểu.** PRD phải nêu nguyên tắc failure fairness: người chơi thua vì lỗi họ nhận ra được, không vì vật lý ngẫu nhiên khó lường.
6. **PRD kết thúc bằng câu hỏi kiểm chứng, không phải lời hứa.** Đặt 3–5 câu hỏi chỉ trả lời được bằng cách đưa bản chơi được cho người thật (hiểu ngay không? chết có restart không? có "one more run" không?) — và quy tắc: nếu không, sửa core loop, đừng thêm nội dung.

## Khung PRD (đi theo đúng thứ tự này)

1. **Trang bìa 6 dòng:** tên tạm · nền tảng & hướng màn hình · engine đích (ở bộ này: HTML canvas/three.js) · thể loại · input chính · mô hình kinh doanh (chưa rõ thì ghi TBD — thiết kế quanh gameplay trước).
2. **Product vision + fantasy 1 câu:** người chơi *là ai, mạnh ở điểm nào, yếu ở điểm nào* (mẫu: "Bạn không mạnh hơn cảnh sát. Bạn khó bắt hơn."). Kèm 3–4 trụ cột trải nghiệm dạng phép cộng (điều khiển dễ + truy đuổi hung hăng + hỗn loạn vật lý + áp lực leo thang).
3. **Core loop:** sơ đồ chữ dạng mũi tên (START → hành động → phản ứng hệ thống → phần thưởng → áp lực tăng → … → kết thúc → restart), kèm **thời lượng run mục tiêu** và **thời gian restart tối đa** (chuẩn: restart < 2s).
4. **Design principles:** 3–6 nguyên tắc đánh số, mỗi nguyên tắc là một câu kiểm chứng được khi chơi (ví dụ "điều khiển hiểu trong vài giây, xe tự tăng tốc, người chơi chỉ lái hướng").
5. **MVP scope:** hai cột LÀM / KHÔNG LÀM. Bản MVP chuẩn của thể loại chase/survival chỉ cần: 1 nhân vật chính, 1 arena/track, 1 địch thường + 1 địch elite, hệ escalation, va chạm, điểm, máu/thua, VFX+âm thanh cơ bản, màn hình game over, restart tức thì.
6. **Đặc tả thực thể:** từng loại nhân vật/địch — hành vi, điểm mạnh/yếu cố ý, và **bảng biến tune** (acceleration, maxSpeed, turnSpeed, grip, driftFactor, mass, collisionForce, drag, recovery… cho xe; tương đương cho thể loại khác).
7. **Điều khiển:** sơ đồ input chính (ưu tiên đơn giản nhất: một ngón/một cụm phím; drag tương đối thay vì tuyệt đối; nhả tay không mất lái) + **1–2 phương án dự phòng ghi rõ "chưa chốt, phải test trên thiết bị thật"**.
8. **AI / hành vi địch:** mục tiêu đón đầu theo vận tốc, và **giới hạn cố ý** (né vật cản kém, tính toán lẫn nhau kém, overshoot cua) — ghi thành yêu cầu, không để lập trình viên "làm AI giỏi quá" phá game.
9. **Escalation:** bảng theo cấp (sao/wave/level): số địch, tốc độ, độ hung hăng, khi nào elite xuất hiện, điều kiện tăng cấp (thời gian + điểm); nêu rõ cuối thang là "gần như không thể qua" nếu đó là chủ đích thể loại.
10. **Điểm số:** bảng hành động → điểm (sống sót theo giây, phá hủy, chuỗi combo với hệ số tăng mạnh cho chain, near-miss…), mọi số đều ghi "configurable".
11. **Máu & thua:** mức sát thương theo cấp va chạm, trường hợp chết ngay, nguyên tắc fairness ở Nguyên lý 5.
12. **Arena / world:** bản đầu **thiết kế tay, không procedural**; phác đồ ASCII hoặc mô tả bố cục chướng ngại có khoảng hở cho tốc độ cao; theme hình ảnh đầu tiên (chọn theme tránh clone game tham chiếu).
13. **Camera:** góc, smoothing, look-ahead, hành vi theo tốc độ — và mục **camera juice** riêng (rung nhẹ/nặng theo sự kiện, hit-stop 50–100ms).
14. **Visual style + VFX tối thiểu:** vài tính từ khóa (chunky, silhouette rõ, ít texture…) + danh sách hiệu ứng bắt buộc cho MVP theo nhóm (player / enemy / environment).
15. **Chồng phản hồi va chạm (collision feedback stack):** viết thành chuỗi cố định IMPACT → impulse vật lý → mảnh vỡ → sparks → khói → rung camera → hit-stop → âm thanh → popup điểm. Đây là "nguồn thỏa mãn chính" — không được cắt khi rút scope.
16. **UI/HUD:** phác ASCII HUD tối giản (điểm, cấp escalation, máu), chỉ dẫn ngoài màn hình cho địch nếu cần; game over: slow-motion ngắn → tổng điểm/best → nút chơi lại, không menu trung gian.
17. **Âm thanh:** danh sách âm bắt buộc theo sự kiện (động cơ, va chạm, phá hủy, tăng cấp, UI) + ghi chú cường độ leo theo escalation.
18. **Kiến trúc kỹ thuật:** cây manager/system vừa đủ (Game/Player/Enemy/Systems/UI), nguyên tắc "không dựng framework hoành tráng"; object pooling cho địch/particles/mảnh vỡ.
19. **Ngân sách hiệu năng:** fps mục tiêu trên thiết bị tầm trung, trần entity đang hoạt động, trần particles, giới hạn light/shadow, yêu cầu test trên thiết bị/máy thật sớm.
20. **Milestones:** 5–7 mốc, mỗi mốc = danh sách build ngắn + **1 success criterion**; mốc 1 luôn là greybox điều khiển trong sân trống (gate cứng), mốc cuối của MVP là "đưa người thật chơi và trả lời câu hỏi kiểm chứng".
21. **Câu hỏi kiểm chứng + Phase 2:** 3–5 câu hỏi kiểu froessell (hiểu ngay không / có restart sau khi thua không / có cố ý tạo combo không / có "one more run" không) và danh sách mở rộng để sau (xe mới, arena mới, unlock, leaderboard…) — chỉ mở khi kiểm chứng đạt.

## Quy trình

1. Đọc ý tưởng của user + 1–2 prompt mẫu ở trên; nếu thiếu thông tin cốt lõi (thể loại, input, nền tảng) thì tự chọn mặc định hợp lý và **ghi rõ giả định** trong PRD thay vì hỏi vòng vo.
2. Viết PRD theo khung 21 mục (bản đầy đủ) hoặc rút còn các mục 1–3, 5, 7, 9–10, 19–20 nếu user chỉ cần bản gọn — và nói rõ đây là bản rút.
3. Trình PRD cho user duyệt **trước khi build** (đây là điểm dừng bắt buộc của skill này — khác với game nhỏ đi thẳng qua master).
4. Sau duyệt: chuyển build cho `opus-game-canvas` hoặc `opus-game-threejs`, bắt đầu ở milestone 1 (greybox) và tôn trọng gate từng mốc; PRD là tài liệu sống — tune thông số thì cập nhật lại bảng CONFIG trong PRD.

## Công thức & kỹ thuật đặc thù

- **Bảng escalation mẫu (chase/survival, 5 cấp):** L1: 2 địch, chậm, tha thứ · L2: 3–4, nhanh hơn chút · L3: 5–6, đón đầu gắt · L4: 7–9, elite vào cuộc · L5: 10+ (theo ngân sách hiệu năng), elite thường xuyên. Run phải có cung cảm xúc: bình yên → áp lực → hỗn loạn → hoảng → thua.
- **Điểm chuỗi (chain) tăng phi tuyến:** đơn 250 → đôi 600 → ba 1.000 → pileup 2.000 (số mẫu của froessell — luôn ghi configurable). Combo là nơi điểm và niềm vui cùng bùng, nên hệ số phải dốc.
- **Near-miss:** phát hiện địch lướt sát ở vận tốc tương đối cao → thưởng điểm + popup; rẻ để làm, khuyến khích chơi mạo hiểm.
- **Elite = glass cannon:** nhanh và hung hăng hơn nhưng dễ vỡ hơn địch thường — tạo quyết định chiến thuật (dụ elite đâm tường trước).

## QA bắt buộc (cho tài liệu PRD)

- Đọc ngược từ cuối: mọi milestone có success criterion chưa; mọi con số gameplay có nằm trong bảng CONFIG/configurable không; MVP scope có cột KHÔNG LÀM không; core loop có khép vòng về restart không; có câu hỏi kiểm chứng không.
- Đối chiếu gate: milestone 1 có phải greybox điều khiển không (nếu không, PRD sai khung).
- Sau khi build xong từng mốc, quay lại PRD đánh dấu đạt/chưa đạt criterion — chưa đạt thì PRD phải ghi quyết định tune hay cắt scope.

## Output contract

Giao: **file PRD (Markdown)** + tóm tắt 5 dòng cho user (fantasy, core loop, MVP gồm gì, milestone 1 là gì, câu hỏi kiểm chứng chính). Chỉ build sau khi user duyệt PRD. Ghi rõ slug mẫu đã tham khảo; nội dung game (tên, theme, nhân vật) là sáng tạo mới, không sao chép game trong prompt mẫu.
