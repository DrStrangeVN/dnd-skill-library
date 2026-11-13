---
name: opuscar-traditional-crafts
description: Kỹ thuật phim thủ công truyền thống (spin-out từ bộ Lemo-Opuscar) — thủy mặc, rối bóng, tranh khắc gỗ Nhật, giấy cắt đỏ, đèn lồng giấy, kính màu, sách minh họa mạ vàng. Dùng khi brief là "kể chuyện bằng thủy mặc", "rối bóng kể chuyện dân gian", "tranh khắc gỗ Nhật", "giấy cắt đỏ", "đèn lồng", "kính màu nhà thờ", hoặc "sách cổ minh họa mạ vàng". Mọi nội dung (chủ đề, câu chuyện, bảng màu) do brief quyết định — skill chỉ giữ vật lý chất liệu và kỷ luật dựng.
---

# Opuscar Traditional Crafts — Thủ công truyền thống

Mỗi style trong nhóm là một nghề thủ công được dựng lại thành máy làm phim: mực và giấy gạo, da rối bóng và đèn dầu, bản khắc gỗ và giấy washi, giấy cắt và đèn lồng, kính màu và chì, vàng lá và da thuộc. Điểm chung: **vật liệu thủ công là luật** — chuyển động cứng theo mảnh/lớp (rối bóng khớp nối, mảnh giấy cắt, bản in khắc), ánh sáng là một phần của chất liệu (đèn dầu, nắng qua kính màu, vàng lá bắt sáng), và khoảng trống là một phần của bố cục.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Code gốc MIT, tài liệu gốc CC BY-NC 4.0; phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

Nguồn kỹ thuật: các style `ink-wash`, `shadow-puppet`, `ukiyoe`, `papercut-red`, `paper-lantern`, `stained-glass`, `gilded-illumination` trong repo Lemo-Opuscar — đọc `STYLE.md` gốc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện, tên phim demo, nhân vật hay nhãn hiệu thật trong demo của repo.

## Khi nào dùng

- Kể chuyện bằng **thủy mặc** trên giấy gạo: mực 5 sắc, khoảng trống lớn, nhạc guqin dẫn (ink-wash).
- Kể chuyện dân gian bằng **rối bóng**: da cắt, đèn dầu, chiêng trống (shadow-puppet).
- Kể chuyện bằng **tranh khắc gỗ Nhật**: bản màu lệch đăng ký, bokashi, xanh Prussian (ukiyoe).
- Kể chuyện bằng **giấy cắt đỏ**: cắt yin/yang, rosette gấp 8, vàng lá một khoảnh khắc (papercut-red).
- Kể chuyện bằng **đèn lồng giấy**: ánh sáng ấm hổ phách, flicker, đèn bật theo stagger (paper-lantern).
- Kể chuyện bằng **kính màu**: backlight, chì gần đen, màu mặt trời = đồng hồ (stained-glass).
- Kể chuyện bằng **sách minh họa mạ vàng**: ultramarine, vàng lá, vellum, đêm xanh không đen (gilded-illumination).

## Khi nào KHÔNG dùng

- Không dùng nhóm này cho phim hội họa phương Tây/hiện đại (sáp, màu nước, sơn dầu — đó là `opuscar-painting-illustration`), cho phim giải thích bằng bảng trắng/marker (`opuscar-sketch-board`), hay cho phim tư liệu thật (`opuscar-edit-documentary`).
- Không dùng nhóm này cho phim cần chuyển động mượt kiểu 3D/photoreal: chuyển động trong nhóm này cứng theo mảnh/lớp (rối bóng khớp nối, mảnh giấy cắt, bản khắc) — làm "mượt" chúng là giết style.
- Không dùng ink-wash cho chuyện cần màu rực (đó là papercut-red hoặc stained-glass); không dùng shadow-puppet cho chuyện cần chi tiết tinh tế (đó là ukiyoe hoặc gilded-illumination); không dùng paper-lantern cho chuyện cần kể nhanh (đó là papercut-red).
- Không dùng nhóm này khi brief cần hình ảnh sắc nét kiểu vector: nét khắc, răng giấy, hạt mực là một phần của style.

## Nguyên lý cốt lõi

