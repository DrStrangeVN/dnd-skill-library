---
name: deck-cobalt-dark-pitch-deck
description: Style deck "Cobalt Ribbon Pitch" cho hệ deck-studio — Pitch đen–cobalt điện: dải ruy-băng xanh phát sáng, panel xanh nhạt lệch, chữ trắng sắc. Dùng khi làm pitch deck sản phẩm/vòng gọi vốn cần nền đen, điểm nhấn cobalt điện và nhịp vấn đề → giải pháp → bằng chứng. Theme có sẵn: ~/workspace/deck-studio/themes/cobalt-dark-pitch-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Cobalt Ribbon Pitch — Pitch đen–cobalt điện: dải ruy-băng xanh phát sáng, panel xanh nhạt lệch, chữ trắng sắc

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Cobalt Ribbon Pitch Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/cobalt-dark-pitch-deck.json` (bg #04060A, nhấn #2E6BFF).

## Khi nào dùng
- Pitch sản phẩm công nghệ/vận hành cho nhà đầu tư hoặc lãnh đạo.
- Deck khái niệm đầu tư cần ra quyết định (decision-oriented).
- Proposal pilot ngắn cần chốt owner + deadline.

## Nguyên lý cốt lõi
- Nhịp pitch khóa cứng: vấn đề → giải pháp → bằng chứng → mô hình → đề nghị (ask) kèm chủ sở hữu và mốc ngày.
- Mỗi slide kết bằng một quyết định hoặc một con số — slide nào không có cả hai thì cắt.
- Bằng chứng (pilot, số liệu, khách hàng) đặt trong panel xanh nhạt để mắt nhận ra ngay 'đây là phần chứng minh'.

## Hệ hình ảnh
- Nền đen gần tuyệt đối; hình dải ruy-băng (ribbon) cobalt phát sáng là motif chủ đạo ở bìa và trang chuyển.
- Panel xanh nhạt (pale blue) đặt lệch (offset) chứa bằng chứng/số liệu, tương phản với nền đen.
- Chữ grotesk trắng cỡ lớn, tracking chặt; kicker mono viết hoa màu xanh nhạt.
- Không màu nào ngoài phổ xanh–trắng–đen.
- Trang trí của theme: decor `band`, bo góc 10px, mật độ standard. Black canvas, electric cobalt ribbon artwork, offset pale-blue panels; white grotesk set tight.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/cobalt-dark-pitch-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/cobalt-dark-pitch-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Ảnh ribbon là ảnh hero — chuẩn bị 1 ảnh 16:9 nền đen cho cover và closing; slide giữa giữ nền đen sạch.
- Số liệu dùng `data` (tối đa 4) và `chart` với thanh cuối highlight = cột mốc/ask.

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
- Pitch ~8 trang: bìa, vấn đề, giải pháp, sản phẩm, bằng chứng, mô hình, đội, ask/quyết định.
- Notes ngắn, mỗi trang một ý nói; HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
