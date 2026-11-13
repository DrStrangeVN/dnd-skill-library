---
name: opuscar-router
description: Router điều phối toàn bộ thư viện phim làm bằng code Lemo-Opuscar (99 style, 15 chuyên đề) — chọn chuyên đề và style theo brief, rồi trỏ sang skill nhóm chuyên trách. Dùng khi brief chưa chốt style, khi cần so sánh nhiều style cho một đề tài, hoặc khi cần pipeline chung (treatment → page contract → render headless → giọng + nhạc + mix → mux −14 LUFS) và QA chung trước khi giao cho skill nhóm làm chi tiết.
---

# Opuscar Router — Điều phối 99 style

Router này không thay thế 15 skill nhóm — nó chọn đúng nhóm, rồi giao việc cho skill đó. Đọc router để chọn style; đọc skill nhóm để giữ đúng bất biến kỹ thuật của style (màu hex, thông số, luật nhịp, luật đọc chữ).

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Giấy phép: code MIT, tài liệu gốc CC BY-NC 4.0 (xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill); phim do mình làm ra thuộc về mình. Mô tả style dưới đây viết lại bằng lời của mình; không dùng lại câu chuyện, nhân vật hay lời thoại của phim demo gốc.

## Cách dùng router

1. Đọc brief: đề tài là gì, khán giả là ai, cảm xúc nào, dữ kiện nào phải đúng, phim dài bao nhiêu, có tư liệu/dữ liệu thật không.
2. Đối chiếu với bảng "Chọn theo brief" bên dưới để khoanh 2–3 chuyên đề.
3. Đọc danh mục 99 style, chọn 1 style chính + 1 style dự phòng.
4. Mở skill nhóm tương ứng (bảng tra cứu cuối file) và làm theo nó từ treatment trở đi. Không dựng phim chỉ từ router.
5. Nếu brief nêu tên một style bằng tên tiếng Anh/tiếng Trung/tên cũ/tên thư mục: tra trong danh mục dưới đây rồi mở đúng skill nhóm.

## Chọn theo brief

| Brief | Chuyên đề ưu tiên | Gợi ý |
|---|---|---|
| Phân tích một pha bóng/trận đấu, vẽ lên hình thật | Edit & Documentary | `telestrator` (skill `opuscar-telestrator` đã có) |
| Tin tức, bản tin, điều tra bằng tư liệu thật | Edit & Documentary; Instruments & Evidence | `caption-news`, `visual-investigation`, `news-package`, `archive-lighttable` |
| Giải thích nhanh một khái niệm, video học thuật ngắn | Sketch & Board; Line Diagrams | `whiteboard`, `stick-explainer`, `sketchnote`, `blueprint`, `iso-infographic` |
| Giải thích máy móc, hệ thống, quy trình | Line Diagrams; Light & Lines | `teardown`, `precise-mechanism`, `assembly-line-diagram`, `circuit-board` |
| Quảng cáo / giới thiệu sản phẩm phần mềm | Screens & Interfaces | `dark-keynote`, `living-screencast`, `desktop-flythrough` |
| Quảng cáo / giới thiệu vật thể | 3D & Miniature; Screens & Interfaces | `glass-product`, `hologram-hud`, `brick-toy` |
| Kể chuyện thiếu nhi, ký ức, truyện cổ | Painting & Illustration; Traditional Crafts; Cartoons | `crayon-book`, `watercolor`, `shadow-puppet`, `papercut-red`, `rubber-hose` |
| Kể chuyện bằng dữ liệu, số liệu có nguồn | Data & Maps; Instruments & Evidence | `dataviz`, `white-model`, `data-physical`, `satellite-briefing` |
| Bản đồ, hành trình, tuyến đường | Data & Maps | `transit-map`, `map-explainer`, `flow-field` |
| Khoa học: đo đạc, mẫu vật, nhiệt, vật liệu | Instruments & Evidence; Light & Lines | `microscope`, `lidar-survey`, `thermal-camera`, `security-xray`, `oscilloscope-math` |
| Lịch sử | Film & Tape; Print & Printmaking; Traditional Crafts | `newsreel`, `silent-film`, `vintage-collage`, `ukiyoe`, `ink-wash` |
| Game, văn hóa chơi game | Games | `pixel-rpg`, `hd-2d`, `microgame`, `game-show` |
| Thơ, cảm xúc, đêm, ánh sáng | Light & Lines; Film & Tape | `firefly-pointillism`, `neon-tubes`, `double-exposure` |
| Một nơi chốn, một địa điểm | 3D & Miniature; Screens & Interfaces | `tilt-shift`, `lowpoly-island`, `memphis-diorama`, `isometric-picture-book` |
| Chữ và đồ họa làm nhân vật chính | Graphic & Type | `swiss-motion`, `bauhaus-shapes`, `text-flash-cuts`, `silhouette-rhythm` |
| Chưa biết chọn gì, cần xem toàn cảnh | Đọc danh mục 99 style bên dưới | Chọn 2–3 style gần brief nhất rồi hỏi user |