1. **Vật liệu thủ công là luật.** Mỗi style có một quy trình thủ công riêng (mực trên giấy gạo, da rối bóng trước đèn dầu, bản khắc gỗ in lên washi, giấy cắt gấp, đèn lồng giấy, kính màu chì, vàng lá trên vellum). Giữ đúng quy trình đó, đừng thay bằng filter.
2. **Khoảng trống là bố cục.** Giấy trống, nền tối, khoảng đen — đều là một phần của hình, không phải chỗ chưa vẽ xong. 60–80% giấy trống trong thủy mặc là luật, không phải thiếu sót.
3. **Ánh sáng là một phần của chất liệu.** Đèn dầu nhấp nháy, nắng qua kính màu đổi màu theo giờ, vàng lá chỉ bắt sáng khi có ánh sáng chiếu — ánh sáng không phải hiệu ứng phủ ngoài, nó là cách chất liệu hiện ra.
4. **Chuyển động cứng theo mảnh/lớp.** Rối bóng khớp nối, mảnh giấy cắt, bản khắc — mỗi mảnh di chuyển như một vật thật (khớp, gấp, trượt), không biến dạng mềm như 3D.
5. **Màu ít, ý nghĩa nhiều.** Mỗi style có một bảng màu nhỏ, mỗi màu có một nghĩa/vai trò cố định (đỏ chu sa chỉ cho triện, vàng lá chỉ một khoảnh khắc, xanh Prussian chủ đạo). Đừng thêm màu.

## Bảy style trong nhóm

### 1. Ink Wash — thủy mặc

- **Bản chất:** tranh thủy mặc trên giấy gạo: mực 5 sắc (từ đậm nhất tới nhạt nhất), 60–80% giấy trống, nhân vật 12 fps, nhạc guqin dẫn. Mực là nhân vật chính — nó loang, nó bay (flying white), nó khô thành vệt. Giấy gạo là nền và là sáng.
- **Vật liệu:** giấy gạo ~`#f2ecde`, có răng và sợi; mực 5 sắc với opacity ~0,96 / 0,82 / 0,60 / 0,34 / 0,16 (từ đậm nhất tới nhạt nhất). Mỗi sắc là một lớp mực riêng; mực đậm vẽ nét, mực nhạt vẽ wash và xa. **Flying white (飛白)**: nét cọ khô để lại vệt trắng đứt quãng trong nét (lông cọ tách ra khi cọ khô) — đó là chữ ký của thủy mặc, không phải lỗi. **Handscroll (quyển trục)**: cuộn giấy dài mở dần — camera đi dọc cuộn, cảnh mở ra như cuộn tranh được mở.
- **Màu:** mực đen/xám 5 sắc + **đỏ chu sa** ~`#b02e22` **chỉ cho triện** (con dấu đỏ) + tối đa **1 accent nhỏ** (một chấm đỏ, một lá đỏ). Không thêm màu. Đỏ không bao giờ tô hình lớn.
- **Chữ:** chữ Hán/viết tay bằng mực trên giấy, viết dọc (theo cuộn), hoặc phụ đề trên giấy. Tiêu đề là chữ mực lớn; triện đỏ đóng sau chữ. Phụ đề (nếu có) trên giấy, không hộp.
- **Nhịp:** nhân vật 12 fps (vẽ theo cặp — cảm giác tranh động, không mượt); camera mượt; mực loang chậm. Nhạc guqin dẫn nhịp — nhạc là nhịp phim, hình đi theo nhạc.
- **Camera:** camera đi dọc cuộn (handscroll): mở cuộn từ phải sang trái (hoặc trái sang phải theo brief), cảnh mở dần; push-in vào chi tiết mực; pull-back về toàn cuộn. Không cắt giữa chừng khi cuộn đang mở.
- **Âm thanh:** nhạc guqin (đàn tranh cổ) dẫn; thêm sáo, trống nhẹ; tiếng cọ trên giấy gạo (swish khô), tiếng mực loang (nhỏ giọt). Im lặng là một phần của thủy mặc — khoảng trống trong nhạc như khoảng trống trên giấy. −14 LUFS.
- **Chiêu đặc trưng:** flying white (nét cọ khô đứt quãng); handscroll (cuộn mở dần); mực 5 sắc (đậm → nhạt là chiều sâu); triện đỏ (dấu đỏ duy nhất); khoảng trống 60–80% giấy.
- **Cạm bẫy:** tô kín giấy (mất thủy mặc); đỏ tô hình lớn (mất ý nghĩa triện); mực loang quá nhanh (mất cảm giác cọ); nhân vật mượt 24 fps (mất cảm giác tranh động).

### 2. Shadow Puppet — rối bóng

