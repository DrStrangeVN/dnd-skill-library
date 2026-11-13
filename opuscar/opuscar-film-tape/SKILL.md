---
name: opuscar-film-tape
description: Kỹ thuật phim mà chất liệu ghi hình là nhân vật chính (spin-out từ bộ Lemo-Opuscar) — 5 style: terminal ký tự CRT, phim câm 1920, băng VHS found footage, phim khắc trực tiếp, chồng hình kép. Dùng khi brief là "kể bằng terminal", "phim câm chiếu trong rạp", "băng VHS quay tay", "vẽ bằng vết cào trên phim", "bóng con vật chứa phong cảnh". Mọi nội dung do brief quyết định — skill chỉ giữ ngữ pháp chất liệu và kỷ luật sản xuất.
---

# Opuscar Film & Tape — Phim nhựa & băng ghi hình

Chất liệu của phương tiện ghi hình là nhân vật chính: ký tự terminal trên màn CRT cong, phim bạc rung xước 4:3, băng VHS quay tay, vết cào trên nhũ phim đen, ảnh chồng trong bóng động vật. Hỏng hóc của phương tiện — nhiễu, xước, mất nét, tracking lệch — mang cốt truyện, không phải lỗi cần sửa.

Nguồn kỹ thuật: 5 style trong repo Lemo-Opuscar tại `~/workspace/lemo-opuscar/styles/{ascii-crt,silent-film,backrooms,scratch-film,double-exposure}/STYLE.md` — đọc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện/nhân vật/nhãn hiệu của phim mẫu.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Giấy phép: code MIT, tài liệu gốc CC BY-NC 4.0 (hệ REUSE của repo); phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

## Khi nào dùng

- Nhật ký máy tính/máy móc kể bằng terminal: chữ gõ, con trỏ nhấp nháy làm hồi hộp, một bất ngờ ấm áp.
- Chuyện kể bằng hành động và thẻ chữ xen kẽ, không lời thoại: phim câm chiếu trong rạp.
- Không gian trống quen thuộc nhưng sai, sợ hãi đến từ lặp lại và máy quay hỏng: băng VHS quay tay góc nhìn thứ nhất.
- Vẽ trực tiếp lên phim: nền đen, sáng là vết cào, màu là thuốc nhuộm trong suốt, nét vẽ sôi 15 lần/giây.
- Hai hình chồng nhau: bóng động vật chứa ảnh phong cảnh thật bên trong, ảnh trong bóng trôi chậm hơn đường viền.
- Không dùng cho: giải thích kỹ thuật chính xác (opuscar-line-diagrams), đồ họa chữ/poster (opuscar-graphic-type), hoạt hình nhân vật diễn thoại (opuscar-cartoons).

## Khi nào KHÔNG dùng

- Cần hình sắc nét, màu thật, âm thanh sạch: nhóm này cố tình làm hỏng hình (nhiễu, xước, tracking, mất nét) — khán giả cần hình sạch thì đây là sai style.
- Cần kể nhanh, nhiều thông tin, nhiều số liệu: phim câm và VHS kể chậm bằng hành động và khoảng trống; nhồi thông tin sẽ vỡ nhịp.
- Cần nhân vật nói nhiều, thoại dài: phim câm không có thoại; terminal chỉ có chữ gõ; VHS chỉ có âm thanh băng ghi được.
- Không có style nào trong nhóm cần máy tạo ảnh — toàn bộ 5 style làm bằng code (double-exposure dùng ảnh phong cảnh: ảnh phải có licence hoặc tự chụp/quay, không lấy ảnh không rõ nguồn).

## Nguyên lý cốt lõi

1. **Phương tiện là người kể.** CRT, phim bạc, băng VHS, nhũ phim, buồng tối — hỏng hóc của chúng (nhiễu, xước, tracking, mất nét, rung) là cách chuyện được kể, không phải lớp phủ trang trí.
2. **Một camera, một luật.** ASCII-CRT: camera duy nhất là chính màn hình, chỉ zoom bằng cách đổi cỡ chữ của lưới. Backrooms: một cú quay tay liên tục, cắt chỉ khi băng đứt. Silent-film: một cuộn phim trong một khung chiếu giữa rèm rạp.
3. **Tốc độ là cảm xúc.** Quay tay chậm (undercrank) cho hoảng loạn, quay đúng tốc độ cho dịu dàng; gõ chữ nhanh cho máy, chậm cho câu kịch tính; ảnh trong bóng trôi chậm hơn đường viền để tạo thị sai.
4. **Ít màu, đúng chỗ.** Đơn sắc phosphor, bạc đơn sắc, một màu bệnh của địa điểm, đen ấm + một kem + vài thuốc nhuộm, ảnh đen trắng + một ấm cho đèn — màu thứ hai chỉ xuất hiện một lần, đúng một khoảnh khắc, cho đúng một thứ.
5. **Im lặng là một nhạc cụ.** Không nhạc nền ở VHS (chỉ âm thanh băng ghi được); piano/organ + tiếng máy chiếu ở phim câm; tiếng cào ở scratch-film; tiếng màn trập ở double-exposure.