Quy tắc chọn nhanh: **tư liệu thật có trước thì chọn nhóm dùng tư liệu** (Edit & Documentary, Instruments & Evidence); **số liệu thật có trước thì chọn nhóm dùng số liệu** (Data & Maps); **không có gì ngoài ý tưởng thì chọn nhóm vẽ bằng code thuần** (Sketch & Board, Graphic & Type, Light & Lines, 3D & Miniature). Style đánh dấu ✦ cần máy tạo ảnh mới bắt đầu được — kiểm tra trước khi hứa.

## Danh mục 99 style (15 chuyên đề)

### 1. Edit & Documentary — Dựng phim & Tư liệu (8) → `opuscar-edit-documentary`
- `caption-news` — Tin tức xem không cần tiếng: chữ caption khổ lớn dẫn nhịp, con số nào cũng kèm nguồn trên màn hình.
- `newsreel` — Phim thời sự thập niên 1920: tư liệu thật trong khung máy chiếu 1.37:1, thuyết minh dí dỏm, nhạc ban nhạc sống.
- `countdown` — Một sự kiện thật chạy đúng thời gian thực, đồng hồ đếm ngược làm chủ, nhiều ô hình chia màn hình đồng bộ từng giây.
- `city-symphony` — Phim về một thành phố: nhạc viết trước làm kịch bản, time-lapse cắt đúng nhịp, máy móc chạy nhanh, con người chạy chậm.
- `visual-investigation` — Điều tra bằng hình: nhiều nguồn độc lập cùng chỉ vào một thời điểm, một đồng hồ chung xuyên suốt.
- `kino-montage` — Tư liệu thật cắt theo nhịp 120 BPM, in hai tông mực giấy, đỏ là màu duy nhất, chữ làm kết cấu.
- `telestrator` — Phân tích thể thao trên hình thật: xem pha chạy trước, đóng băng rồi vẽ vòng tròn/mũi tên lên khung hình. Skill riêng đã có: `opuscar-telestrator`.
- `news-package` — Bản tin truyền hình trọn gói: một hệ đồ họa thống nhất, thứ tự sting → rundown → từng tin → điểm danh → chào kết.

### 2. Painting & Illustration — Hội họa & Minh họa (5) → `opuscar-painting-illustration`
- `crayon-book` — Sách tranh trẻ em vẽ sáp màu trên giấy kem ấm, nét sôi nhẹ từng khung, màu lem ra ngoài viền.
- `watercolor` — Màu nước trên giấy sợi ấm: vệt cọ trong mờ chồng nhau, vật tự vẽ thành hình theo thứ tự kết cấu trước, chi tiết sau.
- `impasto` — Sơn dầu vẽ bằng bay: mỗi nhát bôi là một mặt phẳng màu có gờ, ánh sáng xiên tạo chiều cao cho lớp sơn.
- `urban-sketch` — Ký họa hiện trường: nét bút kim nâu sẫm run nhẹ, màu nước trong phủ lệch khỏi nét, chỗ trắng giấy giữ làm điểm sáng.
- `colored-pencil` — Minh họa khoa học bằng chì màu trên một tờ giấy duy nhất, bố cục cắt mặt đất để lộ thế giới ngầm bên dưới.

