---
name: opuscar-edit-documentary
description: Kỹ thuật dựng phim tư liệu và bản tin từ tư liệu thật (spin-out từ bộ Lemo-Opuscar) — caption dẫn nhịp xem không cần tiếng, phim thời sự thập niên 1920, đếm ngược chia màn hình theo thời gian thực, giao hưởng thành phố cắt theo nhạc, điều tra bằng hình ảnh đồng bộ nhiều nguồn, montage kiến tạo hai tông mực, và bản tin truyền hình trọn gói. Dùng khi brief là "làm tin tức/bản tin/tư liệu từ footage, ảnh lưu trữ và tài liệu thật có nguồn", "điều tra một sự kiện bằng nhiều nguồn", "kể một thành phố bằng nhạc và time-lapse", hoặc "gói một tuần tin thành bulletin". Mọi nội dung (chủ đề, tư liệu, số liệu) do brief quyết định — skill chỉ giữ ngữ pháp dựng và kỷ luật bằng chứng.
---

# Opuscar Edit & Documentary — Dựng phim & Tư liệu

Nhóm này không vẽ ra thế giới — nó sắp xếp lại thế giới thật: footage, ảnh lưu trữ, tài liệu, số liệu có nguồn. Chất liệu nằm ở cách cắt, cách đặt chữ lên hình và cách âm thanh dẫn nhịp. Tám style trong nhóm, mỗi style một luật dựng riêng, nhưng chung một kỷ luật: tư liệu có trước, treatment có sau, mọi con số đều có nguồn hiển thị trên màn hình.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Code gốc MIT, tài liệu gốc CC BY-NC 4.0; phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

Nguồn kỹ thuật: các style `caption-news`, `newsreel`, `countdown`, `city-symphony`, `visual-investigation`, `kino-montage`, `telestrator`, `news-package` trong repo Lemo-Opuscar — đọc `STYLE.md` gốc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện, tên phim demo, nhân vật hay nhãn hiệu thật trong demo của repo.

## Khi nào dùng

- Tin tức xã hội xem không cần tiếng: caption khổ lớn dẫn nhịp, số liệu kèm nguồn trên màn hình (caption-news).
- Kể một câu chuyện lịch sử bằng phim lưu trữ, báo cũ, điện tín, bản đồ (newsreel).
- Một sự kiện thật chạy đúng thời gian thực với đồng hồ đếm ngược làm chủ (countdown).
- Chân dung một thành phố bằng time-lapse/hyperlapse cắt theo nhạc viết trước (city-symphony).
- Điều tra, đối chiếu một sự kiện bằng nhiều nguồn độc lập cùng chỉ vào một thời điểm (visual-investigation).
- Lập luận bằng tư liệu cắt theo nhịp, in hai tông mực giấy (kino-montage).
- Bản tin tuần trọn gói: sting → rundown → từng tin → điểm danh → chào kết (news-package).
- Phân tích thể thao vẽ trên hình: xem skill chuyên sâu `opuscar-telestrator` (mục telestrator bên dưới chỉ trỏ sang đó).

## Khi nào KHÔNG dùng

- Không dùng nhóm này khi brief cần vẽ tay, minh họa hay mô phỏng: đó là việc của `opuscar-painting-illustration` (tranh vẽ), `opuscar-sketch-board` (vẽ bảng giải thích) hoặc `opuscar-line-diagrams` (sơ đồ nét).
- Không dùng khi không có tư liệu thật: nhóm này cấm dùng ảnh tạo sinh thay cho footage lịch sử. Chưa có tư liệu thì đi tìm tư liệu trước, không dựng phim bằng hình bịa.
- Không dùng caption-news cho phim cần đồ thị dài hơi (đó là việc của nhóm dữ liệu/bản đồ); không dùng newsreel cho phim tài liệu hiện đại có talking-head; không dùng countdown cho montage nhảy thời gian (thời gian thực là luật, không được tua hay đảo thứ tự).
- Không dùng visual-investigation để kể chuyện cảm xúc: không slow-motion cảnh thảm họa, không nhạc gợi cảm xúc thay cho bằng chứng.

## Nguyên lý cốt lõi

1. **Tư liệu trước, treatment sau.** Hỏi user có footage, ảnh, tài liệu, dữ liệu của mình không (kèm quyền sử dụng) trước khi viết treatment. Tư liệu của user luôn đứng trước tư liệu tìm được.
2. **Mọi con số đều có nguồn trên màn hình.** Số không có nguồn thì bỏ. Số mạnh hơn nguồn nói là lỗi: viết đúng điều nguồn nói, giữ `FACTS.md` (khẳng định → URL → câu trích gốc → phép tính dẫn xuất kèm số học).
3. **Nhịp dựng là luật, không phải cảm tính.** Mỗi style có một lưới nhịp riêng (120 BPM, 60 BPM, nhịp của ban nhạc thời kỳ) — mọi cú cắt, cú đập chữ, cú vào nhạc đều nằm trên lưới đó.
4. **Chữ là đồ họa, không phải phụ đề dán thêm.** Caption, thẻ nguồn, thẻ địa danh, tem, bảng số đều là một phần của bố cục khung hình, có vị trí, cỡ chữ và thời gian đọc cố định.
5. **Một khung hình, một phát hiện.** Mỗi shot nói một ý; mỗi layout điều tra nói một kết luận. Nhồi hai ý vào một khung là lỗi phải tách.

## Tám style trong nhóm

### 1. Caption News — tin tức đọc được khi tắt tiếng

