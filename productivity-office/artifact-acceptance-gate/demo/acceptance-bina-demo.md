# Demo artifact-acceptance-gate — Nghiệm thu demo video BINA "Hai đội bóng"

Ngày: 28/11/2026. Skill: `artifact-acceptance-gate` (mới chưng cất, chưa push).
Đối tượng: `~/workspace/video-kit/deliverables/bina-demo-hai-doi-bong.mp4`
(demo giao Trí ngày 21/11/2026, QA PASS lúc giao).

## 1. Gate kỹ thuật (chạy lại từ đầu, số đo thật)

| Kiểm tra | Kết quả | Chuẩn | Pass? |
|---|---|---|---|
| ffprobe: 1080×1920@30, H.264 + AAC | 70,2 giây, 5.638.415 byte | dọc 9:16, 60–90 giây | ✅ |
| loudnorm: input_i | −14,00 LUFS | −14 ± 0,5 | ✅ |
| loudnorm: input_tp | −4,77 dBTP | < −1,5 | ✅ |
| loudnorm: input_lra | 2,10 | — | ✅ |
| blackdetect d=0,5 / pic_th=0,98 | 0 đoạn đen | 0 | ✅ |
| blackdetect d=0,2 / pic_th=0,90 | 0 đoạn đen | 0 | ✅ |

## 2. Xem bằng mắt (contact sheet 7 khung, 0–60 giây)

File: `bina-contact-sheet.jpg` (cùng thư mục demo này).

- Khung 0–20 giây: tiêu đề lớn, thẻ Đội 1/Đội 2, pill "CÙNG THÀNH PHỐ /
  SẢN PHẨM GIỐNG NHAU" — chữ không tràn, không đè nhau.
- Khung 20–40 giây: thông điệp "CHÚNG TÔI CHƠI BÓNG RỔ HAY", hình que gia
  đình, thẻ icon vé gia đình / khu vui chơi / giờ thi đấu sớm — đọc rõ.
- Khung 40–60 giây: nhãn đối lập "MỘT ĐỘI BÓNG MỌI NGƯỜI CÓ THỂ THÍCH" vs
  "MỘT LÝ DO ĐỂ CHỌN HỌ", spotlight + hình que, end card playbook + pill
  "BÌNH LUẬN 'ĐỊNH VỊ'" — không lỗi bố cục.
- Dấu tiếng Việt đúng vị trí ở mọi khung xem được.
- Lưu ý: 2 ô đen cuối contact sheet là ô đệm của tile 3×3 (chỉ có 7 frame
  ở fps=1/10 trong 70,2 giây), KHÔNG phải đoạn đen trong video. Đã kiểm
  chứng riêng: độ sáng trung bình frame ở 55/60/65/69/70 giây = 15–21/255
  (khung end card nền tối, có nội dung sáng), blackdetect 0,2 giây cũng 0.

## 3. Quét placeholder

`grep -rniE 'TODO|lorem|placeholder|\[insert|xxx'` trên
`scripts/`, `QA.md`, `projects/demo/Demo.tsx` của project bina-demo:
**0 hit — sạch.**

## 4. Đối chiếu số liệu với QA gốc (21/11/2026)

QA gốc ghi: 70,2 giây, −14,00 LUFS, TP −4,77, LRA 2,10, 0 đoạn đen.
Gate chạy lại ngày 28/11 cho số đo **khớp 100%** — file không đổi sau khi
giao, không có sửa chữa lặng lẽ.

## Kết luận: PASS — 0 lỗi

Demo BINA đạt toàn bộ gate kỹ thuật + xem bằng mắt + quét placeholder.
Không cần sửa (0/3 lần sửa đã dùng). Gate này chứng minh skill
`artifact-acceptance-gate` chạy được end-to-end trên một deliverable thật:
đo lại độc lập khớp QA gốc, xem frame thật, quét placeholder, ghi báo cáo.
