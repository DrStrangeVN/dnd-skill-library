---
name: opuscar-graphic-type
description: Kỹ thuật phim đồ họa phẳng & chữ làm hình (spin-out từ bộ Lemo-Opuscar) — 8 style: Swiss lưới, mở đầu gián điệp thập niên 60, Art Deco, pictogram, hình học Bauhaus, du hành tỉ lệ phẳng, chữ chớp cắt, bóng đen theo nhịp. Dùng khi brief là "poster biết chuyển động", "chữ là kiến trúc", "số liệu thành hình", "mở đầu phim kiểu title sequence", hoặc giải thích tỉ lệ/quy tắc bằng đồ họa phẳng. Mọi nội dung do brief quyết định — skill chỉ giữ ngữ pháp đồ họa và kỷ luật sản xuất.
---

# Opuscar Graphic & Type — Đồ họa phẳng & chữ làm hình

Đồ họa phẳng 2D vẽ bằng code, màu đặc không chuyển sắc, lưới và nhịp là luật. Chữ ở đây không phải phụ đề gắn thêm: chữ là kiến trúc, là dữ liệu, là nhân vật. Một phim thuộc nhóm này đọc được ngay từ khung hình đầu — giấy phẳng, một màu tín hiệu, chữ khổ lớn — trước khi nghe một lời thoại nào.

Nguồn kỹ thuật: 8 style trong repo Lemo-Opuscar tại `~/workspace/lemo-opuscar/styles/{swiss-motion,spy-titles,art-deco,pictogram-motion,bauhaus-shapes,flat-space-explainer,text-flash-cuts,silhouette-rhythm}/STYLE.md` — đọc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện/nhân vật/nhãn hiệu của phim mẫu.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Giấy phép: code MIT, tài liệu gốc CC BY-NC 4.0 (hệ REUSE của repo); phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

## Khi nào dùng

- Poster/quy tắc thương hiệu cần "sống dậy": một hệ lưới áp lên nhiều vật phẩm, một quy tắc áp dụng lần lượt rồi sinh ra cả bộ.
- Mở đầu phim/chương trình kiểu title sequence: chữ dựng thành bối cảnh, nhạc cắt hình.
- Số liệu cần thấy bằng mắt: diện tích hình tỉ lệ với con số, một vật đi qua các cấp tỉ lệ từ nhỏ tới lớn.
- Kể chuyện bằng biểu tượng: mỗi thẻ một pictogram làm một hành động, mỗi chương một màu.
- Cảm xúc bằng nhịp và bóng: dàn bóng đen đổi tư thế đúng nhịp, bầu trời đổi màu làm đồng hồ.
- Không dùng cho: phân tích trên footage thật (đó là việc của opuscar-telestrator), giải thích máy móc bằng sơ đồ nét (opuscar-line-diagrams), hoạt hình nhân vật diễn thoại dài (opuscar-cartoons).

## Khi nào KHÔNG dùng

- Cần chiều sâu 3D, phối cảnh thật, vật liệu thật (kính, vải, kim loại): nhóm này cố tình phẳng.
- Cần vẽ nhân vật diễn cảm phức tạp: trừ `text-flash-cuts` (xem giới hạn bên dưới), các style còn lại chỉ có bóng, pictogram, hình khối — nhân vật chi tiết không phải sở trường.
- Nội dung cần tư liệu thật, ảnh lưu trữ, số liệu có nguồn trích dẫn trên màn hình: dùng nhóm Edit & Documentary.
- `text-flash-cuts` (đánh dấu ✦ trong repo): **cần máy tạo ảnh mới bắt đầu được.** Không có image generator thì không làm style này — đề xuất style khác trong nhóm (ví dụ swiss-motion hoặc pictogram-motion). Tuyệt đối không vẽ nhân vật bằng code để thay thế ảnh tạo sẵn.

## Nguyên lý cốt lõi

1. **Phẳng là luật, không phải thiếu sót.** Màu đặc, không gradient (trừ vàng kim loại của art-deco, vốn là dải kim loại có chủ đích), không bóng đổ, không hạt thừa. Thứ gì không phục vụ lưới/nhịp thì bỏ.
2. **Một màu tín hiệu, một vai.** Mỗi phim chỉ một màu nổi bật giữ vai nhân vật chính; đổi màu là đổi chương, đổi ý — không bao giờ thêm màu thứ hai cho "đẹp thêm".
3. **Chữ có khối lượng.** Chữ khổ lớn đứng cạnh chữ ghi chú tí hon; chữ trượt, đóng dấu, bị cắt, dựng thành cột, thành xe, thành cửa — chữ chiếm không gian thật trong khung hình.
4. **Mọi chuyển động bám nhịp.** Cú nhảy, cú cắt, cú xuất hiện đều rơi đúng nhịp nhạc; nhịp là lưới thời gian, như lưới không gian là lưới hình.
5. **Một ngoại lệ có chủ đích.** Cả khung hình tuân thủ hệ thống thì một phần tử phá lưới — đi thẳng, không bám nhịp, lệch khỏi hệ — sẽ trở thành nhân vật.