### 3. Sketch & Board — Phác thảo & Bảng (7) → `opuscar-sketch-board`
- `one-line` — Một nét bút duy nhất không nhấc lên vẽ trọn phim trên giấy trắng ấm, camera bám theo đầu ngòi.
- `whiteboard` — Giảng giải trên bảng trắng thật: bút lông vẽ theo thứ tự tay viết, bảng là bản đồ ý tưởng, camera đi giữa các vùng.
- `chalkboard` — Bảng đen xanh mực sạch trơn: phấn trắng viết đúng thứ tự nét chữ, tối đa ba màu phấn, vật thật trong phòng thật.
- `sketchnote` — Ghi chú trực quan trên giấy chấm lưới: fineliner đen, bút dạ xám và vàng, chữ viết tay, trang giấy dàn như một poster.
- `stick-explainer` — Người que làm sơ đồ: đầu tròn, thân một nét cong liền mạch, nhân vật diễn giải ý tưởng bằng hành động và kết nối.
- `ipad-sketch` — Phác thảo trên một trang giấy số duy nhất: nét chì trước, màu tô sau và lệch khỏi nét, luôn còn dấu vết đang vẽ dở.
- `marker-paper` — Một tờ giấy, một bút marker đầu tròn: đen dựng hình, xanh đánh dấu dữ kiện, đỏ dành cho ẩn số và đáp án cuối cùng.

### 4. Traditional Crafts — Thủ công truyền thống (7) → `opuscar-traditional-crafts`
- `ink-wash` — Thủy mặc trên giấy gạo: mực đen năm sắc cộng một dấu triện đỏ, khoảng trắng lớn, hình được vẽ thành chứ không cắt ghép.
- `shadow-puppet` — Rối bóng da nhuộm sau tấm màn trắng: màu đến từ ánh đèn xuyên qua, rối rung theo tay người điều khiển và dây gậy.
- `ukiyoe` — Tranh khắc gỗ Nhật: giấy washi ấm, màu phẳng in từng bản hơi lệch, đường nét đen, khung viền đôi và triện đỏ.
- `papercut-red` — Mọi thứ đều là giấy đỏ cắt kéo dán phẳng: chi tiết chỉ đến từ phần bị cắt bỏ, nhân vật là rối giấy nối bằng đinh tán.
- `paper-lantern` — Hộp đèn nông chứa nhiều lớp giấy cắt song song: đèn nền và bóng đổ tạo chiều sâu, mỗi cảnh là một vật thể thật.
- `stained-glass` — Cửa sổ kính màu ghép chì: kính chỉ sáng khi có nắng sau lưng và hắt bản sao màu xuống sàn đá, nhân vật cử động từng mảnh.
- `gilded-illumination` — Tranh chép tay dát vàng: màu phẳng viền mực chắc, lá vàng dán từng ô vuông, chỉ lóe sáng khi có ánh sáng quét qua.

### 5. Print & Printmaking — In ấn & Bản khắc (8) → `opuscar-printmaking`
- `risograph` — In riso: 2–3 mực spot trên giấy kem, mực chồng tạo màu thứ ba, bản in lệch nhẹ, chấm halftone cho tông giữa.
- `halftone-dossier` — Hồ sơ vụ án in trên giấy kem: bóng đổ bằng chấm halftone nhiều lớp, kẹp số hồ sơ, con dấu và biển tên tạo khung hành chính.
- `woodcut` — Khắc gỗ: đen là gỗ, trắng là phần dao đã gọt; hình hiện ra bằng từng nhát khắc, chữ bị soi gương cho đến khi kéo giấy.
- `engraving` — Khắc đồng: tông màu chỉ làm bằng đường kẻ — sáng là giấy trắng, tối là nhiều họ đường giao nhau, nét nở rồi thu nhọn.
- `silkscreen-poster` — Poster lụa đang in: mỗi màu là một lớp mực đục riêng, không chuyển sắc, các lớp lệch đăng ký 1–3 px tạo viền giấy hở.
- `printed-long-take` — Tranh cào một cú máy dài: chỉ mực, giấy và một màu đỏ; cảnh dựng 3D nhưng mọi giá trị đều là nét cào.
- `pop-art` — Tranh in pop: bốn bản màu trên giấy, tông giữa bằng chấm lưới cố định theo trang, lặp lại cùng một bản in với lệch đăng ký nhỏ.
- `vintage-collage` — Cắt dán từ ấn phẩm cổ thật: nhân vật là mẩu tranh khắc có viền giấy trắng, nền là giấy màu xé tay, mọi mảnh có độ dày và bóng.

