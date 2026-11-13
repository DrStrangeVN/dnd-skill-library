---
name: opuscar-cartoons
description: Kỹ thuật phim hoạt hình 2D vẽ tay mô phỏng bằng code (spin-out từ bộ Lemo-Opuscar) — 6 style: ống cao su 1930, anime cel 80s, sitcom khoa học viễn tưởng, hoạt hình phẳng 50s, lịch sử hài bằng giấy, manga đen trắng. Dùng khi brief là "hoạt hình cổ điển", "anime cel thập niên 80", "kể lịch sử bằng truyện tranh", "manga phân khung". Mọi nội dung do brief quyết định — skill chỉ giữ ngữ pháp hoạt hình và kỷ luật sản xuất.
---

# Opuscar Cartoons — Hoạt hình 2D vẽ tay

Hoạt hình 2D vẽ tay mô phỏng bằng code: cel phẳng bước 8–12fps, viền sôi, màu phẳng, nền sơn riêng. Diễn xuất đến từ tư thế và thời gian, không phải từ chi tiết: một cái chớp mắt giữ 3 nhịp có thể nặng hơn cả một đoạn chạy.

Nguồn kỹ thuật: 6 style trong repo Lemo-Opuscar tại `~/workspace/lemo-opuscar/styles/{rubber-hose,cel-anime-80s,scifi-toon,midcentury-toon,comic-history,manga-panels}/STYLE.md` — đọc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện/nhân vật/nhãn hiệu của phim mẫu.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Giấy phép: code MIT, tài liệu gốc CC BY-NC 4.0 (hệ REUSE của repo); phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

## Khi nào dùng

- Gag hình thể, chase, nhạc dẫn hành động: tay chân ống cao su, mọi vật thở theo nhạc.
- Khung cảnh lớn, nhân vật nhỏ, ánh sáng xuyên cel: anime cel 80s, tĩnh lặng làm kịch tính.
- Hài thoại: mục tiêu nhỏ xíu nhưng dùng phương tiện khổng lồ; hai nhân vật đối lập nhau.
- Giải thích/hướng dẫn bằng người dẫn phẳng 50s: thân giữ nguyên, chỉ tay/mắt/miệng chuyển động.
- Lịch sử/bản đồ đổi chủ: lãnh thổ đổi tay bằng hành động cắt, xé, dán trên bản đồ in cổ.
- Kể chuyện bằng khung truyện: panel là đơn vị thời gian, đọc phải sang trái, trên xuống dưới.
- Không dùng cho: phân tích trên footage thật (opuscar-telestrator), sơ đồ máy móc chính xác (opuscar-line-diagrams), đồ họa chữ/poster (opuscar-graphic-type).

## Khi nào KHÔNG dùng

- Cần diễn xuất mặt chi tiết, lip-sync chính xác từng âm: nhóm này diễn bằng tư thế giữ và thay đổi nhỏ, không phải bằng khẩu hình thật.
- Cần 3D, chuyển động mượt 24fps mọi lớp: nhân vật nhóm này cố tình bước (12fps hoặc 8fps); mượt toàn bộ sẽ mất chất.
- Chủ đề nghiêm túc, tài liệu, điều tra: hài hình thể và cel phẳng sẽ làm lệch tông — dùng nhóm Edit & Documentary hoặc Instruments & Evidence.
- `comic-history` và `manga-panels` (đánh dấu ✦ trong repo): **cần máy tạo ảnh mới bắt đầu được.** Không có image generator thì không làm 2 style này — đề xuất style khác trong nhóm (ví dụ rubber-hose hoặc midcentury-toon). Tuyệt đối không vẽ nhân vật bằng code để thay thế ảnh tạo sẵn.

## Nguyên lý cốt lõi

