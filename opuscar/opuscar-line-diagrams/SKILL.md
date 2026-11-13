---
name: opuscar-line-diagrams
description: Kỹ thuật phim sơ đồ nét giải thích máy móc & hệ thống (spin-out từ bộ Lemo-Opuscar) — 8 style: bản vẽ xanh blueprint, infographic đẳng cự, bóc tách sản phẩm, mặt cắt nét mực, cơ chế tô màu theo hệ, tranh sách hướng dẫn, máy vẽ bút plotter, dây chuyền sản xuất. Dùng khi brief là "tháo ra xem bên trong", "máy này chạy thế nào", "quy trình gồm mấy bước", "vẽ đúng kích thước thật". Mọi nội dung do brief quyết định — skill chỉ giữ ngữ pháp sơ đồ và kỷ luật sản xuất.
---

# Opuscar Line Diagrams — Sơ đồ nét giải thích máy & hệ thống

Nét mực là ngôn ngữ duy nhất. Không phối cảnh trang trí, không vật liệu bóng bẩy che số liệu: hình vẽ ra để đo được, đếm được, kiểm chứng được. Một phim thuộc nhóm này thuyết phục bằng độ chính xác — bánh răng quay đúng tỉ số răng, kích thước lấy từ file kỹ thuật, màu chỉ mang một nghĩa duy nhất trong cả phim.

Nguồn kỹ thuật: 8 style trong repo Lemo-Opuscar tại `~/workspace/lemo-opuscar/styles/{blueprint,iso-infographic,teardown,hardcore-info,precise-mechanism,instruction-manual,pen-plotter,assembly-line-diagram}/STYLE.md` — đọc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện/nhân vật/nhãn hiệu của phim mẫu.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Giấy phép: code MIT, tài liệu gốc CC BY-NC 4.0 (hệ REUSE của repo); phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

## Khi nào dùng

- Bóc tách một sản phẩm thật: từng lớp nổi lên trên một trục, nhãn chỉ đúng bộ phận, số đo ghi kèm.
- Giải thích một cơ chế: bánh răng, van, đồng hồ — chuyển động nào cũng tính từ mô hình thật.
- Quy trình nhiều bước: dây chuyền, lắp ráp, hướng dẫn sử dụng — mỗi bước một trạm, một việc.
- Mặt cắt/cắt lớp: thứ bên trong chỉ thấy khi cắt vỏ, vạch mặt cắt, tô mặt cắt.
- Vẽ dữ liệu địa hình/kỹ thuật bằng máy vẽ: đường đồng mức mọc dần, nét bút là bằng chứng.
- Không dùng cho: kể chuyện cảm xúc bằng nhân vật (opuscar-cartoons), đồ họa chữ/poster (opuscar-graphic-type), phim tư liệu từ footage thật (nhóm Edit & Documentary).

## Khi nào KHÔNG dùng

- Không có số liệu/file kỹ thuật thật mà vẫn muốn ghi số lên phim: nhóm này cấm bịa số. Không đo được thì bỏ số, hoặc ghi rõ "đo từ mẫu".
- Muốn phối cảnh điện ảnh, chiều sâu, ánh sáng kịch tính: nhóm này dùng chiếu trực giao/đẳng cự, cấm phối cảnh biến dạng.
- Chủ đề không có cấu trúc/bộ phận/quy trình để mổ xẻ: sơ đồ nét cần một vật hoặc một hệ để vẽ; ý tưởng trừu tượng thuần thì hợp nhóm Graphic & Type hơn.
- Không có style nào trong nhóm cần máy tạo ảnh — toàn bộ 8 style vẽ bằng code. Nếu brief đòi nhân vật vẽ tay chi tiết thì đó không phải nhóm này.

## Nguyên lý cốt lõi

