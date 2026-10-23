---
name: deck-soft-gradient-deck
description: Style deck "Soft Gradient" cho hệ deck-studio — Nền chuyển sắc pastel có hạt (grain), chữ grotesk đen nặng, khoảng trống rộng. Dùng khi làm deck ra mắt/cập nhật với nền gradient pastel và typography đen mạnh trên nền mềm. Theme có sẵn: ~/workspace/deck-studio/themes/soft-gradient-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Soft Gradient — Nền chuyển sắc pastel có hạt (grain), chữ grotesk đen nặng, khoảng trống rộng

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Soft Gradient Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/soft-gradient-deck.json` (bg #FAF3E3, nhấn #E88CA0).

## Khi nào dùng
- Ra mắt sản phẩm tiêu dùng/công nghệ nhẹ.
- Cập nhật nhà đầu tư dạng thư (investor update).
- Keynote thương hiệu tại sự kiện.

## Nguyên lý cốt lõi
- Gradient là ảnh nền, không phải màu đặc: chuẩn bị ảnh gradient có grain cho bìa/section; các trang chữ dùng nền kem của theme.
- Chữ đen phải đủ đậm và lớn để thắng nền; chữ nhỏ màu xám trên gradient là lỗi QA.
- Giọng văn tối giản, tự tin — style này không hợp nội dung dày đặc.

## Hệ hình ảnh
- Trường màu chuyển sắc pastel (hồng phấn → bạc hà → bơ) phủ trang, có hạt grain nhẹ như in riso.
- Chữ grotesk đen rất đậm tạo tương phản với nền mềm — nghịch lý này là bản sắc style.
- Rất ít thành phần: một tiêu đề, một đoạn ngắn, một chi tiết mỗi trang.
- Không icon, không viền thẻ; các khối phân tách bằng chuyển sắc.
- Trang trí của theme: decor `none`, bo góc 16px, mật độ airy. Grainy pastel gradient wash (pink/mint/butter) as fields; engine themes use the cream base — gradient lives in image slides.

## Quy trình
1. Viết spec `deck.json` theo định dạng deck-studio (9 layout: cover, section, content, two-col, data, chart, quote, image, closing). Mọi slide nên có `notes` cho người thuyết trình. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn, bullets ≤ ~14 từ/dòng.
2. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/soft-gradient-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/soft-gradient-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- Chuẩn bị 2–3 ảnh gradient 16:9 (có grain) dùng cho cover/section/closing qua layout `image`.
- Có validator trong bản gốc (placeholder/id trùng/độ dài trang) — tương đương: chạy verify.py + rà spec bằng mắt theo checklist QA của skill này.

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
- Deck ra mắt/cập nhật thưa trang, nền gradient nhất quán.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
