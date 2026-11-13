---
name: opuscar-games
description: Kỹ thuật phim kể chuyện bằng ngôn ngữ trò chơi điện tử (spin-out từ bộ Lemo-Opuscar) — 4 style: RPG pixel 16-bit, pixel 2.5D HD-2D, microgame tốc độ tăng dần, gameshow theo nhịp. Dùng khi brief là "kể như một game", "nhiệm vụ/vật phẩm/save file", "5 trò chơi 5 giây", "gameshow đếm nhịp". Mọi nội dung do brief quyết định — skill chỉ giữ ngữ pháp game và kỷ luật sản xuất.
---

# Opuscar Games — Kể chuyện bằng ngôn ngữ game

Ngôn ngữ game làm ngôn ngữ kể chuyện: hộp thoại, menu, thanh trạng thái, file save, mạng sống, vòng chơi — không phải trang trí mà là công cụ kể. Khán giả hiểu ngay vì đã chơi game: một hộp thoại mở ra là một nhân vật đang nói, một thanh máu tụt xuống là một cái giá phải trả.

Nguồn kỹ thuật: 4 style trong repo Lemo-Opuscar tại `~/workspace/lemo-opuscar/styles/{pixel-rpg,hd-2d,microgame,game-show}/STYLE.md` — đọc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện/nhân vật/nhãn hiệu của phim mẫu.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Giấy phép: code MIT, tài liệu gốc CC BY-NC 4.0 (hệ REUSE của repo); phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

## Khi nào dùng

- Một hành trình dài kể như RPG: nhiệm vụ, vật phẩm, điểm save, lên cấp, boss cuối.
- Một nơi chốn nhỏ nhìn như mô hình bàn, ánh sáng là nhân vật chính: HD-2D.
- Nhiều việc nhỏ dồn dập, mỗi việc một chất liệu vẽ khác nhau, càng lúc càng nhanh: microgame.
- Nội dung theo vòng, theo nhịp, cần năng lượng gameshow: mỗi vòng một màu, mọi hiệu ứng rơi đúng ô nhịp.
- Không dùng cho: phim tài liệu nghiêm túc (nhóm Edit & Documentary), giải thích máy móc chính xác (opuscar-line-diagrams), hoạt hình diễn thoại dài không có UI game (opuscar-cartoons).

## Khi nào KHÔNG dùng

- Chủ đề cần tông trang trọng, tang lễ, điều tra: UI game (mạng sống, điểm số, fanfare vật phẩm) sẽ làm lệch tông.
- Cần nhân vật diễn cảm mặt chi tiết: sprite pixel 20–34px không có mặt để diễn — cảm xúc đến từ tư thế, hộp thoại và hệ thống.
- Cần hình ảnh thật, footage, ảnh lưu trữ: nhóm này vẽ toàn bộ bằng code, không dùng ảnh thật làm nền (trừ texture pixel trong HD-2D).
- Không có style nào trong nhóm cần máy tạo ảnh — toàn bộ 4 style làm bằng code. Không dùng tên/logo game thật, không nhại UI của một game cụ thể.

## Nguyên lý cốt lõi

1. **Hệ thống game là ngôn ngữ cảm xúc.** Lên cấp, mất máu, hết mạng, save/load — mỗi cơ chế mang một cảm giác mà khán giả đã biết; dùng đúng cơ chế thì không cần giải thích.
2. **UI là kể chuyện, không phải trang trí.** Hộp thoại, menu, thanh trạng thái, file save chỉ xuất hiện khi chúng nói được một điều về câu chuyện. UI thừa là nhiễu.
3. **Pixel là luật, không phải filter.** Độ phân giải gốc, bảng màu giới hạn, phóng to bằng nearest-neighbour, gradient bằng dither có thứ tự — không làm mờ, không blend.
4. **Nhịp là luật chơi.** Mọi hiệu ứng rơi đúng ô nhịp; nhạc sinh ra từ chính timeline của hình nên hình và nhạc không thể lệch nhau.
5. **Ánh sáng kể chuyện (HD-2D), tốc độ kể chuyện (microgame).** Mỗi style có một "đồng hồ" riêng: HD-2D là đèn bật/tắt, microgame là thang tốc độ tăng dần, game-show là lưới nhịp cố định.

## Bảng 4 style — bất biến từng style