### 6. Graphic & Type — Đồ họa & Chữ (8) → `opuscar-graphic-type`
- `swiss-motion` — Đồ họa Thụy Sĩ trên lưới: giấy phẳng, chữ đen, một màu tín hiệu, mọi chuyển động bám lưới và rơi đúng nhịp, không nảy.
- `spy-titles` — Mở đầu phim gián điệp thập niên 1960: mực phẳng bốn màu, mép cắt tay, bóng người làm bằng hình khối, chữ là kiến trúc.
- `art-deco` — Thế giới Art Deco: đường viền vàng trên nền đen ấm, khối airbrush viền vàng, chuyển động cơ học đối xứng quanh một trục dọc.
- `pictogram-motion` — Kể chuyện bằng pictogram: mỗi thẻ một biểu tượng làm một hành động, tiêu đề khổng lồ, mỗi chương một màu riêng.
- `bauhaus-shapes` — Hình học Bauhaus làm dữ liệu: diện tích hình tỉ lệ với con số, tròn là cái lớn lên, vuông là cái ở yên, tam giác là độ dốc.
- `flat-space-explainer` — Du hành tỉ lệ trong không gian phẳng: màu đặc không chuyển sắc, vật sáng nằm trên hai vòng tròn cứng, một nhân vật đeo kính dẫn đường.
- `text-flash-cuts` ✦ — Chữ làm hình ảnh va chạm với kiến trúc phẳng và nhân vật ba trạng thái; thẻ chữ là lời thoại, tiêu đề chương và dấu câu của cú cắt. Cần máy tạo ảnh.
- `silhouette-rhythm` — Bóng đen trên nền sáng: mọi thông tin nằm ở đường viền, tư thế rơi đúng nhịp, bầu trời đổi màu làm đồng hồ.

### 7. Line Diagrams — Sơ đồ nét (8) → `opuscar-line-diagrams`
- `blueprint` — Toàn phim trên một tờ bản vẽ xanh Prussian: nét trắng, phép chiếu trực giao, quy ước kỹ thuật khô và chính xác.
- `iso-infographic` — Infographic đẳng cự phẳng: không phối cảnh, ba tông mặt phân biệt khối, số liệu dựng bằng biểu tượng và cộng được.
- `teardown` — Bóc tách sản phẩm thật: hình học lấy từ file kỹ thuật, các lớp nổi trên một trục, chụp PBR với đường dẫn số liệu.
- `hardcore-info` — Mặt cắt bằng nét mực trên giấy trắng ấm: nét có thứ bậc độ dày, một màu nhấn duy nhất đánh dấu đường đi của câu chuyện.
- `precise-mechanism` — Sơ đồ máy tô màu theo hệ thống: mỗi bộ phận mang màu của hệ nó thuộc về, bánh răng quay đúng tỉ số răng thật.
- `instruction-manual` — Tranh sách hướng dẫn: một góc đẳng cự duy nhất cho cả phim, nét mực một cỡ, màu phẳng tối đa ba màu, khung hình là trang giấy.
- `pen-plotter` — Máy vẽ bút: mọi dấu vết đều là nét bút thật, máy di chuyển đúng tốc độ với tăng/giảm tốc, đổi bút tại giá đỡ.
- `assembly-line-diagram` — Một dây chuyền sản xuất liên tục: mỗi trạm là một cỗ máy dễ đọc, màu là chú giải, hàng hóa đi qua từng bước theo thứ tự.

### 8. Cartoons — Hoạt hình (6) → `opuscar-cartoons`
- `rubber-hose` — Hoạt hình ống cao su thập niên 1930: tay chân ống đều không khuỷu, găng trắng bốn ngón, nền aquarelle xám, phim 35 mm cũ.
- `cel-anime-80s` — Anime cel thập niên 1980: nền sơn airbrush, nhân vật cel phẳng bước 12/8 fps, ánh sáng xuyên cel, phát lại như băng CRT.
- `scifi-toon` — Hoạt hình 2D truyền hình người lớn: viền dày sôi, màu phẳng, hài thoại với mục tiêu nhỏ xíu nhưng dùng phương tiện viễn tưởng khổng lồ.
- `midcentury-toon` — Hoạt hình phẳng thập niên 1950: màu in lệch khỏi nét, đường mực mỏng thở nhẹ, người hình học, phòng chỉ là một mặt màu.
- `comic-history` ✦ — Lịch sử kể bằng giấy: lãnh thổ đổi chủ bằng hành động cắt, xé, dán; quốc gia là rối giấy nối đinh tán trên bản đồ khắc cổ. Cần máy tạo ảnh.
- `manga-panels` ✦ — Trang manga in: chỉ mực và giấy, xám là chấm screentone, khung truyện là đơn vị thời gian, đọc phải sang trái. Cần máy tạo ảnh.