## Bảng 5 style — bất biến từng style

| Style (slug) | Nhận diện nhanh | Màu bất biến | Chữ | Nhịp/chuyển động |
|---|---|---|---|---|
| `ascii-crt` — terminal ký tự CRT | Một màn terminal đơn sắc: phosphor hổ phách (hoặc xanh lá P1) phát sáng trên kính tối, cong mép, có scanline; mọi hình — tiêu đề, phong cảnh, mặt, phòng, phụ đề — đều là ký tự thật xếp trên lưới, chọn theo mật độ mực; camera duy nhất là màn hình | Một phosphor mang mọi thứ (hổ phách/xanh/trắng), theo thang sáng riêng; tối đa một màu phụ mềm, chỉ cho một thứ duy nhất (vật cảm xúc), bật lên đúng một khoảnh khắc, đúng downbeat, không thu lại tùy tiện | Phụ đề là output của terminal: dải LOG dưới cùng — vạch phân cách mờ, tag video-ngược, rồi prompt + câu in hoa ~45px; gõ từng từ đồng bộ giọng (timestamp từng từ), giữ ≥ max(1.8s, thoại + 0.6s); nằm ngoài lưới zoom, như dòng trạng thái, cùng scanline và phát sáng | Ký tự không rời lưới, trừ khoảnh khắc biến đổi đã khai báo; gõ, cuộn, bộ đếm nhảy từng ô; con lăn số lật rời rạc, nhanh rồi chậm dần; chỉ 3 thứ chuyển động liên tục: tỉ lệ lưới (camera), vật lý CRT, hạt trong lúc biến đổi; tốc độ gõ là diễn xuất: máy đều và nhanh (~10–40ms/ký tự), câu kịch tính chậm theo nốt nhạc |
| `silent-film` — phim câm 1920 | Một cuộn phim chiếu: khung 4:3 trong khung cửa rạp giữa rèm; tranh mực với xám wash và gạch chéo, in trên phim bạc rung, xước, cháy mép; không ai nói — nhịp kể bằng hành động ở shot rộng và thẻ chữ xen kẽ; âm thanh duy nhất là nhạc cụ rạp (piano/organ) + tiếng máy chiếu | Bạc đơn sắc, nhuộm màu chỉ theo phim: lạnh và gắt hơn (hỏng nhiều, sepia ít) khi chuyện xấu đi, ấm và sạch hơn khi chuyện dịu lại; nhuộm và hỏng là cần gạt tâm trạng, đặt theo đoạn; giá trị mang mọi thứ (quần áo tối trên tường nhạt, mặt nhạt trên nội thất tối); tối đa một màu, vẽ vào mặt nạ màu riêng | Thẻ chữ là phụ đề; `.srt` liệt kê chữ của thẻ; một thẻ giữ 2.5–3.75s (≥ max(1.8s, thời gian đọc + 0.6s)); thẻ đen vẽ, viền deco theo cảm xúc: một vạch nặng cho hét (chữ rung), vạch đôi góc bậc + quạt cho tường thuật, dây leo/hoa nhỏ cho dịu dàng; font thời kỳ (OFL) | Lấy mẫu tay quay: nhân vật và camera lấy mẫu 16fps (18fps trở lên để quay nhanh cảnh hoảng); flicker/weave/grain/xước đổi mỗi frame xuất (24fps) — hỗn hợp đó tạo cảm giác "được chiếu" chứ không chỉ "ít frame"; tốc độ là cảm xúc: quay nhanh cho hoảng loạn (chuyển động nhanh, flicker nhanh), về 16fps và phim sạch hơn cho cảnh dịu |
| `backrooms` — băng VHS found footage | Một bản ghi camcorder góc nhìn thứ nhất (VHS 1990s, 4:3), quay tay, liên tục; nội thất trống quen thuộc nhưng sai, lặp lại: văn phòng, tầng khách sạn, trường, mall, tầng đỗ xe, hành lang bệnh viện; huỳnh quang vo ve, không người; sợ hãi từ trống rỗng, lặp lại, quy định quan liêu, máy quay hỏng đúng lúc; không gì đuổi theo ai | Một màu bệnh chủ đạo từ vật liệu địa điểm (giấy dán vàng mù, xanh cơ quan, xanh bệnh viện, laminate be), viền tối hơn, sàn lốm đốm cùng họ; trần/tấm đèn gần trắng, hơi ấm; đúng một màu bão hòa: đèn báo đỏ, biển thoát hiểm xanh, đèn cảnh báo hổ phách — chỉ nó mới bloom; ví dụ tông `#8c763c`/`#a89a7d`/`#5e8f96` | Caption kiểu CEA-608: mono (IBM Plex Mono 600) ~42px, trắng trên hộp đen đặc từng dòng, ≤ 32 ký tự, giữa trong khung 4:3, trên OSD; không bị nhiễu băng chạm tới (TV giải mã); giữ ≥ max(1.8s, thoại + 0.6s); dấu người nói: `[PA]` cho loa, italic cho người vận hành, mô tả SDH trong ngoặc | Một cú quay tay liên tục; cắt chỉ khi băng đứt: roll-in khi bật nguồn, xé tracking, tắt REC; quay tay = dáng đi (đầu nhấp vài cm, lắc, lật nhẹ) + thở (~0.27Hz) + rung ở vài tần số, biên độ theo đường cong sợ hãi; nín thở thì đóng băng toàn bộ; nhìn xuống chỉ thấy mũi giày và sàn, không thấy chân; autofocus = khoảng lấy nét đi tìm, exposure tự động cũng đi tìm |
| `scratch-film` — phim khắc trực tiếp | Đen là nền, sáng là vết cắt: khung là nhũ phim đen ấm; mọi thứ sáng là vết cào (một màu kem); mọi thứ có màu là thuốc nhuộm trong suốt đặt trong/bên vết cắt; vùng sáng là gạch chéo dày, không bao giờ tô phẳng; nét vẽ sôi: mỗi hình vẽ lại với rung tay mới 15 lần/giây; cả khung hình là bức vẽ | Nền đen ấm `#050403` với đốm nâu/xanh, không xám; sáng: một kem `#FFF4DC` cho mọi vết cắt (sáng mạnh cũng cùng kem, dày hơn); thuốc nhuộm: vài màu trong suốt, alpha 0.5–0.9, luôn có đường kem phủ trên; một thuốc nhuộm = một loại vật, suốt phim (ví dụ teal `#1FB39A` cho nhân vật chính, xanh `#2F86FF` cho ánh sáng sống, đỏ `#FF3220`, vàng `#FFC81C`, xanh lá `#46D65A`) | Chữ thuộc về bức vẽ: con số bên cạnh thước cào, tiêu đề khắc vào chỗ tối; không hộp, không viền, không bóng đổ; font (OFL): sans hình học nặng tô bằng đường cắt chéo cho tiêu đề (Jost 800), mono chắc cho số (IBM Plex Mono SemiBold), font marker cho chữ CJK (LXGW Marker Gothic) | Mọi thứ bước 2: 15 hình/giây ở 30fps, mỗi hình gieo lại rung; camera và nhân vật cùng bước; camera bước là một phần của vẻ ngoài, nhưng giữ mượt theo thời gian (ease), không giật vị trí; vết cắt hiện dần sau điểm nóng; thuốc nhuộm quét vào sau mép cọ; đèn bật với bloom ngắn; nhân vật: chuẩn bị, flick, follow-through |
| `double-exposure` — chồng hình kép | Bóng động vật × phong cảnh: chủ thể là profile động vật sạch, nhận ra ngay (ngựa, cáo, cú bay, thỏ, rùa); bên trong bóng là ảnh phong cảnh/thị trấn thật thuộc về nó (đồng cỏ, đầm lầy, nông trại, đảo); cặp đôi là ý nghĩa; viền không bao giờ tô màu phẳng hay texture; 2 tốc độ: camera/vật di chuyển thì ảnh trong bóng di chuyển chậm hơn đường viền (hoặc đi theo thân, không theo khung) | Ngoài: ảnh đen trắng + xám vẽ bằng code, từ rừng gần đen tới trời trắng giấy; trời/nước là vùng sáng nhất bên ngoài; ảnh trong bóng tối hơn bên ngoài để bóng giữ được; một tông ấm duy nhất, dành cho ánh đèn trong cửa sổ: đèn, cửa sổ sáng, thành phố đêm, phản chiếu trên nước; không trời cam, không giờ vàng, không động vật có màu | Rất ít chữ; phụ đề lặng: serif (Noto Serif SC 600 cho chữ CJK, Newsreader italic cho tiếng Anh; OFL), chữ CJK ~36px trên tiếng Anh ~28px, mỗi thứ một dòng, trên bóng mềm mờ nhạt; không hộp, không viền; phụ đề đặt ở phần trống của thế giới bên ngoài (trời, nước, tuyết), không bao giờ đè lên ảnh trong bóng; di chuyển theo từng cue | Ones, mượt, mọi thứ là hàm thuần của thời gian; động vật: thở, chuyển trọng lượng giữa các chân, ngẩng đầu, đập cánh với cong đầu cánh giữa nhịp, bơi; nhảy có lấy đà, thoát nhanh, đáp chậm với bắn nước/ổn định; không gì bay lên theo đường thẳng; ảnh trong bóng trôi chậm và liên tục, không tự cắt; đèn sáng theo hướng đi theo câu chuyện |