1. **Bước, không trượt.** Nhân vật bước 12fps (hoặc 8fps cho nhịp diễn), camera và ánh sáng chạy 24fps. Camera bước theo nhân vật sẽ giật — tách 2 tầng nhịp ra.
2. **Nền và nhân vật là 2 thế giới khác nhau.** Nền sơn mềm/chuyển sắc, nhân vật cel phẳng/viền cứng; tương phản đó chính là vẻ đẹp. Đừng đồng nhất chúng.
3. **Diễn bằng tư thế giữ.** Một tư thế giữ lâu + một thay đổi nhỏ (mắt liếc, nuốt nước bọt, giọt mồ hôi) kể nhiều hơn một đoạn chuyển động dài.
4. **Nhịp là kịch bản.** Beat nhạc = beat hành động: bước chân là nốt, cú đấm là nốt, cú cắt là nốt. Chọn tempo sao cho một beat là số frame nguyên ở 24fps (8, 10, 12, 16 hoặc 20 frame).
5. **Màu phẳng, viền có ý.** Viền sôi (boil), màu tô lệch khỏi nét, bóng là mảng cứng — không gradient trên cel, không bóng đổ mềm.

## Bảng 6 style — bất biến từng style

| Style (slug) | Nhận diện nhanh | Màu bất biến | Chữ | Nhịp/chuyển động |
|---|---|---|---|---|
| `rubber-hose` — ống cao su 1930 | Tay chân ống đều, không khuỷu/khớp; găng trắng 4 ngón; mắt bánh (đồng tử đen có khe); giày tròn lớn; nền aquarelle xám; phim 35mm cũ, khung 4:3 | Chỉ thang xám: ~6 bậc xám + trắng nhân vật riêng; không một sắc màu nào, kể cả vết xước phim; nhân vật giữ 2 cực trắng/đen, nền ở xám giữa; tăng tương phản cuối ~1.1–1.15 | Phụ đề là thẻ tiêu đề thời kỳ: tấm gần đen, viền đôi trắng, góc trang trí chấm-vòng; chữ IM Fell English SC ~36px, trắng giấy; thẻ bật/tắt, không fade; giữ ≥ max(1.8s, thoại + 0.6s) | Nhân vật bước 12fps, camera 24fps; mọi vật thở theo nhạc: squash/stretch theo `cos(2π·beats)`, cực trị mỗi nhịp; chu trình chạy ~8 hình, một bước mỗi nhịp |
| `cel-anime-80s` — anime cel 80s | 4 lớp: nền sơn airbrush → cel phẳng → ánh sáng xuyên cel → băng CRT; cel viền màu (không đen tuyền), bóng/mảng sáng cạnh cứng | Nền sơn mang gradient/không khí; cel phẳng, ít màu, bão hòa; mỗi thời điểm trong ngày một bộ màu riêng, không dùng filter phủ khung; nhân vật chính một màu nhấn xuyên mọi bộ sáng; da có màu riêng từng bộ sáng | Phụ đề trên băng, trong lớp CRT: sans bán condensed (Barlow Semi Condensed 600, ~50–56px), vàng kem, viền tối dày, ~96px trên đáy; tiêu đề: chữ Latin nghiêng nặng, hiệu ứng chrome; giữ ≥ max(1.8s, thoại + 0.6s) | Nhân vật bước 12fps; nhịp diễn (chớp, mở mắt, mấp máy) bước 8fps; camera/ánh sáng/mưa 24fps; tóc/vải là dải sóng sine, chu trình 4 hình (6 khi lặng); di chuyển ánh sáng, không vẽ thêm hình |
| `scifi-toon` — sitcom khoa học viễn tưởng | Hoạt hình TV 2D cho người lớn: viền dày đều sôi, màu phẳng, bóng mảng cứng, mắt trắng lớn đồng tử nhỏ, miệng đàn hồi, sinh vật kỳ dị mà dễ thương, máy móc viễn tưởng như đồ gia dụng | Một bảng màu mỗi thế giới, 3–5 màu, khác hẳn thế giới trước cả sắc lẫn giá trị để khán giả đọc được "đã nhảy"; màu viền và trắng mắt không đổi; màu phát sáng chỉ thuộc về thiết bị du hành | Phụ đề: sans tròn nặng (Baloo 2 ExtraBold ~50px), trắng viền đen ~11px, kèm viên ghi tên người nói màu của nhân vật (viền sôi); dòng dài >1300px ngắt 2 dòng; dòng cũ mờ ~70%; giữ ≥ max(1.8s, thoại + 0.6s) | Nhân vật bước 12fps; camera/xoáy cổng/vật bay 24fps; diễn trên chuyển động: tư thế giữ + thay đổi nhỏ (mắt giật, đồng tử trượt, nuốt, mồ hôi); thở squash ±1%; mọi cử chỉ có chuẩn bị → hành động |
| `midcentury-toon` — hoạt hình phẳng 50s | Màu in phẳng, viền mực mỏng thở nhẹ không khép kín; mỗi mảng màu là một "cel" in lệch vài px khỏi nét, đổi lại mỗi 2 frame nên hình rung như sơn đăng ký tay; người hình học, phòng chỉ là một mặt màu | Nền giấy ấm, mực gần đen ấm, màu bổ sung dịu thời kỳ nguyên tử; không màu thuần/neon; một màu nền mỗi cảnh (tường tông nhạt, sàn tông đậm); vật phẩm giữ một màu suốt phim, màu nhấn khác sắc với nó | Script 50s cho dòng mở (Oleo Script Bold); serif slab cho tiêu đề/số (Alfa Slab One); sans hình học cho thân/nhãn (Jost 500/600); thẻ chú thích: tấm giấy bo tròn viền mực mỏng, chữ sans ~40px | Tư thế/tay/viền rung đổi ở 12fps; camera/iris wipe/mũi tên 24fps; thân người dẫn giữ nguyên, chỉ tay/mắt/miệng động; tay: chuẩn bị → hành động nhanh 0.15–0.25s → thu về, đáp đúng nhịp |
| `comic-history` ✦ — lịch sử hài bằng giấy | Bản đồ in cổ trên giấy (gợn bờ biển, lưới kinh vĩ, viền mực, mảng in phẳng, tên small-caps); quốc gia là rối giấy nối đinh tán đồng, đầu tròn lớn, đổi biểu cảm bằng cách thay đầu; lãnh thổ đổi chủ bằng cắt/xé/dán, không bao giờ chỉ tô lại | 2 nhân vật chính giữ 2 màu suốt phim (ví dụ xanh in + xám in); nước láng màu in nhạt (cát, xô thơm, gạch, đất son), không tranh; miếng đất mới chỉ lệch một nấc so với màu in của chủ; mực một màu nâu đen ấm, giấy kem ấm `#F1E8D2` | Tên địa danh: serif khắc small-caps (IM Fell English SC), tracking rộng, mực thuần, không viền/phát sáng/bóng; chữ nhỏ: cùng họ roman/italic; mọi con số: serif có lining figures (Old Standard TT) — số kiểu cũ biến 1975 thành "I975" nên cấm dùng | Rối bước 12fps, camera/bóng 24fps; keyframe có overshoot lò xo: nhảy, lấy đà, đánh, ổn định; thay đầu nảy 1.07–1.10× trong 1–2 frame; một hình trung gian gánh cú đánh lớn |
| `manga-panels` ✦ — manga đen trắng | Chỉ mực và giấy: mọi xám là chấm/lằn screentone, không xám liên tục, không gradient; panel là đơn vị thời gian, mở theo thứ tự đọc phải→trái, trên→dưới, đúng nhịp; chữ hiệu ứng vẽ, không gõ máy | Giấy `#F3F0E8`, mực `#121212`, một màu spot duy nhất (mặc định đỏ son `#F03C1E`, có thể đổi sang màu thương hiệu của user, giữ bão hòa và đứng một mình); spot chỉ thuộc về một chủ thể và đồ họa nói thay nó | Hiệu ứng âm: katakana (Dela Gothic One), mỗi chữ slam 1.6–1.9×→1× overshoot, lệch 0.03–0.09s, xoay ±10°, 3 lớp (viền mực ×0.34, viền giấy ×0.27, tô mực), sôi ±1.5px ở 12fps; chữ nhỏ 0.62× và hạ thấp; thoại trong bóng, tường thuật trong hộp | Panel mở bằng wipe 0.1s theo hướng đọc, nội dung đáp từ hướng đó 40–110px, ổn định trong 0.22s; sôi: đường focus/speed/chữ vẽ lại 8–12 lần/giây với seed mới, hình đứng yên; rung: jitter tắt dần (τ 0.07s, 6–40px) mỗi cú đánh; dừng sôi tự nó đã là một sự kiện (thời gian đóng băng) |

