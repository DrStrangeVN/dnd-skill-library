---
name: opuscar-screens-interfaces
description: Kỹ thuật làm phim về màn hình và giao diện kiểu Lemo-Opuscar (nhóm Screens & Interfaces, 6 style) — keynote tối, ghi màn hình có linh vật pixel, HUD hologram quét vật thể, bàn làm việc với thẻ giao diện giấy, phim trong bảng tính, và thế giới 2 mực chấm dither. Dùng khi brief là giới thiệu phần mềm/sản phẩm số, hướng dẫn dùng app, giải thích thông số kỹ thuật, hoặc kể chuyện bằng chính giao diện. Màn hình là sân khấu; mọi giao diện đều vẽ lại bằng code, không quay màn hình thật, không dùng ảnh chụp giao diện của sản phẩm khác.
---

# Opuscar Screens & Interfaces — Màn hình & Giao diện

Sáu cách biến màn hình thành sân khấu. Điểm chung của cả nhóm: cái người xem nhìn là giao diện — nhưng giao diện đó được vẽ lại hoàn toàn bằng code (HTML/CSS/SVG/canvas/three.js), nên camera đi được bất cứ đâu, chữ luôn sắc nét ở mọi mức zoom, và mọi pixel đều nằm dưới quyền kiểm soát của đạo diễn. Không bao giờ quay màn hình thật, không dùng ảnh chụp giao diện của người khác.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Giấy phép: code MIT, tài liệu gốc CC BY-NC 4.0 (xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill); phim do mình làm ra thuộc về mình. Nội dung dưới đây viết lại bằng lời của mình, chỉ giữ các bất biến kỹ thuật (màu hex, thông số, luật nhịp, luật đọc chữ).

## Khi nào dùng

- Giới thiệu một phần mềm, ứng dụng, tính năng mới: keynote tối (`dark-keynote`) hoặc ghi màn hình có linh vật (`living-screencast`).
- Giải thích thông số kỹ thuật của một vật thể: quét hologram (`hologram-hud`).
- Kể quy trình qua nhiều công cụ: bàn làm việc một cú máy dài (`desktop-flythrough`).
- Kể chuyện bằng dữ liệu trong bảng tính: mỗi ô là một điểm ảnh (`spreadsheet`).
- Muốn một thế giới 3D mà chỉ có hai mực: chấm dither (`one-bit-dither`).
- Không dùng cho: phim kể chuyện nhân vật (nhóm Cartoons / Painting), giải thích máy móc bằng sơ đồ nét (nhóm Line Diagrams), điều tra bằng chứng từ dữ liệu thật (nhóm Instruments & Evidence).

## Khi nào KHÔNG dùng

- Brief cần cảm xúc nhân vật, diễn xuất, gương mặt: nhóm này không có nhân vật diễn — "nhân vật" ở đây là con trỏ, linh vật pixel, hoặc chính giao diện.
- Cần chứng minh bằng dữ liệu/tư liệu thật có nguồn: đó là việc của `opuscar-instruments-evidence` (ảnh vệ tinh, LiDAR, hiển vi) và `opuscar-data-maps` (biểu đồ, bản đồ).
- Muốn vẽ tay, vẽ cọ, chất liệu giấy/vải: sang nhóm Sketch & Board, Painting & Illustration, Traditional Crafts.
- Sản phẩm thật có giao diện riêng mà brief bắt phải giống hệt từng pixel: nhóm này vẽ lại giao diện theo tinh thần sản phẩm, không sao chép giao diện, logo, font hệ thống hay tên của bất kỳ sản phẩm thật nào. Nếu brief yêu cầu quay màn hình thật thì đây không phải nhóm đúng.

## Nguyên lý cốt lõi