## Bảng 8 style — bất biến từng style

| Style (slug) | Nhận diện nhanh | Màu bất biến | Chữ | Nhịp/chuyển động |
|---|---|---|---|---|
| `swiss-motion` — đồ họa Thụy Sĩ | Giấy phẳng, chữ đen, lưới 12 cột, một màu tín hiệu | Giấy `#EAE9E5`, mực `#111111`, tín hiệu `#E30613` (hoặc `#FF5A00` / `#1F3FFF`, chọn một) | Một họ neo-grotesque (Archivo/Inter…), nhiều weight; tiêu đề có thể thường, tracking −2% ở ≥90px | Chỉ 2 đường cong: snap `cubic-bezier(.7,0,.2,1)` và tuyến tính; không nảy, không lò xo; cú nhảy bắt đầu sớm một nốt và đáp đúng nhịp; 24fps |
| `spy-titles` — mở đầu gián điệp 60s | Mực phẳng 4 màu, mép cắt tay, bóng người dạng khối, chữ là kiến trúc | Đen `#1b1714`, kem `#efe4c9`, nóng `#d23a22`, phụ ấm `#e2a52a` (có thể đổi bộ 4 mực khác) | Credit sống trong bối cảnh, không nằm dải phụ đề; phụ đề trên dải giấy cắt mép, chữ sans hình học ~44px, giữ ≥ max(1.8s, thoại + 0.6s) | Hình rối bước 12fps, camera/credit bước 24fps; nhạc brass stab là điểm cắt; có khoảng dừng toàn hình vài nhịp trong im lặng |
| `art-deco` — Art Deco | Đường viền vàng trên đen ấm, khối airbrush viền vàng, đối xứng quanh một trục dọc | Đen ấm + vàng kim (dải tối–sáng–nóng–sáng–tối) + ngà; một màu bão hòa duy nhất cho nhân vật chính | Limelight (tiêu đề), Poiret One (số, bảng hiệu), Josefin Sans (phụ đề ~40–42px), Italiana (chữ số) | Nhân vật bước 12fps, camera/ánh sáng/bóng đèn 24fps; mọi thứ mở ra từ tâm, đối xứng; bóng đèn sáng vượt ~1.6× rồi ổn định trong ~0.18s |
| `pictogram-motion` — pictogram | Mỗi thẻ một pictogram làm một hành động + tiêu đề khổng lồ + chỉ số `07 / N`; nền là lưới đĩa/nửa đĩa 5 tông một màu, hàng bị cắt lệch | 5 màu, mỗi màu 5 tông (tông giữa là nền); một màu trung tính tối; kem + mực dùng chung mọi màu | Tiêu đề grotesk 900, 150–330px ở 1080p; ngôn ngữ thứ hai là họ nặng; meta mono ~22px; HUD góc + thanh tiến độ N vạch | Mọi shot bắt đầu đúng nhịp, hành động chính đáp đúng nhịp nguyên; thẻ thường dài một nhịp (bar), thẻ phụ chạy nhanh gấp đôi; chữ trượt lên qua mặt nạ |
| `bauhaus-shapes` — hình học Bauhaus | Số thành hình: diện tích tỉ lệ với số; tròn = lớn lên/chuyển động, vuông = ở yên/nặng, tam giác = độ dốc/thời gian/trục | 6 màu theo vai (không theo sắc): giấy, nhân vật chính, trường (một mảng lớn duy nhất), trục, phụ, nền nhạt; ví dụ `#F8F7F3` / `#2138C8` / `#E9476B` / `#F4E04D` / `#0E9F7A` | Sans hình học (Jost…): từ khóa/số 800 tracking −2…−6; dòng nhẹ 300 tracking +12…+18; nhãn nhỏ caps 600–700 | Lăn thuần (vận tốc góc = quãng đường ÷ bán kính); hình lớn lên bằng vòng tròn đáp từng lớp; vuông trượt theo lưới rồi khóa với overshoot nhỏ |
| `flat-space-explainer` — du hành tỉ lệ phẳng | Màu đặc, vật sáng nằm trên 2 vòng tròn cứng; một nhân vật dẫn đường có mắt là thấu kính; tỉ lệ thật trong từng khung, có dải đọc camera | Nền xanh đêm `#1D2052`…; xanh `#3A5FD9`, bạc hà `#3FD8AE`, san hô `#FF6B5E`, vàng mặt trời `#F2A12F` (mọi "con trỏ"), kem `#F0DCC0` | Sans hình học (Jost): tiêu đề 96–132px weight 700; nhãn 26–34px weight 600; tag caps 16–18px | 24fps, mọi khung trên ones; diễn xuất có chuẩn bị–hành động–overshoot–ổn định; mắt dẫn đường mang biểu cảm (mí chớp, mống mắt cong khi cười) |
| `text-flash-cuts` ✦ — chữ chớp cắt | 3 lớp va nhau: chữ làm hình + kiến trúc biểu tượng phẳng + nhân vật phẳng chỉ 3 trạng thái (bóng đen xa / cel màu giữa / mảnh cận cảnh) | Đỏ `#d4162b`, đen `#0a0a0c`, giấy `#f2efe8`, xám `#8d8a84` (chỉ cho dòng tiếng Anh) | Noto Serif SC 900: glyph đơn 700–1100px (được tràn khung), cột thoại 120–170px; tiếng Anh Cormorant Garamond Italic 600, cỡ ~1/4 chữ chính | Thẻ chớp 2–9 frame ở 30fps; shot kiến trúc 0.3–1.6s; không gì đứng yên quá 1s; lưới nhịp 150 BPM = 12 frame/nhịp; thẻ đáp: frame 0 ở 1.08×, frame 1 ở 1.02×, rồi 1.0; rung 10–14px hai frame đầu |
| `silhouette-rhythm` — bóng đen theo nhịp | Mọi hình là một khối đen duy nhất trên nền sáng; tư thế đáp đúng nhịp; bầu trời đổi màu làm đồng hồ | Hình đen ánh tím `#090307`; trời chỉ đi qua tông ấm (vàng, cam, san hô, đỏ thẫm, magenta, tím `#1A083D`/`#380A52`); mặt trời kem `#FFF6DC`, điểm sáng `#FFB347`/`#E0245C`/`#FC4D2B` | Sans condensed nặng cho tiêu đề 120–150px (Anton…), condensed nhỏ 30–40px; chữ kem đặt ở vùng nước tối phía dưới, trái, không nằm trong mặt trời | 30fps, mọi thứ trên ones; tư thế snap vào chỗ trong ~0.13s với overshoot nhỏ rồi giữ tới nhịp sau; chân bám đất (IK 2 khớp), không trượt |