- **Bản chất:** rối bóng da trước đèn dầu: các mảnh da cắt (nhân vật, vật, cảnh) được chiếu bóng lên màn, đèn dầu nhấp nháy, chiêng trống dẫn nhịp. Rối di chuyển bằng khớp nối (tay, chân, đầu xoay quanh khớp) — chuyển động cứng, cót két, như rối thật. Ánh sáng là một phần của câu chuyện: đèn dầu nhấp nháy làm bóng rung.
- **Vật liệu:** da rối cắt (mảnh da mỏng, có lỗ khắc chi tiết), đèn dầu (nguồn sáng điểm, nhấp nháy ~7 Hz — tần số nhấp nháy của ngọn lửa dầu), màn trắng (nơi bóng hiện ra). **Mô hình truyền sáng**: `tonemap = 1 − exp(−hdr)` — ánh sáng xuyên qua da theo độ dày (da mỏng sáng hơn, da dày tối hơn, mực đen nhất). Rối 24 fps, mảnh hiệu ứng (lửa, khói, nước) đổi 12 fps.
- **Màu:** 3–5 thuốc nhuộm (đỏ, xanh, vàng, xanh lá, tím — chọn theo chủ đề) + da thô (màu da tự nhiên) + mực đen (nét và chi tiết khắc). Màu nhuộm trong mờ (ánh sáng xuyên qua). Không thêm màu.
- **Chữ:** chữ viết trên màn (như chữ trên màn rối), hoặc phụ đề dưới màn. Tiêu đề là chữ trên màn. Không font in hiện đại.
- **Nhịp:** rối 24 fps (chuyển động khớp nối mượt vừa đủ); mảnh hiệu ứng 12 fps; đèn dầu nhấp nháy ~7 Hz làm bóng rung nhẹ. Nhịp phim là nhịp chiêng trống — rối di chuyển theo trống.
- **Camera:** camera khóa trên màn (xem bóng); push-in vào chi tiết rối; pull-back để thấy cả màn và đèn dầu; thỉnh thoảng cho thấy tay người điều khiển rối (ở mép khung, mờ). Không di chuyển camera nhiều — màn là sân khấu.
- **Âm thanh:** bộ gõ chiêng trống dẫn nhịp (trống cái, trống con, chiêng, phách); tiếng da rối cọ (khi khớp di chuyển), tiếng đèn dầu (lửa cháy nhẹ). **Press-on / lift-off**: rối ấn xuống màn (bóng đậm, rõ) và nhấc lên (bóng mờ, xa) — âm thanh theo đó (ấn = thump, nhấc = nhẹ). −14 LUFS.
- **Chiêu đặc trưng:** press-on/lift-off (rối ấn/nhấc khỏi màn làm bóng đậm/mờ); đèn dầu nhấp nháy ~7 Hz; khớp nối (tay/chân/đầu xoay quanh khớp); chiêng trống dẫn nhịp; bóng là nhân vật (không thấy rối thật, chỉ thấy bóng).
- **Cạm bẫy:** rối di chuyển mềm như 3D (mất cảm giác khớp nối); đèn không nhấp nháy (mất cảm giác dầu); thấy rối thật thay vì bóng (mất ảo giác); màu nhuộm đục (ánh sáng không xuyên qua).

### 3. Ukiyoe — tranh khắc gỗ Nhật