1. **Màn hình là sân khấu, độ chính xác của giao diện là vẻ đẹp.** Mọi phần tử bám lưới, mọi chuyển động đáp đúng nhịp, mọi âm thanh thuộc một họ đã thiết kế.
2. **Một màu nhấn duy nhất.** Mỗi style trong nhóm chỉ cho một màu nhấn làm vai chính; màu thứ hai (nếu có) chỉ xuất hiện khi có vai trò riêng và biến mất cùng vai trò đó.
3. **Vẽ lại, không chụp lại.** Giao diện thật được dựng lại bằng code để camera tự do; nội dung demo (code, số liệu, kết quả test) phải nhất quán và ứng dụng trong phim phải thay đổi thật theo hành động.
4. **Chữ là một thành phần giao diện**, không phải lớp phủ ngoài: phụ đề nằm trong thẻ/toast/pill của chính thế giới đó, giữ tối thiểu theo công thức đọc (xem từng style).
5. **Kịch tính đến từ đối lập có trật tự**: lộn xộn → một hành động quyết đoán → khoảng trống; hoặc: chưa thấy → quét tới → con số khóa lại.

## Hệ màu / bảng chất liệu bất biến (theo style)

### dark-keynote — Keynote công nghệ nền tối
- Sân khấu gần đen, hơi lạnh (không nâu ấm), lưới mảnh trắng ~3% (mỗi đường thứ 4 ~6%) trên module 48 px, vignette góc 50–55%, không hạt nhiễu. Ba bậc mặt nổi tối, viền 1 px (~8% trắng), highlight trong 1 px ở mép trên.
- Chỉ một màu nhấn bão hòa, có glow riêng, dành cho thứ sản phẩm *là* hoặc *làm*: ví dụ chanh `#B7F34A`, tím điện `#8B7CFF`, cam tín hiệu. Hai thứ cùng màu nhấn là sai. Màu báo lỗi (thường đỏ) chỉ tồn tại trong lúc lỗi còn đó, xong là biến mất hẳn.
- Chữ: Inter cho UI/phụ đề/tiêu đề, Inter Tight 600 cho con số khổng lồ (tracking khoảng −4,5%), JetBrains Mono cho nhãn, tên file, trạng thái. Một dòng tiêu đề mỗi màn hình; con số lớn có màn hình riêng, không caption đè lên.

### living-screencast — Ghi màn hình có linh vật pixel
- Màu sắc theo đúng theme sáng/tối thật của sản phẩm. Linh vật giữ màu của sản phẩm/thương hiệu, hoặc một hue bão hòa mà không phần tử UI nào dùng, để mắt luôn tìm thấy nó.
- Linh vật và đạo cụ (bút chì, dấu "!", tia sáng, bụi) chung một lưới pixel vuông, cạnh sắc; vị trí bám theo nửa pixel nên chuyển động có bước. Linh vật chỉ đứng trên mép trên của một phần tử thật (ô nhập, menu, dòng code, nút, thanh trạng thái, chữ tiêu đề) — vị trí đo từ DOM đang chạy mỗi khung hình, không đặt tay bằng tọa độ.
- Hai diễn viên, không bao giờ có bàn tay: con trỏ là người dùng, linh vật là phần mềm. Cửa sổ app nổi trên hình nền desktop, zoom không bao giờ vượt ra ngoài màn hình.

### hologram-hud — HUD hologram khoa học viễn tưởng
- Một hue lạnh làm chủ + một màu ấm làm nhấn. Hue lạnh mang đường nét, HUD, vùng fill. Màu nhấn chỉ dùng cho giá trị đã khóa: con số chuyển sang màu nhấn đúng khung hình nó trở thành thật, không dùng vào việc khác. Trắng là nhiệt: cạnh gần trắng và flash một khung đánh dấu thứ đang hoạt động.
- Vật thể luôn là wireframe ánh sáng trên bệ chiếu tròn, nét cộng ~1,3 px, sương chiều sâu (xa chỉ còn ~25% độ sáng), hai lượt glow độ phân giải thấp. Ba lớp chiều sâu luôn có: lưới chấm nền (parallax chậm), vật thể với bệ và sàn, HUD tiền cảnh (khung góc, thước parallax nhanh, chữ trạng thái).
- Chữ: Rajdhani viết hoa (Light cho số lớn và tên sản phẩm, Medium/SemiBold cho nhãn), Share Tech Mono cho dữ liệu vi mô. Số dùng font mono để cuộn số không rung; dấu thập phân là ô vuông nhỏ.

