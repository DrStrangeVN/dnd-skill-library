---
name: social-media-agent-guide
description: Guide for the "Social Media Agent" label shown in the Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA". The video gives no repo or product link, and no matching repo was verified, so this skill does not install or endorse any product called Social Media Agent. Use when the user asks about a social media agent, multi-channel posting from one source, or scheduling to X/LinkedIn, to route to verified skills instead of guessing a repo.
---

# Social Media Agent — hướng dẫn (CHƯA XÁC ĐỊNH ĐƯỢC SẢN PHẨM)

## Trạng thái xác minh (kiểm tra 02/11/2026)

- **Chưa xác định được repo hay sản phẩm đúng.** Video chỉ hiển thị tên "Social Media Agent" ở giai đoạn "MỘT NGUỒN NHIỀU KÊNH", kèm hình một bài viết mẫu tại `example.org/bai-viet` (link placeholder, không phải URL thật), chữ "Bản nhập" và các nhãn "X / Lịch / LinkedIn". Không có link GitHub, tên repo, hay URL sản phẩm nào trong video, mô tả, hay bình luận.
- Tìm kiếm theo tên này cho ra nhiều sản phẩm/agent khác nhau cùng tên, không có sản phẩm nào khớp chắc chắn với mô tả trong video. **Không cài đặt bất cứ thứ gì chỉ vì nó tên Social Media Agent.**
- Nếu Trí gửi link repo/sản phẩm cụ thể, xác minh lại từ link đó rồi mới quyết định cài hay dựng skill riêng.

## Chức năng video gợi ý — chỉ ở mức suy đoán có ghi rõ

Từ hình ảnh trong video, khâu này có vẻ là: lấy một nguồn nội dung, soạn bản đăng, rồi đăng/lên lịch lên nhiều kênh (X, LinkedIn, và các kênh khác). Đây là suy đoán từ hình ảnh, không phải xác nhận của tác giả video.

## Dùng giải pháp đã có thay thế

Khi Trí muốn soạn và đăng/lên lịch nội dung đa kênh, dùng các skill đã có và đã kiểm chứng trong thư viện, thay vì tìm sản phẩm chưa rõ:

- `social-publishing` (skill hệ thống): lập kế hoạch, tạo và đăng/lên lịch bài đăng mạng xã hội sau khi Trí duyệt đúng nội dung và media, rồi kiểm chứng từng bài đã đăng.
- `content-repurposing` (ScrapeCreators, cài 02/11/2026): chuyển video/bản ghi/bài đăng công khai thành tài sản tái dùng như bài LinkedIn, chuỗi X, kịch bản, bản tin. Lưu ý skill này cần key API ScrapeCreators (`SCRAPECREATORS_API_KEY`) mới chạy được.
- `blog-repurpose`: chuyển bài blog sang các nền tảng khác.
- `scheduling` (skill hệ thống): tìm giờ chung và đặt lịch/lên lịch khi cần phối hợp nhiều người.

## Quy tắc áp dụng — bắt buộc

- Mọi bài đăng công khai đều cần Trí duyệt từng lần (fresh approval). Ngoại lệ tự đăng duy nhất đã chốt chỉ áp cho tài khoản riêng của kênh Học Bóng Rổ; không mở rộng sang X, LinkedIn, hay kênh khác qua skill này.
- Trước khi đăng/lên lịch qua bất kỳ công cụ nào, kiểm tra đúng tài khoản/kênh và đúng identity (quy tắc Facebook identity vẫn áp dụng cho Facebook; tương tự kiểm tra tài khoản cho X/LinkedIn).
- Không ghi key, token, hay thông tin đăng nhập của bất kỳ dịch vụ "Social Media Agent" nào vào file skill, memory hay repo khi chưa xác minh được dịch vụ đó.
- Khi có link xác thực, cập nhật skill này: ghi repo, giấy phép, yêu cầu key, và đổi trạng thái từ "chưa xác định" sang "đã xác minh" kèm ngày kiểm tra.