- **Bản chất:** phim tin xã hội cho feed: footage thật làm nền, caption khổ lớn làm diễn viên chính, mỗi con số đều kèm nguồn hiển thị.
- **Bảng màu:** mật ong `#FFC21A` = điểm nhấn/từ khóa/tăng; đỏ `#FF4A3D` = mất mát/con số xấu; ngà `#F7F5EF` = chữ; xám `#8D8B83` = nhãn/đơn vị; `#5E5C55` = cột không quan trọng; nền thẻ số liệu `#151512` với đường kẻ mờ mỗi 54 px và lề đỏ đôi.
- **Chữ:** dòng chính sans đậm 88 px (dòng kết luận 110 px), ngà, bóng mờ tối 20 px, chia 2–3 cụm, mỗi cụm đập vào sau cụm trước 0,12 s (scale 1,3 → 1 trong 0,13 s); một từ khóa duy nhất trong khối vàng `#FFC21A`, chữ chuyển thành mực `#0E0E0C`; dòng tiếng Anh nhỏ hơn bên dưới, mờ dần và dâng 10 px trong 0,18 s. Một dòng mỗi ngôn ngữ, không ngắt dòng; caption giữ ≥ 1,8 s, lý tưởng ≥ câu nói + 0,6 s.
- **Nhịp:** cắt trên lưới nửa nhịp 120 BPM (mọi cú cắt là bội số của 0,5 s); shot footage 1,5–3 s, thẻ dữ liệu/tài liệu 3–4,5 s; so sánh giữ đến khi mọi mục đã hiện đủ ≥ 2,5 s.
- **Đồ họa:** thẻ số liệu trượt từ phải vào trong 0,18 s; bộ đếm lăn với ô số cố định bề rộng (không rung); biểu đồ vẽ từng đoạn, điểm chính có vòng lan 0,7 s; bản đồ tô theo 5 bước một tông màu; tài liệu hiển thị ở 220 dpi trên bàn tối, highlight quét trái → phải 0,3–0,5 s theo tọa độ trích xuất từ file gốc; chia đôi màn hình có vạch vàng 4 px; lưới 3 panel dâng lệch nhau 0,1 s.
- **Âm thanh:** nhạc 120 BPM (kick theo nhịp, bass nốt tám, marimba nốt mười sáu, kèn đồng staccato vào con số lớn), giọng đọc nhanh hơn nhạc ~8 dB; hook đánh ngay frame thứ 4; một khoảng lặng cứng trước bước ngoặt; foley cho mọi thao tác đồ họa (đập cụm chữ, tick bộ đếm mỗi 45 ms, tiếng highlight, tiếng đóng tem). Master −14 LUFS, true peak ≤ −1 dBTP.
- **Chiêu đặc trưng:** số lớn nhất xuất hiện ngay frame 4 và lăn tới giá trị trong 0,45 s; một đường vàng quét qua footage tới đúng phần trăm, phần đã quét chuyển xám tối; tài liệu được highlight rồi con số bật ra thành khối vàng bên cạnh trang giấy; freeze + câu hỏi với nhạc cắt sang im lặng.

### 2. 1920s Newsreel — phim thời sự thập niên 1920

- **Bản chất:** tư liệu thật trong khung máy chiếu, vật phẩm tin tức (báo, tạp chí, điện tín, bản đồ, đĩa hát) được quay phim thật thay vì đánh máy thành slide; giọng thuyết minh ngắn, dí dỏm, nói trên tất cả.
- **Khung hình:** cửa chiếu 1480×1080 trong 1920×1080 (tỉ lệ 1,37:1), bo góc 26 px, đen tuyệt đối bên ngoài; không vẽ gì ngoài cửa chiếu. Hai lớp: lớp hình (chịu grade phim) và lớp chữ (giữ sắc nét, đứng yên).
- **Grade:** đơn sắc bạc ấm: xám hóa → kéo percentile (0,6% → đen, 99,6% → trắng; bản in 0,2–0,3% / 99,0–99,7%, đen nâng lên 26–30) → đường cong S nhẹ → ra 14–238; phủ ấm `#efe7d6` (multiply) + `#17140f` (screen); vignette 0,42H → 0,95H; nhấp nháy ±3,5% mỗi frame + trôi 3 Hz; rung cửa ±1,6/±2,2 px; 0–3 vết xước dọc sống 9 frame; 0–4 hạt bụi 1 frame. Một bộ mức sáng cho cả clip, không tính lại từng frame. Upscale tư liệu tối đa ~2,5×; phim 24 fps.
- **Màu/chữ:** hình bạc ấm; chữ kem trên gần đen (`#f3eee4`/`#d6cfc0` trên `rgba(12,11,10,.8)`), khung 2 px kem; chữ bạc gradient cho ident (`#fff → #d9d4ca | #9e978a → #efebe2`, ngắt cứng ở giữa, viền đen 0,12 em). Không màu nhấn, không phủ sepia. Ident dùng font display cổ điển 104–118 px; thẻ địa danh "ĐỊA ĐIỂM · NGÀY" chữ hoa 26–34 px; phụ đề 40 px trên 29 px, dải tối đáy cửa chiếu cao 180 px, giữ qua khoảng trống < 1 s để không nhấp nháy.
- **Nhịp:** ban nhạc là đồng hồ: tempo 190–220 BPM, mọi cú cắt, cú đáp, cú vào nhãn nằm trên nhịp, đa số cắt ở vạch nhịp; shot lưu trữ 1,5–2,5 s, bản in 2,5–4 s. Chuyển đoạn chỉ dùng thủ pháp thời kỳ (iris, wipe chéo viền sáng 6 px, lật trục dọc, mành 12 lá, wipe đồng hồ từ 12 giờ, giấy xoay, lật trang, đẩy panel, freeze) — mỗi thủ pháp dùng một lần như dấu câu; không dissolve.
- **Âm thanh:** giọng thuyết minh sáng, tốc độ ~1,15–1,2, 6–12 từ mỗi câu, xử lý như rãnh quang 1930 (high-pass 260 Hz, low-pass 3,7 kHz, +4 dB ở 1,5–2,3 kHz, wow 0,22% ở 0,55 Hz); ban nhạc (tuba nhịp 1–3, banjo 4 phách, kèn trombone, piano honky-tonk, trumpet tắt tiếng rồi mở); đĩa 78 vòng công cộng có thể tiếp quản nhạc nền; tiếng máy chiếu (24 Hz) chạy từ đầu tới cuối. Giọng ~12 dB trên nhạc.
- **Chiêu đặc trưng:** nghi thức ident (đèn rọi bật, quả cầu xoay, iris khép); tờ giấy xoay và đập xuống; bản đồ lan theo nhịp với tiếng điện tín; lưới ảnh đáp từng ô theo nhịp rồi dive vào làm flip-book; gạch dưới bằng chì mềm trên tài liệu; freeze + khoanh tròn bằng bút mỡ.

