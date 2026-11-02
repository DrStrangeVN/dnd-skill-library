---
name: podcastify-guide
description: Guide for the "Podcastify" label shown in the Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA". The video gives no repo or product link, and no matching repo was verified, so this skill does not install or endorse any product called Podcastify. Use when the user asks about Podcastify or turning a document into a podcast episode, to route to verified alternatives instead of guessing a repo.
---

# Podcastify — hướng dẫn (CHƯA XÁC ĐỊNH ĐƯỢC SẢN PHẨM)

## Trạng thái xác minh (kiểm tra 02/11/2026)

- **Chưa xác định được repo hay sản phẩm đúng.** Video chỉ hiển thị tên "Podcastify" ở giai đoạn "MỘT NGUỒN NHIỀU KÊNH", kèm hình một tài liệu ở giữa có biểu tượng micro. Không có link GitHub, tên repo, hay URL sản phẩm nào trong video, mô tả, hay bình luận.
- Tìm kiếm theo tên này cho ra nhiều sản phẩm khác nhau cùng tên, không có sản phẩm nào khớp chắc chắn với mô tả trong video. **Không cài đặt bất cứ thứ gì chỉ vì nó tên Podcastify.** Cài theo tên đoán mò là cách cài nhầm đã được ghi nhận trong vụ việc này.
- Nếu Trí gửi link repo/sản phẩm cụ thể, xác minh lại từ link đó rồi mới quyết định cài hay dựng skill riêng.

## Chức năng video gợi ý — chỉ ở mức suy đoán có ghi rõ

Từ hình ảnh trong video, khâu này có vẻ là: lấy một nguồn (tài liệu/bài viết) làm đầu vào, chuyển thành tập podcast (âm thanh có người dẫn). Đây là suy đoán từ hình ảnh, không phải xác nhận của tác giả video.

## Dùng giải pháp đã có thay thế

Khi Trí muốn chuyển tài liệu/bài viết thành podcast, dùng các skill đã có và đã kiểm chứng trong thư viện, thay vì tìm sản phẩm chưa rõ:

- `generate_podcast` (skill hệ thống): nghiên cứu, viết kịch bản, sản xuất tập podcast có một hoặc nhiều giọng, giao/sắp lịch trong phạm vi đã duyệt.
- `blog-audio`: đọc bài blog bằng giọng TTS của Gemini, dùng khi nguồn là bài blog.
- `spoken_audio` (skill hệ thống): đọc văn bản thành giọng nói, dùng khi chỉ cần file âm thanh đọc nguyên văn.
- Giọng đọc tiếng Việt sản xuất của Trí vẫn là VieNeu Studio API; các skill trên không thay quy tắc đó khi làm nội dung cho kênh của Trí.

## Quy tắc áp dụng

- Mọi tập podcast đăng công khai vẫn cần Trí duyệt từng lần (fresh approval), trừ khi thuộc ngoại lệ tự đăng duy nhất đã chốt cho kênh Học Bóng Rổ — kênh podcast không thuộc ngoại lệ đó.
- Không ghi key, token, hay thông tin đăng nhập của bất kỳ dịch vụ "Podcastify" nào vào file skill, memory hay repo khi chưa xác minh được dịch vụ đó.
- Khi có link xác thực, cập nhật skill này: ghi repo, giấy phép, yêu cầu key, và đổi trạng thái từ "chưa xác định" sang "đã xác minh" kèm ngày kiểm tra.