- **Bản chất:** tranh khắc gỗ Nhật (ukiyo-e): mỗi bản màu in lệch đăng ký 1,5–2,5 px (như in thủ công không khớp hoàn toàn), nét key 2,4–3 px, bokashi (chuyển màu mượt bằng cách chà mực), 6–9 màu phẳng, xanh Prussian chủ đạo, đỏ hiếm. Nhân vật 8 fps, mưa 12 fps, camera 24 fps. Nhạc shamisen/shakuhachi.
- **Vật liệu:** giấy washi (giấy Nhật, có sợi, hơi vàng); bản khắc gỗ (mỗi màu một bản khắc riêng); mực in (màu phẳng, không gradient — trừ bokashi). **Lệch đăng ký 1,5–2,5 px**: mỗi bản màu lệch một chút khỏi bản key (như in tay không khớp) — đó là chữ ký, không phải lỗi. **Bokashi**: chuyển màu mượt trong một bản (vd: trời từ xanh đậm xuống nhạt) bằng cách chà mực không đều trên bản khắc.
- **Màu:** 6–9 màu phẳng; **xanh Prussian chủ đạo** (xanh đậm đặc trưng của ukiyo-e); đỏ hiếm (chỉ cho một điểm nhấn); các màu khác: vàng, xanh lá, nâu, xám, trắng giấy. Màu phẳng, không gradient (trừ bokashi).
- **Chữ:** chữ Nhật viết tay (hoặc chữ Hán) trên tranh, viết dọc; tiêu đề là chữ khắc; phụ đề (nếu có) trên giấy washi. Không font in hiện đại.
- **Nhịp:** nhân vật 8 fps (chuyển động cứng, như tranh động); mưa 12 fps (mưa rơi nhanh hơn nhân vật); camera 24 fps (mượt). **Reveal in từng bản ~0,3 s**: mỗi bản màu hiện ra lần lượt (như đang in từng bản lên giấy) — đó là cách cảnh được dựng.
- **Camera:** camera trên tranh; từ điển: khóa tranh (đang in từng bản), push-in (chi tiết khắc), pull-back (toàn tranh), pan ngang (tranh dài, như cuộn). Không cắt giữa chừng khi đang in bản.
- **Âm thanh:** nhạc shamisen (đàn ba dây) và shakuhachi (sáo trúc); tiếng khắc gỗ (dao khắc), tiếng in (bản ấn xuống giấy), tiếng mưa (nếu có mưa). −14 LUFS.
- **Chiêu đặc trưng:** lệch đăng ký 1,5–2,5 px (in tay không khớp); bokashi (chuyển màu bằng chà mực); reveal in từng bản ~0,3 s (in từng màu lên giấy); xanh Prussian chủ đạo; đỏ hiếm.
- **Cạm bẫy:** các bản khớp hoàn toàn (mất cảm giác in tay); gradient mượt bằng blend pixel (không phải bokashi); đỏ dùng nhiều (mất ý nghĩa hiếm); nhân vật mượt 24 fps (mất cảm giác tranh động).

### 4. Papercut Red — giấy cắt đỏ

- **Bản chất:** giấy cắt đỏ (Trung Quốc): đỏ ~`#d2201f` (dải `#c8102e`–`#d7261e`), cắt yin/yang (phần cắt bỏ và phần giữ lại đều có nghĩa), rosette gấp 8, nhân vật 12 fps, vàng lá chỉ một khoảnh khắc muộn. Giấy cắt là nhân vật chính — nó được gấp, cắt, mở ra. **Fold–cut–unfold**: gấp giấy, cắt, mở ra thành hình đối xứng.
- **Vật liệu:** giấy đỏ (một tờ giấy đỏ duy nhất, không nhiều lớp); cắt yin/yang: phần cắt bỏ (yin — lỗ trống) và phần giữ lại (yang — hình đỏ) đều là hình; **rosette: 1 wedge 45° nhân 8× (D4)** — gấp giấy thành 8 lớp (mỗi wedge 45°), cắt một lần, mở ra thành hoa 8 cánh đối xứng (nhóm đối xứng D4). Vàng lá chỉ xuất hiện **một khoảnh khắc muộn** trong phim (vd: cuối phim, một chi tiết vàng lá hiện ra).
- **Màu:** đỏ ~`#d2201f` (dải `#c8102e`–`#d7261e`) là màu duy nhất cho giấy cắt; nền là giấy trắng/kem (để đỏ nổi); **vàng lá chỉ 1 khoảnh khắc muộn** (không xuất hiện sớm, không lặp lại). Không thêm màu.
- **Chữ:** chữ cắt giấy (chữ là hình cắt, không phải chữ in); tiêu đề là chữ cắt đỏ; phụ đề (nếu có) trên giấy trắng. Không font in.
- **Nhịp:** nhân vật 12 fps (chuyển động cứng, như giấy cắt động); gấp–cắt–mở là nhịp chính (mỗi lần gấp/cắt/mở là một beat). Camera mượt.
- **Camera:** camera trên tờ giấy; từ điển: khóa tờ (đang gấp/cắt), push-in (chi tiết cắt), pull-back (toàn tờ sau khi mở), tilt (xem hình cắt từ góc khác). Không cắt giữa chừng khi đang gấp/cắt.
- **Âm thanh:** tiếng giấy gấp (crease), tiếng kéo cắt giấy (snip), tiếng giấy mở (unfold — whoosh nhẹ), nhạc dân gian nhẹ (sáo, đàn tranh). Vàng lá xuất hiện kèm một nốt nhạc đặc biệt (điểm nhấn âm thanh). −14 LUFS.
- **Chiêu đặc trưng:** fold–cut–unfold (gấp, cắt, mở thành hình đối xứng); rosette D4 (1 wedge 45° × 8); cắt yin/yang (lỗ trống cũng là hình); vàng lá một khoảnh khắc muộn.
- **Cạm bẫy:** giấy cắt nhiều lớp chồng (mất cảm giác một tờ); vàng lá xuất hiện sớm hoặc nhiều lần (mất ý nghĩa khoảnh khắc); cắt không đối xứng (mất rosette); đỏ không đúng dải (quá cam hoặc quá tím).