### 3. Live Countdown Split-screen — đếm ngược chia màn hình

- **Bản chất:** một đoạn sự kiện thật chạy đúng thời gian thực, không cắt, không tua, không đảo thứ tự. Đồng hồ là diễn viên chính; số ô hình tăng dần về phía số 0 rồi thu về một hình duy nhất tại 0.
- **Bảng màu:** nền `#06080A`, panel `#0B0E11`, chữ chính `#F2F5F7`, chữ phụ `#7C878D`; cam `#FF5B1F` = "đang diễn ra/đã đồng bộ/đã xong"; đỏ `#FF3B30` = đèn đang nói/thẻ "đã nghe"; sau số 0, khối đồng hồ đảo ngược (nền cam, chữ `#0A0B0C`).
- **Chữ:** số đồng hồ sans condensed, ô số cố định bề rộng (không rung), tới 132 px, dấu T−/T+ ở 0,85×, phần mười giây 0,41× màu xám, thanh 10 đoạn dưới đồng hồ; nhãn/mã dùng monospace; transcript trực tiếp là phụ đề (nói từng từ hiện từng từ, fade 0,08 s mỗi từ, con trỏ khối; dòng tiếng Hoa hiện nguyên khi cue bắt đầu).
- **Nhịp:** mọi thay đổi layout rơi vào một lời gọi thật trong âm thanh gốc hoặc một sự kiện thấy được trong hình — nhạc theo sau, không bao giờ đặt cắt. Đổi layout 0,34 s `easeInOutCubic`; ô mới mở từ mép trái, ô rời khép về trái, viền cam 3 px lóe ~0,2 s khi ô đáp xuống. Số ô tăng dần về 0: 1 → 2 → 3–4 → nhiều (6–9, đồng hồ thành ô giữa) → một hình tại 0. Nhạc tắt 0,25 s trước 0; chỉ còn âm thanh gốc và tiếng đồng hồ.
- **Âm thanh:** âm thanh gốc của sự kiện luôn ở trên cùng, không bao giờ duck; giọng dẫn riêng chỉ chen vào khoảng trống của âm gốc; tiếng tick mỗi giây (hai cao độ xen kẽ quanh 1,5–1,9 kHz, pan ±15%), to dần trong 10 giây cuối; nhạc 60 BPM (1 nhịp = 1 giây = 1 tick): drone trầm mở dần về 0, trống bass mỗi nhịp, timpani lăn vào 0, im lặng, rồi hợp âm đồng trầm + chuông ống tại 0.
- **Chiêu đặc trưng:** nhiều ô hợp thành một hình tại 0 (mỗi ô trượt về ô của nó trong lưới 3×3 rồi crossfade sang cùng một shot toàn màn hình, flash trắng ấm, 0,42 s); dải kiểm soát (ai đang nắm quyền, ô đang hoạt động tô cam khi có lời bàn giao); checklist kế hoạch đối chiếu "đã nghe" (thẻ đỏ "heard −32,1" kèm sóng âm); đồng hồ thứ hai đếm tới mốc tiếp theo kèm sơ đồ vẽ theo thời gian; huy hiệu đồng bộ trên mỗi ô (`LIVE SYNC` / `cùng khung giờ · chưa đồng bộ từng frame` / `slow-motion đã đưa về 1×`) — trung thực là một phần của hình thức.
- **Rủi ro lớn nhất:** footage không đồng bộ được thì không giả vờ đồng bộ: ghi nhãn rõ, giữ khỏi những giây then chốt, ghi vào `FACTS.md`. Đo số 0 bằng hai dấu độc lập (sự kiện thấy được + thời điểm lời nói).

### 4. City Symphony — giao hưởng thành phố

