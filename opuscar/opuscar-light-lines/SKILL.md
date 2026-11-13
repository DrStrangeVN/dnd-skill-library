---
name: opuscar-light-lines
description: Kỹ thuật làm phim bằng ánh sáng và đường nét kiểu Lemo-Opuscar (nhóm Light & Lines, 5 style) — mạch in nhìn từ trên xuống, điểm sáng đom đóm, đường dòng của trường gió, toán học trên máy hiện sóng, và ống neon thủy tinh thật trên phố mưa. Dùng khi brief là giải thích một dòng chảy/hệ thống/thông tin chuyển động, hoặc kể chuyện bằng ánh sáng thay vì bằng vật thể. Ánh sáng là vật liệu, đường nét là thông tin; không có bề mặt đặc.
---

# Opuscar Light & Lines — Ánh sáng & Đường nét

Năm style, một nguyên tắc: không có bề mặt đặc. Hình ảnh được làm từ ánh sáng (điểm sáng, tia sáng, ống thủy tinh phát sáng, dòng điện chạy trên đồng) và từ đường nét (đường dòng, đường cong toán học, mạch in). Nền tối hoặc giấy ấm. Cái chuyển động *là* lời giải thích: cách ánh sáng chạy dọc một đường đã nói lên dòng chảy đó là gì.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Giấy phép: code MIT, tài liệu gốc CC BY-NC 4.0 (xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill); phim do mình làm ra thuộc về mình. Nội dung dưới đây viết lại bằng lời của mình, chỉ giữ các bất biến kỹ thuật (màu hex, thông số, luật nhịp, luật đọc chữ).

## Khi nào dùng

- Giải thích một hệ thống có dòng chảy: điện, nước, tín hiệu, hàng hóa, tiền (`circuit-board`).
- Kể chuyện dịu dàng, đêm tối, bằng điểm sáng: ký ức, thiên nhiên, gặp gỡ (`firefly-pointillism`).
- Cho thấy một trường vô hình: gió, dòng hải lưu, giao thông, bất kỳ dòng chảy nào (`flow-field`).
- Chứng minh toán học bằng hình: chuỗi Fourier, dao động, sóng (`oscilloscope-math`).
- Kể chuyện đêm phố mưa bằng biển hiệu: hành trình, danh sách địa điểm, một nhân vật đi qua các bảng hiệu (`neon-tubes`).
- Không dùng cho: giải thích máy móc bằng sơ đồ nét khô (nhóm Line Diagrams), kể chuyện nhân vật diễn xuất (nhóm Cartoons), chứng minh bằng dữ liệu đo thật (nhóm Instruments & Evidence).

## Khi nào KHÔNG dùng

- Brief cần vật thể đặc, bề mặt, chất liệu (gỗ, vải, kim loại nhìn thấy được): sang nhóm 3D & Miniature hoặc Traditional Crafts.
- Cần biểu đồ/trục/số liệu dạng bảng: đó là việc của `opuscar-data-maps` (`dataviz`).
- Muốn ánh sáng "đẹp cho đẹp" mà không mang thông tin: cả năm style đều bắt ánh sáng phải có nghĩa — màu sai, đường vẽ cho vui, hay tia sáng trang trí đều là lỗi của nhóm này.
- Cần nhân vật nói nhiều, thoại dài: `neon-tubes` kể chuyện tốt nhất không lời thoại; `oscilloscope-math` và `circuit-board` dùng chữ in trên thế giới, không dùng phụ đề dạng thanh bar.

## Nguyên lý cốt lõi

1. **Ánh sáng là vật liệu, đường nét là thông tin.** Không tô màu lên bề mặt; màu đến từ chính nguồn sáng (khí trong ống, dòng điện trên đồng, điểm sáng) hoặc từ mật độ đường nét.
2. **Mọi đường đều từ một mô hình thật.** Đường dòng tính từ trường thật (hàm `field(x, y, t)` từ dữ liệu hoặc mô hình công bố); đường cong toán học là chuỗi Fourier thật; mạch in chỉ vẽ tuyến thật; ống neon cong theo đúng thực hành uốn thủy tinh. Không đặt xoáy, không vẽ tuyến trang trí bằng mắt.
3. **Chuyển động của ánh sáng là lời giải thích.** Dòng một chiều chạy khác dòng xoay chiều; điểm sáng tụ lại khác điểm sáng tan ra; ống neon bật khác ống neon hỏng. Người xem phải đọc được ý từ cách sáng di chuyển, không chỉ từ lời thoại.
4. **Nền tối hoặc giấy ấm, không bề mặt đặc.** Đen chiếm hơn nửa khung (`firefly-pointillism`), hoặc giấy ấm làm màn hình (`flow-field`), hoặc nền gần đen của màn hình đo (`oscilloscope-math`).
5. **Mỗi màu mang một vai, không đổi vai giữa phim.** Đặc biệt: đỏ chỉ dành cho lỗi/vượt ngưỡng và xuất hiện tối đa một lần; màu nhấn chỉ dành cho thứ đang quan trọng.

