---
name: deck-confetti-gathering-deck
description: Style deck "Confetti Gathering" cho hệ deck-studio — deck poster cho khái niệm sum họp cộng đồng: mỗi slide một nền màu phẳng (hồng/xanh dương/xanh trời/vàng/xanh lá/đỏ san hô) có lưới mờ, hình khối phẳng (sao 4 cánh, chùm sao, quạt tia, nét uốn, chấm), chữ italic đậm khổ lớn, ảnh tròn, panel kem. Cấu trúc gốc 12 slide, mỗi slide một bố cục riêng — không có footer/số trang. Dùng cho deck sự kiện cộng đồng, chương trình fan, ngày hội cần cảm giác poster vui và ấm. Theme: ~/workspace/deck-studio/themes/confetti-gathering-deck.json. Engine + quy trình: skill deck-studio (master); demo chuẩn: ~/workspace/skillry-slides/demos/confetti-gathering-deck/ (deck.json + build_spec.py + make_assets.py + PREVIEW-MAP.md + FIDELITY.md).
---

# Deck Confetti Gathering — Poster sum họp: nền màu phẳng, khối phẳng, chữ italic đậm

Style house của deck-studio, chưng cất từ mô tả + preview công khai của skill "Confetti Gathering Deck" (Skillry, gói trả phí) và rà sát lại theo previews ngày 23/10/2026 — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh, cấu trúc và công dụng. Theme: `themes/confetti-gathering-deck.json`.

## Cấu trúc gốc (12 slide — mỗi slide một bố cục riêng, khóa cứng)
1. Bìa (hồng): khối azure góc trái trên (caps italic + dòng phụ), ảnh tròn lớn, sao xanh lá, vòng vàng + 3 chấm đỏ, headline italic ~92px, pill kem rộng, nửa đĩa đỏ + quạt tia xanh ở góc phải dưới, chùm sao vàng góc trái dưới kèm dòng italic.
2. Mục lục (xanh dương): title italic trắng căn giữa; lưới 2×2 mục đánh số 01–04 (heading italic + thân chữ trắng).
3. Chương trình (vàng): title căn giữa; 4 cột — vòng tròn đỏ san hô + icon nét trắng, heading italic, chú thích căn giữa; footnote nhỏ góc trái dưới.
4. Tuyên ngôn (xanh lá): panel kem lớn ở giữa — micro caps, headline italic ~72px, một dòng phụ.
5. Chào đón (xanh trời): ảnh tròn lớn trái; title italic trắng + 3 hàng (vòng kem + icon nét azure + heading italic + thân chữ).
6. Bốn bước (xanh lá): title trái; 4 vòng kem "STEP 01–04" (chữ xanh italic), tên bước + chú thích căn giữa bên dưới.
7. Trước bữa tối (vàng): title căn giữa; 2 ảnh ngang + heading italic + chú thích dưới mỗi ảnh.
8. Chi tiết nhỏ (hồng): title căn giữa; 3 vòng trắng chứa ảnh sản phẩm + heading/chú thích căn giữa.
9. Kết nối (xanh lá): title trái; donut 4 đoạn (đỏ/vàng xen kẽ, tâm xanh "chiếc bàn chung") ở giữa; 4 khối chữ ở 4 góc.
10. Con người (đỏ san hô): title trắng căn giữa; 3 ảnh tròn + heading/chú thích; dòng miễn trừ hư cấu góc trái dưới.
11. Giữ lại (xanh dương): cột chữ trái (title + 2 đoạn); 2 khung điện thoại chứa ảnh, mỗi khung một pill chú thích kem; dòng miễn trừ dưới khung.
12. Kết (vàng): panel kem — headline italic ~74px + dòng phụ; dòng ghi chú nhỏ dưới panel.

## Hệ hình ảnh
- Bảng màu theo slide: hồng #F6AFC2, azure #0B96E6, sky #55C1E8, vàng #FFC61A, xanh lá #12A94C, đỏ #FF4049, kem #FFF6DC, mực #16130F. Mỗi slide MỘT màu nền + các màu còn lại làm điểm nhấn hình khối.
- Lưới mờ trên nền: nướng sẵn vào ảnh nền theo màu (Pillow, pitch 40px stage, đường tối hơn nền ~6%).
- Hình khối phẳng là vựng tập cố định: sao 4 cánh, chùm sao 12 cánh, quạt tia từ góc, nét uốn (squiggle), chồng 3 chấm, blob tràn mép, đĩa/nửa đĩa. Vẽ bằng Pillow thành PNG alpha (xem make_assets.py của demo).
- Chữ: display = Be Vietnam Pro 900 italic (font italic đậm duy nhất có đủ dấu tiếng Việt trên máy); thân chữ Be Vietnam Pro thường. KHÔNG dùng Baloo 2 (không có italic thật, sai giọng).
- Ảnh: ảnh đời thực ấm; luôn trong vòng tròn (pre-mask Pillow) hoặc khung bo góc/điện thoại. KHÔNG footer, KHÔNG số trang, KHÔNG logo.

## Quy trình
1. Spec bằng layout `free`; nên viết builder Python như `build_spec.py` của demo chuẩn (helper cho dots/panel/tiêu đề) thay vì gõ JSON tay cho 12 bố cục.
2. Assets bằng pipeline kiểu `make_assets.py`: sinh ảnh gốc → cắt đúng tỉ lệ/mask; hình khối + icon + donut vẽ Pillow; ghi `assets/CREDITS.txt`.
3. Build + verify + chụp cả 12 slide:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/confetti-gathering-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/confetti-gathering-deck.json -o <thư-mục-ra>/deck.pptx
   ~/workspace/tools/deck-venv/bin/python verify.py <deck.json> <thư-mục-ra>/deck.pptx   # phải ALL PASS
   node screenshot.js <thư-mục-ra>/deck.html <thư-mục-ra>/shots 0,1,2,3,4,5,6,7,8,9,10,11
   ```
4. Đọc sheet bằng mắt: khối hình có đè chữ không, chữ italic có tràn không, mỗi slide đúng MỘT màu nền chủ đạo chưa.

## Giới hạn cần nhớ
- Donut/pie: engine không có nguyên thủy pie — nướng đoạn vào PNG, số + nhãn để chữ native đè lên.
- Thứ tự phần tử trong spec `free` = thứ tự lớp vẽ.
- Slide 1 field `title` phải là dòng đầu headline bìa (verify đối chiếu).