- **Bản chất:** phim tư liệu về một nơi chốn; nhạc viết trước làm kịch bản, mọi cú cắt nằm trên nhịp hoặc phân nhịp của nhạc. Máy móc chạy nhanh thành vệt sáng, con người chạy chậm; khoảnh khắc chậm duy nhất dành cho thứ mong manh.
- **Grade:** một look phim 35 mm thống nhất: matte 1,85:1 (vạch đen 21 px trên 1920×1080), highlight ấm, đen nâng, bloom highlight, grain cụm ở mid-tone, rung cửa ±0,5 px, vignette mềm. Tư liệu lưu trữ ≤ 2,5×, hiện đại ≤ 1,5×. Không ảnh tạo sinh, không bản lưu trữ đã phục chế/tô màu.
- **Màu/chữ:** chữ trắng ấm `#EDE8DF`, dòng phụ `#B0AAA0`, cam natri `#D9772F` là màu nhấn duy nhất (gạch dưới số, đường vệt đám đông, kim vòng ngày). Font Latin display chữ hoa tracking 0,06–0,32 em; chữ Hoa sans nhẹ 300–350. Căn trái, lề 168–196 px, không bao giờ căn giữa, không hộp nền — chỉ một vùng tối mềm hình ellipse (α ≤ 0,6) sau khối chữ. Thẻ số: số 84 px, gạch natri 2 px mọc dưới, một dòng chữ Hoa 28 px + một dòng tiếng Anh 14–16 px ghi rõ thứ được đếm và năm nguồn.
- **Nhịp:** tốc độ là nhạc cụ chính: shot chạy 0,3×–75×, mọi tốc độ > 1× dùng frame blending (màn trập 360°: mỗi frame ra là trung bình các frame nguồn nó phủ, có giới hạn số frame); ramp tốc độ smoothstep và luôn mang ý nghĩa (tăng tốc ra khỏi thời gian thực, phanh vào slow-motion 2,2× → 0,3× trong 0,55 s đúng vạch nhạc dừng). Cắt theo bảng nhịp: mở đầu 2 vạch → 1 vạch, buổi sáng 2 nhịp → 1 nhịp, lưới chia ô sáng từng 1–2 frame, phanh 3–4 s một hai shot, hoàng hôn ½ nhịp → 4 frame → 2 frame, dừng cứng cắt sang đen đúng vạch nhịp. Một time-lapse dài một camera ≥ 12 h làm đồng hồ, quay lại 3–4 lần từ cùng vị trí.
- **Âm thanh:** chỉ nhạc, không thuyết minh, không tiếng nguồn, không hiệu ứng âm thanh. Dàn nhạc mẫu (organ, gió staccato, dây spiccato, kèn, trống bass, chũm chọe, glockenspiel chỉ cho số khóa). Cấu trúc: arpeggio trên một hợp âm mỗi vạch → chồng lớp (nốt tám → triplet trên nốt tám → nốt mười sáu) → break: mọi arpeggio dừng cùng lúc vào một hợp âm giữ → quay lại bằng cú organ đầy → dừng khô cắt mọi nhạc cụ trong 15 ms, chỉ còn reverb → coda một hợp âm mềm không giải quyết.
- **Chiêu đặc trưng:** sông ánh sáng (đèn xe thành vệt liền nhờ blending); đám đông thành vệt (nền = median cả shot, centroid nối nhau bằng đường 2 px, mờ ×0,9 mỗi frame); lưới chia ô 1×2 → 2×2 → 3×3 → 4×4, ô mới sáng theo thứ tự rải rác trong 0,3 s; chia đôi đối vị (lưu trữ trái, hôm nay phải, cùng loại địa điểm); nhấp nháy ngày/đêm (cùng camera, frame trưa và đêm xen nhau mỗi 2 frame); vòng ngày 24 giờ góc dưới phải, kim natri, đóng băng và mờ trong lúc phanh, quay ngược trong flashback ngược.

### 5. Visual Investigation — điều tra bằng hình ảnh

- **Bản chất:** nhiều nguồn độc lập cùng chỉ vào một thời điểm, một địa điểm. Điểm cắt là điểm đồng bộ. Mỗi layout nói một kết luận; không chắc chắn thì vẽ ra (`≈`, *suy luận*, *sơ đồ*, hộp đứt nét), cột đã biết và cột chưa giải quyết tách riêng.
- **Bảng màu:** nền `#0B0C0E`, panel `#141619`, đường viền `#2E3238`, chữ `#ECEAE4`, chữ phụ `#8B9097`, không chắc chắn `#4A4F57`; đỏ `#FF4A2E` là màu duy nhất và chỉ dùng để chỉ: vòng tròn, playhead biểu đồ, đường đồng bộ, highlight, huy hiệu ✓, vùng hội tụ, cột chưa giải quyết. Mọi nguồn đều xám (footage `grayscale(1) contrast(1.22) brightness(0.94)`; giấy `contrast(1.05) brightness(0.86)`); thẻ điện tín giấy `#E4E0D4` mực `#1D1D1B`.
- **Chữ:** tiêu đề/kết luận sans đậm 30–124 px; thẻ, timecode, tick dùng monospace; trích dẫn gốc dùng serif italic, bản dịch serif bên dưới màu phụ (chỉ khi phụ đề chưa nói). Ít chữ mỗi frame: chỉ readout chính, câu gốc được highlight, một thẻ nguồn ngắn mỗi mảnh bằng chứng. Thẻ nguồn: chip 6×12 + `loại · nguồn` ≤ ~12 ký tự. Phụ đề song ngữ dưới khung (Hoa 34 px đậm trên Anh 23 px, một dòng mỗi ngôn ngữ, đo trong trang với 1.500 px). Mọi chữ chính giữ đủ thời gian đọc CJK ÷ 4,5 + Latin ÷ 15 + 1,5 s; khung kết luận/so sánh giữ ≥ 2,5 s với mọi mục hiện đủ.
- **Nhịp:** 30 fps; phần tử cắt vào (≤ 0,1 s) kèm flash trắng 3–4 frame; chỉ thứ được *vẽ* mới tiến triển (vòng tròn vẽ theo chiều kim đồng hồ 0,5 s, leader 0,4–0,8 s, highlight quét, chữ điện tín gõ từng ký tự). Đồng hồ sự kiện chạy tốc độ không đổi trong một đoạn timed-run (mỗi tick = một giây thật). Thang thời gian đổi ở cú cắt đoạn (phút → giây → ngày), mang bởi readout đổi dạng (đồng hồ → `T+` → ngày), không zoom dải timeline.
- **Âm thanh:** bed trầm (contrabass + cello giữ nốt D thấp); tick đồng hồ mỗi 0,5 s ở đoạn thang phút, mỗi giây sự kiện trong timed-run; pizzicato ostinato nốt tám lặng lẽ; foley theo vật liệu (giấy, màn trập, Morse, máy teletype, tiếng bút chì vẽ sơ đồ, một thump trầm cho khoảnh khắc va chạm rồi gần như im lặng); âm thanh gốc (bình luận lưu trữ, radio) band-pass 180 Hz–5,5 kHz, hiện sóng với play-line đỏ và từng từ sáng dần, nhạc duck −12 dB dưới nó; giọng đọc bình thản, nhạc duck ~−9 dB. −14 LUFS.
- **Chiêu đặc trưng:** freeze, khoanh tròn đỏ 2,5 px, loupe ×2 mở bên cạnh (crop từ đúng pixel nguồn, không vượt 1 px nguồn/px màn hình); lưới đồng bộ 3 cột (tài liệu/ảnh/video dưới một đồng hồ bấm giờ, mỗi cột cắt vào đúng lúc nguồn của nó bắt đầu); rewind mở đầu lạnh (đóng băng khung quyết định rồi tua ngược về đầu); điện tín đáp đúng timestamp kèm Morse, leader đỏ đứt nét nối thẻ với chốt trên trục biểu đồ; biểu đồ dữ liệu có playhead đỏ; bản đồ → mặt bằng đo đạc (vị trí, góc, vòng khoảng cách, nón tầm nhìn suy luận); chấm cho người (mỗi người một chấm, người mất thành vòng đỏ rỗng lần lượt); bản đồ bằng chứng cuối phim.
- **Kỷ luật:** không slow-motion thảm họa, không lửa toàn màn hình, không hiệu ứng âm thanh trên cái chết; thương vong đếm bằng chấm và số. Không ô trống "không có footage" — trông như lỗi render; nguồn chưa tới thì đơn giản là chưa hiện.

