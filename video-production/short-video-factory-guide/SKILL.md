---
name: short-video-factory-guide
description: Guide to Short Video Factory (AI Short Video Factory), the desktop short-video app shown in the Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA". Use when the user asks about Short Video Factory, one-click AI short-video generation, or batch auto-editing of product/marketing shorts. This is a guide skill only; the app itself is not installed here and its code was not copied into the skill library.
---

# Short Video Factory — hướng dẫn

## Nguồn đã xác minh (kiểm tra 02/11/2026)

- Repo: `YILS-LIN/short-video-factory`, giấy phép AGPL-3.0, khoảng 6.009 sao, đẩy lần cuối 02/11/2026.
- Đây là một ứng dụng desktop hoàn chỉnh, KHÔNG phải skill. Không đổ code của ứng dụng vào thư viện skill.
- Trong video, tên này xuất hiện ở giai đoạn "DỰNG VIDEO CẮT SHORTS". Video không cho link repo; repo trên được xác định bằng tìm kiếm theo tên và đối chiếu mô tả.
- README gốc viết bằng tiếng Trung, có bản tiếng Anh tại `README.en.md`.

## Ứng dụng làm gì

Ứng dụng desktop tạo video ngắn từ prompt văn bản cộng nguồn hình/video theo kịch bản, tích hợp tạo văn bản bằng AI, tổng hợp giọng nói, cắt ghép video và hiệu ứng phụ đề, hướng tới video marketing sản phẩm và nội dung chung, xử lý hàng loạt. README nêu hỗ trợ tạo kịch bản qua API tương thích OpenAI và ghi nhận edge-tts trong danh mục cảm ơn.

## Khi nào dùng, khi nào không

- Dùng khi Trí muốn thử một công cụ desktop tạo nhanh video ngắn marketing, ngoài pipeline Remotion/VieNeu đang chạy.
- Không dùng thay cho pipeline video đang chạy của Trí (Học Bóng Rổ, Chuyện Ngày Xưa, AI 60 Giây, NGẦM ĐỜI): các kênh này có chuẩn riêng đã chốt (độ dài, giọng VieNeu API, phong cách hình ảnh, kiểm tra trùng lặp trước khi xếp lịch). Video do ứng dụng này tạo ra vẫn phải qua QA và duyệt như mọi video khác, và vẫn tuân thủ quy tắc kiểm tra trùng lặp trước khi xếp lịch (`recut_overlap_replace_guard`).
- Không dùng giọng của ứng dụng này rồi gọi là "Nam - Nhật Phong". Giọng sản xuất tiếng Việt của Trí là giọng VieNeu Studio API.

## Cách dùng (chưa cài thử trên máy này)

Đọc mục "Getting Started" trong `README.en.md` của repo trước khi cài; skill này không chép lại hướng dẫn cài đặt vì hướng dẫn có thể đổi theo bản phát hành. Các điểm cần xác nhận khi đọc README:

- Hệ điều hành và bản phát hành desktop nào được hỗ trợ, tải ở đâu.
- Nhà cung cấp mô hình / giọng nói nào cần cấu hình, key lấy ở đâu, chi phí ra sao.
- Định dạng đầu vào (prompt + nguồn hình/video) và đầu ra (tỉ lệ, độ phân giải, phụ đề) có khớp chuẩn dọc 9:16 của Trí không.

## Giới hạn cần kiểm chứng trước khi dùng

- Chưa cài, chưa chạy thử, chưa đo chất lượng đầu ra. Không có căn cứ để khẳng định ứng dụng này tốt hơn pipeline hiện tại.
- Giấy phép AGPL-3.0 là giấy phép copyleft mạnh: nếu sửa đổi và phân phối/chạy dịch vụ từ code này thì nghĩa vụ công bố nguồn có thể phát sinh. Chỉ dùng bản phát hành nguyên trạng thì ít rủi ro hơn, nhưng vẫn đọc LICENSE trước khi dùng cho công việc thương mại.
- Ứng dụng cần key API của nhà cung cấp mô hình/giọng nói bên ngoài (theo README). Key không ghi vào file skill, memory hay repo.
- Giao diện và tài liệu ưu tiên tiếng Trung; bản tiếng Anh có thể không đầy đủ bằng bản gốc.