## Hệ màu / bảng chất liệu bất biến (theo style)

### circuit-board — Mạch in
- Nền: mask hàn xanh lá ba bậc — laminate tối `#05190F`, pour giữa `#1C6A44`, viền/sợi sáng `#4AA977`. Không đổi màu mask theo cảnh. Kim loại: vàng ENIG `#D9B25B` cho pad và via, tối đa một điểm nhấn đồng trần. Mực: một trắng ngà cho mọi silkscreen.
- Ánh sáng mang nghĩa và là màu bão hòa duy nhất: **hổ phách** cho năng lượng/dòng điện (lõi gần trắng), **bạc-xanh** cho dòng thứ hai (nước, dữ liệu, hàng hóa) khi câu chuyện có hai dòng. Dòng thứ ba chỉ thêm màu sáng thứ ba nếu bắt buộc phải phân biệt. Đỏ dành cho lỗi, xuất hiện tối đa một lần.
- Mọi thứ nhìn từ trên xuống, không phối cảnh. Tuyến chạy 0/45/90° với góc vát (mitred); hai tuyến không cắt nhau trên cùng một lớp đồng — muốn cắt phải qua via xuống lớp dưới hoặc đi vòng.

### firefly-pointillism — Điểm sáng đom đóm
- Đen chiếm hơn nửa khung; mọi ánh sáng đến từ chính các điểm, không có ánh sáng môi trường, không bầu trời gradient, không bề mặt đặc.
- Một hồ điểm duy nhất cho cả phim, không tạo thêm, không hủy đi: điểm bay khỏi chỗ này tụ lại thành thứ khác ở chỗ kia. Nhân vật là silhouette chấm (viền dày, ruột thưa), đọc qua tư thế và hành động, không qua gương mặt.
- Bảng màu (tông giữa / lõi cháy): nhân vật chính vàng ấm `#B2A076` / `#F5ECC6`; bạn đồng hành xanh lá `#A3B286` / `#EEF5D6`; đom đóm và ánh sáng môi trường `#A6B279` / `#F0F5C8`; sao lạnh `#A6AAB2` / `#F0F2F5`; nền `#050708` → `#060907`. Độ sâu bằng kích thước và độ mờ: điểm nét thì nhỏ sắc, điểm mờ thành đĩa lớn nhạt.
- Render: splat vào 5 mức mờ σ ≈ 1,0 / 2,1 / 4,8 / 10,5 / 23 px (độ phân giải 1 / 1 / ½ / ¼ / ⅛); mỗi điểm rải ~16% năng lượng lên hai mức cao hơn để tạo halo; tone mapping tuyến tính × exposure, `1 − exp(−x)`, gamma 2,2.

### flow-field — Đường dòng gió
- Giấy ấm làm màn hình (khoảng `#ECE0C4` đến `#E9D3A6`), đất là wash nâu sẫm nhạt hơn, nước là xám lạnh mờ. Mực xanh-đen (khoảng `#262C38`) cho trạng thái lặng, bờ biển và chữ.
- Một thang độ lớn duy nhất, mực → slate → nâu → ochre → cam → đỏ son, chia bậc ở ngưỡng có nghĩa (cấp gió, giới hạn, mức an toàn). Thang đó in luôn thành chú giải, nên đường dòng tự làm khóa đọc của nó. Đỏ son (`#C83A24`) dành cho dải cực đoan và cho một verdict duy nhất trên màn hình. Không cầu vồng, không glow, không giấy màu.
- Hai lớp mực: đường khắc nền mảnh, và vệt ngắn hình thoi chạy dọc đường, nhanh hơn ở nơi trường mạnh hơn.