### desktop-flythrough — Bàn làm việc, thẻ giao diện bay qua
- Nền sáng: thảm giấy có lưới chấm, bàn gỗ sáng, thẻ gần trắng cùng nhiệt độ màu, một mực tối để in, một màu nhấn dành cho thứ đang quan trọng (lộ trình, huy hiệu bước hiện tại, nút gửi, cửa sổ sáng, từ khóa). Đỏ chỉ cho lỗi/trục trặc, xanh lá chỉ cho thành công.
- Ánh sáng: một mặt trời hướng thấp từ phía sau-trái (cao khoảng 20°, bóng dài gấp 2–3 lần vật), bản đồ bóng mềm 4096 bám theo mục tiêu camera, fill bán cầu trời lạnh/đất ấm (bóng xanh, mặt sáng ấm).
- Diễn viên là sprite pixel dựng thành khối voxel: một khối vát mỗi pixel, dày hơn ở trong, mắt nổi lên; kích thước khoảng 1/5–1/3 thẻ nó đứng (mỗi pixel ~0,006–0,0075 đơn vị, sprite 16 px rộng ~0,1). Nhỏ hơn nữa là mất mặt trong cảnh vừa.

### spreadsheet — Phim trong bảng tính
- Trang trắng; màu chỉ có nghĩa khi một luật định dạng có điều kiện kích hoạt. Tối đa 5 hue làm việc + xám ấm của vỏ phần mềm: hai cho nhị phân/phân loại chính, một cho biến thứ hai, một cho nhân vật chính (ô được chọn, kết quả thắng), còn lại là mực.
- Ô ở 100% rộng khoảng 2,9:1 (mẫu dùng 64×22 px); mọi đường chéo và cong đều thành bậc thang ngang. Mỗi ô được tô đều giữ một giá trị nhỏ, mờ (1/0, chữ cái mã, bậc thang màu) và giá trị đó chọn màu fill.
- Vỏ phần mềm không bao giờ rời khung hình: thanh tiêu đề, thanh công cụ, ô tên, thanh công thức, chữ cái cột, số dòng, tab trang, thanh trạng thái. Vỏ không zoom; chỉ trang tính zoom.

### one-bit-dither — Hai mực chấm
- Đúng hai màu trên màn hình, chọn một lần cho cả phim: mực gần đen và giấy trắng hơi ngả (ấm, lạnh hoặc xám xanh). Không màu thứ ba, kể cả chữ hay thẻ kết. Ví dụ: mực `#16161A`, giấy `#E9E6D6`.
- Mỗi môi trường một loại chấm riêng: thế giới là dither có thứ tự (Bayer 8×8); bản fax/ảnh in là khuếch tán sai số (chấm hữu cơ kiểu Atkinson) ở bước cố định; ảnh báo là lưới halftone 45°, cỡ chấm theo tông. Chấm bám theo bề mặt vật (không gian vật thể), camera di chuyển chấm vẫn đi cùng vật như texture in.
- Khung hình render ở 960×540 rồi phóng lên bằng nearest neighbour; chi tiết chọn cho lưới đó.

## Quy trình sản xuất

1. **Chốt brief và style trước.** Sáu style này trông giống nhau ở chỗ đều có màn hình, nhưng ngữ pháp khác hẳn: keynote tối kể bằng con số và khoảng trống; ghi màn hình kể bằng hành động thật của app; hologram kể bằng quét và khóa số; bàn làm việc kể bằng một cú máy dài; bảng tính kể bằng công thức; dither kể bằng hai mực. Chọn sai style thì treatment không cứu được.
2. **Treatment ngắn trước khi dựng:** một ý chính, tối đa 2 ý phụ; mỗi ý: phát hiện duy nhất là gì, cần mấy beat, beat nào là đỉnh. Với `living-screencast`: liệt kê đúng tính năng, nút, chế độ của sản phẩm thật — tra tài liệu sản phẩm, thứ không có trong tài liệu thì không có trong phim.
3. **Dựng page theo page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` thuần theo `t` (cấm `Date.now()`, cấm `Math.random()` không seed), `window.EV` — danh sách sự kiện âm thanh `{t, type}`, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`. Render bằng cách seek `t` qua headless Chrome.
4. **Timeline là nguồn sự thật duy nhất:** một bảng beat (mốc giây → sự kiện hình → sự kiện âm) mà hình, phụ đề, nhạc, mix đều đọc từ đó.
5. **Render thử các frame hero của từng beat** → contact sheet soát thứ tự lập luận, độ bám lưới, độ đọc được của chữ trước khi render full.
6. **Âm thanh theo bảng âm của style, mix xong đo loudness trên file cuối** (chuẩn −14 LUFS, trừ `one-bit-dither` đo −16 LUFS trước mastering, true peak ≤ −3 dBTP), QA đầy đủ rồi mới giao.