## Quy trình sản xuất

1. **Chọn style trước, chọn nhịp trước.** Style quyết định lưới, màu, chữ; tempo (BPM) quyết định mọi thời lượng. Ghi cả hai vào treatment trước khi dựng một frame nào.
2. **Treatment ngắn:** 3 cấu trúc ứng viên rồi chốt một; mỗi chương/đoạn: ý duy nhất, màu của chương, native move dùng (xem dưới), số thẻ/shot.
3. **Bảng beat là nguồn sự thật duy nhất:** một bảng mốc giây → sự kiện hình → sự kiện âm mà hình, chữ, nhạc, mix đều đọc từ đó. Nhịp hình và cue âm lệch nhau là lỗi.
4. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi phần tử là hàm của `t`, chữ và hình xuất hiện theo tiến độ trong cửa sổ beat của nó.
5. **Render thử các frame hero của từng beat** → contact sheet soát lưới, độ đọc của chữ khổ lớn, và việc màu tín hiệu có đúng một vai không — trước khi render full.
6. **Âm thanh theo bảng âm của style**, mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng

- **Swiss:** trang đôi (trái: chương trình — số, luật, ghi chú; phải: vật phẩm) → pan cứng một trang/cột → xoay 90° rồi dừng → kéo ra thành tường vật phẩm → đẩy vào một module. Chuyển đoạn bằng wipe; trong đoạn cắt cứng.
- **Spy-titles:** mở rộng trên một dòng credit → truck-in → tracking ngang một hướng → cắt cứng đúng brass stab → match cut hình học (cùng hình, cùng vị trí) → bóng người trước vòng tròn khổng lồ.
- **Art-deco:** mở từ tâm (điểm → đường mảnh → thanh mở đối xứng → chữ dâng lên → cánh + tia sáng) → cửa tách đôi dọc đường nối → cắt kiến trúc (kéo ra thấy mặt cắt tòa nhà) → đẩy vào mặt đồng hồ/huy chương.
- **Pictogram:** thẻ chương full-bleed mở chương (một màu) → thẻ mục một nhịp một thẻ → chạy nhanh gấp đôi cho nhóm phụ → tường gạch tổng kết. Nền thở: hàng trôi ngược chiều nhau, nhảy 1/4 ô đúng nhịp ở thẻ chương.
- **Bauhaus:** chấm → vạch (chấm di chuyển vẽ đường) → mặt phẳng; quả cầu tuyết lăn lên dốc, mỗi bước thêm một vòng; thước kẻ: dốc xoay phẳng, vạch dâng tới đúng chiều cao đã đạt.
- **Flat-space:** tia ngắm từ thấu kính bắn tới điểm dừng → xuyên qua vòng (vòng lớn dần lấp khung, cấp mới lớn lên bên trong từ một điểm) → dải tỉ lệ ở góc cập nhật cùng camera.
- **Text-flash-cuts:** răng cưa chữ–hình–chữ (thẻ 2–9 frame xen shot hình 3–6 frame) → ray dọc mép khung theo màu người nói → thẻ chương là một glyph khổng lồ tràn khung.
- **Silhouette:** hàng bóng đổi tư thế đồng loạt đúng nhịp → thác (cùng hành động chuyền dọc hàng, mỗi hình một nhịp/nửa nhịp) → đóng băng: hình, giọt, gợn, mây dừng; chỉ trời và mặt trời tiếp tục đổi màu.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; nhiễu "cắt tay"/rung phải suy từ hash xác định), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Lưới là dữ liệu:** ở swiss-motion, cột/hàng mang một đại lượng (tầng, giờ, quận); ở pictogram-motion, ô lưới ≈ 1/6 chiều cao khung, quy định cả dải, chuyển cảnh và tường gạch; ở bauhaus-shapes, diện tích hình phải khớp số — khung hình sai tỉ lệ thì đổi cách đóng khung, không bóp số.
- **Mép cắt tay (spy-titles):** mỗi đa giác lấy mẫu lại mỗi ~9–10px, lệch dọc pháp tuyến bằng nhiễu tần thấp (biên độ ~1.2–2.2px); cắt một lần trong không gian cục bộ rồi cache — mép cắt di chuyển cùng mảnh, không vẽ lại theo màn hình. Khe cắt ~2.4px + bóng giấy (lệch vài px, blur ~5, alpha ~0.3).
- **Vàng kim (art-deco):** dải kim loại tối–sáng–nóng–sáng–tối, animate `sheen` để quét sáng; nét vàng đặc trưng có gạch chân khắc tối rộng hơn ~1.6px + highlight mảnh trên cùng. Không viền đen kiểu cartoon.
- **Chữ giữ tối thiểu:** chữ bắt buộc đọc giữ ≥ max(1.8s, thoại + 0.6s); thẻ cần đọc số giữ ≥ 1.6s; credit trong spy-titles phải có khoảnh khắc đọc trọn dòng. Kiểm tra bằng `TEXTS(t)`.
- **Âm thanh:** nhạc có lưới riêng (motorik/krautrock, techno tối giản, marimba cho swiss; big band gián điệp 60s với brass stab là điểm cắt cho spy-titles; jazz giao hưởng 20s–30s cho art-deco; bộ gõ làm xương sống + nhạc cụ màu theo chương cho pictogram; tiếng vật liệu in ấn khô, không reverb cho swiss; tiếng giấy/kim loại cho spy-titles). Foley khớp hình từng cú đáp/cắt/đóng dấu. Mix cuối chuẩn −14 LUFS.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1920×1080, 24fps — riêng text-flash-cuts 30fps, silhouette-rhythm 30fps), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) mọi phần tử bám lưới (không lệch nửa ô, không tràn cột ngoài chủ đích); (b) chỉ một màu tín hiệu giữ vai chính; (c) chữ khổ lớn đọc được, không bị cắt mất phần cần đọc (trừ glyph tràn khung có chủ đích ở text-flash-cuts).
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn thẻ, không đè lên hình cần thấy.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame; cú snap/cắt rơi đúng nhịp.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Riêng bauhaus-shapes: đối chiếu diện tích hình với số liệu gốc — sai tỉ lệ là lỗi nội dung, không phải lỗi thẩm mỹ.
- Riêng text-flash-cuts: xác nhận ảnh đã có từ máy tạo ảnh trước khi dựng; không có ảnh thì dừng và đổi style, không vẽ nhân vật bằng code.
- Bản quyền: font dùng phải OFL và tự host; không gắn tên/logo/nhân vật thật vào phim; credit hư cấu, không dùng tên người thật.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: style đã dùng + tempo, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.