### oscilloscope-math — Toán học trên máy hiện sóng
- Một họ phosphor; màu là vai, không phải trang trí. Xanh lá tia (`#4DFF88`) cho thứ tín hiệu vẽ; xanh lá nhạt (`#8DFFB0`) cho lưới và chữ; trắng nóng (`#E6FFEC`) cho điểm mới nhất của tia, khớp nối và tia chớp của thứ vừa tạo. **Hổ phách (`#FFB547`) là kênh thứ hai**: con trỏ đo, giá trị đo, dấu của một phát hiện — không bao giờ dùng trang trí, không bao giờ dùng cho chính tín hiệu. Không hue nào khác. Nền màn hình `#010402`, ambient `#0B2412`.
- Ánh sáng phát ra, không phải mực: lõi sắc, bloom mềm, tâm trắng nóng ở nơi tia nhanh hoặc mới. Không fill màu phẳng. Vẽ bằng đường có bề rộng hằng số theo pixel màn hình (1,2–3,2 px) để đường vẫn là tia ở mọi mức zoom. Không có scanline (máy hiện sóng analog là màn hình vector).

### neon-tubes — Ống neon
- Nền tối trung tính (mặt tiền đêm, nhựa đường ướt); hue chỉ đến từ ống và ánh sáng chúng hắt ra. Màu khí theo vật lý: thủy tinh trong + neon = đỏ-cam; thủy tinh trong + argon và một giọt thủy ngân = xanh dương. Mọi màu khác là lớp phosphor (trắng sữa khi tắt). Ống chưa sáng vẫn thấy rõ là thủy tinh trong hoặc trắng sữa.
- Ống là hình trụ thật: cột khí bão hòa trong lòng (70–85% bán kính), thành thủy tinh mỏng, highlight dọc mép trên, halo tràn ra phía sau. Ống đứng cách bảng sơn trên giá đỡ với dây buộc; nét nối bằng double-back sơn đen; mỗi ống kết thúc bằng điện cực đen; có hộp biến áp gần đó. Đường kính ống 1,0–1,9 cm; dây buộc mỗi 22 cm.
- Mỗi biển một hue riêng để phố đọc thành một chuỗi. Nhân vật giữ hue của mình ở mọi nơi; không biển nào trong cùng cảnh dùng hue của nhân vật. Bảng sơn là phiên bản đậm, bão hòa thấp của màu ống (navy, đỏ rượu, tím cà, xanh chai).

## Quy trình sản xuất

1. **Chốt mô hình thật trước.** `flow-field`: viết trường dưới dạng hàm từ dữ liệu hoặc mô hình công bố — không đặt xoáy bằng mắt; đất, địa hình và vật thể tác động lên trường, không tác động lên nét vẽ. `oscilloscope-math`: một bộ số duy nhất sinh ra cả hình, cả số đọc, cả công thức — khung hình nào đóng băng lại cũng phải kiểm chứng được. `circuit-board`: chỉ vẽ tuyến thật; đồng trống lấp bằng thứ mạch thật có (via khâu, hàng rào via, vân mask), không tuyến trang trí.
2. **Treatment ngắn trước khi dựng:** chọn một ý chính + tối đa 2 ý phụ; mỗi ý: dòng chảy/thông tin nào đang chuyển động, nó thay đổi ra sao, beat nào là đỉnh. Với `firefly-pointillism`: liệt kê các lần điểm tụ/tan (mỗi lần tụ là một lần đổi cảnh, không cắt).
3. **Dựng page theo page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR`, `window.render(t)` thuần theo `t` (cấm `Date.now()`, cấm `Math.random()` không seed), `window.EV` — danh sách sự kiện âm thanh `{t, type}`, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`. Render bằng cách seek `t` qua headless Chrome.
4. **Timeline là nguồn sự thật duy nhất:** một bảng beat mà hình, phụ đề, nhạc, mix đều đọc từ đó.
5. **Render thử các frame hero của từng beat** → contact sheet soát: đường dòng có cắt nhau không, điểm sáng có đọc thành hình không, số đọc có khớp hình không — trước khi render full.
6. **Âm thanh theo bảng âm của style, mix xong đo loudness trên file cuối** (chuẩn −14 LUFS), QA đầy đủ rồi mới giao.