### 5. Paper Lantern — đèn lồng giấy

- **Bản chất:** đèn lồng giấy: một hộp đèn (0,56×0,33×0,16 m) với giấy mờ, ánh sáng ấm hổ phách bên trong, flicker nhẹ, đèn bật theo stagger ~0,4 s (mỗi đèn bật lệch nhau 0,4 s — như người ta thắp đèn lần lượt). Đèn lồng là nhân vật chính — nó sáng lên, nó tắt đi, nó dẫn câu chuyện.
- **Vật liệu:** hộp đèn 0,56×0,33×0,16 m (kích thước thật của đèn lồng giấy); giấy mờ (độ xuyên sáng 0,9 ở xa → 0,05 ở gần — giấy mỏng ở xa sáng hơn, giấy dày ở gần tối hơn); lớp z −0,14→0 (chiều sâu của hộp đèn); ánh sáng ấm hổ phách bên trong. **Flicker**: `1 + 0,06·sin(7,3t)·sin(3,1t)` — ánh sáng nhấp nháy nhẹ theo hai tần số (như ngọn nến/lửa dầu).
- **Màu:** ánh sáng ấm hổ phách (vàng cam ấm) là màu chính; giấy trắng/kem (khi chưa sáng) và đỏ (đèn lồng đỏ truyền thống, nếu brief chọn); nền tối (đêm) để đèn nổi. Không thêm màu rực.
- **Chữ:** chữ trên đèn lồng (chữ viết trên giấy đèn), hoặc phụ đề dưới đèn. Tiêu đề là chữ trên đèn. Không font in hiện đại.
- **Nhịp:** 30 fps; đèn bật theo stagger ~0,4 s (mỗi đèn bật lệch nhau); flicker liên tục nhẹ. Nhịp phim là nhịp đèn bật — mỗi đèn bật là một beat.
- **Camera:** camera trong không gian đèn lồng; từ điển: khóa đèn (đang bật), push-in (chi tiết giấy/ánh sáng), pull-back (nhiều đèn), pan ngang (dãy đèn). Camera mượt, chậm.
- **Âm thanh:** tiếng đèn bật (click nhẹ), tiếng giấy đèn (xào xạc), nhạc nhẹ (sáo, đàn tranh, dây), tiếng đêm (dế, gió nhẹ). Im lặng giữa các đèn bật là nhịp thở. −14 LUFS.
- **Chiêu đặc trưng:** đèn bật theo stagger ~0,4 s (thắp đèn lần lượt); flicker hai tần số; độ xuyên sáng theo khoảng cách (xa sáng, gần tối); hộp đèn kích thước thật.
- **Cạm bẫy:** tất cả đèn bật cùng lúc (mất stagger); flicker quá mạnh (đọc như đèn hỏng); ánh sáng trắng lạnh (mất hổ phách ấm); đèn không có hộp (mất cảm giác vật thể).

### 6. Stained Glass — kính màu

