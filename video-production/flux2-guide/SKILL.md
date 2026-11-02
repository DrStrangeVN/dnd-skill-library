---
name: flux2-guide
description: Guide to FLUX.2, the Black Forest Labs image model shown in the Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA" for thumbnails and banners. Use when the user asks about FLUX.2, FLUX.2 dev/klein/pro/flex/max, or generating and editing images with FLUX.2. For the existing video-frame workflow, prefer the flux-image-gen skill; this guide covers choosing a FLUX.2 variant and its license.
---

# FLUX.2 — hướng dẫn

## Nguồn đã xác minh (kiểm tra 02/11/2026)

- Repo mã suy luận: `black-forest-labs/flux2`, giấy phép Apache-2.0 cho repo; nhà phát triển: Black Forest Labs (BFL).
- Ra mắt: FLUX.2 [dev] ngày 25/11/2025; họ FLUX.2 [klein] ngày 15/01/2026.
- Trong video, tên "FLUX.2" xuất hiện ở giai đoạn "TỪ SCRIPT THÀNH MEDIA" với nhãn phụ "Thumbnail / banner". Video không cho link repo hay bản model nào; các bản dưới đây lấy từ README của repo chính thức.

## Các bản và giấy phép — đọc kỹ trước khi dùng cho việc thương mại

Giấy phép khác nhau theo bản, kể cả trong cùng một họ. Bảng dưới đây chép từ README của repo `black-forest-labs/flux2`:

| Bản | Tham số | Giấy phép model |
|---|---|---|
| FLUX.2 [klein] 4B (đã chưng cất) | 4B | Apache-2.0 |
| FLUX.2 [klein] 4B Base | 4B | Apache-2.0 |
| FLUX.2 [klein] 9B | 9B | FLUX Non-Commercial License |
| FLUX.2 [klein] 9B KV | 9B | FLUX Non-Commercial License |
| FLUX.2 [klein] 9B Base | 9B | FLUX Non-Commercial License |
| FLUX.2 [dev] | 32B | FLUX Non-Commercial License |

- Chỉ bản klein 4B là Apache-2.0 và dùng thương mại được theo giấy phép đó. Các bản 9B và [dev] dùng giấy phép phi thương mại; dùng cho công việc kinh doanh cần giấy phép thương mại riêng từ BFL.
- Các tầng [pro], [flex], [max] chỉ dùng qua API của BFL, trả phí theo ảnh, không có trọng số mở. Đọc tài liệu API tại `docs.bfl.ai` trước khi dùng.
- Tất cả các bản mở trên đều hỗ trợ tạo ảnh từ văn bản và sửa ảnh theo 1 ảnh tham chiếu hoặc nhiều ảnh tham chiếu, theo README. Họ klein được thiết kế cho tạo/sửa nhanh, chạy được trên GPU tiêu dùng (README nêu ví dụ RTX 3090/4070 cho klein 4B).

## Khi nào dùng, khi nào không

- Dùng khi cần ảnh thumbnail/banner hoặc ảnh tham chiếu cho video, và đã chọn đúng bản theo giấy phép ở trên.
- Workflow khung hình video đang có của Trí nằm ở skill `flux-image-gen` (ràng buộc độ phân giải, chiến lược batch, tính nhất quán). Ưu tiên đọc skill đó khi làm khung hình video; skill này chỉ bổ sung phần chọn bản FLUX.2 và giấy phép. Không chép đè các ràng buộc của `flux-image-gen` bằng suy đoán về FLUX.2.
- Chữ tiếng Việt trong ảnh AI thường sai dấu. Chữ lớn tiếng Việt trong video của Trí dùng font Be Vietnam Pro Black theo quy tắc đã chốt trên máy này; với ảnh do FLUX.2 tạo, kiểm tra dấu tiếng Việt bằng mắt trước khi dùng, và đừng tin ảnh AI viết đúng chữ tiếng Việt khi chưa xem.
- Kiểm tra quyền sử dụng đầu ra cho mục đích cụ thể trong giấy phép của đúng bản đang dùng; tóm tắt này không phải tư vấn pháp lý.

## Cách dùng

Repo `black-forest-labs/flux2` chứa mã suy luận tối thiểu cho các bản trọng số mở. Cách chạy chi tiết, yêu cầu phần cứng và mã mẫu nằm trong README của repo và model card trên Hugging Face của từng bản (`black-forest-labs/FLUX.2-klein-4B`, `FLUX.2-klein-9B`, `FLUX.2-dev`). Skill này không chép lại mã suy luận vì mã và yêu cầu có thể đổi theo bản phát hành; đọc README/model card của bản đang dùng trước khi chạy.