## Ngữ pháp dựng (theo style)

- **circuit-board:** camera luôn nhìn thẳng xuống (chỉ xoay quanh trục nhìn, ít). Các kiểu dòng phân biệt chỉ bằng cách ánh sáng chạy: xoay chiều — vệt ngắn lắc qua lại trên tuyến (tần số nguồn làm chậm) trên nền đường mờ đã tích điện; một chiều — dòng sáng liên tục sau một đầu chạy, có vệt chậm bên trong và dư sáng mờ dần sau đầu; hạ áp — tuyến mỏng dần, vệt nhỏ dần; dòng thứ hai — nhiều đường song song chạy vệt ở tốc độ khác nhau, nhanh ở giữa, có glint ngắn. 30 fps, từng khung; motion blur từ chuyển động màn hình đo được (shutter 180°, sub-frame 1 đến ~20), không blur qua cắt.
- **firefly-pointillism:** mọi chuyển cảnh đều xảy ra *bên trong* chất liệu: một dòng sáng đổ vào từ ngoài khung và đáp xuống từng điểm thành thế giới; điểm tụ lại thành hình mới; cơn gió đổi cảnh (một phía rời đi trước theo tọa độ x). Lấy nét là hình hiện ra: điểm kéo từ mờ thành sắc. 60 fps, từng khung; đường đi của hạt luôn là đường cong; thở chậm (±22%), đom đóm phần lớn tối — xung hẹp nên mỗi lúc chỉ khoảng 1/4 sáng.
- **flow-field:** đường dòng không bao giờ bật, nhấp nháy hay sắp lại: mọi thay đổi đều liên tục theo thời gian (trường, trọng số mức, fade, camera). Vệt chạy 60–300 px/giây; nén tốc độ để vệt nhanh nhất di chuyển chưa tới một chiều dài của chính nó trong một khung. Thời gian trong truyện chạy với tốc độ nào cũng được nhưng không bao giờ chạy ngược, ánh xạ qua một đường cong đơn điệu. Trong lúc giữ hình, camera vẫn creep chậm và vệt vẫn chạy: thế giới không bao giờ đóng băng. 30 fps.
- **oscilloscope-math:** camera sống trong thế giới (tâm và zoom); zoom logarit, tâm di chuyển để mục tiêu đứng yên trên màn hình khi zoom (bay tới một điểm). Chữ thành hình học: tiêu đề do tia viết, rồi chữ biến hình thành chủ thể của cảnh tiếp theo. Vật mới mọc ra từ điểm nó bám vào trong ~0,45 s, chớp trắng. Thêm vào thì tăng tốc chứ không lặp lại: một, rồi vài, rồi nhiều tới không đếm được. STOP đóng băng tín hiệu; camera vẫn có thể đi tiếp qua thế giới đóng băng.
- **neon-tubes:** nhân vật chuyển tư thế, không bao giờ tween/morph: một tư thế khóa mỗi beat hoặc mỗi nốt 8; đổi tư thế là tức thời. Tư thế phải mạnh: cú nhảy duỗi thành một đường, đáp tụ thành quả bóng. Strike (bật sáng): 100% trong 50 ms, tối 70 ms, 70%, tối, ramp lên đủ sáng trong 0,1 s. Ống argon-thủy ngân khởi đầu tím mờ rồi ấm dần thành xanh. Mọi cú chuyển đều đáp lên lưới nhạc (beat, nốt 8, nốt 16). 30 fps.

## Công thức & kỹ thuật đặc thù

