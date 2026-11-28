---
name: agent-self-review-loop
description: Vòng lặp tự review của agent chạy nền — memory upkeep, dreaming synthesis, skill review/retire — để rút ra bài học từ công việc đã làm và cải thiện lần sau. Dùng định kỳ (cuối ngày / cuối tuần / sau một đợt việc lớn), không chạy trong lúc đang làm việc dở.
---

# Agent Self-Review Loop

> Chưng cất từ tài liệu `self_improvement.md` (vòng lặp nền của agent) trong
> bản lưu trữ không chính thức https://github.com/win4r/MuseAI-Skills
> (`home/hatch/docs/self_improvement.md`, HEAD 6c12bde, 26/11/2026).
> Repo nguồn KHÔNG CÓ LICENSE và là snapshot skill hệ thống của Muse — skill
> này viết lại hoàn toàn bằng lời của mình, KHÔNG chép nguyên văn. Tài liệu
> gốc mô tả các lượt chạy nền tự động; skill này là bản checklist để chạy một
> vòng review thủ công có kiểm chứng, không tự nhận mình là hệ thống nền.

## Mục đích

Sau một đợt việc, agent dừng lại một vòng để trả lời: cái gì hiệu quả, cái
gì rạn nứt, Trí đang trở thành ai, workflow nào lặp lại đủ để thành skill,
skill nào không còn giúp thì retire. Không có vòng này, cùng một lỗi sẽ lặp
lại và cùng một workflow sẽ phải viết lại từ đầu mỗi lần.

## Nguyên tắc quan trọng nhất

- **Phân biệt "run thành công" với "Trí đã nhận được."** Một lượt chạy
  xong, một handoff đã gửi, một file đã ghi — chưa chứng minh Trí đã thấy
  kết quả. Chỉ tính là giao xong khi có bằng chứng Trí đã nhận (tin nhắn đã
  gửi, file đã trình, Trí đã trả lời).
- **Giải thích đề xuất phải dựa trên evidence đã lưu, không bịa lý do
  sau.** Khi nói "vì Trí thích X" thì phải chỉ ra được dòng memory/file nào
  ghi X. Không tìm thấy evidence thì nói rõ "chưa xác lập được lý do".
- **Claim mới thay claim cũ, có trail.** Ghi đè memory phải giữ lại lịch sử
  (dated notes), không xóa lặng lẽ.

## Các chặng trong một vòng review

### 1. Memory upkeep
- Đọc lại công việc vừa làm: quyết định mới, sở thích mới, sự kiện mới của
  Trí. Ghi vào memory những gì bền (quyết định, quy tắc, cam kết), không ghi
  chi tiết ngày thường. Claim mới thay claim cũ phải ghi rõ thay cái gì.

### 2. Relationships
- Có người/cộng sự mới xuất hiện không? Vai trò, mức thân thiết, việc đang
  cùng làm là gì? Cập nhật page người/nhóm tương ứng.

### 3. Idea curation
- Từ việc vừa làm, có ý tưởng mới nào đáng làm không? Chấm feasibility,
  fit với Trí, novelty rồi mới đề xuất — không đề xuất ý tưởng chưa chấm.

### 4. Studying / briefing theo goal
- Mỗi goal đang chạy: tiến độ tới đâu, tắc ở đâu, bước tiếp theo là gì?
  Ghi lại để lần sau không hỏi lại từ đầu.

### 5. Dreaming synthesis
- Viết ngắn: việc gì hiệu quả, việc gì rạn nứt (lỗi, hiểu lầm, chỗ Trí phải
  sửa lại), Trí đang trở thành ai (hướng làm việc đang dịch chuyển ra sao).
  Ghi vào file dated, không chỉ giữ trong đầu.

### 6. Skill review / retire
- Workflow nào vừa lặp lại lần 2–3 thì chưng cất thành skill mới (demo trước
  khi push, theo cổng nghiệm thu đã chốt).
- Skill nào đã có mà lần này không giúp, hoặc đã lỗi thời (tool đổi, nguồn
  đổi), thì ghi chú retire hoặc cập nhật — không để skill chết nằm trong thư
  viện.
- Kiểm tra skill vừa dùng: lệnh/path/auth trong skill còn khớp runtime thật
  không (xem thêm `skill-design-review`).

### 7. Quiet-moment pass (sau hội thoại dài)
- Khi một cuộc trao đổi dài vừa lặng xuống: một lượt quét ngắn để nội hóa
  những gì vừa xảy ra (quyết định, cảm xúc, việc treo). Tối đa vài lần một
  ngày, không chạy sau mỗi tin nhắn.

## Nhịp chạy

| Vòng | Tần suất | Ghi ở đâu |
|---|---|---|
| Memory + relationships | Khi có tín hiệu mới | `MEMORY.md`, `~/memory/` |
| Idea curation | Hàng ngày | Ideas tab / file ghi chú |
| Studying / briefing goal | Hàng ngày, qua đêm | Goal workspace |
| Dreaming synthesis | Hàng đêm | `~/dreams/` (dated) |
| Skill review / retire | Hàng ngày | Skill library / file review |
| Quiet-moment pass | Sau hội thoại dài, vài lần/ngày | Ghi chú ngắn |

## Output của một vòng review

- File ghi vòng review (dated `.md`): hiệu quả / rạn nứt / Trí đang trở
  thành ai; skill mới đề xuất; skill cần retire/cập nhật; việc treo còn lại.
- Không có output là không có vòng review — suy nghĩ trong đầu không tính.

## Giới hạn

- Vòng review không tự chạy việc mới, không tự push skill, không tự nhắn
  Trí. Nó chỉ ghi lại và đề xuất; hành động vẫn cần Trí duyệt (trừ việc đã
  có ủy quyền từ trước).
- Không bịa evidence: không tìm thấy lý do thì ghi "chưa xác lập".
- Không chạy vòng review giữa lúc đang làm việc dở — review sau khi xong
  việc, không xen giữa.

## Nguồn

- Thiết kế vòng lặp: `self_improvement.md` trong
  https://github.com/win4r/MuseAI-Skills (không license, snapshot skill hệ
  thống Muse, HEAD 6c12bde). Skill này chưng cất lại bằng lời của mình.
