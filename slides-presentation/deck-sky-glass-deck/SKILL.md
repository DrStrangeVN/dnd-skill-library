---
name: deck-sky-glass-deck
description: Style deck "Sky Glass" cho hệ deck-studio — Ảnh trời thật dưới lớp thẻ kính mờ, chữ serif–grotesk thanh lịch. Dùng khi làm deck về khí hậu/thiên văn/quan trắc với ảnh trời khổ lớn và thẻ kính trong suốt. Theme có sẵn: ~/workspace/deck-studio/themes/sky-glass-deck.json. Engine, định dạng spec và quy trình đầy đủ: xem skill deck-studio (master) và catalogue ~/workspace/skillry-slides/SLIDES-INDEX.md.
---

# Deck Sky Glass — Ảnh trời thật dưới lớp thẻ kính mờ, chữ serif–grotesk thanh lịch

Style house của deck-studio, chưng cất từ mô tả + ảnh preview công khai của skill "Sky Glass Deck" (Skillry, gói trả phí) — nội dung viết lại hoàn toàn, chỉ giữ hệ hình ảnh và công dụng. Theme: `themes/sky-glass-deck.json` (bg #103E5E, nhấn #38A1E8).

## Khi nào dùng
- Báo cáo năm của đài/trạm quan trắc, tổ chức khí hậu.
- Sản phẩm dữ liệu môi trường trình bày cho đối tác.
- Thư thường niên của tổ chức thiên văn/khoa học khí quyển.

## Nguyên lý cốt lõi
- Ảnh trời phải là ảnh thật có nguồn rõ (đài quan trắc, vệ tinh mở, nhiếp ảnh gia có licence) — ảnh AI không qua được QA của style này.
- Số liệu khí hậu luôn ghi kỳ dữ liệu và đơn vị ngay trong thẻ kính.
- Một trang tối đa 2 thẻ kính; nhiều thẻ hơn sẽ làm mất cảm giác 'nhìn qua kính lên trời'.

## Hệ hình ảnh
- Ảnh trời THẬT (bình minh, mây, hoàng hôn) làm nền: bìa dùng ảnh khổ dọc bên trái, các trang dữ liệu dùng ảnh toàn nền.
- Thẻ kính (glass card) THẬT kể từ engine v2: HTML dùng fill trắng 12% + viền trắng 45% + `backdrop-filter: blur(14px)` — nhìn xuyên qua thẻ thấy ảnh nền mờ đi; PPTX dùng fill trắng alpha 12% + viền sáng (không có blur sống trong PowerPoint — cùng đánh đổi như bản gốc Skillry).
- Panel gradient xanh sâu (#081F33 → #3E84BE) cho bìa phải, trang giải thích và trang chốt.
- Hai giọng chữ TRỘN TRONG CÙNG MỘT TIÊU ĐỀ: grotesk đậm cho phần chính, serif (Playfair) cho cụm kết — đánh dấu cụm serif bằng `~…~` trong spec.
- Chrome riêng của style: header caps in đậm góc trái trên + counter "Khái niệm thực địa NN / TT" góc phải trên, thay footer mặc định.
- Điểm ấm duy nhất là tông hổ phách của ảnh hoàng hôn; chữ và thẻ giữ phổ xanh lạnh.
- Theme: decor `none`, bo góc 18px, mật độ airy + khóa `glass` / `gradient` / `photo_bg` (xem README của deck-studio, mục Glass / photo mode).

## Quy trình
1. Chuẩn bị ảnh: ảnh trời thật có nguồn/licence rõ (Wikimedia Commons là nguồn an toàn), khổ ngang ≥1920px cho trang toàn nền; nếu ảnh có phần không dùng (cỏ, mặt đất) thì cắt sẵn bản chỉ-trời. Ghi nguồn vào `assets/CREDITS.txt` cạnh deck.
2. Viết spec `deck.json` theo ngữ pháp của style (xem Công thức bên dưới). Mọi slide có `notes`; nội dung demo/giả tưởng phải ghi rõ DEMO trong notes. Chữ tiếng Việt dài dễ tràn — giữ tiêu đề ngắn.
3. Build HTML studio + PPTX:
   ```bash
   cd ~/workspace/deck-studio
   python3 build_deck.py <deck.json> themes/sky-glass-deck.json -o <thư-mục-ra>/deck.html
   ~/workspace/tools/deck-venv/bin/python export_pptx.py <deck.json> themes/sky-glass-deck.json -o <thư-mục-ra>/deck.pptx
   ```

## Công thức & kỹ thuật đặc thù
- **Bìa `cover` + `"variant": "split-glass"`** (đúng bìa bản gốc): trái 46% ảnh trời toàn chiều cao — headline serif trắng phía trên, MỘT thẻ kính lớn (nhãn caps + tiêu đề grotesk + dòng phụ), MỘT chip kính nhỏ chồng góc dưới-trái của thẻ; phải 54% panel gradient — kicker caps, tiêu đề hỗn hợp grotesk/serif (`~…~`), body muted, tối đa 2 nút pill (`light` = trắng, `accent` = xanh). Trường: `photo`, `headline`, `card_label/title/sub`, `chip_label/text`, `kicker`, `title`, `body`, `buttons`, `footer_note`, `header`, `counter`, `counter_label`. Hai trường v3 nên dùng: `"scrim": true` (gradient tối dọc dưới vùng kính — nhãn caps hết chìm vào mây sáng) và `"glass_blur": 3` khi thẻ kính phủ lên KHUÔN MẶT (blur đầy đủ 14px làm tan nét mặt; đã đo đối chiếu — xem QA demo v3).
- **Ảnh bìa có người** (chuẩn v3): tạo ảnh biên tập bằng image generation — người ngước nhìn trời, trời chiếm ~2/3 khung, một vùng trời êm ở giữa-phải cho thẻ kính; bố cục GỐC, không sao chép người mẫu/trang phục của bản Skillry. Hoặc ảnh CC trên Commons có người + trời lớn. Ghi prompt/nguồn vào `assets/CREDITS.txt` của deck.
- **Trang sáng `statement`**: nền gần trắng #F4F6F7, header + counter, tiêu đề hỗn hợp căn giữa, subline, MỘT nút pill tối, ghi chú chân trang trái. Chuẩn v3: `"orbs": [7 file PNG]` — artwork cầu kính THẬT có alpha nằm trên vòng cung cố định (cách làm: generate một dải cầu kính trên nền trắng sạch, cắt từng cầu bằng mặt nạ tròn khớp cung bằng Pillow; motif gợi ý: gió, sóng, mây, nắng ở đỉnh cung, sóng, mầm, khối kính). Cách cũ `"spheres": true` (3 vòng CSS; PPTX oval bán trong) chỉ là fallback — khai rõ khi bàn giao nếu dùng.
- **Trang dữ liệu trên ảnh**: `data` hoặc `two-col` + `"bg": "photo"` (+ `photo` riêng nếu khác `photo_bg` của theme) — thẻ chỉ số/so sánh tự thành thẻ kính trên ảnh. Tối đa 4 chỉ số; kỳ dữ liệu + đơn vị nằm ngay trong nhãn thẻ; takeaway cũng là dải kính.
- **Trang giải thích `glass-panel`**: gradient toàn trang, kicker + tiêu đề hỗn hợp + body bên trái; thẻ kính lớn bên phải chứa các hàng đánh số `card_items[{n, text}]` cách nhau bằng hairline.
- **Trang chốt `closing` + `"bg": "gradient"`**: gradient + thẻ kính căn giữa + nút CTA trong thẻ.
- Một trang tối đa 2–3 thẻ kính; nhiều thẻ hơn sẽ làm mất cảm giác 'nhìn qua kính lên trời'.
- **Kính trong PPTX = blur nướng sẵn (baked blur, engine v3)**: exporter composite nền slide bằng Pillow rồi lấy chính vùng nền dưới panel, blur + tint làm fill dạng picture; viền alpha + bóng mềm nướng kèm; chữ vẫn native sửa được. Không còn là fill bán trong như v2. Chi tiết kỹ thuật: README deck-studio mục "Frosted glass in PPTX".
- Artwork tự do: mọi layout nhận `"art": [{src, x, y, w, h}]` (ảnh có alpha, nằm trên nền/dưới chữ) — dùng cho logo kính, minh họa phụ.
- Khoảng hở còn lại so với bản gốc (khai thẳng, không giấu): (1) blur PPTX là ảnh nướng tại thời điểm xuất — sửa vị trí thẻ trong PowerPoint sẽ không blur lại (đổi spec rồi xuất lại); (2) cầu kính là artwork 2D render sẵn, không phải vật liệu 3D trong file; (3) tỉ lệ người/trời trong ảnh AI tạo một lần có thể khác preview gốc dù cùng ngữ pháp.

## QA bắt buộc (không bỏ qua)
1. `~/workspace/tools/deck-venv/bin/python verify.py <deck.json> <deck.pptx>` — phải đạt: đủ số slide, tiêu đề bìa khớp, mọi slide có text, notes đầy đủ.
2. Chụp ít nhất 3 slide (bìa, một slide data/chart, closing) và ghép contact sheet:
   ```bash
   cd ~/workspace/deck-studio
   node screenshot.js <thư-mục-ra>/deck.html <thư-mục-ra>/shots 0,5,8
   ```
   Đọc sheet bằng mắt: dấu tiếng Việt, tràn chữ, tương phản, đúng vai trò màu của style.
3. Đọc lại PPTX bằng python-pptx (số slide, số text shapes, notes) khi bàn giao deck quan trọng.
4. Với deck kính/trên ảnh: render chính file PPTX (LibreOffice headless → PDF → PNG) và soi panel kính — nền trong panel phải mờ rõ so với ngoài panel (bằng chứng baked blur); lệch xuống dòng nhỏ do font thay thế của LibreOffice là khác biệt renderer, không phải lỗi file.

## Sản phẩm bàn giao (output contract)
- Deck quan trắc: bìa ảnh trời → chỉ số chính → diễn biến → ghi chú phương pháp → liên hệ dữ liệu mở.
- HTML studio + PPTX editable.
- Luôn gồm: `deck.json` (spec), `deck.html` (studio xem/sửa/thuyết trình, mở bằng file://), `deck.pptx` (text + notes sửa được; nền/hình phức tạp thành picture), contact sheet QA.
- Giới hạn engine cần nhớ: không có auto-fit chữ (tràn là lỗi của spec, sửa spec chứ không sửa tay file xuất); layout `image` chỉ nhận file local, phủ đầy 16:9.
