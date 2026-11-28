---
name: skill-design-review
description: Review một skill trước khi đưa vào thư viện — kiểm tra trigger có rõ không, scope có hẹp không, SKILL.md có gọn không, lệnh/path/auth có khớp runtime thật không. Dùng khi viết skill mới, sửa skill cũ, hoặc trước khi push skill lên repo. Bổ sung cho skill-creator local đã có, không thay thế nó.
---

# Skill Design Review

> Chưng cất từ thiết kế workflow của skill `skill-creator` (mục nguyên tắc
> viết skill + `references/authoring_guide.md`) trong bản lưu trữ không chính
> thức https://github.com/win4r/MuseAI-Skills
> (`opt/hatch/skills/skill-creator/`, HEAD 6c12bde, 26/11/2026).
> Repo nguồn KHÔNG CÓ LICENSE và là snapshot skill hệ thống của Muse — skill
> này viết lại hoàn toàn bằng lời của mình, KHÔNG chép nguyên văn.
>
> Vị trí: skill này là **checklist review**, dùng sau khi đã viết skill.
> Việc tạo/sửa skill vẫn theo skill `skill-creator` local đã có trong
> `~/workspace/custom-skills/skill-creator/` — không cài đè, không trùng.

## Mục đích

Một skill tốt là skill dễ kích hoạt, gọn để nạp, và chạy đúng ngay lần đầu.
Review này bắt lỗi trước khi skill vào thư viện: trigger mơ hồ, scope lan
man, SKILL.md dài dòng, lệnh sai đường dẫn, auth viết theo trí nhớ. Review
xong skill mới được push.

## Checklist review (12 điểm)

### 1. Trigger — description có rõ không
- [ ] Đọc description là biết skill làm gì và KHI NÀO dùng.
- [ ] Có cụm trigger cụ thể (từ Trí hay dùng, tên công việc, tình huống).
- [ ] Không có description chung chung kiểu "hỗ trợ nhiều việc".

### 2. Scope — một việc hẹp
- [ ] Một skill = một việc rõ ràng. Việc không liên quan đã tách skill riêng.
- [ ] Không có mục "tiện thể làm thêm" ngoài scope.

### 3. SKILL.md gọn — chỉ giữ lõi vận hành
- [ ] Body nói "làm gì tiếp theo", không giải thích cả lĩnh vực.
- [ ] Tài liệu cồng kềnh (API doc dài, schema, tutorial) đã dồn vào
  `references/` và chỉ nạp khi cần (lazy-load), không nhồi vào SKILL.md.
- [ ] Template/output mẫu chỉ để trong `assets/` khi output cuối thực sự
  dùng tới.
- [ ] Không trùng lặp cùng một hướng dẫn ở cả SKILL.md và references.

### 4. Lệnh, đường dẫn, auth khớp runtime thật
- [ ] Mọi lệnh, path, file đều tồn tại thật trong môi trường (đã kiểm chứng
  bằng `ls`/chạy thử, không viết theo trí nhớ).
- [ ] Auth/flow theo đúng helper/connector thật đang có; không bịa binary,
  path hay flow xác thực.
- [ ] Helper nhị phân/script có sẵn được ưu tiên dùng thay cho hướng dẫn
  auth/protocol dài bằng prompt.
- [ ] Lỗi 401/403 được xử lý đúng: kiểm tra credential có gắn vào request
  chưa trước khi kết luận key sai.

### 5. Ví dụ và output
- [ ] Ví dụ ngắn, chạy được ngay, không phải đoạn văn dài.
- [ ] Output contract rõ: trả file gì, định dạng gì, đặt ở đâu.

### 6. Tên và trùng lặp
- [ ] Tên chưa trùng skill local (`~/workspace/custom-skills/`) và repo
  (`~/workspace/skill-library-repo/`).
- [ ] Không trùng scope với skill đã có — nếu trùng thì bổ sung/sửa skill
  cũ thay vì tạo skill mới.

## Quy trình review

1. Đọc SKILL.md cần review + chạy checklist 12 điểm, đánh dấu từng điểm
   pass/fail kèm dòng cụ thể vi phạm (số dòng, trích dẫn ngắn).
2. Chạy kiểm chứng kỹ thuật: mọi lệnh/path trong skill đều thử `ls` hoặc
   chạy khô; lệnh nào sai thì ghi rõ.
3. Viết báo cáo review: bảng điểm pass/fail, lỗi theo mức (chặn push /
   nên sửa / gợi ý), và bản sửa đề xuất cho từng lỗi (sửa trực tiếp vào
   SKILL.md nếu lỗi nhỏ và rõ ràng; lỗi lớn thì đề xuất, không tự viết lại
   toàn bộ).
4. Skill chỉ được push khi toàn bộ điểm "chặn push" đã pass. Điểm "nên sửa"
   có thể để lại kèm ghi chú trong báo cáo.

## Mức lỗi

- **Chặn push:** trigger mơ hồ, scope lan man, lệnh/path sai, auth bịa,
  trùng tên/trùng scope, chép nguyên văn nguồn có bản quyền.
- **Nên sửa:** SKILL.md dài dòng, ví dụ dài, thiếu output contract, thiếu
  credit nguồn.
- **Gợi ý:** cách diễn đạt gọn hơn, thêm trigger phrase.

## Output

- Báo cáo review (file `.md`): bảng checklist, lỗi + mức, bản sửa đề xuất.
- SKILL.md đã sửa (nếu lỗi nhỏ và đã áp dụng sửa trực tiếp).

## Nguồn

- Thiết kế workflow: skill `skill-creator` trong
  https://github.com/win4r/MuseAI-Skills (không license, snapshot skill hệ
  thống Muse, HEAD 6c12bde). Skill này chưng cất lại bằng lời của mình.
- Skill tạo/sửa skill trong môi trường Trí: `skill-creator` local
  (`~/workspace/custom-skills/skill-creator/`).