| Style (slug) | Nhận diện nhanh | Màu / chất liệu bất biến | Chữ | Nhịp/chuyển động |
|---|---|---|---|---|
| `pixel-rpg` — RPG pixel 16-bit | Khung hình gốc 320×180, phóng ×6 nearest-neighbour lên 1080p; sprite 20–34px, vài frame; mặt diễn trong chân dung; chuyện kể bằng hộp thoại, menu, thanh trạng thái, file save | Bảng màu giới hạn, có chỉ số (indexed); gradient chỉ bằng dither có thứ tự, không blend; đổi bảng màu theo bảng, không theo alpha; độ sâu màu thay cho thời gian (càng xưa càng ít màu, càng thấp độ phân giải); 1–2 màu được bảo vệ, miễn mọi hiệu ứng, làm sợi chỉ xuyên phim và cho phép match cut giữa các thời kỳ | Hộp thoại là phụ đề: viền nhiều lớp (mực/trắng/bạc), nền xanh đậm dither, chân dung 32×32 bên trái, font pixel gốc biến đổi (cap ~7px) bóng 1px; gõ theo giọng ~38–40 ký tự/giây (chậm hơn ở thời kỳ xưa), ▼ nhấp nháy khi xong; giao diện đổi da theo thời kỳ | Xuất 24fps; sprite bước 8fps (đi) tới 12fps (lửa, chớp); camera/parallax chạy ones ở pixel nguyên; diễn xuất kiểu game: nhảy lên hành động, tư thế niệm, giật lùi, quỳ, KO nhấp nháy 12fps rồi biến mất; thở = vai lên 1px; cửa sổ trượt vào ~0.3s (ease-out, pixel nguyên); con trỏ tay bob 1px ở 4fps và dừng khi nhân vật dừng |
| `hd-2d` — pixel 2.5D | Mô hình 3D thu nhỏ bằng hộp/trụ bọc texture pixel, nhân vật sprite 2D phẳng nhận sáng và đổ bóng, camera cao xa nhìn qua dải tilt-shift như mô hình bàn; ánh sáng là chủ thể: đèn thực tế hắt bóng sprite qua sàn, tia sáng/sương/bụi/mưa lơ lửng, bloom mạnh, vignette nặng; trên cùng UI RPG nhỏ | 2 nhiệt độ: một key môi trường lớn (lạnh/nhạt/bụi) đối đầu đèn thực tế nhỏ ấm/bão hòa; đèn thực tế mang chuyện, môi trường mang tâm trạng; giá trị tối nhất là mực ấm, không đen tuyền; sáng nhất là chính nguồn sáng, bloom; mỗi set một màu sương + một key sáng riêng | Serif khắc capital (Cinzel, tracking rộng) cho nhãn chương/tiêu đề; serif cổ (Cormorant, italic) cho phụ đề/thoại/tagline; phụ đề tường thuật italic serif ~46–54px, giữa thấp trên dải tối mềm, một dòng mỗi clip thoại, vào ~0.35s trước giọng; thoại trên màn hình dùng hộp thoại | Sprite bước, mọi thứ khác trôi: chu trình đi 4 frame ở 6–10fps, idle đổi 2 frame ~1–2Hz, chớp mắt vài giây một lần, đổi tư thế là cắt tức thời giữa các hình; camera/đèn/hạt/tia/focus cập nhật mỗi frame xuất (60fps); tư thế là dữ liệu (một object tham số mỗi hình); đèn thở: lửa nhấp nháy bằng tổng vài sine |
| `microgame` — microgame tốc độ tăng dần | Một microgame = một từ lệnh hét lên + 2.5–4s + một hành động + một kết quả (thắng, hoặc thua hài); mỗi microgame một chất liệu hình khác nhau (sáp, mực, terminal, riso, pixel, blueprint, chữ Swiss, đất sét, giấy cắt, khắc gỗ); một sân khấu nhà cố định (host, đếm mạng, số màn) giữ phim lại với nhau giữa các game; càng lúc càng nhanh | Sân khấu nhà: bảng màu tiệc bão hòa — nền đậm sau sunburst xoay, 2–3 màu nhấn lớn, cộng một màu thắng cố định và một màu thua cố định chỉ dùng cho con dấu và bảng mạng; mỗi chất liệu mang bảng màu của truyền thống nó (màu sáp, một mực + đỏ son, phosphor hổ phách, 3 bản riso, bảng pixel giới hạn, trắng-trên-xanh, đen-trắng-đỏ); không nhuộm màu một chất liệu sang chất liệu khác; ví dụ màu sân khấu `#2a0f5c`/`#ff2e88`/`#ffc928`/`#1fd1d1` | Từ lệnh là phụ đề: display nặng (Titan One…), trắng viền mực dày, bóng màu, burst sau lưng, nghiêng vài độ; đáp vào ~3 frame (overshoot → ổn định), giữ, rồi co lại thành tag góc trước hành động đầu tiên để không che kết quả; banner một lần bay ra thay vì gắn tag | Khung hình là một phần của thang tốc độ: nhân vật bước 2 hoặc 8fps lúc đầu, nhanh dần, ones ở cao trào; camera/chuyển cảnh/tia lửa đồng hồ chạy ones; 5 thứ tăng tốc cùng lúc mỗi lần lên tốc: tempo, độ dài game, thời gian ở sân khấu, thời gian giữ lệnh, frame rate nhân vật; đồng hồ hiện rõ và đúng nhịp (ví dụ ngòi nổ một nút mỗi nhịp, tia lửa đi qua từng nút) |
| `game-show` — gameshow theo nhịp | Mọi thứ trên lưới: một tempo cố định, nhanh; mọi cú nảy, rơi, đóng dấu, gõ chữ, punch camera đều nằm ở (bar, beat) và đồng thời là một sự kiện âm thanh; nhạc sinh từ chính timeline của hình; một bộ đồ họa (màu phẳng, một viền mực nặng, đầu tròn, bóng cứng lệch), mỗi vòng một màu nền bão hòa mới; nhân vật là đồ chơi: một cấu trúc thân cho cả dàn, phân biệt bằng màu, mảng bụng, một phụ kiện đầu, thẻ tên | Mực + giấy + kẹo: mực gần đen, trắng, kem ấm cho thẻ/đạo cụ giấy; ~8 màu kẹo bão hòa (vàng, cam, đỏ, hồng, xanh lá, xanh non, xanh trời, xanh dương) + 2–3 màu đậm với bản tối hơn cho set đêm/chung kết; một set = một màu (nền, pattern, thẻ vòng cùng màu); 2 vòng kề nhau không bao giờ cùng màu; ví dụ `#FFA85A`/`#FFB870` | Display: sans tròn nặng cho Latin/số (Fredoka 700), sans đen cho CJK (Noto Sans SC 900), chữ viết tay chỉ cho đạo cụ viết tay (ZCOOL KuaiLe); chữ telop: tô trắng/vàng, viền mực ≈ 14% cỡ chữ vẽ *dưới* lớp tô (`paint-order: stroke`); tiêu đề dựng từng glyph để mỗi ký tự nảy riêng | Nhàn rỗi = nhảy theo nhịp: parabol mỗi nhịp (8–30px), hàng xóm nhảy lệch nhịp để đám đông gợn sóng; trúng = squash: wobble tắt dần (~30 rad/s, ~0.35s) sau mỗi cú trúng, squash nhỏ mỗi downbeat; xuất hiện rơi từ trời với ease-in, đáp đúng nhịp để âm thanh đáp cùng; đám đông rơi một người mỗi nhịp/nửa nhịp; pop dùng back-ease |