- **Bản chất:** kính màu nhà thờ: backlight 2–3× (ánh sáng sau kính mạnh gấp 2–3 lần để màu kính rực), chì gần đen (đường chì nối các mảnh kính), grisaille nâu (màu nâu vẽ chi tiết lên kính), nhân vật 8 fps, **màu mặt trời = đồng hồ** (trắng xanh bình minh → vàng chiều → cam đậm hoàng hôn — màu ánh sáng qua kính đổi theo giờ trong ngày, đó là cách phim nói về thời gian). **Ánh sáng là thời gian.**
- **Vật liệu:** kính màu (mảnh kính màu phẳng, không gradient); chì gần đen (đường chì dày, gần đen, nối các mảnh); grisaille nâu (màu nâu vẽ chi tiết mặt, nếp áo lên kính); backlight 2–3× (ánh sáng sau kính). **Hình chiếu màu xuống sàn mờ, desat ~20%**: ánh sáng qua kính chiếu xuống sàn thành mảng màu mờ, nhạt hơn 20% so với kính.
- **Màu:** màu kính (đỏ, xanh, vàng, xanh lá, tím — chọn theo chủ đề); chì gần đen; grisaille nâu. **Màu mặt trời = đồng hồ**: bình minh = trắng xanh; trưa = trắng vàng; chiều = vàng; hoàng hôn = cam đậm. Màu ánh sáng đổi theo giờ, không đổi theo ý thích.
- **Chữ:** chữ trên kính (chữ khắc/vẽ trên kính), hoặc phụ đề dưới cửa sổ kính. Tiêu đề là chữ trên kính. Không font in hiện đại.
- **Nhịp:** nhân vật 8 fps (chuyển động cứng, như kính màu động); camera 24 fps; màu mặt trời đổi chậm theo giờ (thời gian trôi là nhịp phim). Nhạc organ.
- **Camera:** camera trước cửa sổ kính; từ điển: khóa cửa sổ (đang xem kính), push-in (chi tiết kính/chì), pull-back (toàn cửa sổ + hình chiếu xuống sàn), tilt xuống sàn (xem hình chiếu màu). Camera mượt, chậm.
- **Âm thanh:** nhạc organ (nhạc nhà thờ); tiếng chuông (nếu có); im lặng trong nhà thờ (room tone vang nhẹ). Tiếng bước chân trên sàn đá (nếu có người). −14 LUFS.
- **Chiêu đặc trưng:** màu mặt trời = đồng hồ (ánh sáng đổi màu theo giờ); hình chiếu màu xuống sàn (desat 20%); backlight 2–3×; chì gần đen; organ.
- **Cạm bẫy:** màu mặt trời không đổi theo giờ (mất ý nghĩa đồng hồ); hình chiếu màu quá rõ/bão hòa (mất mờ); chì quá mỏng (mất cảm giác kính màu); nhân vật mượt 24 fps (mất cảm giác kính động).

### 7. Gilded Illumination — sách minh họa mạ vàng

- **Bản chất:** sách minh họa thời Trung cổ (illuminated manuscript): vellum (da thuộc làm giấy), ultramarine, vermilion, verdigris, vàng lá, mực; lá vàng lát ô vuông có seam (đường nối giữa các lá vàng); ánh sáng chỉ chiếu lên vàng, cap 82% (không cháy trắng — vàng lá sáng nhưng không bao giờ trắng tinh); đêm xanh ultramarine đậm, không đen; 30 fps; phụ đề là scroll da cố định một vị trí/kích thước.
- **Vật liệu:** vellum `#efe2c4` (da thuộc, màu kem ấm, có răng); vàng lá (lá vàng mỏng lát thành ô vuông, có seam — đường nối giữa các ô vuông vàng); ultramarine `#22379a` (xanh đậm, màu đắt nhất thời Trung cổ); vermilion `#c8321f` (đỏ son); verdigris `#3f8f7a` (xanh lá đồng); mực `#2a1a10` (mực nâu đen). **Ánh sáng chỉ chiếu lên vàng, cap 82%**: ánh sáng trong phim chỉ làm vàng lá sáng lên, tối đa 82% độ sáng (không bao giờ cháy trắng).
- **Màu:** ultramarine `#22379a` + vermilion `#c8321f` + verdigris `#3f8f7a` + vàng lá mid `#c99a3e` + mực `#2a1a10` + vellum `#efe2c4`. Đêm là xanh ultramarine đậm, **không bao giờ đen**. Không thêm màu.
- **Chữ:** chữ viết tay thời Trung cổ (chữ Gothic/calligraphy) bằng mực trên vellum; tiêu đề là chữ lớn có vàng lá; **phụ đề là scroll da cố định một vị trí/kích thước** (một cuộn da nhỏ ở góc, luôn cùng vị trí và kích thước, không di chuyển). Không font in hiện đại.
- **Nhịp:** 30 fps; trang sách lật chậm; vàng lá bắt sáng khi ánh sáng di chuyển. Nhịp phim là nhịp lật trang và ánh sáng.
- **Camera:** camera trên trang sách; từ điển: khóa trang (đang xem minh họa), push-in (chi tiết vàng lá/minh họa), pull-back (toàn trang), lật trang (sang trang mới). Camera mượt, chậm.
- **Âm thanh:** nhạc cổ (lute, recorder, dây cổ, hát Gregorian nhẹ); tiếng lật trang da (xào xạc dày), tiếng bút lông trên vellum. Im lặng trong thư viện cổ. −14 LUFS.
- **Chiêu đặc trưng:** vàng lá lát ô vuông có seam; ánh sáng chỉ chiếu lên vàng, cap 82%; đêm xanh ultramarine đậm, không đen; phụ đề scroll da cố định; lật trang da.
- **Cạm bẫy:** đêm đen (mất ultramarine); vàng lá cháy trắng (vượt cap 82%); ánh sáng chiếu lên cả trang (chỉ chiếu lên vàng); phụ đề di chuyển (mất cố định); font in hiện đại.