### 9. Games — Trò chơi điện tử (4) → `opuscar-games`
- `pixel-rpg` — RPG 16-bit: khung hình 320×180 phóng to bằng nearest-neighbour, bảng màu giới hạn, kể chuyện bằng hộp thoại, menu và file save.
- `hd-2d` — Mô hình 3D thu nhỏ bọc texture pixel, nhân vật sprite 2D phẳng nhận sáng và đổ bóng, nhìn qua dải tilt-shift như mô hình bàn.
- `microgame` — Chuỗi microgame 2,5–4 giây: mỗi game một chất liệu hình khác nhau, sân khấu cố định giữ nhịp, tốc độ tăng dần theo từng vòng.
- `game-show` — Gameshow theo nhịp: mọi hiệu ứng rơi đúng ô nhịp, mỗi vòng một màu nền bão hòa mới, nhân vật đồ chơi nhún theo beat.

### 10. Film & Tape — Phim nhựa & Băng ghi hình (5) → `opuscar-film-tape`
- `ascii-crt` — Một màn hình terminal đơn sắc: mọi hình ảnh đều là ký tự xếp theo lưới, phốt-pho hổ phách, camera duy nhất là chính màn hình.
- `silent-film` — Phim câm thập niên 1920 chiếu trong rạp: khung 4:3, tranh mực trên phim bạc rung xước, kể bằng hành động và thẻ chữ xen kẽ, nhạc piano.
- `backrooms` — Băng VHS thập niên 1990 quay tay một góc nhìn thứ nhất: không gian trống quen thuộc nhưng sai, sợ hãi đến từ sự lặp lại và máy quay hỏng.
- `scratch-film` — Phim khắc trực tiếp lên phim nhựa: nền đen, sáng là vết cào, màu là thuốc nhuộm trong suốt, nét vẽ sôi lại 15 lần mỗi giây.
- `double-exposure` — Chồng hình kép: bóng động vật chứa ảnh phong cảnh thật bên trong, ảnh trong bóng trôi chậm hơn đường viền tạo thị sai.

### 11. Screens & Interfaces — Màn hình & Giao diện (6) → `opuscar-screens-interfaces`
- `dark-keynote` — Keynote công nghệ nền tối: nhân vật chính là giao diện, mọi phần tử bám lưới, một màu thương hiệu duy nhất, kịch tính từ đối lập lộn xộn → quyết đoán → trống rỗng.
- `living-screencast` — Giả ghi màn hình sản phẩm thật nhưng vẽ lại toàn bộ bằng 2D: linh vật pixel vuông độ phân giải thấp sống trong thế giới UI sắc nét.
- `hologram-hud` — Mô hình dây khung ánh sáng trên bệ chiếu tròn: mặt quét dựng hình, chi tiết tách theo trục lắp ráp, số liệu được tính ngay trên màn hình.
- `desktop-flythrough` — Bàn làm việc là thế giới: giao diện là thẻ giấy dày, nhân vật sprite pixel đứng và nhảy trên thẻ, nắng thấp chiếu bóng dài.
- `spreadsheet` — Phim trong bảng tính: ô là điểm ảnh, hình được tính từ giá trị trong ô, khung phần mềm không bao giờ rời màn hình.
- `one-bit-dither` — Chỉ hai mực, không xám: tông màu là mật độ chấm, mẫu chấm bám theo bề mặt vật thể khi camera di chuyển.

### 12. Light & Lines — Ánh sáng & Đường nét (5) → `opuscar-light-lines`
- `circuit-board` — Mạch in nhìn từ trên xuống: đồng, đường mạch góc 0/45/90°, thông tin di chuyển như ánh sáng trên đồng, hai tỉ lệ trên cùng một bảng.
- `firefly-pointillism` — Mọi thứ đều là điểm sáng trên nền đen hơn một nửa khung hình: chiều sâu bằng kích thước và độ mờ, lấy nét là hình hiện ra.
- `flow-field` — Đường dòng của một trường thật: hàng nghìn đường mảnh không cắt nhau, nét khắc cộng vệt ngắn chạy dọc, giấy ấm mực xanh đen.
- `oscilloscope-math` — Toán học trên máy hiện sóng: đường cong là chuỗi Fourier thật, mọi con số kiểm chứng được, ánh sáng phát ra chứ không phải mực.
- `neon-tubes` — Ống neon là thủy tinh thật: cột khí màu thật theo loại khí, ống chưa sáng vẫn thấy rõ, ống đứng trên bảng sơn với dây buộc và điện cực.