### 6. Constructivist Montage — montage kiến tạo

- **Bản chất:** bằng chứng được cắt lại. Mọi hình đều là tư liệu thật về đúng chủ đề; lập luận đến từ cách cắt và sắp đặt, không từ minh họa. Mọi tư liệu chuyển thành cùng một bản in hai tông (mực ấm → giấy); đỏ là màu duy nhất, đặt lên trên như một yếu tố in.
- **Bảng màu:** đỏ `#D52B1E` (dải, khối, con số chính, vòng tròn, leader); mực `#141210` (chữ, dầm, viền cửa sổ, nền tối); giấy `#EDE4D0` (nền, chữ đảo, viền cut-out). Mọi thứ thuộc ảnh đều là mực-trên-giấy; đỏ không bao giờ đặt trên đỏ (khối đỏ trên nền đỏ đổi thành mực). Đổi nền xen kẽ để cú cắt rơi có lực: giấy → mực → giấy; trong đoạn tăng tốc, nền tự nó luân phiên đỏ/mực theo từng cú cắt.
- **Chữ:** chữ Hoa display sans 900, 110–210 px, xếp dọc 170 px mỗi ký tự; số và dòng Anh sans condensed 600–700, số 230–440 px, dòng Anh 30–62 px chữ hoa tracking 2–10 px; thẻ nguồn/tag footage monospace đậm 17–18 px trên tab mực hoặc đỏ. Chữ đặt dọc trục −18° trên dải, hoặc thành khối mực/đỏ; không bao giờ căn giữa khung, không header. Phụ đề góc dưới trái, thanh mực 90%, tick đỏ 10 px; giữ ≥ max(1,8 s, lời nói + 0,6 s).
- **Nhịp:** một tempo cho hình và nhạc (120 BPM: beat 0,5 s, vạch 2 s); mọi cú cắt, đập, wipe, đếm nằm trên beat, nửa beat hoặc nốt mười sáu. Shot footage 0,5–2 s, một ý mỗi shot; đoạn tăng tốc bằng cách halving (0,5 → 0,25 → 0,125 s, không ngắn hơn 3 frame). Cắt kề nhau phải xung đột ít nhất một trong: hướng (đập trái/phải), giá trị (nền giấy/mực), hình học (dải chéo/cửa sổ đứng). Không hai tài liệu giấy liên tiếp. Chuyển đoạn trong chất liệu: wipe đỏ (dải 260 px, 72°, quét 0,25 s), iris (vòng tròn đỏ mở thành footage), slam (phần tử bay vào dọc trục 0,08–0,2 s, dừng cứng, rung khung biên độ 3–18 px), flash cut (1 frame giấy 50–80%), hard cut trên beat giữa hai nền đối giá trị, jump-in (cắt sang crop 1,2× cùng frame trong freeze). Hai khoảng lặng: một nơi dàn nhạc dừng chỉ còn bản ghi gốc, một nửa vạch thật sự trống (khung mực, một chấm đỏ) trước cú đánh nặng nhất.
- **Đồ họa:** chỉ 4 loại phần tử: dải (đỏ/mực, dọc trục), cửa sổ (chữ nhật hoặc hình bình hành chứa phim/ảnh), cut-out (người cắt khỏi ảnh, viền trắng giấy 7 px), khối chữ; cộng texture sợi giấy phủ toàn khung. Grade in: luminance → kéo percentile (phim 0,7/99,5; ảnh 0,8/99,4) → S-curve (tài liệu nhẹ hơn) → map mực→giấy. Cut-out tách người bằng mô hình phân đoạn, ngưỡng 0,5, lấy thành phần lớn nhất.
- **Âm thanh:** ostinato máy móc nốt tám thứ (cello spiccato + bassoon staccato, tuba/trombone trên beat, snare nốt mười sáu, xylophone cho đếm, kèn đồng stab, timpani lăn vào đổi đoạn, gran cassa + cồng cho cú nặng nhất). Âm thanh gốc xen kẽ với nhạc: một đoạn dàn nhạc dừng, bản ghi thật (máy rivet, máy móc, đám đông) gánh cú cắt một mình. Foley cho mọi hành động in: slam = thump trầm + clank thép, stamp = thump + clack, wipe/iris = whoosh, marker = noise scrub lọc, giấy = rustle band-pass. Nhạc duck ~10 dB dưới giọng; master −14 LUFS, peak giới hạn −1,8 dBFS trước mux, fade 25 ms ở sample 0.
- **Chiêu đặc trưng:** tài liệu được đánh dấu chứ không trích dẫn (vạch đỏ lên đúng câu trên bản scan, con số thành khối đỏ); bản vẽ trên tài liệu được nhấc khỏi trang, xoay và dựng theo tỉ lệ thành biểu đồ; A + B → ý tưởng (hai loại hình xen nhau nhanh dần tới khi một thẻ/số nói ra ý nghĩa va chạm); đếm số đông (bộ đếm theo cú cắt, lưới đầy từng ô, tháp tầng tầng); người xây nên công trình (cut-out xếp chồng thành thứ họ làm); im lặng rồi cú đánh nặng nhất vào kết quả.

