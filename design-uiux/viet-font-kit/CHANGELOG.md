# Nhật ký thay đổi bộ kit

> Quy tắc đánh số: `quy-tac/phien-ban-kit.md`. Bản mới nhất ở trên.

## 1.0.1 · 2026-10-27

Cổng kiểm Word bắt buộc trước khi gửi font (tools/kiemword.py): chặn lỗi Word cắt dấu chồng chữ hoa (Ấ Ễ Ố → Â Ê Ô) do cờ USE_TYPO_METRICS, thiếu cờ tiếng Việt, hinting lỗi, ccmp khai trùng. vnfont.py không còn bật USE_TYPO_METRICS / khai ccmp thứ hai. Font Việt hoá từ trước bị mất dấu ở Word: gửi font, nhắn “kiểm Word”.

## 1.0.0 · 2026-10-27 · bản public đầu tiên

Việt Font Kit — bộ công cụ Việt hoá font cùng Claude: phân tích font, dựng dấu tiếng Việt, trang duyệt artifact (Xem trước · Chỉnh dấu · Bàn vẽ · Kinh nghiệm · Nguồn · Ủng hộ), xuất font. Kèm sẵn kinh nghiệm Việt hoá theo loại font (miễn phí).

Dùng cho mục đích phi thương mại; không thương mại hoá font chưa được cấp phép. Liên hệ: nhatmotion@gmail.com
