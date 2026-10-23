---
name: opuscar-telestrator
description: Kỹ thuật phim phân tích thể thao kiểu telestrator truyền hình (spin-out từ bộ Lemo-Opuscar) — phát tình huống, tua lại, đóng băng khung hình rồi vẽ trực tiếp lên hình: vòng tròn dưới chân cầu thủ, mũi tên đường bóng, vùng đỏ không ai kèm, spotlight người giúp đỡ, kết bằng bảng sơ đồ phẳng. Dùng khi brief là "phân tích chiến thuật như trên TV", "vẽ lên video trận đấu", "breakdown một pha bóng", "giải thích pick & roll / pha dàn xếp bằng hình vẽ trên sân", hoặc làm phim dạy chiến thuật từ một tình huống đóng băng. Mọi nội dung (môn, tình huống, đội) do brief quyết định — skill chỉ giữ ngữ pháp hình ảnh và kỷ luật sản xuất.
---

# Opuscar Telestrator — Phân tích thể thao vẽ trên hình

Một đoạn phân tích như trong phòng bình luận truyền hình: xem tình huống chạy thật trước, rồi mới mổ xẻ. Đóng băng — vẽ — nói đúng một ý — cho chạy tiếp. Sức nặng của thể loại nằm ở chỗ nét vẽ bám đúng hình thật (vòng tròn nằm dưới chân, mũi tên đi theo đường bóng thật) và mỗi lần đóng băng chỉ kết luận một điều.

Nguồn kỹ thuật: style `telestrator` trong repo Lemo-Opuscar (MIT) tại `~/workspace/lemo-opuscar/styles/telestrator/STYLE.md` — đọc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện/logo/đài của phim mẫu.

## Khi nào dùng

- Phân tích một pha bóng cụ thể (bóng đá, bóng rổ, tennis, đua xe...) có camera rộng nhìn thấy toàn bộ tình huống.
- Phim dạy chiến thuật cho HLV/học viện: đọc tình huống, chỉ ra khoảng trống, người giúp đỡ, hai lựa chọn xử lý.
- Recap trận đấu dạng "vì sao pha này thành bàn/điểm" thay vì highlight chạy nhạc.
- Không dùng cho: highlight reel ăn mừng, infographic số liệu thuần (đó là việc của explainer-diagram), hay điều tra đa camera đồng bộ kiểu bằng chứng.

## Nguyên lý cốt lõi

1. **Xem trước, giải thích sau.** Mọi hành động đều được thấy đang chuyển động trước khi bị đóng băng. Không bao giờ mở đầu bằng sơ đồ hay kết luận.
2. **Một lần đóng băng, một phát hiện.** Mỗi freeze nói đúng một ý, một nhãn, tối đa hai nhóm nét vẽ. Cùng vài giây hình được dùng lại nhiều lượt, mỗi lượt sâu thêm một lớp.
3. **Vẽ trên hình thật, không vẽ cạnh hình.** Vòng tròn ôm chân cầu thủ, mũi tên bám đường bóng, đường biên sân được trace lại trên chính đường biên thật. Chỉ ở cuối phim, khi tóm tắt, hình mới được "làm phẳng" thành bảng sơ đồ — và phải làm phẳng *từ* hình thật, không cắt sang một trang sơ đồ rời.
4. **Số liệu chỉ đến từ hình.** Thời gian đếm bằng frame nguồn, khoảng cách đo từ vạch sân (homography theo mốc sân nhìn thấy). Hình không đo được (tốc độ bóng, quãng đường chạy) thì không viết con số lên phim.
5. **Năng lượng studio.** Nét vẽ sáng, flash trắng + cú "punch" ở mỗi lần đóng băng, nhạc dừng cùng lúc với hình. Đây là show bình luận, không phải phim tài liệu trầm.

## Hệ màu ba vai (bất biến)

| Vai | Màu | Dùng cho |
|---|---|---|
| Đội/người ta theo dõi, quả bóng, nét vẽ chính | `#FFD400` vàng huỳnh quang | vòng tròn, mũi tên, nhãn chính |
| Đối thủ | `#3FD8FF` cyan | vòng tròn đối thủ, mũi tên chặn, đường liên kết |
| Khoảng trống không ai chiếm | `#FF3B30` đỏ, fill 0.34–0.38 + viền đứt nét | mảng không gian trống |
| Nét trung tính, trace vạch sân, tem | `#F4F1E8` phấn trắng | đường sân vẽ lại, dấu đóng |
| Nền bảng tóm tắt | `#0C1411` xanh mực gần đen | trang bảng cuối phim |