1. **Số liệu chỉ đến từ mô hình.** Kích thước, số răng, số lượng, tỉ lệ — lấy từ file kỹ thuật (STEP, KiCad, BOM, hướng dẫn lắp ráp) hoặc đo trực tiếp và ghi rõ đã đo. Số không có nguồn thì không lên phim.
2. **Nét có thứ bậc.** Nét viền ngoài dày nhất, nét che khuất vừa, nếp gấp/chi tiết nhỏ mỏng nhất và xám hơn. Nét đều nhau mọi chỗ là lỗi — trông như bản xem trước lưới, không phải bản vẽ.
3. **Một màu, một nghĩa.** Màu nhấn hoặc màu hệ chỉ mang một ý nghĩa duy nhất trong cả phim (một đường đi, một hệ thống, một loại vật liệu). Màu trang trí loang ra ngoài nghĩa đó là lỗi.
4. **Vẽ theo thứ tự người làm thật.** Đường tâm → viền → chi tiết → tô mặt cắt → kích thước → nhãn. Thứ tự vẽ là thứ tự hiểu.
5. **Chuyển động là đo lường.** Bánh răng quay đúng tỉ số răng, dây chuyền chạy tốc độ không đổi, chi tiết tách ra theo trục — chuyển động nào cũng là một phát biểu kỹ thuật, không phải hiệu ứng.

## Bảng 8 style — bất biến từng style

