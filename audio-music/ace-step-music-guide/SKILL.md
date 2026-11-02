---
name: ace-step-music-guide
description: Guide to ACE-Step, the music generation foundation model shown as ACE-Step 1.5 in the Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA". Use when the user asks about ACE-Step, ACE-Step 1.5, or generating background music locally with ACE-Step. Use the official ace-step/ACE-Step repo only; unofficial forks are not a source for this guide.
---

# ACE-Step — hướng dẫn tạo nhạc

## Nguồn đã xác minh (kiểm tra 02/11/2026)

- Repo chính thức: `ace-step/ACE-Step`, giấy phép Apache-2.0, khoảng 5.013 sao. Dự án do ACE Studio và StepFun đồng dẫn dắt, theo README.
- Bản v1.5 được công bố ngày 28/01/2026, theo mục News trong README chính thức.
- Trong video, tên "ACE-Step 1.5" xuất hiện ở giai đoạn "TỪ SCRIPT THÀNH MEDIA" mà không có nhãn phụ đọc được rõ. Video không cho link repo; repo trên được xác định bằng tìm kiếm theo tên và đối chiếu với README chính thức.
- Cảnh báo: có nhiều repo fork/clone cùng tên ACE-Step 1.5 với giấy phép ghi khác nhau. Chỉ dùng repo chính thức `ace-step/ACE-Step` và trang dự án chính thức của nó. README chính thức cảnh báo về tên miền giả mạo; không tải model từ trang không thuộc dự án.

## Model làm gì

ACE-Step là model nền tạo nhạc mã nguồn mở, tạo nhạc từ văn bản và các điều khiển khác, có căn lời bài hát, cấu trúc, và khả năng chỉnh sửa/remix theo README. README tuyên bố model tạo được tới 4 phút nhạc trong 20 giây trên GPU A100 — đó là tuyên bố của dự án, chưa đo trên máy Trí.

## Khi nào dùng, khi nào không

- Dùng khi cần nhạc nền tự tạo cho video, thay cho nhạc có bản quyền chưa rõ phép. Ưu tiên nhạc không lời cho nền video, đúng chuẩn các kênh của Trí (nhạc nền nhẹ, dưới giọng đọc, target −14 LUFS ở khâu hậu kỳ).
- Không dùng nhạc có lời do model tự sinh lời mà chưa nghe kiểm tra: lời có thể vô nghĩa, sai ngôn ngữ, hoặc trùng phong cách gây rủi ro bản quyền. README chính thức cũng cảnh báo nguy cơ vi phạm bản quyền ngoài ý muốn do tương đồng phong cách.
- Không dùng ACE-Step để thay giọng đọc. Giọng đọc sản xuất tiếng Việt của Trí là VieNeu Studio API; nhạc và giọng đọc là hai khâu riêng.
- Không dùng bản nhạc AI tạo ra rồi ghi là nhạc của nghệ sĩ thật, và không dùng cho mục đích lừa dối nguồn gốc.

## Cách dùng (chưa cài thử trên máy này)

Đọc README của repo chính thức trước khi cài: mục Installation, Usage và User Interface Guide. Skill này không chép lại lệnh cài/chạy vì yêu cầu phần cứng (GPU), phiên bản model (v1, v1.5, các bản 3.5B) và giao diện có thể đổi theo bản phát hành. Các điểm cần xác nhận khi đọc README:

- GPU/VRAM cần thiết và bản model nào chạy được trên máy Trí.
- Cách nhập prompt phong cách/tempo, lời (nếu có), độ dài, và cách xuất file âm thanh.
- Giấy phép của đúng bản model đang dùng và điều khoản dùng đầu ra cho mục đích thương mại.

Nghe kiểm tra mọi bản nhạc trước khi đưa vào video, và giữ lại prompt + bản model đã dùng để truy vết khi cần.