Một màu = một danh tính, xuyên suốt phim. Nhãn của đối tượng nào thì thanh màu bên trái nhãn mang màu của đối tượng đó. Được đổi tông màu nếu show cần, không bao giờ đổi ba vai.

## Quy trình sản xuất

1. **Chốt tư liệu trước.** Hỏi user có footage của mình không (video CLB/học viện, bản quyền phát sóng đã có phép). Không có footage thật: dựng "hình nền" bằng code (sân + cầu thủ dạng đĩa số nhìn từ trên cao, góc broadcast) — vẫn giữ nguyên ngữ pháp vẽ-trên-hình, và ghi rõ trong QA là hình dựng, không giả làm footage thật. Fact (tỉ số, phút, diễn biến) phải có nguồn ghi lại; số không có nguồn thì bỏ.
2. **Treatment ngắn trước khi dựng:** chọn 1 tình huống chính để mổ sâu + tối đa 2 tình huống phụ xử lý nhẹ; mỗi tình huống: phát hiện duy nhất là gì, cần mấy freeze, freeze nào là đỉnh. Một phim 20–60s thường có 2–4 freeze cho tình huống chính.
3. **Timeline là nguồn sự thật duy nhất:** một bảng beat (mốc giây → sự kiện hình → sự kiện âm) mà hình, phụ đề, nhạc, mix đều đọc từ đó. Nhịp hình và cue âm lệch nhau là lỗi, không phải "cảm tính".
4. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi annotation là hàm của `t`, nét vẽ xuất hiện theo tiến độ (progress) trong cửa sổ beat của nó.
5. **Đo trước khi vẽ:** tọa độ điểm bám (chân cầu thủ, điểm đặt màn chắn, rổ...) đọc trên frame gốc độ phân giải đầy đủ — sai tọa độ bám là rủi ro lớn nhất của thể loại này. Có chế độ debug vẽ mọi điểm bám để soát.
6. **Render thử các frame hero của từng beat** → contact sheet soát thứ tự lập luận và độ bám của nét vẽ trước khi render full.
7. **Âm thanh theo bảng âm của style** (xem Công thức), mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng (thứ tự trong một tình huống)

Phát trực tiếp 1× (có tiếng trận) → tua lại 0,6s (hình chạy ngược, vệt tracking, ký hiệu ◀◀) → **freeze ①** → phát chậm 0,6–0,85× → **freeze ②** → phát chậm kèm đồng hồ đếm frame → **freeze ③** → đường bóng vẽ đuôi sao băng → góc quay khác (replay), có thể thêm một freeze.

