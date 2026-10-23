---
name: deck-tidal-service-playbook-deck
description: Style deck "Tidal Service Playbook" cho hệ deck-studio — Playbook dịch vụ xanh băng–navy: đường cong hữu cơ, bảng dịch vụ, hành trình nối bước. Dùng khi làm playbook/đào tạo dịch vụ với bảng chuẩn dịch vụ và sơ đồ hành trình khách hàng nối các bước. Theme có sẵn: ~/workspace/deck-studio/themes/tidal-service-playbook-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Tidal Service Playbook — Playbook dịch vụ xanh băng–navy: đường cong hữu cơ, bảng dịch vụ, hành trình nối bước

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Tidal Service Playbook Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/tidal-service-playbook-deck.json` (bg #DFF2F7, nhấn #1D5C8A).

## Khi nào dùng
- Đào tạo lễ tân, chăm sóc khách hàng, vận hành dịch vụ.
- Giới thiệu công ty dịch vụ cho đối tác.
- Onboarding nhân viên tuyến đầu (frontline).

## Nguyên lý cốt lõi
- Playbook phải dùng được trong ca làm việc: mỗi chuẩn dịch vụ viết dạng làm/không làm, có ví dụ câu nói mẫu.
- Hành trình khách hàng vẽ theo bước nối tiếp; điểm gãy (handoff) đánh dấu rõ kèm người chịu trách nhiệm.
- Tình huống khó (complaint, escalation) có trang riêng với quy trình từng bước.

## Hệ hình ảnh
- Trang xanh băng (ice blue) và navy xen kẽ; hình cong hữu cơ (organic contours) như đường thủy triều ở mép trang.
- Chữ grotesk navy thoáng; bảng dịch vụ viền băng mảnh, hàng rõ.
- Sơ đồ hành trình: các bước nối bằng đường cong liền mạch, không mũi tên cứng.
- Có 9 archetype trang trong bản gốc (bìa, chuẩn dịch vụ, hành trình, tình huống, escalation…) — giữ đủ nhịp này.
- Trang trí của theme: decor `none`, bo góc 20px, mật độ standard. Ice-blue and navy pages, organic contour shapes, open typography, service tables, connected journey steps.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/tidal-service-playbook-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/tidal-service-playbook-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Bảng dịch vụ dùng layout `content`/`two-col` với bullets dạng 'Làm: … / Không: …'.
- Sơ đồ hành trình lớn dùng ảnh riêng ở layout `image`; bước đơn lẻ dùng section đánh số.

## QA bắt buộc (không bỏ qua)
1. `~/workspace/tools/deck-venv/bin/python verify.py <deck.json> <deck.pptx>` — phải đạt: đủ số slide, tiêu đề bìa khớp, mọi slide có text, notes đầy đủ.
2. Chụp ít nhất 3 slide (bìa, một slide data/chart, closing) và ghép contact sheet:
   ```bash
   cd ~/workspace/deck-studio
   node screenshot.js <thư-mục-ra>/deck.html <thư-mục-ra>/shots 0,5,8
   ```
   Đọc sheet bằng mắt: dấu tiếng Việt, tràn chữ, tương phản, đúng vai trò màu của style.
3. Đọc lại PPTX bằng python-pptx (số slide, số text shapes, notes) khi bàn giao deck quan trọng.

## Sản phẩm bàn giao (output contract)
- Playbook: bìa → chuẩn dịch vụ → hành trình khách → tình huống → escalation → kiểm tra nhanh cuối ca.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