### 13. 3D & Miniature — 3D & Mô hình thu nhỏ (8) → `opuscar-3d-miniature`
- `brick-toy` — Thế giới gạch nhựa trên mặt bàn thật, quay macro kiểu stop-motion: nhựa ABS bóng, núm trên mọi mặt, nhân vật xếp từ gạch.
- `paper-popup` — Sách pop-up trong căn phòng thật: trang mở dựng phông nền, mọi vật là thẻ giấy cắt bật lên quanh mép dưới, lệch tỉ lệ với thế giới thật.
- `tilt-shift` — Nơi chốn thật nhìn qua ống kính tilt-shift: chỉ một dải ngang sắc nét, màu nắng bão hòa, time-lapse khiến xe cộ như đồ chơi lên dây.
- `lowpoly-island` — Đảo low-poly nổi trong biển đa diện: camera trực giao đẳng cự, ánh sáng chứ không phải texture kể thời gian.
- `glass-product` — Vật thể thủy tinh hư cấu lơ lửng trong studio đen vô hạn: dải sáng dài biến kính trong thành viền trắng cầu vồng, chuyển động chậm chính xác.
- `memphis-diorama` — Mô hình phong cách Memphis: màu phẳng bão hòa, viền chàm, họa tiết chấm/sọc/zigzag, khung hình tròn hữu cơ tan vào hạt nhiễu.
- `isometric-picture-book` — Một địa điểm thật tràn khung hình: người gầy nhìn từ sau lưng, không mặt không tay, ai đi trước ai chờ chính là thông tin.
- `crayon-world` — Thế giới 3D thật nhưng chỉ thấy qua nét sáp màu: mỗi khung hình được vẽ lại bằng sáp trên giấy, 12 hình mỗi giây.

### 14. Instruments & Evidence — Dụng cụ & Bằng chứng (8) → `opuscar-instruments-evidence`
- `satellite-briefing` — Ảnh vệ tinh thật có tọa độ: lớp ảnh là thứ vệ tinh thấy, đường kẻ mảnh là thứ chuyên gia đo, zoom một mạch từ quỹ đạo xuống mặt đất.
- `briefing-board` — Bảng họp kỹ thuật trong phòng thật: ảnh cắt dán nổi khỏi bảng, mực than chì, xanh đo đạc, đỏ chỉ quyết định, camera đi dọc một bức tường liên tục.
- `lidar-survey` — Đám mây điểm LiDAR thật: điểm không bao giờ bị dời chỗ, mặt quét ngưng tụ điểm thành mô hình, phân loại lớp để bóc tách.
- `microscope` — Mẫu vật là ảnh hiển vi thật: một cú lặn logarit qua các lớp của cùng một mẫu, thước tỉ lệ nhảy theo dãy 1-2-5.
- `archive-lighttable` — Tư liệu lưu trữ thật trên bàn sáng: ánh sáng từ dưới lên, kính lúp là cửa vào chi tiết, mỗi vật mang mã số thật từ đơn vị lưu giữ.
- `security-xray` — Ảnh X-quang an ninh: mỗi pixel là độ dài đường tia qua vật chất, mã màu cam/xanh lá/xanh dương theo vật liệu, có người vận hành sau máy.
- `dark-documentary` — Phim tài liệu quét radar: không có ánh sáng môi trường, vật chỉ hiện khi mặt quét chạm tới, tiếng vọng ghi lại thời gian.
- `thermal-camera` — Camera nhiệt: mỗi pixel là nhiệt độ biểu kiến qua một bảng màu, độ phân giải cảm biến thô, vật lý dòng nhiệt quyết định thứ gì phát sáng.