- Biến thể nhẹ cho tình huống phụ: *freeze-in-play* (không tua lại — chạy 1× tới pha quyết định rồi đóng băng, vẽ, chạy tiếp tới kết quả) và *freeze hai góc* (hai cửa sổ split-screen cùng tới một khoảnh khắc và đóng băng đồng thời, cùng một cầu thủ được khoanh ở cả hai góc).
- Freeze dài 1,8–2,4s; quá ~2,5s phải có hành động thứ hai bên trong freeze. Quá 4 freeze cho một tình huống thì chèn replay ở giữa.
- Chuyển đoạn chỉ bằng wipe đóng gói của show (băng chéo màu accent quét qua khung 0,34s). Trong đoạn: cắt cứng. Không dissolve, không lật trang.
- Khung so sánh cuối (bản đồ pha bóng, thẻ số liệu) phải được vẽ xong sớm và giữ ≥ 2,5s trước khi cắt.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; nhiễu "tay vẽ" phải suy từ hash xác định của đỉnh), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Vào freeze:** flash trắng 0,1s (alpha 0,55) + scale punch 1,035 → 1,0 trong 0,35s ease-out + khử bão hòa ~42% + phủ tông lạnh + vignette nặng hơn; sau đó hình "trôi" rất chậm (creep ~1,2%). Mọi overlay phải chịu cùng transform với hình, nếu không nét vẽ trượt khỏi cầu thủ.
- **Spotlight:** vùng ngoài ellipse trọng tâm tối xuống hệ số 0,42 (khoét lỗ even-odd), fade 0,3s.
- **Nét bút dạ (marker line):** lõi màu vai + viền tối (rộng hơn lõi 6px, đen 0,55) + glow ~18px + một vệt highlight trắng mỏng (0,28× bề rộng lõi); vẽ dọc theo chiều dài theo progress; đầu mũi tên bật vào trong 10% cuối; rung nhẹ xác định ở các đỉnh cho cảm giác vẽ tay. Nét liền = đã xảy ra; nét đứt = ý định/tương lai (đường chạy, đường chuyền sắp tới).
- **Vòng tròn cầu thủ:** ellipse phối cảnh (ry = 0,36r) nằm dưới chân, vẽ theo chiều kim đồng hồ; thêm vòng đứt nét ngoài quay 60px/s; khi cầu thủ di chuyển, điểm bám nội suy tuyến tính giữa các keyframe tọa độ chân cách nhau ~3–6 frame nguồn.
- **Thứ tự vẽ trong một freeze:** vòng tròn (ai) → mảng/đường liên kết (chuyện gì xảy ra) → nhãn (kết luận một dòng), cách nhau 0,3–0,6s.
- **Đường bóng:** chỉ giữ ~0,6s đuôi gần nhất trong không gian màn hình (bóng ~0,24s) — camera pan thì đuôi dài sẽ đáp sai chỗ.
- **Đồng hồ đếm frame:** bắt đầu ở frame nhận bóng, đếm frame nguồn ÷ fps, dừng và chuyển vàng ở khoảnh khắc dứt điểm.
- **Làm phẳng phối cảnh (native move):** đánh dấu 6–8 điểm sân đã biết kích thước thật trong frame dứt điểm, fit homography mặt đất (sai số dư ≤ 6px là đạt); dựng lưới tam giác trên mặt sân (ô ~1,5m), mỗi đỉnh đi từ vị trí ảnh về vị trí bảng, hình mờ dần khi bảng phấn hiện lên; các pha khác (mỗi pha một ma trận riêng) thả điểm chân lên cùng bảng.
- **Đóng gói show (packaging):** bug góc (tên show + trạng thái TRỰC TIẾP/ PHÂN TÍCH/ XEM LẠI bằng màu vai) và thanh tỉ số hiện từ frame 1, đặt đè đúng vị trí logo/URL của đài gốc nếu có; wipe chéo màu accent là chữ ký chuyển đoạn. Tên show, màu, logo là hư cấu của phim — không dùng nhận diện của bất kỳ đài/kênh thật nào.
- **Chữ:** in đậm trên thẻ đen (nền `rgba(8,12,14,0.9)`, thanh màu vai ở mép trái), không font viết tay. Số đóng gói (tỉ số, đồng hồ, số liệu lớn) dùng font condensed/italic hoặc mono. Chữ bắt buộc đọc giữ ≥ 2,5s; nhãn freeze đi cùng phụ đề thì giữ ~1s là đủ vì phụ đề mang nội dung.
- **Âm thanh:** 3 lớp — tiếng trận + nhạc nền + foley. Foley bắt buộc khớp hình: tiếng rít bút dạ cho mỗi nét vẽ, tiếng "pop" khi vòng tròn khép, tick khi nhãn đáp xuống, whoosh ở wipe, tiếng máy tua khi rewind, tick đồng hồ mỗi 0,2s, thump khi đóng tem. Khi freeze, nhạc nền dừng cùng hình: một stab ngắn + thump trầm, sau đó chỉ còn lớp nền mỏng. Voice (nếu có) đè các lớp khác xuống ~0,55. Mix cuối chuẩn −14 LUFS.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1280×720 hoặc 1920×1080, 30fps), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) nét vẽ tiến triển thật giữa các beat — so frame giữa-cửa-sổ-vẽ và frame cuối-cửa-sổ của cùng một nét; (b) vòng tròn/nét vẽ bám đúng vị trí cầu thủ ở mọi frame; (c) spotlight và nhãn không che hành động chúng mô tả.
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn thẻ, nhãn nằm trên vùng trống (cỏ/khán đài/vùng tối), không nằm đè cầu thủ.
- Đồng bộ cue: mọi mốc trong `window.EV` (flash freeze, nét vẽ, nhãn) có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích (fade cuối nếu có phải ghi trong QA).
- Đếm freeze và phát hiện: số freeze khớp treatment, mỗi freeze đúng một phát hiện — freeze nào nói hai ý là lỗi phải tách.
- Bản quyền: ghi rõ nguồn footage/hình nền trong QA.md; footage không rõ licence thì không dùng. Không gắn tên/logo đội bóng, cầu thủ, đài truyền hình thật vào phim dựng bằng code.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: nguồn tư liệu + licence, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.