## Hệ màu / bảng chất liệu bất biến (tóm tắt theo style)

| Style | Chất liệu | Màu (bất biến) | Nhịp |
|---|---|---|---|
| ink-wash | Giấy gạo `#f2ecde`, mực 5 sắc | Mực 5 sắc + đỏ chu sa `#b02e22` chỉ triện | Nhân vật 12 fps, guqin dẫn |
| shadow-puppet | Da rối, đèn dầu ~7 Hz, màn | 3–5 thuốc nhuộm + da thô + mực | Rối 24 fps, hiệu ứng 12 fps |
| ukiyoe | Giấy washi, bản khắc, lệch 1,5–2,5 px | 6–9 màu phẳng, xanh Prussian chủ đạo, đỏ hiếm | Nhân vật 8 fps, mưa 12 fps, camera 24 fps |
| papercut-red | Giấy đỏ `#d2201f`, cắt yin/yang | Đỏ duy nhất + vàng lá 1 khoảnh khắc muộn | Nhân vật 12 fps, gấp–cắt–mở |
| paper-lantern | Hộp 0,56×0,33×0,16 m, giấy mờ | Hổ phách ấm, giấy kem, đỏ (nếu có) | 30 fps, đèn bật stagger ~0,4 s |
| stained-glass | Kính màu, chì gần đen, backlight 2–3× | Màu kính + chì + grisaille nâu; mặt trời = đồng hồ | Nhân vật 8 fps, organ |
| gilded-illumination | Vellum `#efe2c4`, vàng lá, mực `#2a1a10` | Ultramarine `#22379a`, vermilion `#c8321f`, verdigris `#3f8f7a`, vàng `#c99a3e` | 30 fps, lật trang da |

## Quy trình sản xuất

1. **Chốt brief trước.** Chủ đề, câu chuyện (dân gian, lịch sử, tôn giáo, thiên nhiên), bảng màu theo style (mỗi style có bảng màu riêng — chọn từ brief, không lấy màu của demo gốc). Hỏi user có tư liệu tham chiếu của mình không (tranh cổ, mẫu vật, câu chuyện dân gian).
2. **Treatment ngắn trước khi dựng:** chọn 1 style (không trộn 2 style trong một phim trừ khi brief yêu cầu rõ và có điểm chuyển chất liệu), chọn 3 chiêu đặc trưng sẽ dùng (xem từng style), mỗi chiêu: nó nói ý gì, xuất hiện khi nào. Một phim 20–60 s thường dùng 2–4 chiêu.
3. **Look test trước:** render frame tĩnh/đoạn ngắn bằng đúng cách làm của style (mực loang, rối bóng, bản khắc lệch, giấy cắt, đèn lồng, kính màu, vàng lá) và đối chiếu với `STYLE.md` gốc: chất liệu có đúng vật lý không (mực có 5 sắc không, bản khắc có lệch không, vàng lá có seam không).
4. **Timeline là nguồn sự thật duy nhất:** một bảng beat (mốc giây → sự kiện hình → sự kiện âm) mà hình, phụ đề, nhạc, mix đều đọc từ đó. Nhịp hình và cue âm lệch nhau là lỗi, không phải "cảm tính".
5. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi nét/vật là hàm của `t` với seed cố định; vật đã xong đứng yên (trừ luật sôi/nhấp nháy riêng của từng style); chữ viết/vẽ theo đúng thứ tự tay.
6. **Render thử các frame hero của từng beat** → contact sheet soát: chất liệu, độ đọc của chữ, bố cục khoảng trống, trước khi render full.
7. **Âm thanh theo bảng âm của style** (xem từng style), mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng (chung cho nhóm)