| Style (slug) | Nhận diện nhanh | Màu bất biến | Chữ | Nhịp/chuyển động |
|---|---|---|---|---|
| `blueprint` — bản vẽ xanh | Toàn phim trên một tờ giấy xanh Prussian đặt trên bàn vẽ tối; nét trắng, chiếu trực giao, quy ước kỹ thuật khô và chính xác | Chỉ xanh + trắng: xanh `#18336B`→`#2A58A6`, nét `#E7F0F9`, bàn `#0D1116`; một màu con dấu duy nhất (đỏ cổ điển) mang "phán quyết", dùng đúng một lần | Chữ viết tay cho tiêu đề/nhãn/ghi chú (Architects Daughter…), sans kỹ thuật cho ô title-block (B612…), script chỉ cho chữ ký; phụ đề là ghi chú vẽ, có ô "NOTE / n" | Camera và vẽ-trên-giấy ở 24fps (ones); vẽ theo thứ tự lớp, mỗi lớp bắt đầu đúng nhịp; chi tiết tách ra theo trục, cắt cứng theo nhịp giữa các phần |
| `iso-infographic` — infographic đẳng cự | Phẳng, đẳng cự thật, không phối cảnh; mặt khối phân biệt chỉ bằng 3 tông; số dựng bằng biểu tượng giống hệt nhau và cộng được | Nền nhạt (kem/xám giấy/xanh nhạt) + 5–7 màu phẳng, mỗi màu 3 tông; một màu mực; một màu = một vật liệu/vai, không tái dùng | Một sans hình học (Jost): tiêu đề caps 600 tracking ~0.12em, số lớn ~44px, đơn vị cỡ một nửa; chữ có quầng ~7px màu nền; nhãn ghim: chấm → đường dẫn dọc → thước ngang → chữ | Mọi chuyển động đều có đường dẫn trước: đường tuyến vẽ trước, đường cắt vẽ trước rồi vỏ mới trượt ra; mặt cắt: cắt ~0.3s → vỏ trượt ~0.35s → viền mặt cắt mờ dần vào |
| `teardown` — bóc tách sản phẩm | Vật thật, chính xác, chụp bằng vật liệu PBR: đèn chính studio, viền lạnh, bóng tiếp xúc mềm; các lớp nổi trên một trục, khoảng cách đều, vẫn giữ hướng lắp | Khung trung tính tối; vật là thứ sáng và bão hòa nhất; chữ trắng ấm 2 độ (tên đủ, spec ~60%); một màu nhấn duy nhất cho thứ đo được (đường kích thước, số thứ tự nhãn); ví dụ nhấn `#ff6b3d`, nền `#0d0e10`, giấy `#f1efe9` | Tên: sans sạch medium 28–32px; spec/số: mono 15–22px (JetBrains Mono…) để chữ số thẳng hàng; nhãn cố định: số thứ tự 2 chữ số màu nhấn + tên + một dòng spec, luôn ghi đơn vị (mm, MB, ×n) | 24fps ones, trơn và xác định; tách lớp: bắt đầu mượt, giữa nhanh, kết thúc dài (ease-in-out cubed), lớp trên đi trước, cách nhau 0.15–0.2s; chi tiết lặp tỏa sóng theo khoảng cách từ một góc |
| `hardcore-info` — mặt cắt nét mực | Mọi thứ là nét trên giấy trắng ấm có lưới mờ; nét có 3 bậc độ dày; một màu nhấn duy nhất đánh dấu đường đi của câu chuyện | Giấy `#F6F5F0`, lưới ~4% mực; mực gần đen `#141414`, chì `#4A4A49`; một màu nhấn `#FF4D1A` chỉ cho đường đi được giải thích (dây, mạch, điểm đến, nhãn chỉ nó) | Sans kỹ thuật cho tên/tiêu đề (IBM Plex Sans SemiBold, tên caps tracking +1.4px) + mono cùng họ cho spec/đơn vị/chú thích; tiêu đề 54–64px với một từ màu nhấn; tên chi tiết 21px, spec 15px mono, chú thích 12px | 24fps ones, xác định, không sôi; tách lớp từng lớp đúng nhịp, settle overshoot ~2.5%; đường dẫn màu nhấn chạy tốc độ đều, đầu sáng hơn, rồi tràn vào chi tiết đích |
| `precise-mechanism` — cơ chế tô màu theo hệ | Màu là cấu trúc: mỗi chi tiết mang màu của hệ nó thuộc về; cel mềm 2 tông, viền là tông đậm của chính màu đó, không viền đen | Nền trắng ấm `#F3F0EA`; chi tiết không bàn tới: trung tính nhạt `#DDD8CF`; 3 màu hệ: vàng ấm = nguồn năng lượng `#E6B94F`, xanh xám = truyền động `#79B09F`, tím xám = điều khiển/đo `#8A97D4`; cảnh báo `#E8472A` | Grotesk trung tính cho tiêu đề/nhãn (Inter 600–650, tracking chặt); mono caps tracking rộng cho dòng hình, số đo, đơn vị (IBM Plex Mono); tối đa 3 cấp chữ | 24fps ones, camera mượt; một đồng hồ chủ đạo: đường cong tốc độ mượt (thời gian thật, tua chậm, dừng), tích phân của nó điều khiển mọi thứ; góc quay bánh răng tính từ số răng của bánh dẫn, khớp răng luôn khớp |
| `instruction-manual` — tranh sách hướng dẫn | Một góc đẳng cự duy nhất cả phim (azimuth 45°, cao 35.264°, 3 trục gặp nhau 120°, cạnh ngang 30°, cạnh đứng giữ đứng); khung hình là một trang giấy nhìn thẳng | Giấy `#F4F1EA`, mực `#1E1D1B`; chi tiết đã lắp: trắng/xám 3 tông `#FFFFFF`/`#ECE8DF`/`#DCD7CC`; chi tiết mới của bước này: vàng 3 tông `#F7D35A`/`#F2C230`/`#DEAA1F`, lắp xong nhạt dần thành trắng; tối đa 3 màu phẳng | Trên trang chỉ có số bước (sans hình học 700, ~150px, góc trên trái từng khu vực) và số lượng trong hộp linh kiện ("4×"); phụ đề dưới trái, 2 dòng; không chữ giải thích trên hình — hình và giọng nói làm việc đó | Chi tiết bay dọc đường chấm thẳng, ease-in, dừng với settle nhỏ, một nhịp tĩnh sau mỗi lần đáp; mũi tên vẽ trước, chi tiết đi theo sau đúng một lần rồi giữ; góc nhìn không bao giờ đổi |
| `pen-plotter` — máy vẽ bút | Mọi dấu vết đều là nét bút thật: không tô, không gradient, không chữ dựng bằng font; tông bằng gạch chéo; máy (khung, xe, giá bút) là vật thể có trọng lượng trong khung hình | Giấy kem `#F1ECDF` dưới đèn ấm; phòng tối gần đen; một mực cho khung/chữ, một mực cho địa hình/dữ liệu, một mực nhạt cho tông/lưới, một màu nhấn cho phát hiện (`#CC221A`…), nhấn xuất hiện muộn và có chủ đích | Chữ là nét đơn: sans một nét cho số/chữ Latin (2.5–10mm trên giấy, số hero 40–50mm), chữ CJK nét mảnh 3–5mm, serif gạch chéo cho tiêu đề tờ; chữ được nướng thành dữ liệu nét, trang không tải font | 30fps, không bước nhảy; bút tăng/giảm tốc thật, không dịch chuyển tức thời trong shot; time-lapse bằng jump-cut: trong đoạn bút chạy tốc độ thật, giữa các đoạn thời gian máy nhảy tới, đúng nhịp, camera vẫn trôi |
| `assembly-line-diagram` — dây chuyền | Một dây chuyền liên tục, hàng đi qua từng trạm theo thứ tự; mỗi trạm là một cỗ máy đọc được ngay (ép, sàng, cân, cần cẩu); biển ghi 2 tên: tên máy + tên thật | Giấy + mực + một nền tối + 4 màu spot làm chú giải, mỗi màu một nghĩa suốt phim (ví dụ: đất son = giấy, đỏ son = nhựa, teal = thủy tinh `#2E8D87`); nền `#1D2030`, giấy `#FBF7EE`, vàng `#F3B23A`, đỏ `#E04A2F` | 3 họ: display công nghiệp condensed cho biển/chú giải/tiêu đề (Big Shoulders Display 800–900); grotesk cho nhãn nhỏ/phụ đề (Archivo 600–800); sans CJK cho một dòng ngắn trên mỗi biển (Noto Sans SC 700, ≥34px); ~7 mảnh chữ mỗi khung, không hơn | Băng tải không dừng, hàng chạy tốc độ không đổi; trạm khởi động đúng nhịp hàng đáp (con lăn quay, vòi phun, máy ép dập), công nhân làm động tác 2 khung, vòng số đầy và nảy (scale 0.9→1 overshoot); biển thả bằng xích, nảy một lần |