- **circuit-board:** các lớp từ dưới lên, tất cả trong không gian mạch dưới một camera world→screen: laminate FR-4 xanh tối với texture dệt thủy tinh hai octave crossfade; copper pour lấp đầy mạch, mọi thứ là clearance đục ra khỏi nó (kênh, hồ, biển, keep-out); render hai lượt (viền sáng với clearance thường, rồi fill với clearance nở ~1,6 px) để mọi mép đồng có viền vát; tuyến: nét viền + nét fill hẹp hơn, đầu tròn, kênh laminate trần chạy hai bên. Chữ là silkscreen: một font nét đơn đi như tuyến (nét 0/45/90°, góc vát, đầu tròn), vẽ từng nét một; chữ Hán cũng đi trên lưới 0/45/90° với cùng bề rộng nét, chỉ dùng chữ giản thể, kiểm từng glyph ở cỡ lớn.
- **firefly-pointillism:** nhân vật là rig xương 2D (capsule và polygon thuôn); điểm bám theo tọa độ cục bộ chuẩn hóa trên từng bộ phận nên tư thế, tỉ lệ, lật hình không bao giờ resample. Chữ tiêu đề làm bằng điểm: render chữ thành mask, lấy mẫu trên lưới jitter (không random), một hạt mỗi mẫu — tiêu đề CJK 140–170 px cần ~3.400 điểm, dòng Latin 30–40 px cần ~800; thưa hơn là nét chữ không đọc được. Chữ đã đáp thì đứng yên tuyệt đối (chỉ shimmer dưới pixel), có flash ngắn khi đáp.
- **flow-field:** engine đường dòng cho trường biến thiên theo thời gian: hạt giống là điểm cố định của lưới jitter *theo đơn vị thế giới*, một lưới mỗi mức chi tiết (khoảng cách hạt giống giảm một nửa mỗi mức); mỗi đường tích phân số bước RK2 cố định, độ dài cố định, cả hai hướng, bước chỉ thu nhỏ gần điểm lặng. Không test va chạm, không dừng sớm: mỗi đường là hàm liên tục của trường. Mật độ: trọng số mức = 1 − |log₂(khoảng cách hạt giống trên màn hình / mục tiêu)|; hai mức kề luôn cộng thành một. Khoảng cách hạt giống ≈ 36 px ở 1080p, nửa dài 4 khoảng cho đường cách nhau trung bình ~6 px.
- **oscilloscope-math:** ba kênh sáng (vết tia, lưới + chữ, lõi trắng nóng) cộng một kênh thứ hai tùy chọn cho đo đạc; bloom là nhiều lần blur Gaussian ở cỡ 1/2 đến 1/16 cộng lại; chỗ sáng chồng lên nhau chuyển dần sang trắng qua vai mềm, không clip. Afterglow vẽ ra, không tích lũy khung: 8–10 bóng ma cách nhau vài mili-giây, mờ theo đường cong lũy thừa, cộng vệt ngắn sau điểm chuyển động. Tia nhanh để lại ít sáng hơn: đoạn dốc vẽ mờ hơn (khoảng 55–60% ở cạnh dọc); phần cũ của vết cuộn mờ dần theo tuổi. Lưới: đường chấm nhỏ, trục giữa đặc với vạch 0,2 division, tinh dần theo mức 5 khi camera zoom.
- **neon-tubes:** ống = polyline đường tâm theo mét, góc fillet bán kính khoảng một đường kính ống, nối bằng double-back sơn đen, tay áo sơn và nắp điện cực ở mỗi đầu (đầu vỡ không có). Lớp mặt cắt: mỗi ống vẽ thành dải đồng tâm theo chiều cao hình trụ `h = sqrt(1 − r²)` kèm mã vật liệu (trong, phủ, sơn đen, kim loại); shader lấy normal từ gradient Sobel của profile đó: cột khí trong 70–85% bán kính, viền thủy tinh, mép Fresnel, vệt specular, khúc xạ thứ phía sau. Lớp phát sáng ở nửa độ phân giải, blur thành pyramid, dùng hai lần: làm sáng bề mặt (lobe cỡ mét, 2 cm đến 3 m) và làm bloom trên màn hình. Nhân vật dựng từ silhouette: rig nhỏ (mông, thân, ngực, cổ, đầu, mõm, tai, chân hai đoạn) hợp thành bằng SDF, lấy contour ngoài bằng marching squares, mở một điểm cho điện cực (thường dưới thân).

## Âm thanh (theo style)