- Vật liệu thủ công là luật: không phủ filter lên ảnh có sẵn; không làm "mượt" chuyển động cứng theo mảnh/lớp.
- Khoảng trống là bố cục: giấy trống, nền tối, khoảng đen đều là một phần của hình. Đừng lấp đầy khoảng trống vì sợ "trống".
- Ánh sáng là một phần của chất liệu: đèn dầu, nắng qua kính, vàng lá bắt sáng — ánh sáng không phải hiệu ứng phủ ngoài.
- Một style = một phim (trừ khi brief yêu cầu rõ và có điểm chuyển chất liệu). Không trộn thủy mặc với rối bóng trong một shot.
- Chữ bắt buộc đọc giữ ≥ 1,8 s (hoặc ≥ câu nói + 0,6 s); công thức đọc chung: CJK ÷ 4,5 + Latin ÷ 15 + 1,5 s tính từ lúc khối chữ hoàn chỉnh.
- Số liệu (nếu có) phải thật và có nguồn ghi lại; không bịa số trong phim tư liệu/truyền thống.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; mọi jitter/nhấp nháy phải suy từ seed cố định theo index của vật), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Seed và sôi/nhấp nháy:** mọi vật có seed cố định; random chỉ được tiêu thụ cùng một cách ở mọi tiến độ. Chỉ phần style cho phép mới động (đèn dầu flicker, vàng lá bắt sáng, mực loang) và theo công thức cố định của style (flicker đèn lồng: `1 + 0,06·sin(7,3t)·sin(3,1t)`; đèn dầu ~7 Hz).
- **Ánh sáng theo chất liệu:** ánh sáng tính từ chất liệu (truyền sáng qua da: `tonemap = 1 − exp(−hdr)`; backlight kính 2–3×; vàng lá cap 82%), không phải đèn phủ ngoài.
- **Chữ viết/vẽ:** chữ hiện bằng cách viết dọc skeleton glyph hoặc stroke-by-stroke (không wipe, không fade); triện/chữ khắc đóng/dập (không fade).
- **Cache:** vật đã xong cache thành sprite; chỉ vẽ stroke-by-stroke thứ đang được vẽ hoặc biến hình.
- **Âm thanh:** master −14 LUFS, true peak ≤ −1 dBTP; giọng đọc kiểm tra bằng ASR trên giọng sạch và trên phim hoàn chỉnh.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1280×720 hoặc 1920×1080, 30 fps; ink-wash/shadow-puppet/ukiyoe có nhịp riêng theo style — xem bảng), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) chất liệu đúng vật lý của style (mực 5 sắc / da rối truyền sáng / bản khắc lệch / giấy cắt đối xứng / đèn lồng flicker / kính màu backlight / vàng lá seam); (b) chữ đọc được, đủ thời gian đọc, không bị vật che; (c) khoảng trống đủ cho bố cục (không lấp đầy); (d) màu đúng bảng của style (không thêm màu, đỏ/vàng lá đúng vai trò).
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn, nhãn nằm trên vùng trống, không đè lên chủ thể.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Bản quyền: ghi rõ nguồn tham chiếu/hình ảnh trong QA.md; không dùng artwork, tên phim demo, nhân vật hay nhãn hiệu thật của repo gốc.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: nguồn tham chiếu, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.

## Phân biệt với các nhóm skill opuscar khác

- `opuscar-painting-illustration`: hội họa phương Tây/hiện đại trên giấy/canvas (sáp, màu nước, sơn dầu) — nhóm này là thủ công truyền thống (thủy mặc, rối bóng, khắc gỗ, giấy cắt, đèn lồng, kính màu, vàng lá), chuyển động cứng theo mảnh/lớp.
- `opuscar-sketch-board`: bút/phấn/marker hiện đại để giải thích — nhóm này là nghề thủ công truyền thống để kể chuyện.
- `opuscar-edit-documentary`: sắp xếp tư liệu thật, không dựng lại thế giới bằng chất liệu — ngược với nhóm này.
- `opuscar-printmaking`: in ấn là luật (bản in, halftone, lệch đăng ký) — nhóm này có ukiyoe cũng là in khắc gỗ, nhưng ukiyoe ở đây là một phần của truyền thống thủ công (cùng với thủy mặc, rối bóng), còn printmaking là cả một hệ in ấn hiện đại (risograph, silkscreen, pop-art).
- Các nhóm còn lại (graphic & type, line diagrams, cartoons, games, film & tape, screens & interfaces, light & lines, 3D & miniature, instruments & evidence, data & maps): khi brief nói "thủy mặc / rối bóng / khắc gỗ Nhật / giấy cắt / đèn lồng / kính màu / sách mạ vàng" thì nhóm này là đáp án.