### 7. Telestrator — phân tích thể thao vẽ trên hình

Đã có skill chuyên sâu riêng: `opuscar-telestrator` (đọc skill đó khi brief là phân tích chiến thuật thể thao). Trong nhóm này chỉ cần nhớ vị trí của nó: cùng họ tư liệu thật, nhưng là style duy nhất mà nét vẽ tay là diễn viên chính — xem tình huống chạy thật trước, đóng băng, vẽ vòng tròn/mũi tên trực tiếp lên hình, mỗi freeze một phát hiện, màu vàng/cyan/đỏ theo vai đội. Đừng nhầm với visual-investigation (điều tra đa nguồn, vòng đỏ chỉ điểm đồng bộ) hay caption-news (caption dẫn nhịp, không vẽ lên hình).

### 8. Broadcast News Package — bản tin truyền hình trọn gói

- **Bản chất:** một hệ đồ họa thống nhất dùng xuyên suốt bulletin: brand plate (hình bình hành), tab màu nhấn, paper strap, thẻ mực viền nhấn, dateline mono, tem. Thứ tự: sting → rundown (hôm nay có 4 tin) → từng tin → quay lại rundown đánh dấu đã xong → sign-off. Một fact mỗi màn hình.
- **Bảng màu:** mực `#121417`; mực 2/3 `#1B1E23`/`#22262C`; nhấn chanh `#F2CF1D` (sáng `#F8DE4A`, tối `#D8B30C`); vàng gold `#D4B064` (ngưỡng, dateline, huy hiệu); giấy `#F4F1E8` (strap, tài liệu, đường biểu đồ); báo động `#FE6B3D` chỉ dành cho BREAKING/LIVE (bản tin tuần không có thì không xuất hiện). Đổi brand thì giữ cấu trúc: một nhấn + một phụ dạng gold + giấy + mực + một màu báo động dự trữ. Chữ mực trên màu nhấn; trên giấy, dòng Anh phụ dùng olive tối `#6E5A1E` vì gold quá nhạt.
- **Chữ:** chữ Hoa sans 900 (headline, strap) / 700 (nhãn); Latin condensed 800 (số, tên, plate), 600 (dòng phụ, trích dẫn), 600 italic (tiêu đề Anh ở end card); mono 500 cho dateline, nguồn, trục. Mọi nhãn song ngữ, mỗi ngôn ngữ một dòng, không ngắt dòng. Không font viết tay.
- **Khung hình 1920×1080:** nội dung x 96–1824, y 56–840; strap dưới: tab x 96 y 856 cao 48, strap 1250×104 ở y 904 + khối mực cuối 120 px; dòng nguồn căn phải x 1836, y 950/978, mono 13 px, mờ 75%; bug kênh góc trên phải; thẻ góc trên trái `ILLUSTRATION / 示意` (trên plate tạo sinh) hoặc `SCHEMATIC / 示意图` (trên biểu đồ sơ đồ), lật vào/ra 0,2 s.
- **Bộ phận:** sting 0–1,5 s (hai vạch nhấn → plate đập vào kèm vòng impact và rung → chữ rơi từng ký tự → plate bay lên góc phải thành bug, dải dọc wipe vào shot đầu; cú đánh trong 0,4 s); brand plate hình bình hành 520×180; rundown (khối ngày trái, 3 hàng phải 1024×140, lật dọc theo nhịp, cuối chương trình quay lại và từng hàng được tick); strap (tab = category, đổi chữ bằng lật dọc 0,32 s, tab flash trắng khi đổi category; bản profile đặt tên người nói); bảng split-flap (ô 220×130, giá trị cũ và mới trên cùng bảng); biểu đồ ngưỡng (đường tiến một ngày mỗi bước, bước cuối vượt ngưỡng đứt nét gold, rung + vòng, panel readout trượt vào sau); cột mọc từ đường 0 xuống cho số âm; bản đồ giải thích một long take (thành viên sáng theo khoảng cách từ thành phố); tài liệu 380×490 bay ra khỏi chấm thành phố theo cung 0,5 s; thẻ trích dẫn (dấu ngoặc nhấn lớn đáp trước, dòng đẩy lên từng dòng 0,18 s, gạch dưới quét đúng từ khóa khi giọng nói tới — trích dẫn nguyên văn, không diễn giải trong ngoặc kép); thẻ spec (mọi cột tỉ lệ trên một thang duy nhất); tem (đáp từ 1,9× trong 0,16 s kèm ellipse lan, tối đa một tem mỗi tin).
- **Nhịp:** lưới 120 BPM, beat 0 ở cuối sting (1,5 s); mọi cú cắt/wipe trên beat hoặc nửa beat. Shot: sting 1,5 s; rundown 4–5 s; shot tin 3–7 s; map long take 6–12 s làm nhịp thở; so sánh giữ tới khi mọi mục hiện đủ ≥ 2,5 s. Một hành động package mỗi 0,5–1 s trong shot. Chuyển đoạn: wipe dải dọc (nhấn 84 px + mực 5 px + gold 14 px, 0,3 s) giữa các tin và phần chương trình; hard cut + timpani trong một tin; wipe chéo vào end card. Lớp package đi cùng hình của nó qua wipe (mỗi phía vẽ strap/tab/nguồn/thẻ góc của riêng mình) — strap không bao giờ lật hay chồng chữ. Không dissolve, không lật 3D, không bay xuyên.
- **Âm thanh:** giọng anchor một câu mỗi graphic, bắt đầu 0,1 s sau cú cắt; nhạc theme 120 BPM thứ (violin spiccato nốt tám, bass pizzicato trên beat, kèn pad, kick 1–3, snare 2–4); tâm trạng theo mục (thị trường: violin xuống quãng tám + tremolo + kick 4-on-the-floor; chính sách: pizzicato + kèn); hit chữ ký (tutti sting, glockenspiel khi hàng rundown đáp, timpani ở hard cut, một beat im lặng trước break lớn nhất rồi cú nặng nhất, drone giữ sau tem kết luận, nâng trưởng cho tin cuối); foley (whoosh wipe, click split-flap, thump + clack tem, tick phòng giao dịch dưới biểu đồ thị trường, click bản đồ mỗi nước sáng, ping sonar trên thành phố). Nhạc duck ~−7 dB dưới giọng. Master −14 LUFS.
- **Chiêu đặc trưng:** sting hóa thành bug; tab strap = category; rundown rồi tick hết; thẻ spec (toàn thể và phần trên một thang); strap không bao giờ rời từ tin đầu tới recap; split-flap trước/sau; vượt ngưỡng (đường tiến từng bước, nhạc dừng một beat trước bước cuối); ngày trong eyebrow (mọi graphic mang nguồn + ngày bằng mono caps); thành phố gửi thư (tài liệu bay khỏi thành phố tới người nhận trên map long take); thẻ trích dẫn + tem kết luận.