### 15. Data & Maps — Dữ liệu & Bản đồ (6) → `opuscar-data-maps`
- `dataviz` — Biểu đồ là phim: mỗi dấu là một con số thật có thể truy nguồn, mỗi chuyển động là một thao tác biểu đồ có ý nghĩa.
- `white-model` — Mô hình trắng của một nơi thật: dữ liệu là ánh sáng chiếu lên, màu không bao giờ sơn vào vật liệu, từng lớp đến một kèm cử chỉ sáng riêng.
- `data-physical` — Dữ liệu vật chất hóa: một tấm/khối/đồng xu bằng một lượng đã nêu, tỉ lệ chính xác, dữ liệu tăng lên bằng cách đặt thêm mảnh.
- `transit-map` — Bản đồ tuyến in trên giấy: chỉ tám hướng, đường chỉ tồn tại tới đâu đầu bút đi tới đó, ga sáng khi bút đi qua.
- `map-explainer` — Bản đồ 3D từ dữ liệu địa hình thật: độ cao phóng đại, lớp dữ liệu phát sáng là thứ duy nhất sáng, tuyến đường vẽ thêm phải ghi rõ là sơ đồ.
- `pip-simulation` — Mô phỏng thật có hạt giống cố định: mỗi Pip là một cá thể có vị trí, năng lượng và con cháu; thay luật là đổi phim.

Tổng: 8 + 5 + 7 + 7 + 8 + 8 + 8 + 6 + 4 + 5 + 6 + 5 + 8 + 8 + 6 = **99 style**.

## Pipeline chung làm phim bằng code

Áp cho mọi style; skill nhóm giữ chi tiết riêng của từng style.

1. **Brief (một lần, hỏi gọn).** Chốt: style, đề tài, facts không được tự quyết (tên, logo, sản phẩm phải xuất hiện), tư liệu/dữ liệu/giọng/nhạc/font của user (nếu có), ngôn ngữ phim, có cần duyệt storyboard trước không, máy user còn thiếu gì (chạy script kiểm tra môi trường của repo trước khi hỏi). Với style ✦: hỏi user sẽ tạo ảnh bằng công cụ nào; không có máy tạo ảnh thì nói thẳng là phim chưa bắt đầu được và đề xuất 2–3 style khác. Không bao giờ vẽ nhân vật bằng code để thay cho ảnh tạo.
2. **Treatment trước, demo sau.** Viết `TREATMENT.md` trong thư mục dự án với ba cấu trúc ứng viên và lựa chọn của mình, **trước khi** mở `DEMO.md` hay code demo của style. Sau đó chỉ dùng demo để học kỹ thuật (engine cọ, rig, shader, mix), không bao giờ dùng lại truyện, arc, cảnh, đạo cụ hay timeline của demo. Ngoại lệ: style cắt từ tư liệu thật (Edit & Documentary, Instruments & Evidence) thì thu thập tư liệu trước treatment; vẫn chỉ đọc demo sau khi treatment đã viết xong. Không bao giờ làm việc trong `styles/` của repo: copy thứ cần vào thư mục dự án.
3. **Look.** Render frame mẫu/model sheet bằng code vẽ thật, đối chiếu với `STYLE.md` của style trước khi dựng tiếp.
4. **Storyboard — chỉ khi user yêu cầu.** Nếu có thì dừng lại chờ duyệt. Không yêu cầu thì không dừng.
5. **Sản xuất.** Giọng đọc → kiểm tra → nhạc (có thể chạy song song) → animation → mix → render.
6. **Tự kiểm và giao** (xem QA chung bên dưới).

## Page contract (bất biến cho mọi phim code)

Một trang HTML/Canvas duy nhất:

- `window.DUR` — tổng thời lượng (giây).
- `window.render(t)` — hàm thuần của `t`: cùng một `t` luôn cho cùng một khung hình. Cấm `Date.now()`, cấm `Math.random()` không seed; nhiễu "tay vẽ" phải suy từ hash xác định của đỉnh/vật.
- `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue.
- `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc.
- Render bằng cách seek `t` qua headless Chrome, từng khung hình; không quay màn hình trình duyệt đang chạy.

## Giọng + nhạc + mix + mux

- Giọng: thu giọng đọc theo kịch bản đã chốt; kiểm tra phát âm, tốc độ, độ dài trước khi dựng hình theo giọng. Phụ đề/chữ trên màn hình giữ tối thiểu theo luật đọc của style (mặc định: giữ ≥ max(1,8 s, thời gian nói + 0,6 s)).
- Nhạc: viết/cắt theo bảng beat, không loop nhạc nền dưới hình một cách tùy tiện; sự kiện hình đáp đúng nhịp nhạc (xem skill nhóm: có style nhạc đi trước và hình theo nhạc).
- Foley: mọi hành động có âm thanh của nó, lấy từ `window.EV`; cue âm và cue hình lệch ≤ 1 frame.
- Mix cuối: đo loudness trên file cuối, chuẩn **−14 LUFS ± 0,5** (một số style đo −16 LUFS trước mastering — xem skill nhóm). Mux: H.264 + AAC; frame rate theo style (mặc định 24 fps; một số style 30/60 fps — xem skill nhóm).

