# Demo wide-research-coordinator — So sánh 3 nền tảng bán vé cho Danang Dragons

Ngày: 28/11/2026. Skill: `wide-research-coordinator` (mới chưng cất, chưa push).
Nhiệm vụ demo: so sánh 3 nền tảng bán vé ngày thi đấu (Ticketbox, TicketGo,
Eventbrite) theo cùng một output schema, qua 1 manager + 3 worker song song
(mỗi worker 1 nền tảng, chỉ dùng nguồn công khai).

## Coverage: 3/3 — 100%, 0 failure, 0 retry

| Mục | Trạng thái | Ghi chú |
|---|---|---|
| Ticketbox | ✅ success | fee_model + payout: null (không công khai) |
| TicketGo | ✅ success | fee_model: chỉ có ước tính bên thứ ba, chưa xác nhận; payout: null |
| Eventbrite | ✅ success | Đủ trường; vn_support: không hỗ trợ VN |

Không có mục lỗi nên không cần retry (quy tắc retry tối đa 1 lần không kích
hoạt).

## Bảng kết quả (chuẩn hóa theo schema)

| Trường | Ticketbox | TicketGo | Eventbrite |
|---|---|---|---|
| Website | ticketbox.vn | ticketgo.vn | eventbrite.com |
| Phí BTC | Không công khai (null) | Không công khai; bên thứ ba ước 5–9%/vé, chưa xác nhận | 3,7% + 1,79 USD/vé + 2,9% xử lý (mức Mỹ); phí theo quốc gia |
| QR check-in | ✅ app Ticketbox Event Manager | ✅ QR qua email, dùng 1 lần | ✅ app Eventbrite Organizer |
| Sơ đồ chỗ ngồi | ✅ chọn ghế | ✅ chọn ghế theo hạng | ✅ reserved seating, giá theo khu |
| Hạng vé / mã giảm giá | ✅ nhiều hạng, mã giảm giá | ✅ nhiều hạng, mã khuyến mãi | ✅ nhiều loại vé, early-bird/VIP/nhóm |
| Bán vé tại cửa | Không ghi nhận | Vé cứng giao tận nhà / đổi tại quầy | ✅ bán tại cửa + Tap to Pay |
| Payout | Không công khai (null) | Không công khai (null) | Sau sự kiện 3 ngày + tối đa 5–7 ngày làm việc; giữ 20% dự phòng |
| Hỗ trợ VN | ✅ tiếng Việt, MoMo, thẻ Visa/Master/JCB; ZaloPay/VNPay chưa xác minh chính thức | ✅ song ngữ Việt/Anh; VietQR, MoMo, ZaloPay, ATM nội địa; hotline VN; có sự kiện tại Đà Nẵng | ❌ không tiếng Việt, không có VN trong danh sách payout; gợi ý PayPal |

## Khoảng trống chưa xong (failures: 0 mục lỗi, nhưng 3 trường null)

- Phí ban tổ chức của Ticketbox và TicketGo đều không công khai — cần liên
  hệ trực tiếp (TicketGo: 08.999.80.818) để báo giá, không dùng ước tính bên
  thứ ba làm số quyết định.
- Payout/chu kỳ đối soát của cả 2 nền tảng VN đều không tìm thấy công khai.
- Eventbrite không phù hợp thị trường VN (không tiếng Việt, không payout VN).

## Kết luận demo

- Pattern chạy đúng: 1 manager fan-out 3 worker song song, cùng schema,
  coverage 3/3, không mục lỗi, không retry. Worker không bịa số liệu: trường
  nào không có nguồn công khai đều ghi null + ghi rõ đã thử nguồn nào.
- File dữ liệu thô: `results.json` (cùng thư mục demo này).
- Khuyến nghị sơ bộ (để Trí quyết, không phải kết luận của nghiên cứu):
  TicketGo có dấu hiệu hợp nhất cho vé ngày thi đấu tại Đà Nẵng (thanh toán
  VN đầy đủ + có sự kiện tại Đà Nẵng), nhưng phí và payout phải hỏi trực
  tiếp mới chốt được.