## Ngữ pháp dựng (theo style)

- **dark-keynote:** hỗn loạn do luật sinh ra (hàng trăm mục sinh nhanh dần) → một hành động quyết đoán → khoảng trống. Mọi thứ đáp xuống lưới và đáp đúng nhịp; chuyển động bắt đầu sớm hơn nhịp một nhịp. Spawn ngắn có kiểu (rơi + nảy, quăng, trượt vào, bật; 0,2–0,3 s), một kiểu chuyển động cho mỗi loại phần tử. Easing fast-out với một overshoot nhỏ (`back`, s ≈ 1,3). 24 fps, từng khung, không stepping, không sôi.
- **living-screencast:** một cú máy liên tục trong màn hình, zoom ≥ 1, chỉ cắt ở chỗ chuyển chương. Con trỏ di chuyển mượt (spring-eased), nhấn nhẹ khi click, không dịch chuyển tức thời. Linh vật nhảy có lấy đà, duỗi khi cất cánh, co chân, đáp squash với nảy tắt dần và bụi; mắt diễn (nhìn về thứ quan trọng). Mọi hành động của linh vật phải gây ra thay đổi trạng thái thật của UI. 30 fps; UI từng khung, linh vật bước theo lưới pixel.
- **hologram-hud:** mặt quét dựng mô hình → target box khóa (vừa khung trong ~0,2 s, flash trắng 3 khung đúng nhịp) → tách rời cục bộ dọc trục lắp ráp → leader kéo ra (vòng neo → chéo → ngang tới thẻ, ~0,5 s) → con số cuộn từ ký tự rác thành giá trị thật, khóa phải→trái, chuyển màu nhấn đúng nhịp với flash một khung → giá trị xong trượt vào ray bên. 24 fps, từng khung; chỉ glyph xáo trộn là bước theo khung.
- **desktop-flythrough:** một cú máy, không cắt. Camera lướt, bay quanh, cẩu và whip giữa các trạm; kết bằng pull-back toàn bàn. Một tempo ổn định (110–130 BPM); mọi hành động trên lưới 16 nốt, khoảnh khắc lớn đúng nhịp mạnh. Nhảy: cung có squash và stretch (giãn ~14% trên không, squash ~30% trong 0,2 s khi đáp, squash lấy đà trước khi cất cánh). Nhóm di chuyển nối đuôi, mỗi con chậm hơn con trước một nốt 16. 30 fps.
- **spreadsheet:** một beat bắt đầu bằng công thức gõ từng chữ trên thanh công thức (14–30 ký tự/giây; một công thức gõ xong trong ~0,8–1,4 s; con trỏ nhấp 4 Hz), Enter là cắt cứng trạng thái: ô nhập đóng, giá trị bật lên 30%, trang tính phản ứng. Tô màu lan theo vòng hoặc quét từ một ô (vài chục mili-giây mỗi ô, thanh trạng thái đếm số ô). Ô di chuyển bám lưới: vị trí snap theo ô nguyên nên ô nhảy từng bước. Camera (zoom, cuộn) mượt từng khung. 24 fps.
- **one-bit-dither:** camera di chuyển mượt (khóa spline, ease vào/ra), tránh pan ngang nhanh qua cấu trúc lặp mịn. Không có "vách vận tốc": dừng đột ngột, khởi động hết tốc, giữ 0,1 s giữa chuyển động đều đọc thành giật — nối các đoạn camera bằng vận tốc liên tục (Hermite/Bézier, chồng và blend), giữ tốc độ xoay dưới ~3°/khung. Đảo ngược mực (đổi mực↔giấy một hai khung) là điểm nhấn của chất liệu: chỉ dùng cho cú va chạm, không trang trí. 30 fps, từng khung.