## Quy trình sản xuất

1. **Chọn style trước, chọn phương tiện trước.** Style quyết định mọi hỏng hóc cho phép; ghi danh sách hỏng hóc (nhiễu/xước/tracking/mất nét/rung) vào treatment — hỏng hóc ngoài danh sách là lỗi.
2. **Treatment ngắn, viết trước khi mở demo:** 3 cấu trúc ứng viên rồi chốt một. Với double-exposure: liệt kê ảnh phong cảnh cần (tự chụp/quay hoặc có licence) + cặp động vật–phong cảnh trước; chưa có ảnh thì chưa bắt đầu dựng.
3. **Bảng beat là nguồn sự thật duy nhất:** một bảng mốc giây → sự kiện hình → sự kiện âm mà hình, chữ, nhạc, mix đều đọc từ đó. Ở backrooms, đường cong sợ hãi điều khiển biên độ rung, focus, exposure — ghi nó vào bảng beat.
4. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi hỏng hóc là hàm của `t` (nhiễu/xước phải gieo theo seed xác định của frame, không random tự do), vật di chuyển theo tiến độ trong cửa sổ beat của nó.
5. **Render thử frame hero** (một khung CRT, một thẻ chữ phim câm, một hành lang VHS, một vết cào sáng, một bóng chồng hình) → contact sheet soát chất liệu trước khi render full.
6. **Âm thanh theo bảng âm của style**, mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng

- **ASCII-CRT:** câu chữ vỡ ra, chữ cái sắp theo mật độ mực thành hình chỉ chứa những chữ đó → font size = camera (đẩy vào tới khi một ký tự lấp khung và chính nó làm từ chữ nhỏ hơn) → LOG strip gõ từng từ đồng bộ giọng → một màu phụ bật lên đúng một downbeat.
- **Silent-film:** chuỗi một cú dài (A gây B, B rời khung, khán giả chờ, B quay lại đánh C) → suýt trúng (bàn tay khép đúng chỗ vật vừa ở một frame trước) → thẻ chữ lật nghĩa (thẻ viết lại shot tiếp theo bằng vài từ) → undercrank cho hoảng loạn, về 16fps cho dịu dàng.
- **Backrooms:** autofocus/exposure đi tìm (thứ gì đó chỉ có khi focus đúng) → xé tracking (vết xé là cú cắt vũ trụ làm: cùng khung hình sau đó, nhưng đồng hồ nhảy, pin tụt, một đèn chết) → quy định quan liêu trên loa PA → nín thở: đóng băng mọi rung.
- **Scratch-film:** khắc vào (đường/vật khắc trực tiếp sau điểm nóng) → gạch chéo là ánh sáng (nguồn sáng là một trường gạch chéo; vật không cắt bên trong là bóng; gạch lấp đầy vật thì bóng biến mất) → một nét thành cả một nơi (một chủ thể vẽ ra thành hàng nghìn).
- **Double-exposure:** cửa sổ (bóng chứa nơi nó thuộc về, trượt với tốc độ khác đường viền) → hiện hình lần 2 (bóng đứng tối trước, rồi ảnh in vào từ dưới lên khi màn trập kêu) → đèn sáng theo hướng câu chuyện.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; nhiễu/xước/rung phải suy từ hash xác định của frame), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **CRT (ascii-crt):** lưới ký tự 2·cw cao mỗi ô; video-ngược phải dùng canvas đen đục + atlas chữ đen (destination-out chỉ đổi alpha, upload sẽ bỏ qua); ký tự phủ định phải map đúng lưới (sai tâm ô sẽ trôi qua hàng trăm cột); zoom chỉ bằng đổi cỡ chữ của lưới.
- **Phim bạc (silent-film):** lấy mẫu tay quay 16fps cho nhân vật/camera, hỏng hóc (flicker/weave/grain/xước) đổi mỗi frame xuất 24fps; nhuộm và hỏng đặt theo đoạn; thẻ chữ giữ 2.5–3.75s; kiểm tra mọi shot ở cỡ thumbnail (giá trị phải đọc được khi nhỏ).
- **VHS (backrooms):** một cú liên tục; đèn không xuyên tường (vùng chết cần mọi đèn trong ~±5m đều chết, phía sau tối); nền ở cuối hành lang = sương × ~0.15, không phải hình chữ nhật sáng; huỳnh quang 120Hz (hoặc 100Hz) + hài + vo ve ballast; không nhạc nền — nhạc chỉ tồn tại trong thế giới (nhạc chờ, radio qua tường, jingle PA), lọc và vang, có thể chậm theo wow của băng.
- **Vết cào (scratch-film):** vùng sáng luôn là gạch chéo, xếp lớp thưa cho gradient; rung theo pixel màn hình (rung scale theo zoom sẽ rung macro và mờ wide shot); chữ sôi sẽ khó đọc — giữ chữ ít và lớn; vết cắt nghe được: tiếng cào sạn cao + tiếng rít mỏng lang thang, tick khô mỗi vết nhỏ.
- **Chồng hình (double-exposure):** một bên đơn giản (trời, nước, sương), một bên chi tiết — 2 ảnh bận chồng nhau thành nhiễu xám; ngoài sáng hơn trong; viền tối + halo để bóng không thành sticker; ảnh trong bóng trôi chậm hơn đường viền; màn trập là âm thanh của phương tiện: click khi ảnh hiện vào hình, click nữa khi 2 ảnh thành một.
- **Chữ:** thẻ phim câm giữ 2.5–3.75s; LOG strip ascii-crt gõ từng từ đồng bộ giọng; caption VHS ≤ 32 ký tự/dòng, không bị nhiễu chạm; phụ đề double-exposure đặt ở vùng trống bên ngoài, không đè ảnh trong bóng.
- **Âm thanh:** ascii-crt: tiếng gõ máy, cursor, quạt máy, bíp; silent-film: piano/organ rạp + tiếng máy chiếu trong booth; backrooms: chỉ âm thanh băng ghi được (huỳnh quang, bước chân, thở, PA); scratch-film: vibraphone/glockenspiel/pizzicato/log drum + tiếng cào; double-exposure: dây (cello, double bass, viola, violin) + harp/glockenspiel mỗi đèn + màn trập. Mix cuối chuẩn −14 LUFS.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (ascii-crt: màn hình terminal; silent-film/backrooms: 4:3 trong khung 16:9 nếu brief chốt vậy; còn lại mặc định ngang 1920×1080), thời lượng khớp `window.DUR`; frame rate: silent-film lấy mẫu 16fps trong xuất 24fps, scratch-film 15 hình/giây ở 30fps.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) hỏng hóc đúng danh sách trong treatment, không thêm loại hỏng mới giữa chừng; (b) chữ đọc được ở cỡ thumbnail (silent-film) và ở cỡ chữ thật (ascii-crt: ký tự không vỡ lưới); (c) double-exposure: ngoài sáng hơn trong, bóng không thành sticker; (d) backrooms: không có hình chữ nhật sáng ở cuối hành lang, vùng tối đủ tối.
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, thẻ chữ không tràn, caption VHS ≤ 32 ký tự/dòng.
- Đồng bộ cue: mọi mốc trong `window.EV` (màn trập, xé tracking, thẻ chữ, đèn bật) có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích (chú ý: nền đen là chủ đích ở scratch-film — ghi rõ trong QA để không nhầm với đoạn đen lỗi).
- Riêng double-exposure: ghi rõ nguồn từng ảnh phong cảnh trong QA.md; ảnh không rõ licence thì không dùng.
- Bản quyền: không gắn tên/logo/nhãn hiệu thật vào phim; font dùng phải OFL và tự host; không dùng lại track lời thoại demo dùng TTS online của repo.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: style đã dùng + danh sách hỏng hóc cho phép, nguồn ảnh (double-exposure), bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian (với silent-film, `.srt` liệt kê chữ của các thẻ chữ).