## Hệ màu / bảng chất liệu bất biến (tóm tắt theo style)

| Style | Nền & chất liệu | Màu nhấn (bất biến) | Chữ |
|---|---|---|---|
| caption-news | Footage thật + thẻ số liệu `#151512` | Vàng mật `#FFC21A`; đỏ `#FF4A3D` | Sans đậm 88 px, một từ khóa/khung |
| newsreel | Cửa chiếu 1,37:1, bạc ấm, grain ở mux | Không màu nhấn (bạc ấm) | Display cổ điển + Oswald, phụ đề trên dải tối |
| countdown | Ô hình trên `#06080A`, viền 1 px | Cam `#FF5B1F`; đỏ `#FF3B30` | Số đồng hồ condensed, ô số cố định |
| city-symphony | Phim 35 mm, matte 1,85:1, bloom + grain | Cam natri `#D9772F` duy nhất | Display chữ hoa + sans nhẹ, căn trái |
| visual-investigation | Nguồn xám trên `#0B0C0E` | Đỏ `#FF4A2E` duy nhất | Sans đậm + mono, ít chữ mỗi frame |
| kino-montage | In hai tông mực → giấy | Đỏ `#D52B1E` duy nhất | Sans 900 dọc trục −18°, số khổng lồ |
| telestrator | Footage thật + nét vẽ | Vàng/cyan/đỏ theo vai đội | Xem `opuscar-telestrator` |
| news-package | Đồ họa phẳng trên mực `#121417` | Chanh `#F2CF1D` + gold `#D4B064` | Sans 900 + condensed 800 + mono |

Một màu = một vai, xuyên suốt phim. Đổi tông theo brand được, không bao giờ đổi vai của màu.

## Quy trình sản xuất

1. **Chốt tư liệu trước.** Hỏi user có footage/ảnh/tài liệu/dữ liệu của mình không (kèm quyền dùng). Không có tư liệu thật thì đi tìm trước khi viết treatment — nhóm này viết treatment sau tư liệu (ngoại lệ duy nhất so với các nhóm vẽ).
2. **Tìm và ghi nguồn.** Chỉ dùng nguồn có licence rõ: Wikimedia Commons (đọc licence từng file: CC0, public domain, CC BY — ghi đủ tác giả, tiêu đề, licence trên màn hình và trong `CREDITS`; không dùng CC BY-SA, "no known restrictions", bản re-upload YouTube, bản tô màu/phục chế); cơ quan liên bang Mỹ (tác phẩm của nhân viên liên bang là public domain — kiểm tra không ghi công nhà thầu); Internet Archive (chỉ mục ghi rõ public domain/CC0/CC BY; tác phẩm Mỹ xuất bản trước 1931 là public domain); Library of Congress (đọc rights statement từng mục); NASA; tài liệu/số liệu chính thức từ trang của cơ quan ban hành. Trước khi tải, nói với user sẽ lấy gì, từ đâu, theo licence nào, dung lượng bao nhiêu. Ghi mọi asset vào `SOURCES.jsonl`/`SOURCES.md` (tiêu đề, tác giả, ngày, licence, trang, giây nào được dùng). Tải tuần tự, có back-off (Commons giới hạn tốc độ, HTTP 429).
3. **Treatment ngắn trước khi dựng:** chọn cấu trúc (kim tự tháp ngược có bước ngoặt giữa phim; danh sách ba mục ngoặt ở mục ba; đếm ngược các con số kết ở con số quan trọng nhất — cho caption-news; hoặc cấu trúc riêng của style đã chọn), liệt kê từng shot với: tư liệu nào, fact nào, nguồn nào, chữ nào trên màn hình.
4. **`FACTS.md` là hợp đồng sự thật:** mọi khẳng định trên màn hình/trong giọng đọc → URL nguồn → câu trích gốc. Suy luận ghi riêng. Số liệu từ trang chính thức, trích kèm năm; trang cập nhật thì kiểm tra lại trước lần render cuối.
5. **Timeline là nguồn sự thật duy nhất:** một bảng beat (mốc giây → sự kiện hình → sự kiện âm) mà hình, phụ đề, nhạc, mix đều đọc từ đó. Nhịp hình và cue âm lệch nhau là lỗi, không phải "cảm tính".
6. **Chuẩn bị tư liệu:** footage hiện đại scale ≤ 1,5× (tư liệu lưu trữ ≤ 2,5× sau khử block); cắt bỏ logo đài bằng crop (không che bằng caption); làm mờ chi tiết riêng tư đọc được (số điện thoại, tên, biển số); bỏ shot có chữ cháy sẵn trong hình; ảnh/tài liệu quét ở độ phân giải đủ cho kích thước hiển thị; bản đồ dùng hình học Natural Earth (public domain).
7. **Dựng page theo page contract** (xem Công thức), render thử các frame hero của từng beat → contact sheet soát thứ tự lập luận và độ đọc của chữ trước khi render full.
8. **Âm thanh theo bảng âm của style** (xem từng style), mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng (chung cho nhóm)