## QA chung (áp cho mọi phim, trước khi giao)

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief, thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm nét vẽ/đường/màu có tiến triển thật giữa các beat; chữ đọc được ở zoom nó xuất hiện; nhãn không che thứ nó mô tả; không có yếu tố nào của style bị vi phạm (xem mục Pitfalls trong skill nhóm).
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn thẻ, không tràn khung.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích (ghi rõ trong QA.md nếu có fade đen chủ đích).
- Bản quyền: ghi rõ nguồn tư liệu/dữ liệu/hình nền + licence trong QA.md và `CREDITS`; không dùng tên/logo/font hệ thống/giao diện của bất kỳ sản phẩm, hãng, đài hay đội bóng thật nào; không dùng lại truyện, nhân vật, lời thoại demo của repo gốc; không dùng 6 track lời thoại demo làm bằng TTS online; phim tự làm thuộc về người làm.

## Bảng tra cứu — 15 skill nhóm + skill đã có

| # | Chuyên đề | Skill nhóm | Style |
|---|---|---|---|
| 1 | Edit & Documentary | `opuscar-edit-documentary` | caption-news, newsreel, countdown, city-symphony, visual-investigation, kino-montage, news-package (+ `telestrator` → skill riêng `opuscar-telestrator` đã có) |
| 2 | Painting & Illustration | `opuscar-painting-illustration` | crayon-book, watercolor, impasto, urban-sketch, colored-pencil |
| 3 | Sketch & Board | `opuscar-sketch-board` | one-line, whiteboard, chalkboard, sketchnote, stick-explainer, ipad-sketch, marker-paper |
| 4 | Traditional Crafts | `opuscar-traditional-crafts` | ink-wash, shadow-puppet, ukiyoe, papercut-red, paper-lantern, stained-glass, gilded-illumination |
| 5 | Print & Printmaking | `opuscar-printmaking` | risograph, halftone-dossier, woodcut, engraving, silkscreen-poster, printed-long-take, pop-art, vintage-collage |
| 6 | Graphic & Type | `opuscar-graphic-type` | swiss-motion, spy-titles, art-deco, pictogram-motion, bauhaus-shapes, flat-space-explainer, text-flash-cuts ✦, silhouette-rhythm |
| 7 | Line Diagrams | `opuscar-line-diagrams` | blueprint, iso-infographic, teardown, hardcore-info, precise-mechanism, instruction-manual, pen-plotter, assembly-line-diagram |
| 8 | Cartoons | `opuscar-cartoons` | rubber-hose, cel-anime-80s, scifi-toon, midcentury-toon, comic-history ✦, manga-panels ✦ |
| 9 | Games | `opuscar-games` | pixel-rpg, hd-2d, microgame, game-show |
| 10 | Film & Tape | `opuscar-film-tape` | ascii-crt, silent-film, backrooms, scratch-film, double-exposure |
| 11 | Screens & Interfaces | `opuscar-screens-interfaces` | dark-keynote, living-screencast, hologram-hud, desktop-flythrough, spreadsheet, one-bit-dither |
| 12 | Light & Lines | `opuscar-light-lines` | circuit-board, firefly-pointillism, flow-field, oscilloscope-math, neon-tubes |
| 13 | 3D & Miniature | `opuscar-3d-miniature` | brick-toy, paper-popup, tilt-shift, lowpoly-island, glass-product, memphis-diorama, isometric-picture-book, crayon-world |
| 14 | Instruments & Evidence | `opuscar-instruments-evidence` | satellite-briefing, briefing-board, lidar-survey, microscope, archive-lighttable, security-xray, dark-documentary, thermal-camera |
| 15 | Data & Maps | `opuscar-data-maps` | dataviz, white-model, data-physical, transit-map, map-explainer, pip-simulation |

Lưu ý: các skill nhóm 1–10 đã có hoặc do nhóm khác phụ trách — router chỉ trỏ tới, không viết lại nội dung của chúng. Skill `opuscar-telestrator` đã có từ trước, giữ nguyên.
