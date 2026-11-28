---
name: artifact-acceptance-gate
description: Nghiệm thu một deliverable trước khi giao cho Trí — render lại từ đầu và xem bằng mắt thứ Trí sẽ thấy, quét placeholder còn sót, sửa tối đa 3 lần. Dùng mỗi khi sắp trả link hoặc file: video, deck, tài liệu, bảng tính, web artifact, báo cáo.
---

# Artifact Acceptance Gate

> Chưng cất từ thiết kế workflow của skill `artifacts/testing` trong bản lưu
> trữ không chính thức https://github.com/win4r/MuseAI-Skills
> (`opt/hatch/skills/artifacts/testing/SKILL.md`, HEAD 6c12bde, 26/11/2026).
> Repo nguồn KHÔNG CÓ LICENSE và là snapshot skill hệ thống của Muse — skill
> này viết lại hoàn toàn bằng lời của mình, KHÔNG chép nguyên văn. Các lệnh
> gate gốc (`render_audit.mjs`, `validate_pdf.sh`...) là tool nội bộ của Muse,
> không có trong môi trường này — bảng gate dưới đây thay bằng công cụ thật
> Trí đang dùng (ffmpeg, LibreOffice, python-pptx, trình duyệt).

## Nguyên tắc chung (áp cho mọi loại deliverable)

1. **Render lại rồi xem bằng mắt.** Deliverable chỉ được coi là đạt khi đã
   xem thứ Trí sẽ thấy, render tươi từ file cuối — không tin code đã sinh ra
   nó. Người làm ra file luôn nhìn thấy thứ mình mong đợi, không phải thứ đã
   render thật.
2. **Không trả link khi gate chưa pass.** Gate rớt thì sửa, không giao.
3. **Tối đa 3 lần sửa.** Sau 3 lần sửa vẫn rớt thì dừng, báo lỗi cụ thể
   (lỗi gì, ở đâu, đã thử gì) và hỏi Trí hướng xử lý — không lặp vô hạn.
4. **Quét placeholder trước khi giao.** Tìm trong nội dung: TODO, lorem,
   placeholder, `[insert...`, `xxx`, hàng mẫu Trí không yêu cầu. Tìm thấy là
   sửa, không giao.
5. **Không báo xong khi chưa nghiệm thu.** Không dùng từ "xong/hoàn thành"
   nếu gate chưa pass; không báo deploy thành công nếu chưa kiểm tra live.

## Gate theo loại file

| Loại | Gate (chạy thật, đo thật) |
|---|---|
| Video (mp4) | `ffprobe` thời lượng/khổ/fps; `loudnorm` đo LUFS/TP; `blackdetect` quét đoạn đen; trích frame (contact sheet + still từng đoạn) và **xem bằng mắt**: chữ tràn/đè nhau, dấu tiếng Việt sai vị trí, artifact sai nội dung |
| PDF | Render sang ảnh từng trang (`pdftoppm`), xem bằng mắt từng trang: tràn chữ, lệch bố cục, chữ mờ, trang trắng |
| DOCX | Convert sang PDF bằng LibreOffice headless (`soffice --headless --convert-to pdf`), render ảnh rồi xem bằng mắt |
| PPTX/XLSX | Mở bằng python-pptx/openpyxl đọc lại nội dung (số liệu, text) đối chiếu nguồn; render sang PDF/ảnh nếu cần xem bố cục; kiểm tra link trong slide có bấm được không |
| CSV/MD | Đọc ngược lại bằng parser (csv: đọc bằng Python `csv`; md: đọc file) — số cột, encoding, ký tự lạ |
| Web artifact | Mở link production bằng trình duyệt thật, xem bằng mắt ở desktop + mobile 390px: tràn ngang, chữ đè, nút không bấm được, dữ liệu mẫu còn sót |

## Checklist xem bằng mắt (mọi loại)

- Chữ tràn khỏi khung, bị cắt, đè lên nhau.
- Khoảng cách chật/lệch, căn lề không đều.
- Chữ mờ, tương phản thấp, khó đọc.
- Trang trí/template thừa còn sót (header/footer mẫu, watermark).
- Số liệu trong deliverable khớp với nguồn (đối chiếu, không tin trí nhớ).
- Link/QR/nút bấm được và dẫn đúng chỗ.

## Quy trình chạy gate

1. Chạy gate kỹ thuật của loại file, ghi số đo thật (không đoán).
2. Render/xuất ra dạng xem được, xem bằng mắt toàn bộ (video: xem đủ các
   đoạn; tài liệu dài: xem tối thiểu trang bìa, trang số liệu, trang cuối).
3. Quét placeholder trong nội dung.
4. Ghi `QA.md` cạnh deliverable: số đo, lỗi tìm thấy, lỗi đã sửa, lỗi còn
   lại (nếu có).
5. Pass → giao cho Trí kèm link/file. Fail → sửa (tối đa 3 lần) rồi chạy lại
   từ bước 1. Quá 3 lần → báo lỗi cụ thể và hỏi hướng.

## Giới hạn

- Gate kỹ thuật không thay mắt người: số đo đạt vẫn phải xem frame/trang.
- Không dùng kết quả kiểm tra cũ cho file mới — mỗi lần sửa là một lần gate
  lại từ đầu.
- Không tự ý hạ chuẩn khi deadline gấp: chuẩn không đổi, chỉ báo rõ rủi ro
  nếu Trí quyết giao bản chưa pass.

## Nguồn

- Thiết kế workflow: skill `artifacts/testing` trong
  https://github.com/win4r/MuseAI-Skills (không license, snapshot skill hệ
  thống Muse, HEAD 6c12bde). Skill này chưng cất lại bằng lời của mình,
  thay tool nội bộ bằng công cụ thật trong môi trường của Trí.