## Quy trình sản xuất

1. **Chọn style trước, chọn tempo trước.** Style quyết định tầng hình (nền/cel/ánh sáng/băng), tempo quyết định beat. Ghi cả hai vào treatment trước khi dựng.
2. **Treatment ngắn, viết trước khi mở demo:** 3 cấu trúc ứng viên rồi chốt một; mỗi đoạn: mục tiêu nhỏ của nhân vật, cú lật, kết. Với comic-history/manga-panels: liệt kê ảnh cần tạo + prompt + tên file trước — chưa có ảnh thì chưa bắt đầu dựng.
3. **Bảng beat là nguồn sự thật duy nhất:** một bảng mốc giây → sự kiện hình → sự kiện âm mà hình, chữ, nhạc, mix đều đọc từ đó. Beat nhạc và beat hành động lệch nhau là lỗi.
4. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi tư thế/viền sôi là hàm của `t`, nhân vật đổi tư thế theo tiến độ trong cửa sổ beat của nó.
5. **Render thử model sheet/frame hero** (tư thế chính, biểu cảm chính, bảng màu từng thế giới) → soát với STYLE.md trước khi render full. Với style ✦: kiểm tra ảnh tạo ra khớp model sheet (cùng nhân vật, cùng bảng màu) trước khi dựng.
6. **Âm thanh theo bảng âm của style**, mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng

- **Rubber-hose:** mọi vật thở theo nhịp → Mickey-mousing (mỗi bước là một nốt, đạo cụ thành nhạc cụ: cầu thang thành piano, máy chữ thành trống) → tay chân ống vươn dài bất kỳ → cả thế giới nhảy đồng bộ ở đỉnh.
- **Cel-anime-80s:** nhân vật nhỏ phẳng trong thế giới sơn khổng lồ → tĩnh lặng làm kịch tính (cận cảnh giữ lâu, hòa âm đứng) → ánh sáng xuyên cel (biển hiệu/đèn/title phát sáng xuyên khung) → ngữ pháp tốc độ (vạch tốc độ, cắt nhanh, giữ hình).
- **Scifi-toon:** thế giới song song (mỗi lần nhảy = bảng màu mới + nhạc mới + sinh vật mới) → cặp đối lập (điềm tĩnh vs hoảng loạn) → luật 3 rồi bắn liên thanh (2 đáp án sai chậm, rồi thế giới 1 giây cắt theo nhịp) → mục tiêu nhỏ, phương tiện khổng lồ.
- **Midcentury-toon:** thân giữ, tay làm bước (một hành động tay mỗi bước, đúng nhịp) → thẻ gọi tròn (call-out) → màu lệch đăng ký làm thẻ thông tin ấm và thủ công → tuyến đường uốn quanh chướng ngại, mỗi vùng một nhịp.
- **Comic-history:** vạch cắt chấm in dọc biên giới → kéo cắt dọc vạch, đất cắt xám và gạch chéo → miếng mới rơi xuống với bóng lớn, đập xuống → xé lại (miếng bị xé rách xơ, còn mảnh vụn bên dưới) và ném sang rối đối thủ.
- **Manga-panels:** panel = cú cắt, một panel mỗi nhịp → panel tách = nổ (1→2→4→8→16, mỗi ô một frame của chuyển động, đánh số theo thứ tự đọc, chớp mỗi ô mới) → panel hợp thành spread đôi (đường gutter co về 0) → dừng sôi = đóng băng thời gian.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; sôi/rung phải suy từ hash xác định của frame), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Tầng hình:** tách nền sơn, cel nhân vật, lớp ánh sáng, lớp phát lại (CRT/băng/phim cũ) thành các canvas riêng; cel bước 12fps, camera/ánh sáng 24fps; không bao giờ để camera bước theo nhân vật.
- **Viền sôi (boil):** viền/vệt tốc độ/chữ hiệu ứng vẽ lại 8–12 lần/giây với seed mới; hình nhân vật đứng yên khi sôi chỉ chạy trên đường nét. Ở midcentury-toon, mảng màu lệch khỏi nét vài px và đổi lại mỗi 2 frame.
- **Ánh sáng xuyên cel (cel-anime-80s):** nền sơn vẽ 1 lần lúc tải (cặp màu + phát sáng), sau đó chỉ trượt; ánh sáng đi qua cel bằng cách quét dải màu trên cel đang giữ; bloom lấy từ canvas phát sáng, ngưỡng cao, yếu trên màu.
- **Màu spot (manga-panels, comic-history):** một màu duy nhất, không lan sang quần áo/chữ/hiệu ứng; xám chỉ bằng chấm/lằn screentone, tính ở kích thước hiển thị; fade bằng wipe, không bằng alpha.
- **Chữ:** chữ bắt buộc đọc giữ ≥ max(1.8s, thoại + 0.6s); phụ đề scifi-toon có viên tên người nói; comic-history: không 2 bóng thoại cùng lúc, bóng thoại không đè tên địa danh; manga: hiệu ứng âm sôi, chữ nhỏ hạ thấp 0.62×.
- **Âm thanh:** nhạc dẫn hành động (rubber-hose: ban nhạc sống thời kỳ, mỗi bước là nốt); anime 80s: synth/ballad thời kỳ + tiếng băng CRT (chroma bleed là âm thanh, không chỉ hình); scifi-toon: thoại là nhạc, ngắt lời và khoảng lặng vụng về là nhịp; midcentury: nhạc nhẹ thời kỳ + tiếng tay/đạo cụ; comic-history/manga: tiếng giấy (cắt, xé, dán, lật) + tiếng bút mực + chớp panel. Mix cuối chuẩn −14 LUFS. Lưu ý: không dùng lại track lời thoại demo dùng TTS online của repo.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1920×1080, 24fps; rubber-hose 4:3 trong khung 16:9 nếu brief chốt vậy), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) nhân vật bước đúng nhịp (so frame giữa-nhịp và cuối-nhịp của cùng một tư thế); (b) nền và cel tách lớp rõ, không lẫn; (c) màu spot/màu nhấn không lan; (d) viền sôi chạy mà hình không rung theo.
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn thẻ/bóng thoại, thẻ tiêu đề thời kỳ không che hành động.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame; beat hành động rơi đúng beat nhạc.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Riêng style ✦ (comic-history, manga-panels): xác nhận ảnh đã có từ máy tạo ảnh và khớp model sheet trước khi dựng; không có ảnh thì dừng và đổi style, không vẽ nhân vật bằng code.
- Riêng manga-panels: mọi xám phải là chấm/lằn — xám liên tục, gradient, alpha phủ tone đều là lỗi; panel mở đúng thứ tự đọc phải→trái, trên→dưới.
- Bản quyền: font dùng phải OFL và tự host; không gắn tên/logo/nhân vật thật vào phim; không dùng nhân vật thuộc bên thứ ba; credit hư cấu, không dùng tên người thật.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: style đã dùng + tempo, bảng beat đã thực hiện, nguồn ảnh (với style ✦: máy tạo ảnh nào, prompt/file nào), kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian, model sheet.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.
