# Vòng self-review — 28/11/2026

Skill: `agent-self-review-loop` (mới chưng cất, chưa push). Vòng review thủ
công đầu tiên chạy theo skill này, trên công việc 21–28/11/2026.
Evidence: file báo cáo và deliverable đã ghi trong workspace (ghi rõ nguồn
từng claim bên dưới); chỗ nào không có evidence thì ghi "chưa xác lập".

## 1. Memory upkeep — việc mới đáng ghi

- 21/11: Trí gửi reel BINA → rea-video phân tích → demo "Hai đội bóng"
  70,2 giây, QA PASS, Trí chọn hướng demo tiếng Việt. (Evidence:
  `video-kit/demos/bina-brand/breakdown/QA.md`,
  `video-kit/demos/bina-demo/QA.md`.)
- 27/11: kiểm tra cập nhật skill tuần — marketingskills lên v2.14.29, chờ
  Trí quyết; quyết định v2.14.25 tuần trước chưa được trả lời nên đã bị thay
  thế. (Evidence:
  `goals/private-github-skill-library/hidden_files/skill-update-check-2026-11-27.md`.)
- 28/11: khảo sát 7 nguồn use case Muse + repo win4r/MuseAI-Skills; Trí
  duyệt chưng cất 5 + 5 skill mới, demo rồi mới push. (Evidence: 2 file
  khảo sát ngày 28/11 trong `hidden_files/`.)
- Chưa ghi vào MEMORY.md trong vòng này — vòng review chỉ ghi lại, việc cập
  nhật MEMORY.md để cho lượt chính (không tự sửa memory trong demo).

## 2. Relationships — không có người/cộng sự mới

Không ai mới xuất hiện trong tuần. Không cập nhật page người/nhóm.

## 3. Idea curation — ý tưởng nảy ra từ việc vừa làm

- Mảng nội dung "định vị thương hiệu qua 2 trường hợp" kiểu BINA có thể
  thành series cho kênh Học Bóng Rổ (đã đề xuất với Trí ngày 21/11, Trí
  chưa trả lời). Feasibility: cao (đã có demo QA PASS). Fit: cao (đúng
  chuẩn 60–90 giây). Novelty: trung bình (mẫu BINA đã có sẵn).
- Chưa đề xuất chính thức lần 2 — theo quy tắc một lần nhắc rồi im lặng.

## 4. Studying / briefing theo goal

- Goal skill library: repo 2.556 skill, HEAD 7915ee9 (21/11). Treo: quyết
  định marketingskills v2.14.29; push 10 skill mới sau khi demo xong.
- Goal kênh Học Bóng Rổ: plan 10 ngày 18–27/11 đã xong; Mẻ 7 xong; tháng 2
  chưa có hướng (Trí chưa chốt).
- Goal Dragons/VBA: hồ sơ 14/11 quá hạn, chưa xác nhận đã gửi — vẫn treo
  từ 16/11, không có diễn biến mới.

## 5. Dreaming synthesis — hiệu quả / rạn nứt / Trí đang trở thành ai

- **Hiệu quả:** pipeline rea-video → demo chạy ổn định (BINA: phân tích
  17 phút, demo QA PASS ngay lần giao); cổng demo-trước-khi-duyệt giữ được
  kỷ luật (10 skill mới chưa push skill nào khi chưa có demo); nghiên cứu
  song song bằng subagent fan-out cho kết quả nhanh (khảo sát 7 nguồn xong
  trong một buổi).
- **Rạn nứt:** (a) VieNeu API sập nặng ngày 21/11 (HTTP 503 cả Mac 27 và
  Mac 14), phải chạy 5 lượt mới đủ 9 segment giọng — rủi ro lịch đăng nếu
  API sập vào ngày sản xuất; (b) quyết định marketingskills v2.14.25 treo
  từ 20/11 không có trả lời, phải làm lại với v2.14.29 — quyết định treo
  quá lâu sẽ bị phiên bản mới thay thế, cần ghi rõ hạn của từng quyết định
  khi trình Trí; (c) repo win4r ban đầu tưởng là nguồn skill mới, thực chất
  là skill hệ thống không license — may mà khảo sát kỹ trước khi chép, nếu
  chép thẳng vào repo public đã sai bản quyền.
- **Trí đang trở thành ai:** từ người thu thập skill (2.556 skill) sang
  người chưng cất thiết kế workflow thành skill của mình — 10 skill đợt
  này đều là workflow, không phải clone. Hướng này đúng và nên giữ.

## 6. Skill review / retire

- Workflow lặp lại lần 2–3 trong tuần, đã thành skill đợt này: nghiên cứu
  song song (wide-research-coordinator), nghiệm thu deliverable
  (artifact-acceptance-gate), review skill (skill-design-review), pipeline
  video kể chuyện (magic-moment-video), vòng tự review
  (agent-self-review-loop).
- **Retire: chưa phát hiện skill nào cần retire trong vòng này.** Ghi chú:
  cần một lượt rà soát riêng các skill video-kit cũ trùng scope
  (motion-video các variant) vào dịp khác — chưa làm trong vòng này.
- Kiểm tra lệnh/path trong 5 SKILL.md mới: đã kiểm tra tên không trùng;
  path `~/workspace/video-kit/demos/` và `ffmpeg` đã kiểm chứng thật trong
  demo skill-design-review.

## 7. Việc treo còn lại

1. Trí quyết marketingskills v2.14.29 (widget đã gửi 27/11).
2. Demo video magic-moment đang chạy (subagent) + 3 worker nghiên cứu nền
   tảng vé — xong sẽ tổng hợp báo cáo coverage.
3. Push 10 skill mới — chỉ sau khi Trí duyệt demo từng skill.
4. Hướng tháng 2 kênh Học Bóng Rổ + mảng BINA series — chờ Trí.