## Quy trình sản xuất

1. **Chọn style trước, chọn tempo/luật chơi trước.** Pixel-rpg cần bảng màu + thời kỳ; hd-2d cần key sáng + màu sương từng set; microgame cần thang tốc độ; game-show cần tempo cố định + bảng màu từng vòng. Ghi vào treatment trước khi dựng.
2. **Treatment ngắn:** 3 cấu trúc ứng viên rồi chốt một. Với pixel-rpg: danh sách nhiệm vụ/vật phẩm/file save; với microgame: danh sách game (lệnh + chất liệu + kết quả) theo thứ tự tăng tốc; với game-show: danh sách vòng (số + tên + tag) và màu từng vòng.
3. **Bảng beat/timeline là nguồn sự thật duy nhất:** một bảng mốc (bar, beat) → sự kiện hình → sự kiện âm mà hình, chữ, nhạc, mix đều đọc từ đó. Ở game-show, nhạc sinh từ chính bảng này — không có danh sách cue riêng.
4. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi tư thế sprite/UI là hàm của `t`; tư thế tính lại từ `t` mỗi lần render (không cập nhật state có nhớ — worker render song song bắt đầu lạnh sẽ hiện trạng thái ban đầu sai).
5. **Render thử frame hero** (hộp thoại, một set HD-2D có đèn, một microgame, một thẻ vòng) → contact sheet soát bảng màu, độ đọc UI, ánh sáng — trước khi render full.
6. **Âm thanh theo bảng âm của style**, mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng

- **Pixel-rpg:** sụp đổ/bão hòa bảng màu (độ sâu màu giảm một bậc mỗi nhịp, hoặc màu tràn lại qua sóng dither) → match cut bằng màu được bảo vệ (một màu miễn hiệu ứng nối 2 thời kỳ ở cùng vị trí màn hình) → file save làm ký ức (danh sách file, mỗi file một thời điểm) → fanfare vật phẩm khi nhận đồ.
- **HD-2D:** bóng nhảy khi đèn bật (đèn thực tế bật cạnh sprite, bóng quét qua sàn) → ánh sáng mang theo làm thước đo (độ sáng của đèn nhân vật mang lên xuống theo thứ đang đo) → camera cao xa qua dải tilt-shift, cắt sang set mới là đổi màu sương + key sáng.
- **Microgame:** đổi chất liệu mỗi game → từ lệnh (một động từ vừa là kịch bản, vừa là phụ đề, vừa là downbeat) → mạng sống làm UI (bộ đếm mang cảm xúc mà không cần lời) → thang tốc độ: 5 thứ tăng cùng lúc, thất bại ở tempo cao phải đọc được ngay (làm chậm lại một nhịp cho cú thua).
- **Game-show:** thẻ vòng 1 bar (số vòng + tên + tag như năm/bước) bay vào theo jingle rồi chơi → báo cáo (recap gõ máy + con dấu điểm) → hỏi-đáp thành pattern nhịp, tăng tốc dần → mỗi vòng một màu nền mới, nhân vật đồ chơi nhún theo beat.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; mọi tư thế/nhịp tính lại từ `t`), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Framebuffer pixel (pixel-rpg):** mọi thứ, kể cả chữ, sống trong framebuffer 320×180 rồi phóng ×6 nearest-neighbour; camera/parallax di chuyển theo pixel nguyên; sprite bước 8–12fps; hộp thoại gõ ~38–40 ký tự/giây; đổi bảng màu theo bảng chỉ số, không theo alpha.
- **Ánh sáng HD-2D:** sprite 2D phẳng nhưng nhận sáng/đổ bóng trong set 3D; đèn thực tế đặt lệch ~0.45m về phía camera để không đốt cháy sprite mang nó; giới hạn sáng trên sprite trong shader (`min(outgoingLight, diffuse * 1.35 + emissive)`); dải dither vừa phải (~0.22 trên sprite, ~0.45 trên texture) — quá rộng sẽ thành bàn cờ.
- **Lưới nhịp (game-show, microgame):** mọi hiệu ứng gắn vào (bar, beat); nhạc sinh từ timeline hình; danh sách cue suy ra từ một bảng duy nhất — cue, flash, jingle, arrangement tách thành nhiều danh sách tay sẽ lệch nhau.
- **Chữ:** hộp thoại pixel-rpg gõ theo giọng, ▼ nhấp nháy khi xong; phụ đề HD-2D italic serif vào ~0.35s trước giọng; từ lệnh microgame đáp ~3 frame rồi co thành tag góc; chữ telop game-show viền mực vẽ dưới lớp tô, dựng từng glyph.
- **Âm thanh:** chiptune/fanfare kiểu game cho pixel-rpg (tiếng nhận vật phẩm, tiếng menu, tiếng save); HD-2D: nhạc nền mỏng + tiếng đèn (bật, thở, tắt) + tiếng bước sprite; microgame: mỗi game một họ âm theo chất liệu + tiếng còi/đồng hồ; game-show: jingle mỗi vòng + tiếng nảy/đóng dấu theo nhịp, nhạc sinh từ timeline. Mix cuối chuẩn −14 LUFS.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (pixel-rpg: framebuffer 320×180 phóng ×6 lên 1920×1080; các style còn lại mặc định ngang 1920×1080), thời lượng khớp `window.DUR`; frame rate: pixel-rpg xuất 24fps, hd-2d 60fps cho camera/đèn (sprite vẫn bước 6–10fps).
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) pixel không bị làm mờ/blend (so frame phóng to: cạnh phải sắc, dither có thứ tự); (b) UI đọc được, không che hành động; (c) màu được bảo vệ giữ nguyên qua các lần đổi bảng; (d) HD-2D: sprite không cháy sáng, bóng đổ đúng hướng đèn.
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ (font pixel phải có đủ dấu tiếng Việt — thiếu dấu thì đổi font, không bỏ dấu), không tràn hộp thoại, hộp thoại không che nhân vật đang nói.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame; hiệu ứng game-show/microgame rơi đúng (bar, beat).
- Tính lại từ `t`: render 1 frame đơn lẻ và render tuần tự phải cho cùng tư thế — khác nhau là lỗi state có nhớ.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Bản quyền: font dùng phải OFL và tự host (font pixel phải tự vẽ hoặc OFL, không lấy font của game thật); không gắn tên/logo/UI của game thật vào phim; nhân vật và tên game trong phim là hư cấu.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: style đã dùng + tempo/bảng màu, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian, bảng màu (palette) từng thời kỳ/set/vòng.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.