## Quy trình sản xuất

1. **Thu thập file kỹ thuật trước khi viết treatment.** STEP/KiCad/BOM/hướng dẫn lắp ráp, hoặc đo trực tiếp và ghi vào file facts. Không có nguồn số thì treatment không được ghi số.
2. **Treatment ngắn:** chọn 1 vật/hệ chính + tối đa 2 phụ; mỗi cái: câu hỏi duy nhất cần trả lời, mấy lần tách/cắt, lần nào là đỉnh. Một phim 20–60s thường có 2–4 lần tách cho vật chính.
3. **Bảng beat là nguồn sự thật duy nhất:** một bảng mốc giây → sự kiện hình → sự kiện âm mà hình, chữ, nhạc, mix đều đọc từ đó.
4. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi nhãn/đường dẫn là hàm của `t`, chi tiết tách ra theo tiến độ trong cửa sổ beat của nó.
5. **Kiểm tra số trước khi vẽ:** tỉ số răng, kích thước, số lượng — đối chiếu lại với file gốc; sai số là rủi ro lớn nhất của nhóm này. Có chế độ debug hiện mọi điểm neo/số đo để soát.
6. **Render thử các frame hero của từng beat** → contact sheet soát thứ tự lập luận và độ bám của nhãn/đường dẫn trước khi render full.
7. **Âm thanh theo bảng âm của style**, mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng

- **Blueprint:** đường tâm → viền → chi tiết → tô mặt cắt → kích thước → bóng số → nhãn; chi tiết tách ra dọc trục, "FIG. 1" gạch đi viết lại "FIG. 2 · EXPLODE"; con dấu phán quyết đóng đúng một lần ở cuối.
- **Iso-infographic:** đường tuyến vẽ trước rồi vật mới đi theo → mặt cắt (vạch cắt, vỏ trượt, viền gạch chéo) → số dựng bằng biểu tượng (mỗi biểu tượng nảy lên đúng một nhịp con, số đếm chạy cùng lúc) → focus + context (mọi thứ xám lại, chỉ chủ thể giữ màu).
- **Teardown:** sóng nâng (chi tiết lặp dâng theo sóng) → chui vào khe giữa hai lớp đã nâng để thấy mặt khuất → nhãn macro đáp xuống đúng chi tiết → đóng lại từ dưới lên, lớp cuối đáp kèm phản hồi cơ khí thật (phím đi hết hành trình rồi trở lại).
- **Hardcore-info:** mặt cắt quét (mặt phẳng cắt chạy dọc vật, mặt cắt tô gạch chéo) → tách lớp đúng nhịp, đường dẫn đứt nét mọc theo khi nâng → đường một màu: xung từ nguồn, màu nhấn chạy dọc đường, tràn vào chi tiết đích.
- **Precise-mechanism:** nhuộm màu theo hệ theo chiều dòng năng lượng → mặt cắt hình quạt/tấm cắt vỏ, mặt cắt tô gạch trong không gian thế giới → tách theo hệ, rút một lớp ra cho thấy nó đã làm gì.
- **Instruction-manual:** mở hộp, chi tiết bay dọc đường chấm tới bảng liệt kê có đếm → đường nét mọc dần (sàn → vật → người → mũi tên → kính lúp) rồi mới tô màu phẳng → lắp ráp theo mũi tên, chi tiết mới màu vàng nhạt dần thành trắng khi đã lắp.
- **Pen-plotter:** đường đồng mức mọc từ ngoài vào, mỗi mức nhảy một nhịp → tờ giấy dựng đứng, đường đã vẽ nâng lên thành giá trị thật (cao/thời gian/số lượng) rồi hạ về; bút đổi màu tại giá đỡ khi tới lượt nhấn.
- **Assembly-line:** hàng đáp → trạm khởi động → công nhân hành động → vòng số đầy → biển thả xuống; tách màu: một khối vào sàn phân loại, ra thành 3 dòng màu khác nhau vào 3 ống riêng, thẻ chú giải thả xuống từng dòng.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; nhiễu phải suy từ hash xác định), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Chiếu đẳng cự (instruction-manual, iso-infographic):** azimuth 45°, cao 35.264° (arctan 1/√2); 3 trục gặp nhau 120°, cạnh ngang 30°, cạnh đứng giữ đứng, không nhỏ dần theo khoảng cách. Không xoay/ nghiêng phối cảnh trong cả phim.
- **Thứ bậc nét (hardcore-info, blueprint):** viền ngoài dày nhất, nét che khuất vừa, nếp gấp/chi tiết nhỏ mỏng nhất và xám hơn; có thêm bậc thứ tư nhạt hơn cho tay và dụng cụ. Nét đều nhau là lỗi.
- **Tỉ số răng (precise-mechanism, teardown):** góc quay mọi bánh răng tính từ bánh dẫn qua số răng; khớp răng luôn khớp; chạy tự do phải kết thúc ở số nguyên răng; răng mịn: bước răng ≥ 12px, render 2×, không quay nhanh (≤ 45°/frame với chi tiết đối xứng 4 cánh — chậm thời gian lại thay vì quay nhanh).
- **Nhãn:** cấu trúc cố định (số thứ tự màu nhấn + tên + một dòng spec + đơn vị); đường dẫn (leader) đáp xuống đúng chi tiết, không chỉ gần đúng; nhãn không che chi tiết nó mô tả; nhãn ghim iso: chấm → đường dẫn dọc → thước ngang → chữ, chọn hướng theo trạm để không che chủ thể.
- **Chữ:** chữ bắt buộc đọc giữ ≥ 2,5s (teardown: nhãn giữ ≥ 2,5s trước khi cắt); phụ đề blueprint là ghi chú vẽ trong hộp mờ có 2 vạch trắng; số đo luôn kèm đơn vị.
- **Âm thanh:** tiếng máy thật theo vật liệu (bút sột soạt, giấy, kim loại, cơ khí), tiếng "click" khi lớp đáp, tiếng bút khi đường dẫn mọc; nhạc nền mỏng, dừng khi cần nghe tiếng máy; voice (nếu có) đè các lớp khác xuống ~0,55. Mix cuối chuẩn −14 LUFS.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1280×720 hoặc 1920×1080, 30fps — riêng pen-plotter 30fps, còn lại 24fps), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) số liệu trên hình khớp file facts (kích thước, số răng, số lượng); (b) nét có thứ bậc, không đều nhau; (c) màu chỉ mang một nghĩa, không loang; (d) nhãn/đường dẫn bám đúng chi tiết ở mọi frame.
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn thẻ, nhãn nằm trên vùng trống, không đè chi tiết.
- Đồng bộ cue: mọi mốc trong `window.EV` (tách lớp, đáp, nhãn) có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Riêng instruction-manual: mọi hình của vật (từng bước, bảng liệt kê, trang cuối) vẽ từ cùng một hàm với bảng trạng thái — đếm lại số lượng linh kiện ở bảng liệt kê khớp với từng bước.
- Riêng teardown/hardcore-info/precise-mechanism: số nào không có nguồn trong file facts thì phải gỡ khỏi phim trước khi giao.
- Bản quyền: ghi rõ nguồn file kỹ thuật/hình nền trong QA.md; file không rõ licence thì không dùng; không gắn tên/logo/nhãn hiệu thật vào phim dựng bằng code.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: nguồn tư liệu + licence, file facts (nguồn từng con số), bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian, file facts.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.