## Công thức & kỹ thuật đặc thù

- **dark-keynote:** sân khấu 2.5D (`s = 1/(1/zoom − z)`), thẻ gần ống kính mờ với phóng đại; xoay dùng strip-rendered perspective (rotY ≤ ~24°). Ánh sáng là công cụ reveal: chỉ pixel ánh sáng đi qua mới bật. Phụ đề là toast dưới-giữa (pill tối mờ, viền sáng 1 px, Inter 500 ~40 px, chấm nhấn nhỏ "đang nói"), vào bằng rise + fade ~0,16 s, giữ ≥ max(1,8 s, lời nói + 0,6 s).
- **living-screencast:** rack focus (mờ panel không quan trọng, không bao giờ mờ chữ cần đọc), motion blur chỉ trên whip (làm mờ trên wrapper chưa transform). Lớp thông tin duy nhất được phép phủ: pill chương (01–04), HUD phím bấm kiểu KeyCastr, pill phụ đề kính mờ, tag tua nhanh "▶▶ 4×" khi có.
- **hologram-hud:** bệ chiếu phối cảnh thật (vòng đồng tâm một sáng một đứt nét, vạch, tia mờ), xoay chậm và xoay theo mọi chuyển động turntable. Hologram đặc: mặt fill bằng Fresnel × interlace cuộn, đường nét dày lên khi bật sáng, sóng sáng leo dọc mô hình. Chữ không bao giờ nằm trên wireframe: mỗi khối chữ có plate tối riêng (gần đen mờ, viền 1 px, vạch góc).
- **desktop-flythrough:** three.js PBR, tone mapping trung tính; thẻ 0,3–0,7 đơn vị rộng (1000 px canvas mỗi đơn vị), chấm cách 0,03. Pop sticker→đồ chơi trong 0,25–0,5 s (bật bản lề với overshoot, ô pixel đùn từ giữa, nhảy nhỏ, squash khi đáp). Chữ chỉ đọc được khi camera ngẩng 55–70°; camera thấp thì chữ phải nằm trên vật đứng (thẻ lều).
- **spreadsheet:** canvas 2D, một hàm world→screen; độ rộng cột biến thiên là một phần của mô hình (cột ẩn rộng 0, mọi vị trí x là tổng tiền tố độ rộng, mở/đóng cột làm toàn trang reflow và camera đi theo). Giá trị ô ở 11 px × zoom; dưới ~6,5 px thì không vẽ giá trị nữa. Ô được tô flash trắng ~0,12 s khi luật kích hoạt. Phụ đề là ghi chú ô: note vàng nhạt, viền mực, tam giác đỏ ở góc, dock dưới-trái, một dòng ngôn ngữ phim trên một dòng ngôn ngữ thứ hai, không wrap.
- **one-bit-dither:** ba lượt render: (1) shading vào target half-float 960×540; (2) G-buffer ghi normal octahedral, ngưỡng Bayer gắn bề mặt, độ sâu (độ sâu âm đánh dấu lớp không có outline: trời, glow, tia sáng); (3) 1-bit: luminance → gamma → `smoothstep(lo, hi)` → so với ngưỡng; outline từ gãy độ sâu/normal. Chữ sống trong thế giới (viết, gõ, stencil, in, đóng dấu lên vật), không caption phủ; CJK ≥ 11 px nội bộ mới đọc được, Latin cap height ≥ 9 px nội bộ.

## Âm thanh (theo style)