- Cắt cứng là mặc định; dissolve gần như bị cấm trong cả nhóm (trừ fade từ đen cho trang sách/end card ở city-symphony và dissolve 0,5–1,2 s trong một số chuyển cảnh của nhóm thủ công — không áp ở đây).
- Chữ bắt buộc đọc giữ ≥ 1,8 s (hoặc ≥ câu nói + 0,6 s); so sánh giữ tới khi mọi mục hiện đủ ≥ 2,5 s; công thức đọc chung: CJK ÷ 4,5 + Latin ÷ 15 + 1,5 s tính từ lúc khối chữ hoàn chỉnh.
- Không frame nào phẳng quá 1 s mà không có gì chuyển động (bộ đếm lăn, đường vẽ, highlight quét, push chậm giữ nó sống); giữ một hơi thở 2–3 s sau bước ngoặt.
- Người thật trên màn hình: nhân vật công chúng và người trong sự kiện tin tức thì được; không close-up hay slow-motion người thường có thể nhận diện; không làm người thường thành nhân vật chính bị chậm lại.
- Không dùng ảnh tạo sinh làm footage. Không dùng logo/nhận diện của đài/kênh thật; tên kênh, màu, logo trong phim là hư cấu.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; nhiễu "tay vẽ"/rung cửa phải suy từ hash xác định của frame hoặc đỉnh), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Caption/counter:** số lăn dùng ô số cố định bề rộng để không rung; bộ đếm chỉ báo giá trị cuối là fact (giá trị giữa chừng là đồ họa); nhãn thay đổi nội dung thì `TEXTS` báo giá trị cuối của nó.
- **Tài liệu trên màn hình:** trang PDF render 220 dpi làm giấy trắng trên bàn tối (nghiêng ±1–2°, bóng mềm, vignette), highlight đặt theo tọa độ trích xuất từ file gốc (1 pt = 3,0556 px), blend `multiply`, quét trái → phải 0,3–0,5 s; chữ in trên trang là hình, thứ phải đọc thì đánh máy lại bằng type.
- **Grade thống nhất:** một grade cho mọi footage trong phim (caption-news: `contrast(1.07) saturate(0.92) brightness(0.98)` + lớp warm soft-light 6%; countdown: `eq=contrast=1.07:saturation=0.9:gamma=0.97:brightness=-0.01` + colorbalance lạnh bóng/ấm highlight); grain thêm ở mux, không thêm trong page.
- **Đồng bộ countdown:** một mapping `M = t − T0` cho toàn phim; mỗi camera có offset nguồn riêng đo một lần và nướng vào tên frame khi trích xuất, page không tự tính sync.
- **Chữ:** mọi chữ trên màn hình là vector, không bao giờ là footage đã scale. Phụ đề `.srt` sinh từ cùng timeline với hình.
- **Âm thanh:** master −14 LUFS, true peak ≤ −1 dBTP; giọng đọc kiểm tra bằng ASR trên giọng sạch và trên phim hoàn chỉnh (đồng âm dễ nghe nhầm thì viết lại câu).

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1920×1080, 30 fps; newsreel 24 fps; countdown 30 fps; printed-long-take 30 fps — xem style), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) chữ đọc được trong thời gian shot cho phép (chạy readcheck: mọi khối chữ đủ CJK ÷ 4,5 + Latin ÷ 15 + 1,5 s); (b) caption một dòng mỗi ngôn ngữ, không ngắt dòng; (c) thẻ nguồn có mặt trong cùng shot với mọi con số; (d) không logo đài, không chữ cháy trong hình, không chi tiết riêng tư chưa làm mờ.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame; cắt nằm trên lưới nhịp của style.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Kiểm fact: đối chiếu `FACTS.md` với mọi số/ngày/khẳng định trên màn hình và trong giọng đọc trước lần render cuối; suy luận nào không ghi `≈/suy luận/sơ đồ` trên màn hình là lỗi.
- Bản quyền: ghi rõ nguồn tư liệu + licence trong QA.md và `CREDITS`; tư liệu không rõ licence thì không dùng. Không gắn tên/logo đội bóng, nhân vật, đài truyền hình thật vào phim dựng bằng code.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: nguồn tư liệu + licence, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `timeline.json` (caption, thời điểm giọng đọc, khoảng lặng, hit), script sinh âm thanh, frames trung gian, `FACTS.md`, `SOURCES.md`, `CREDITS`.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.

## Phân biệt với các nhóm skill opuscar khác

- `opuscar-telestrator`: cùng họ tư liệu thật nhưng chuyên sâu một style — phân tích thể thao vẽ trên hình; nhóm này trỏ sang đó, không viết lại.
- `opuscar-painting-illustration`, `opuscar-sketch-board`: vẽ ra thế giới bằng chất liệu hội họa/bảng — ngược với nhóm này (sắp xếp tư liệu thật).
- `opuscar-traditional-crafts`, `opuscar-printmaking`: mô phỏng vật liệu thủ công/in ấn — hình vẽ bằng code, không dùng footage thật làm nền.
- Các nhóm còn lại (graphic & type, line diagrams, cartoons, games, film & tape, screens & interfaces, light & lines, 3D & miniature, instruments & evidence, data & maps): mỗi nhóm một ngữ pháp riêng; khi brief nhắc tới tư liệu thật + nguồn + bản tin thì nhóm này là đáp án, các nhóm khác không thay thế được kỷ luật bằng chứng ở đây.
