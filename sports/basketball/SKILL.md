---
name: basketball
description: Bộ quản lý đội, câu lạc bộ hoặc học viện bóng rổ dùng cho roster, lịch tập, vận hành trận đấu và giải, ngân sách, tuyển thành viên, tài trợ và báo cáo mùa; không thay thế chuyên môn y tế.
---

# Quản lý bóng rổ

Nhận yêu cầu qua skill `basketball` được chọn bằng @ trong ChatGPT, bằng $ trong Codex, hoặc bằng yêu cầu tự nhiên như `basketball [mục] [yêu cầu]`. Mặc định tiếng Việt. Chỉ gọi tên bộ thì hiển thị bảng mục và ví dụ; không tự lập cả mùa giải.

| Mục | Đầu ra | Ví dụ |
|---|---|---|
| season | Kế hoạch mùa giải với mục tiêu, mốc, nhân sự, nguồn lực và KPI | `basketball season Lập kế hoạch mùa 3 tháng cho đội phong trào` |
| roster | Bảng cầu thủ và tình trạng đăng ký/tham gia | `basketball roster Tạo mẫu quản lý 15 cầu thủ` |
| training | Lịch tập, điểm danh và phối hợp huấn luyện viên | `basketball training Lịch 2 buổi mỗi tuần trong 8 tuần` |
| gameday | Checklist trước–trong–sau trận và phân công vận hành | `basketball gameday Checklist cho trận giao hữu sân nhà` |
| tournament | Phương án vận hành giải, thể thức và lịch đấu dự kiến | `basketball tournament Lên phương án giải 8 đội trong 2 ngày` |
| budget | Ngân sách, thu chi, phí thành viên và tình trạng thanh toán | `basketball budget Dự toán mùa giải cho 15 cầu thủ` |
| recruit | Quy trình tuyển thành viên, đăng ký và tổ chức tryout | `basketball recruit Kế hoạch tuyển cầu thủ cho đội U18` |
| sponsor | Đề xuất tài trợ, bảng quyền lợi và theo dõi thực hiện | `basketball sponsor Xây gói tài trợ cho mùa giải mới` |
| report | Báo cáo hoạt động, tài chính, thành tích và việc cần xử lý | `basketball report Tổng kết tháng từ số liệu sau: …` |

## Xác định bối cảnh

Phân biệt đội phong trào, đội thi đấu, học viện và đơn vị tổ chức giải. Dùng thông tin đã có về độ tuổi, số người/đội, địa điểm, thời gian, sân, ban huấn luyện, ngân sách và giải tham dự. Nếu thiếu điểm quyết định tính khả thi, hỏi ngắn gọn; vẫn tạo khung có thể điền. Đánh dấu mọi giả định; không bịa tên cầu thủ, lịch sân, thành tích, hợp đồng, hạn đăng ký hoặc điều lệ.

## Quy trình theo mục

- **Season:** xác định mục tiêu chuyên môn và vận hành riêng; phân giai đoạn, mốc đăng ký, lịch tập/thi đấu dự kiến, người phụ trách và phụ thuộc. Tránh đặt mục tiêu vô địch như cam kết kết quả.
- **Roster:** mã cầu thủ, tên, nhóm tuổi khi cần, vị trí tự khai/HLV xác nhận, số áo, tình trạng tham gia, đăng ký và liên hệ nếu cần cho công việc. Không thu thập số giấy tờ hoặc hồ sơ sức khỏe chi tiết mặc định. Trạng thái đủ điều kiện thi đấu phải dựa trên điều lệ và hồ sơ xác minh.
- **Training:** ngày/giờ, sân, mục tiêu buổi, HLV, số lượng dự kiến, điểm danh và phương án khi sân không khả dụng. Tổng thời lượng các phần phải khớp buổi. Giáo án chuyên môn là đề xuất để HLV điều chỉnh theo độ tuổi/trình độ; không tự chẩn đoán hay quyết định trở lại thi đấu sau chấn thương.
- **Gameday:** lịch tập trung, di chuyển, sân, trang phục, danh sách đăng ký, trọng tài/bàn thư ký theo phạm vi, thiết bị, đầu mối hỗ trợ khẩn cấp, truyền thông và quyết toán. Mỗi việc có mốc, vai trò và trạng thái; thông tin chưa xác nhận đánh dấu rõ.
- **Tournament:** xác nhận số sân, khung giờ, thể thức, thời lượng một slot gồm cả chuyển sân/nghỉ và yêu cầu thời gian nghỉ giữa trận. Tính số trận theo thể thức, kiểm tra trùng đội/trùng sân, trận phụ thuộc kết quả và tổng công suất sân. Nếu không đủ thời gian, đưa lựa chọn điều chỉnh; không xuất lịch bất khả thi. Luật, giới hạn tuổi, roster và xếp hạng phải đối chiếu điều lệ giải hiện hành; không mặc định mọi giải dùng nguyên luật FIBA hoặc NBA.
- **Budget:** tách dự toán/thực tế, thu/chi, phải thu/đã thu, phải trả/đã trả và tài trợ tiền mặt/hiện vật. Có số lượng, đơn giá, thành tiền, kỳ và tiền tệ; số dư tiền = đầu kỳ + thực thu − thực chi. Không cộng hiện vật vào tiền mặt; đánh dấu báo giá chưa xác minh.
- **Recruit:** tiêu chí phù hợp trình độ/mục tiêu đội, lịch tryout dự kiến, người đánh giá, thang đánh giá và quy trình thông báo. Với đội trẻ, đưa phần liên hệ/đồng ý của phụ huynh vào quy trình khi phù hợp; không công khai danh sách trẻ và liên hệ mặc định.
- **Sponsor:** phân biệt quyền lợi đề xuất và quyền đã được phép cung cấp; ghi hạng mục, số lượng, thời điểm, cách chứng minh bàn giao, chi phí và người phụ trách. Không bịa reach hoặc doanh thu; không hứa độc quyền nếu chưa xác minh. Theo dõi thực hiện quyền lợi tách khỏi thanh toán.
- **Report:** ghi kỳ, nguồn, kết quả tập luyện/thi đấu, điểm danh, tài chính, vấn đề và quyết định cần có. Thống kê thiếu mẫu số hoặc phút thi đấu không dùng để so sánh cầu thủ như kết luận chắc chắn.

## Công cụ và đầu ra

Mặc định cung cấp bảng/checklist dùng ngay. Khi cần file Excel, Word, PDF hoặc slide, dùng skill tạo file tương ứng đang có; khi cần nội dung tuyển sinh/truyền thông, dùng skill `marketing` nếu khả dụng. Đọc skill liên quan trước khi dùng. Chỉ cập nhật dữ liệu đội ở hệ thống ngoài hoặc gửi thông báo khi người dùng yêu cầu trong phạm vi cụ thể.

## Plugin độc lập

Plugin này chỉ chứa skill hiện tại. Khi được chọn, xử lý yêu cầu trực tiếp; không yêu cầu người dùng chọn Steven Toolkit. Các skill và công cụ được nhắc đến ở trên là tùy chọn: chỉ nạp nếu thực sự có trong phiên, không đọc đường dẫn skill ngang hàng hoặc giả định plugin khác đã cài. Nếu không có skill phụ trợ, tự hoàn thành nội dung theo quy trình ở đây; nếu thiếu công cụ tạo file/dịch vụ, trả nội dung dùng ngay và nói rõ giới hạn thực thi.