- **dark-keynote:** bộ gõ lên dây và pad (marimba, vibraphone, glockenspiel, celesta, pad synth, xung sine trầm, shaker, synth pluck, piano nỉ). Nhạc là một quá trình nhìn thấy được: phasing, cộng dần (một nốt mỗi bar), trừ dần, chia nhịp để tăng tốc thay vì đổi tempo. Hai họ âm = câu chuyện: lộn xộn nghe *rải rác* (lệch tông hàng chục cent, pan ngẫu nhiên, mỗi âm một timbre), trật tự nghe đồng nhất.
- **living-screencast:** hai độ phân giải trong nhạc — lớp hi-fi (piano, bass, kit, glockenspiel) là thế giới, giọng chiptune square/pulse là linh vật; hai lớp có thể đổi vai, song ca, hòa vào nhau. Foley: phím gõ (thock + click, jitter thời gian như người thật), click trackpad, swish panel, pop popup, chuông thông báo, tick CI, màn trập chụp màn hình; bước/nhảy/đáp của linh vật là 8-bit.
- **hologram-hud:** nhạc đi trước, trên lưới (một bar = một beat thông tin); khóa đáp đúng nhịp mạnh. Synth: arpeggio saw/square với delay ping-pong, pulse vuông, bass 8 nốt, hat và clap synth, pad saw lệch tông. Mật độ theo thông tin: half-time để có thời gian đọc, một beat **im lặng số thật**, drop, thêm/bớt lớp theo từng bộ phận.
- **desktop-flythrough:** nhạc sáng ấm, cảm giác acoustic (marimba, vibraphone dưới nốt dài, bass pluck, kick synth mềm, clap, shaker, pad dây lặng). Một tông, hợp âm diatonic, khoảng một hợp âm mỗi bar. Dưới lời thoại nhạc duck ~16 dB. Foley: mọi hành động đều có tiếng — pop (nốt marimba theo hợp âm hiện tại + sweep lên), hop (tick mềm), đáp (thump nỉ), ding (hai nốt chuông theo hợp âm), whip camera (whoosh theo tốc độ camera đo được).
- **spreadsheet:** foley của trang tính — click phím mỗi ký tự gõ, clack + thump trầm khi Enter, tick mỗi lần ô được chọn nhảy, blip sine nhỏ mỗi ô được tô (cao độ tăng theo tiến độ), click ratchet mỗi cột mở, pop menu/kết quả, ding cho giá trị thắng, whoosh cho zoom lớn. Nhạc office-pop (kit, bass điện, piano stab, marimba, xylophone, glockenspiel); tăng tốc bằng cách làm dày pattern, không đổi tempo.
- **one-bit-dither:** chất liệu cơ khí, in ấn — đồng hồ, relay, tone quét, xước stylus, giấy, dấu cao su trên nút bần, công tắc, motor. Nhạc: ensemble nhỏ, hơi lạnh (clarinet/bass clarinet, glockenspiel, pizzicato và dây trầm bowed, piano upright hơi lệch tông, brushed). Im lặng là công cụ: cắt hết nhạc cho chân không/đêm/verdict, giữ một yếu tố xa, đã lọc để im lặng không chết.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1280×720 hoặc 1920×1080, 30 fps trừ `dark-keynote`/`hologram-hud` 24 fps), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) chữ đọc được ở zoom nó xuất hiện (đặc biệt `spreadsheet`: số lời thoại dùng phải ≥ 26 px trên màn hình; `one-bit-dither`: chữ đủ đậm, không xám); (b) linh vật chỉ đứng trên mép trên phần tử thật, không che chữ cần đọc (`living-screencast`); (c) không có hai thứ cùng màu nhấn (`dark-keynote`, `hologram-hud`); (d) chấm dither không bơi khi camera di chuyển (`one-bit-dither`).
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn thẻ, nhãn nằm trên vùng trống, không đè lên thứ nó mô tả.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame.
- Loudness đo trên file cuối: −14 LUFS ± 0,5 (riêng `one-bit-dither` −16 LUFS trước mastering); blackdetect: 0 đoạn đen ngoài chủ đích.
- Bản quyền: ghi rõ nguồn giao diện/số liệu/hình nền trong QA.md; không dùng tên/logo/font hệ thống/giao diện của bất kỳ sản phẩm, hãng hay đài thật nào. Không gắn tên/logo đội bóng, cầu thủ, đài truyền hình thật vào phim dựng bằng code.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: nguồn tư liệu + licence, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.
