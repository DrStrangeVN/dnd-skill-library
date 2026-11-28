---
name: wide-research-coordinator
description: Điều phối nghiên cứu song song trên nhiều input độc lập — một manager subagent fan-out cùng một nhiệm vụ qua nhiều mục, trả về một tập kết quả chuẩn hóa kèm báo cáo coverage. Dùng khi cần khảo sát hàng loạt: đối thủ, thị trường, nguồn skill, video mẫu, nền tảng, sản phẩm.
---

# Wide Research Coordinator

> Chưng cất từ thiết kế workflow của skill `wide-research` trong bản lưu trữ
> không chính thức https://github.com/win4r/MuseAI-Skills
> (`opt/hatch/skills/wide-research/SKILL.md`, HEAD 6c12bde, 26/11/2026).
> Repo nguồn KHÔNG CÓ LICENSE và là snapshot skill hệ thống của Muse — skill
> này viết lại hoàn toàn bằng lời của mình, KHÔNG chép nguyên văn.

## Mục đích

Một nghiên cứu "rộng" là nhiều nghiên cứu nhỏ giống nhau chạy song song: mỗi
input độc lập, cùng một bộ câu hỏi, cùng một định dạng trả lời. Thay vì làm
tuần tự từng mục (chậm) hoặc giao lung tung (kết quả lệch nhau), skill này
đặt một manager điều phối: chia việc, chuẩn hóa đầu ra, báo cáo bao nhiêu mục
xong / bao nhiêu mục lỗi.

## Khi nào dùng / không dùng

Dùng khi:
- Nhiệm vụ tách được thành nhiều mục độc lập (mỗi công ty / người / chủ đề /
  nguồn là một mục), mỗi mục trả về cùng một bộ trường.
- Số mục từ 3 trở lên; càng nhiều mục càng đáng dùng.
- Trí nói "khảo sát hàng loạt", "so sánh nhiều bên", "nghiên cứu song song".

Không dùng khi:
- Chỉ có 1 mục duy nhất — làm trực tiếp, không cần điều phối.
- Các mục phụ thuộc lẫn nhau (kết quả mục sau cần kết quả mục trước).

## Hợp đồng đầu vào (đưa cho manager subagent)

- `operation_brief`: một câu mô tả nhiệm vụ (ngắn, rõ).
- `inputs`: danh sách mục, mỗi mục độc lập, đã khử trùng lặp và chuẩn hóa
  (tên, link, định danh chính xác — không để 2 mục trùng nhau dưới 2 tên).
- `output_schema`: các trường bắt buộc + kiểu dữ liệu cho mỗi mục. Giữ tối
  thiểu và rõ ràng; tránh trường tự do trừ khi Trí yêu cầu.
- `worker_prompt_template`: hướng dẫn cho worker xử lý một mục (nguồn nào
  được dùng, kiểm chứng ra sao, không được đoán).
- `completion_format`: hình dạng JSON cuối cùng manager phải trả.

## Hợp đồng đầu ra (manager phải trả)

- `total`: tổng số mục.
- `success_count` / `failure_count`.
- `results`: kết quả từng mục theo đúng `output_schema`.
- `failures`: mục lỗi + lý do lỗi (nguồn không mở được, không có dữ liệu...).
- `notes`: ghi chú (nguồn nào yếu, số liệu nào chưa kiểm chứng).

## Quy tắc vận hành

1. Khử trùng lặp và chuẩn hóa danh sách input trước khi giao cho manager.
2. Chỉ dùng ĐÚNG MỘT manager subagent cho một mục tiêu của Trí; không fan-out
   nhiều root-level subagent song song (manager tự chia worker bên trong).
3. Manager giao một worker cho một input; mỗi worker chỉ làm mục của mình.
4. Giữ output schema tối thiểu, rõ ràng; không thêm trường tự do.
5. Nếu cần đủ số lượng và có mục lỗi: chỉ retry các mục lỗi, tối đa 1 lần.
6. Báo Trí ngay khi nghiên cứu bắt đầu (đang chạy, chưa cần chờ kết quả).
7. Khi trả kết quả cuối: LUÔN báo coverage (`success_count/total`) và các
   khoảng trống chưa xong. Không giấu mục lỗi.
8. Kết quả từng mục phải ghi nguồn (link/file) — mục nào không có nguồn thì
   ghi rõ "chưa kiểm chứng", không đoán là đúng.

## Output

- Báo cáo tổng hợp (file `.md`): bảng kết quả theo schema, coverage, mục lỗi
  + lý do, nguồn từng mục.
- File dữ liệu thô (JSON theo `completion_format`) để dùng lại cho lần sau.

## Giới hạn

- Manager không tự quyết thay Trí: kết quả nghiên cứu là đầu vào để Trí
  quyết, không phải quyết định.
- Không dùng kết quả nghiên cứu cũ để kết luận trạng thái live hiện tại
  (giá, slot, số liệu kênh) — tra cứu live đi luồng riêng.
- Worker không được bịa số liệu khi nguồn không có: ghi "không có dữ liệu".

## Nguồn

- Thiết kế workflow: skill `wide-research` trong
  https://github.com/win4r/MuseAI-Skills (không license, snapshot skill hệ
  thống Muse, HEAD 6c12bde). Skill này chưng cất lại bằng lời của mình.
