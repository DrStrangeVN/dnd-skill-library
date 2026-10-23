---
name: marketing
description: Bộ lập chiến lược và vận hành marketing dùng cho kế hoạch, campaign, lịch content, nội dung social, quảng cáo, brief sáng tạo và báo cáo hiệu quả; không tự chạy quảng cáo hay đăng nội dung.
---

# Marketing

Nhận yêu cầu qua skill `marketing` được chọn bằng @ trong ChatGPT, bằng $ trong Codex, hoặc bằng yêu cầu tự nhiên như `marketing [mục] [yêu cầu]`. Viết tiếng Việt trừ khi người dùng chọn ngôn ngữ khác. Chỉ gọi tên bộ thì hiển thị các mục và ví dụ.

| Mục | Đầu ra | Ví dụ |
|---|---|---|
| plan | Kế hoạch marketing gắn mục tiêu kinh doanh, đối tượng, thông điệp, kênh, ngân sách, KPI | `marketing plan Kế hoạch 3 tháng cho học viện bóng rổ mới` |
| campaign | Kế hoạch một chiến dịch từ tiếp cận tới chuyển đổi và giữ chân | `marketing campaign Tuyển sinh lớp bóng rổ hè trong 4 tuần` |
| content | Trụ cột nội dung và lịch xuất bản có mục tiêu, định dạng, CTA | `marketing content Lịch Facebook 14 ngày cho câu lạc bộ` |
| social | Bài đăng, caption hoặc kịch bản video theo kênh và giọng thương hiệu | `marketing social Viết bài giới thiệu buổi tập thử` |
| ads | Brief và phương án thử nghiệm quảng cáo, phân bổ ngân sách dự kiến | `marketing ads Kế hoạch thử nghiệm với ngân sách 5 triệu đồng` |
| brief | Brief cho designer, video hoặc đội triển khai | `marketing brief Brief poster tuyển thành viên đội bóng` |
| audit | Đánh giá dữ liệu/tài sản được cung cấp và xếp thứ tự cải thiện | `marketing audit Đánh giá nội dung fanpage từ các bài sau: …` |
| report | Báo cáo hiệu quả có đối chiếu mục tiêu và hành động tiếp theo | `marketing report Phân tích kết quả chiến dịch từ bảng sau: …` |

## Thực hiện

Lấy từ ngữ cảnh: sản phẩm/dịch vụ, đối tượng, địa bàn, mục tiêu, thời gian, ngân sách, kênh và nguồn lực. Chỉ hỏi các khoảng trống có ảnh hưởng lớn; với bản nháp, ghi rõ giả định và dùng chúng nhất quán. Không tự mặc định doanh nghiệp là đội bóng chỉ vì bộ basketball cũng được cài.

- Plan/campaign: nối mục tiêu → đối tượng → thông điệp → kênh → hoạt động → KPI. Bảng triển khai gồm việc, thời điểm, vai trò phụ trách, chi phí dự kiến, chỉ số và cách đo. Chỉ chọn kênh phù hợp nguồn lực.
- Content/social: mỗi nội dung có người đọc, mục tiêu, ý chính, mở bài và CTA phù hợp. Phân biệt đề xuất chủ đề với bài viết hoàn chỉnh; theo đúng số lượng được yêu cầu. Không bịa testimonial, ưu đãi, thành tích hoặc thông tin sản phẩm.
- Ads: tách sản xuất, media, phí và dự phòng khi áp dụng; tổng phân bổ phải khớp ngân sách. Nêu giả thuyết, biến thử, cách đánh giá và ngưỡng dừng/điều chỉnh đề xuất. Không cam kết kết quả hoặc coi benchmark là dữ liệu thật.
- Brief: mục tiêu, đối tượng, thông điệp chính, tài sản đầu vào, hạng mục bàn giao và tiêu chí duyệt; chỉ dùng thông số nền tảng hiện hành khi đã xác minh hoặc được cung cấp.
- Audit/report: ghi kỳ, nguồn, giới hạn dữ liệu và định nghĩa chỉ số. Tách paid/organic khi có dữ liệu; không cộng reach độc nhất giữa nền tảng. CTR = click/impression; CPC = chi phí/click; CPL = chi phí/lead; ROAS = doanh thu quy cho ads/chi phí ads. Nêu loại click, cửa sổ ghi nhận và nguồn doanh thu; mẫu số 0/thiếu trả “N/A”, không suy ra 0. ROAS không phải lợi nhuận.

Tra cứu nguồn hiện hành khi cần thị trường, đối thủ, benchmark, quy định hay thông số nền tảng; nếu không truy cập được, nêu phần chưa xác minh. Kết luận từ dữ liệu hạn chế phải được ghi là giả thuyết.

## Tài sản và thực thi

Dùng các skill Canva, imagegen, presentations, spreadsheets hoặc Sites đang khả dụng khi người dùng cần tài sản tương ứng; đọc skill trước khi áp dụng. Không gọi công cụ thiết kế chỉ để lập kế hoạch bằng văn bản. Không tự đăng bài, gửi đối tác hoặc khởi chạy quảng cáo từ yêu cầu soạn kế hoạch. Nếu được yêu cầu thực thi, thực hiện đúng phạm vi và quyền truy cập hiện có.

## Plugin độc lập

Plugin này chỉ chứa skill hiện tại. Khi được chọn, xử lý yêu cầu trực tiếp; không yêu cầu người dùng chọn Steven Toolkit. Các skill và công cụ được nhắc đến ở trên là tùy chọn: chỉ nạp nếu thực sự có trong phiên, không đọc đường dẫn skill ngang hàng hoặc giả định plugin khác đã cài. Nếu không có skill phụ trợ, tự hoàn thành nội dung theo quy trình ở đây; nếu thiếu công cụ tạo file/dịch vụ, trả nội dung dùng ngay và nói rõ giới hạn thực thi.
