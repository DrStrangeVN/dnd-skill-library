---
name: deck-gallery-catalogue-deck
description: Style deck "Gallery Catalogue" cho hệ deck-studio — catalogue triển lãm trên nền trắng: serif Playfair với dòng roman + italic trong cùng một title, chip nhãn vàng mù tạt, khung vàng mảnh vẽ chồng lên ảnh, chú thích như nhãn treo tường, dòng script viết tay trên ảnh, và chrome chân trang cố định (tên deck caps nhỏ — đường kẻ vàng — số trang NN / 12). Cấu trúc gốc 12 slide, mỗi slide một bố cục riêng. Dùng cho catalogue triển lãm/bộ sưu tập, hồ sơ hiện vật, tài liệu trình bày kiểu bảo tàng. Theme: ~/workspace/deck-studio/themes/gallery-catalogue-deck.json. Engine + quy trình: skill deck-studio (master); demo chuẩn: ~/workspace/skillry-slides/demos/gallery-catalogue-deck/ (deck.json + build_spec.py + make_assets.py + PREVIEW-MAP.md + FIDELITY.md).
---

# Deck Gallery Catalogue — Catalogue triển lãm: giấy trắng, khung vàng, nhãn treo tường

Style house của deck-studio, chưng cất từ mô tả + preview công khai của skill "Gallery Catalogue Deck" (Skillry, gói trả phí) và rà sát lại theo toàn bộ previews ngày 23/10/2026 — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh, cấu trúc và công dụng. Theme: `themes/gallery-catalogue-deck.json`.

## Cấu trúc gốc (12 slide — mỗi slide một bố cục riêng, khóa cứng)

1. **Bìa.** Ảnh tường sơn vàng–đen phủ kín khung; kicker caps trắng góc trái trên; title grotesk đậm trắng căn giữa (~78–88px); dưới title một vạch trắng dày (~8px) RỘNG gần bằng title; subline caps nhỏ giãn chữ rộng; footer chạy trên ảnh.
2. **Chào mừng.** Trang trắng lồng trên nền tách khối không đối xứng (trái đen ~46%, phải vàng mù tạt); title serif 3 dòng (dòng đầu roman, các dòng sau italic bằng marker `*italic*`); 2 đoạn xám; một dòng script; ảnh (mural/tranh tường màu) bên phải cao hết trang; footer nằm TRONG trang trắng.
3. **Thư viện vật chất.** Nền trắng; ảnh phủ chiều cao bên phải (~46%); KHUNG VÀNG MẢNH vẽ từ lề trái tràn chồng lên ảnh — chi tiết chữ ký của style; chip vàng + title serif + 2 đoạn; footer kết thúc trước ảnh.
4. **Nhìn gần hơn.** Ảnh mural chân dung phủ nửa trái + khung vàng lồng trong ảnh + dòng script trắng viết trên ảnh; cột phải: 3 mục đánh số (heading caps đậm + 2 dòng thân).
5. **Đối thoại vật chất.** Chip + title serif; ảnh tĩnh vật lớn bên trái; 3 hàng bên phải: ẢNH TRÒN + nhãn đánh số + ghi chú.
6. **Thuộc về một nơi chốn.** Ảnh hẻm phố phủ kín; khối teal ở mép trái; panel trắng chồng lên ảnh (chip, title, 2 đoạn, footer trong panel); chữ dọc caps "PLACE / LIGHT / SEQUENCE" trên ảnh bên phải — nướng vào PNG alpha (engine không xoay chữ).
7. **Vật thể mang theo.** Ảnh nội thất gallery phủ kín + khung vàng lồng toàn slide; THẺ TRẮNG bên phải chứa title serif + thân chữ nhỏ kiểu chú thích + footer trong thẻ.
8. **Ý tưởng bất ngờ.** Gương của slide 4: chữ bên trái (chip, title, 2 đoạn); ảnh tay đeo trang sức vàng trên nền teal bên phải + khung vàng lồng + script trắng.
9. **Khoảng dừng sáng hơn.** Ảnh flat-lay hồng phủ mép trái + khung TRẮNG lồng + script; hai thẻ bên phải: ảnh chân dung, nhãn caps, THANH VÀNG DÀY (~13px), ghi chú.
10. **Bốn cách nhìn.** Header caps nhỏ; 4 ảnh chân dung một hàng; dưới mỗi ảnh: tên caps, thanh vàng chứa nhãn caps trắng 9.5px, một dòng ghi chú.
11. **Ba chủ đề.** Dải ảnh trời hoàng hôn ngang trên cùng, có NÊM TRẮNG CHÉO cắt vào và mép phải tối dần (cả hai nướng vào ảnh dải bằng Pillow); 3 thẻ ảnh bo góc chồng lên dải; dưới mỗi thẻ: icon nét vàng + title caps nhỏ + ghi chú 2 dòng căn giữa.
12. **Lời mời nhìn lại.** Panel vàng mù tạt phủ nửa phải, ảnh tablet đặt giữa panel; chữ bên trái; footer kết thúc trước panel.