- **circuit-board:** tất cả tổng hợp — tone sine/saw, sóng xung, chuông FM và glockenspiel, click relay (transient hai click), kick mềm và tick 16 nốt, noise đã lọc. Drone chỉnh theo hum nguồn (50 Hz ≈ G1; 60 Hz ≈ B♭1) để hum thuộc về tông nhạc. Luật tai nghe theo được: tone tremolo theo biên độ = xoay chiều, tone ổn định = một chiều; linh kiện đổi dạng này sang dạng kia nghe như tremolo mượt thành tone dài. Tiếng đến nơi là click relay hoặc burst noise đã lọc; hạ áp là relay thấp dần mỗi lần; vẽ silkscreen là tiếng xước hạt mờ.
- **firefly-pointillism:** nhạc cụ thật lấy mẫu — harp (glissandi cho dòng chảy, arpeggio cho tụ lại, hợp âm cho đáp xuống), glockenspiel, chuông tay, glass harp, vibraphone cho từng ánh sáng, chạm và chớp; pad dây và tremolo, sáo, timpani và cymbal treo cho tụ hình và gió. Trưởng với màu Lydian ♯4: sáng và diệu kỳ, không buồn; có thể chuyển thứ khi mất mát. Hành động của hạt ↔ âm thanh: tụ lại = arpeggio dâng + swell cymbal đáp đúng hợp âm; tan ra = gió và glockenspiel rơi; đáp xuống = pluck harp hoặc chuông tay; chớp đồng bộ = sweep harp nhanh.
- **flow-field:** trường là nhạc cụ chính — noise đã lọc ba dải (thân 90–420 Hz, giữa 0,4–1,6 kHz, không khí 1,8–6,5 kHz) với mức theo độ lớn trung bình trên màn hình, và tiếng huýt dải hẹp theo giá trị mạnh nhất (≈ 400 Hz + 24 Hz mỗi m/s); gust chậm, xác định; pan về phía mạnh nhất của màn hình. Nhạc nền: dây trầm giữ lâu, một harmonic dài, pluck/mallet thưa. Mỗi bản ghi dữ liệu một tone có cao độ (cao dần theo hạng); verdict đáp trên piano trầm và timpani.
- **oscilloscope-math:** tín hiệu nghe được — tone lặng tính từ cùng con số với vết trên màn hình (mỗi vòng tròn mới thêm một harmonic của nó). Lead: tone synth pluck mà timbre theo tín hiệu (sine thuần cho một số hạng, giàu dần mỗi khi thêm số hạng); chuông đã chỉnh (glockenspiel, vibraphone bowed, chuông sine) cho sự kiện; bass synth mềm với harmonic 2 và 3. Foley dụng cụ: clack relay cho RUN/STOP và nguồn, click detent núm, blip ngắn cho readout và con trỏ, tick mỗi glyph khi tia viết, sweep noise đã lọc cho morph và dive, zap rơi cho tắt nguồn; hum điện mờ.
- **neon-tubes:** âm của chính chất liệu — hum biến áp 100/120 Hz với harmonic vo ve, click mỗi lần chớp, clack relay cho chaser và khung chuyển, crackle cho ống hỏng, ting thủy tinh và xì cho vết nứt, mưa trên nhựa đường ướt, nhỏ giọt, plop trong vũng. Nhân vật "nói" bằng neon: hơi thở là hum có run, bước chân là click relay, đáp xuống là thump mềm; không tiếng động vật. Nhạc: city pop / electronic pop tổng hợp ở tempo nhảy; mỗi biển bật sáng chơi nốt tiếp theo của một dòng đi lên; biển tắt chơi dòng đi xuống. Im lặng vẫn có hum.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1280×720 hoặc 1920×1080), thời lượng khớp `window.DUR`. `circuit-board` và `neon-tubes`: 30 fps; `firefly-pointillism`: 60 fps; `flow-field`: 30 fps.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) đường dòng không cắt nhau, hạt giống không đổi theo khung (`flow-field`); (b) số đọc tính từ đúng giá trị vẽ ra, không gõ tay (`oscilloscope-math`, `circuit-board`); (c) màu khí đúng vật lý — không ống trong màu xanh lá, không neon màu xanh dương (`neon-tubes`); (d) nhân vật đọc được qua silhouette, outline đủ ~0,7 điểm mỗi pixel (`firefly-pointillism`); (e) tuyến không có tuyến trang trí, không cắt nhau trên một lớp (`circuit-board`).
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn thẻ, chữ Hán (nếu có) kiểm từng nét ở cỡ lớn, không đoán nét.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame. Riêng `neon-tubes` và `circuit-board`: mọi cú chuyển/bật sáng đáp đúng lưới nhạc.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Bản quyền: ghi rõ nguồn dữ liệu/mô hình trong QA.md; không dùng tên/logo/thương hiệu thật, không dùng lại câu chuyện demo của repo gốc.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: nguồn dữ liệu/mô hình + licence, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.