## Chrome (bắt buộc, gần như mọi slide)

Footer: tên deck caps 10px giãn chữ ở trái — đường kẻ vàng mảnh `#C7A962` — counter `NN / 12` ở phải. Khi slide có panel/thẻ trắng, footer nằm trong panel/thẻ đó; khi có ảnh phủ mép, footer dừng trước vùng ảnh.

## Hệ hình ảnh

- Bảng màu: trắng `#FFFFFF`, mực ấm `#1D1B18`, xám chú thích `#8A857C`, vàng chip/thanh `#DFA320`, vàng kẻ `#C7A962`, khối đen `#111110` / mù tạt `#E8A90C` / teal `#527F88`.
- Chữ: display Playfair Display (roman + italic trộn dòng bằng marker `*…*`); thân Be Vietnam Pro xám ~12.5–14.5px, leading rộng 1.55; script = Dancing Script (font script duy nhất trong pipeline có đủ dấu tiếng Việt — dùng cho các dòng viết tay trên ảnh); chip = rect vàng góc gần vuông, chữ trắng caps 10.5px giãn chữ.
- Ảnh: biên tập bão hòa, khổ chữ nhật (không bo góc) trừ ảnh tròn slide 5 và thẻ bo góc slide 11; cắt đúng tỉ lệ khung đặt trước khi build (PPTX exporter kéo giãn ảnh theo khung, không crop). Khung vàng/trắng lồng trên ảnh = rect native không fill, `line_color` vàng `#C7A962` (hoặc trắng), `line_w` 1.25–2.

## Quy trình

1. Spec bằng layout `free`; nên viết builder Python như `build_spec.py` của demo chuẩn (helper chip/footer/serif/script) thay vì gõ JSON tay cho 12 bố cục. Mọi slide có `notes` (ghi rõ DEMO nếu là nội dung minh họa).
2. Assets theo pipeline `make_assets.py` của demo: sinh ảnh gốc theo đúng bố cục preview → cắt tỉ lệ/mask vòng tròn/bo góc bằng Pillow; nêm chéo + vệt tối nướng vào ảnh dải trời; chữ dọc nướng PNG; icon nét vàng vẽ Pillow; ghi `assets/CREDITS.txt`.
3. Build + verify + chụp cả 12 slide:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/gallery-catalogue-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/gallery-catalogue-deck.json -o <thư-mục-ra>/deck.pptx
   ~/workspace/tools/deck-venv/bin/python verify.py <deck.json> <thư-mục-ra>/deck.pptx   # phải ALL PASS
   node screenshot.js <thư-mục-ra>/deck.html <thư-mục-ra>/shots 0,1,2,3,4,5,6,7,8,9,10,11
   ```
   (screenshot.js nhận index 0-based, xuất slide-01.png… theo thứ tự.)

## QA bắt buộc (không bỏ qua)

1. `verify.py` ALL PASS + đọc lại PPTX bằng python-pptx (số slide, text frames, pictures, notes).
2. Contact sheet cả 12 slide, đọc bằng mắt: dấu tiếng Việt (đặc biệt chữ script), tràn chữ, khung vàng có chồng đúng lên ảnh, footer không chạy vào vùng ảnh.
3. So sánh bìa + 2 slide chữ ký với preview gốc (comparison có nhãn hai phía) khi làm bản fidelity/nghiệm thu.

## Sản phẩm bàn giao (output contract)

- `deck.json` (spec), `deck.html` (studio), `deck.pptx` (text + notes sửa được; ảnh/phần nướng là picture), contact sheet + comparison khi nghiệm thu, `FIDELITY.md` khi rà sát theo bản gốc.
- Giới hạn engine cần nhớ: không xoay được chữ (nướng PNG); không có primitive đường chéo/nêm (nướng vào ảnh); không auto-fit chữ — tràn là lỗi của spec, sửa spec rồi build lại, không sửa tay file xuất.
