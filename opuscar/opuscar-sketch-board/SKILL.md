---
name: opuscar-sketch-board
description: Kỹ thuật phim vẽ tay trên bảng và giấy (spin-out từ bộ Lemo-Opuscar) — một nét liền, bảng trắng marker, bảng phấn, sketchnote, người que giải thích, vẽ số trên iPad, marker trên giấy. Dùng khi brief là "giải thích một ý nhanh bằng cách vẽ ra trước mắt người xem", "vẽ trên bảng trắng/bảng phấn", "sketchnote một buổi nói chuyện", "người que minh họa một quy trình", hoặc "vẽ tay trên iPad". Mọi nội dung (chủ đề, câu chuyện, bảng màu) do brief quyết định — skill chỉ giữ vật lý của bút, phấn, bảng và kỷ luật dựng.
---

# Opuscar Sketch & Board — Vẽ tay trên bảng & giấy

Mỗi style trong nhóm là một cách **giải thích bằng tay vẽ**: nét xuất hiện đúng thứ tự tay viết, tốc độ bút là nhịp phim, và bàn tay (hoặc bút dẫn) là người dẫn chuyện. Khác với nhóm hội họa (chất liệu là nhân vật chính), ở đây **ý tưởng là nhân vật chính** — nét vẽ chỉ là cách ý tưởng hiện ra. Giấy/bảng là mặt phẳng làm việc, không phải thế giới.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Code gốc MIT, tài liệu gốc CC BY-NC 4.0; phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

Nguồn kỹ thuật: các style `one-line`, `whiteboard`, `chalkboard`, `sketchnote`, `stick-explainer`, `ipad-sketch`, `marker-paper` trong repo Lemo-Opuscar — đọc `STYLE.md` gốc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện, tên phim demo, nhân vật hay nhãn hiệu thật trong demo của repo.

## Khi nào dùng

- Giải thích một ý tưởng bằng **một nét liền không nhấc bút** (one-line): một vật, một quá trình, một hành trình — nét là câu chuyện.
- Dạy/giải thích trên **bảng trắng** với marker, nam châm, cục tẩy tự di chuyển (whiteboard).
- Giảng bài kiểu lớp học trên **bảng phấn** xanh đậm: viết — xóa — viết lại, panel trượt (chalkboard).
- Tóm tắt một buổi nói chuyện/bài giảng thành **sketchnote** trên giấy chấm lưới (sketchnote).
- Minh họa quy trình bằng **người que** chuyển động mượt, vật lý lò xo (stick-explainer).
- Vẽ minh họa trên **iPad**: nét chì trước, màu tô sau lệch khỏi nét (ipad-sketch).
- Giải một bài toán/bài tập trên **giấy marker**: đen dựng hình, xanh là dữ kiện, đỏ là đáp án (marker-paper).

## Khi nào KHÔNG dùng

- Không dùng nhóm này khi brief cần chất liệu hội họa làm nhân vật chính (sáp, màu nước, sơn dầu bay — đó là `opuscar-painting-illustration`), khi cần tư liệu thật (`opuscar-edit-documentary`), hay khi cần in ấn (bản in, halftone — `opuscar-printmaking`).
- Không dùng whiteboard cho bài giảng cần cảm giác lớp học cổ điển (đó là chalkboard); không dùng chalkboard cho giải thích nhanh cần màu marker rõ (đó là whiteboard); không dùng one-line cho bài có nhiều ý cần ghi chú (đó là sketchnote).
- Không dùng stick-explainer cho giải thích cần vẽ chi tiết kỹ thuật (đó là marker-paper hoặc whiteboard); không dùng marker-paper cho kể chuyện dài (đó là one-line hoặc ipad-sketch).
- Không dùng nhóm này cho phim cần hình ảnh sắc nét kiểu vector/photoreal: nét run, rung tay, overshoot là một phần của style — làm "sạch" chúng là giết style.

## Nguyên lý cốt lõi

1. **Nét xuất hiện đúng thứ tự tay viết.** Nét vẽ là một hành động có thời gian: bắt đầu, đi, kết thúc. Người xem thấy ý tưởng được vẽ ra, không phải hiện ra.
2. **Tốc độ bút là nhịp phim.** Nét dài vẽ chậm, nét ngắn vẽ nhanh; pause giữa các nét là nhịp thở của bài giảng. Đừng tua nhanh bút để "tiết kiệm thời gian" — bút chính là nhịp.
3. **Một màu, một nghĩa.** Mỗi màu bút/phấn/marker có một nghĩa cố định trong cả phim (đen = dựng hình, xanh = dữ kiện, đỏ = đáp án/ẩn số). Đừng đổi nghĩa giữa chừng.
4. **Giấy/bảng là mặt phẳng làm việc.** Không tô tới mép; để lề cho chữ; trang là đơn vị tổ chức (một tờ = một ý; lật trang = đổi ý).
5. **Bút dẫn camera.** Camera đi theo ngòi bút, không đi theo kịch bản riêng. Khi bút dừng, camera dừng; khi bút chuyển trang, camera chuyển theo.

## Bảy style trong nhóm

### 1. One-Line Drawing — một nét liền

- **Bản chất:** toàn bộ phim là **một nét liền không nhấc bút** vẽ nên thế giới: một đường mực duy nhất uốn lượn thành nhân vật, vật, cảnh, chữ. Nét là câu chuyện — nó đi đâu, câu chuyện đi đó. Không có nét thứ hai, không có màu tô (trừ tối đa một accent, dùng một lần duy nhất).
- **Vật liệu:** giấy ấm (~`#f4efe4`), mực gần đen (~`#1d1a17`), một nét duy nhất bề rộng gần như đều, rung tay nhẹ. Áp lực nét theo tốc độ: chậm = đậm, nhanh = nhạt (`0.66 + 0.8·exp(−v/300)` — càng chậm càng đậm). Nét không bao giờ đứt; khi cần "nhấc bút", nét đi vòng qua mép trang hoặc cuộn thành xoắn ốc rồi tiếp tục.
- **Màu:** giấy + mực + tối đa **một accent** (đỏ, xanh, vàng — chọn một), dùng **một lần duy nhất** cho khoảnh khắc quan trọng nhất của phim (vd: vật chính xuất hiện, đáp án hiện ra). Accent không bao giờ xuất hiện hai lần.
- **Chữ:** phụ đề là chữ viết tay (vd Caveat), viết dọc theo nét (chữ là một phần của nét liền — nét viết chữ rồi tiếp tục đi). Tiêu đề cũng là nét viết. Không dùng font in cho chữ chính; chữ in chỉ cho credit nhỏ.
- **Nhịp:** 24 fps; nét vẽ với tốc độ thay đổi theo ý nghĩa (chậm ở chi tiết quan trọng, nhanh ở đoạn chuyển). Camera bám ngòi bút với lag −0,55…+0,4 s (camera đi sau bút một chút, như mắt người xem đuổi theo tay vẽ). Pause giữa các đoạn nét là nhịp thở.
- **Camera:** camera đi theo ngòi bút trên một trang lớn; từ điển: follow sát ngòi bút (câu chuyện đang được vẽ), pull-back về toàn trang (xem toàn bộ nét đã vẽ), push-in vào chi tiết (nét đang vẽ chi tiết), tilt theo hướng nét đi. Không cắt giữa chừng khi nét đang đi — cắt chỉ khi nét dừng ở một điểm nghỉ.
- **Âm thanh:** tiếng bút trên giấy (noise band-pass theo tốc độ nét: nhanh = cao, chậm = trầm), nhạc acoustic nhẹ (guitar nylon, piano felt, sáo), im lặng ở pause. Giọng kể (nếu có) đi cùng tốc độ nét — nói chậm khi nét chậm. −14 LUFS.
- **Chiêu đặc trưng:** nét không nhấc bút (đi vòng, cuộn xoắn, qua mép trang để tiếp tục); accent một lần duy nhất; nét viết chữ; pull-back cuối phim để thấy toàn bộ một nét đã vẽ thành gì.
- **Cạm bẫy:** nét đứt giữa chừng (đọc như lỗi render, không phải style); accent dùng hai lần (mất ý nghĩa); camera đi trước bút (người xem thấy chỗ trống trước khi nét tới); nét vẽ quá nhanh ở chi tiết quan trọng (người xem không kịp đọc).

### 2. Whiteboard — bảng trắng marker

- **Bản chất:** giải thích trên một **bảng trắng lớn** (vd 8000×4500) bằng marker, với nam châm và cục tẩy tự di chuyển như có tay vô hình. Không có tay người trong khung hình — bút, nam châm, cục tẩy tự di chuyển. Bảng là mặt phẳng làm việc vô hạn: camera đi trên bảng, nội dung cũ trượt ra ngoài khung khi nội dung mới tới.
- **Vật liệu:** bảng trắng sạch, hơi bóng (sheen 10–16% chạy 0,35× camera — ánh bóng di chuyển chậm hơn camera, tạo cảm giác bề mặt thật). Marker: nét đậm, đều, hơi rung; đầu bút tròn. **Ghost mark 5–10%**: vết marker cũ đã xóa vẫn còn mờ trên bảng (như bảng thật đã dùng) — không bao giờ bảng trắng tinh hoàn toàn. Nam châm tròn nhỏ giữ giấy ghi chú; cục tẩy tự di chuyển xóa nội dung cũ.
- **Màu:** tối đa **3 màu marker**, mỗi màu một nghĩa cố định trong cả phim. Ví dụ: đen `#23262c` = dựng hình/chữ chính; xanh `#2a5cb3` = dữ kiện/nhấn mạnh; cam `#d97757` = đáp án/cảnh báo. Không thêm màu thứ tư. Màu không bao giờ đổi nghĩa giữa chừng.
- **Chữ:** font single-line (vd EMS Tech — font vẽ bằng một nét duy nhất, như chữ viết bằng bút marker thật), viết trái → phải với tốc độ bút thật. Tiêu đề lớn, rõ; ghi chú nhỏ hơn. Chữ viết xong đứng yên; không sôi.
- **Nhịp:** nét vẽ với tốc độ bút thật (chữ lớn chậm hơn chữ nhỏ); pause giữa các ý. Nam châm/cục tẩy di chuyển với easing mượt. Camera đi theo bút. Không tua nhanh bút.
- **Camera:** camera đi trên bảng lớn; từ điển: follow bút (đang viết), pull-back (xem toàn bộ bảng), push-in (chi tiết), pan sang vùng bảng mới (ý mới), giữ khung khi bút đang viết. Bảng cũ trượt ra ngoài khung khi ý mới tới; cục tẩy xóa nội dung cũ trước khi viết mới lên cùng chỗ.
- **Âm thanh:** tiếng marker trên bảng (squeak nhẹ theo tốc độ nét), tiếng nam châm "tock", tiếng cục tẩy xoa, nhạc nền nhẹ (piano/guitar), giọng giảng đi cùng tốc độ viết. −14 LUFS.
- **Chiêu đặc trưng:** nam châm/cục tẩy tự di chuyển (bảng có "tay vô hình"); ghost mark (bảng đã dùng); bảng vô hạn (camera đi mãi, nội dung cũ trượt ra); bút dẫn camera.
- **Cạm bẫy:** bảng trắng tinh hoàn toàn (đọc như slide, không phải bảng); quá 3 màu (mất kỷ luật); tay người xuất hiện (phá ảo giác "tự vẽ"); chữ hiện bằng fade thay vì viết; camera đi trước bút.

### 3. Chalkboard — bảng phấn

- **Bản chất:** giảng bài kiểu lớp học cổ điển trên **bảng phấn xanh đậm, sạch** (không vết phấn cũ — bảng mới lau). Phấn trắng là chính, thêm một phấn nhấn và một phấn nhạt (tay thứ hai). Nhịp phim là **viết — xóa — viết lại tại chỗ**: ý cũ bị xóa để nhường chỗ cho ý mới trên cùng một bảng. Panel trượt sang ngang để đổi bảng.
- **Vật liệu:** bảng xanh mực đậm, bề mặt hơi nhám; phấn trắng phủ ~90%, hạt phấn mịn; nét phấn có độ dày thay đổi theo áp lực; xóa để lại vệt phấn mờ nhẹ (không sạch hoàn toàn). **Chữ Hoa là stroke data tự viết** (không dùng outline font — chữ Hoa phải là nét phấn vẽ tay, không phải font chữ in).
- **Màu:** trắng (phấn chính) + **một phấn nhấn** (vàng hoặc cam, cho đáp án/điểm quan trọng) + **một phấn nhạt** (xanh nhạt hoặc hồng nhạt, cho ghi chú phụ/tay thứ hai). Không thêm màu.
- **Chữ:** chữ viết tay bằng phấn, viết với tốc độ ~0,1 s/nét (chữ lớn); chữ Hoa là stroke data tự viết. Tiêu đề phấn lớn; công thức/thông tin viết từng dòng. Chữ viết xong đứng yên.
- **Nhịp:** 30 fps; viết — xóa — viết lại là nhịp chính. Xóa là một hành động có thời gian (không snap). Panel trượt sang ngang với easing mượt khi đổi bảng. Pause giữa các ý.
- **Camera:** camera khóa trên bảng; từ điển: khóa bảng (đang viết), push-in (chi tiết/công thức), panel trượt (đổi bảng), pull-back (toàn bảng). Không di chuyển camera nhiều — bảng là sân khấu, nội dung thay đổi trên bảng.
- **Âm thanh:** tiếng phấn trên bảng (scratch khô, theo tốc độ nét), tiếng xóa (xoa bảng), nhạc nền cổ điển nhẹ (piano, dây), giọng giảng. Mix ~−16 LUFS trước mastering (để headroom cho tiếng phấn). −14 LUFS sau mastering.
- **Chiêu đặc trưng:** viết — xóa — viết lại tại chỗ (ý cũ nhường chỗ cho ý mới); panel trượt (đổi bảng); phấn nhấn cho đáp án; chữ Hoa stroke data.
- **Cạm bẫy:** bảng có vết phấn cũ (đọc như bảng bẩn, không phải bảng mới); dùng outline font cho chữ Hoa (mất cảm giác phấn); xóa snap (không có hành động xóa); quá 3 màu phấn.

### 4. Sketchnote — ghi chú vẽ tay

- **Bản chất:** tóm tắt một buổi nói chuyện/bài giảng thành **một trang sketchnote**: giấy chấm lưới, fineliner đen + marker xám + một màu vàng nhấn, bố cục dàn như poster (tiêu đề lớn, các ý xếp thành khối, mũi tên nối ý, icon vẽ tay). Trang là đơn vị tổ chức: một trang = một buổi/một chủ đề.
- **Vật liệu:** giấy chấm lưới: pitch 26 px, chấm 1,3 px, giấy `#fbfaf6`, mực `#1e1e22`. Fineliner đen vẽ khung, chữ, icon; marker xám 3 độ (nhạt, vừa, đậm) tô bóng và phân cấp; **một vàng** `rgba(255,205,40,.80)` làm highlight duy nhất (tô dưới chữ quan trọng, khoanh ý chính). Chỉ **wobble fineliner boil** (chu kỳ 2 frame, 3 bản vẽ luân phiên) — marker và giấy không sôi.
- **Màu:** giấy + mực đen + xám 3 độ + **một vàng duy nhất**. Không thêm màu. Vàng chỉ cho highlight, không tô hình.
- **Chữ:** font viết tay cho tiêu đề và ghi chú (vd Kalam Bold cho tiêu đề, Patrick Hand cho ghi chú). Chữ viết tay, không font in. Tiêu đề lớn, đậm; ghi chú nhỏ, rõ; nhãn ngắn. Chữ viết theo thứ tự tay viết.
- **Nhịp:** trang dàn dần: tiêu đề trước, rồi từng khối ý xuất hiện theo thứ tự nói; mũi tên nối ý mọc sau. Pause giữa các khối. Trang hoàn thành thì giữ một lúc để người xem đọc toàn trang, rồi lật sang trang mới.
- **Camera:** camera trên trang lớn; từ điển: khóa toàn trang (xem bố cục), push-in vào khối ý đang được viết, pull-back về toàn trang (đọc tổng thể), pan sang khối ý mới. Không cắt giữa chừng khi đang viết một khối.
- **Âm thanh:** tiếng bút fineliner trên giấy (scratch nhẹ), tiếng marker (swish), nhạc nền nhẹ, giọng kể/tóm tắt (nếu có) đi cùng thứ tự khối ý. −14 LUFS.
- **Chiêu đặc trưng:** trang dàn như poster (bố cục là một phần của thông điệp); vàng highlight duy nhất; mũi tên nối ý; icon vẽ tay thay cho chữ dài; lật trang = đổi chủ đề.
- **Cạm bẫy:** quá nhiều chữ (sketchnote thành slide text); vàng dùng để tô hình (mất ý nghĩa highlight); bố cục lộn xộn không có thứ tự đọc; font in thay cho chữ viết tay.

### 5. Stick Explainer — người que giải thích

- **Bản chất:** minh họa quy trình/khái niệm bằng **người que**: đầu tròn + thân một nét cong liền mạch, một độ dày nét (~8 px với nhân vật cao 380 px), chuyển động mượt 60 fps với vật lý lò xo giảm chấn. Người que là diễn viên — nó đi, chạy, nhảy, đẩy, kéo, chỉ, ngã, đứng dậy. Mọi thứ khác (vật, chữ, mũi tên) cũng vẽ bằng cùng một nét.
- **Vật liệu:** giấy `#f3f0ea`, mực `#24242c`, accent `#eb4a2a` (đỏ cam, cho vật chính/điểm nhấn). Nét người que: đầu tròn, thân một nét cong liền mạch (không gấp khúc), tay nắm thành một đường cong tiếp tuyến liên tục (tay không bao giờ là đoạn thẳng rời). Một độ dày nét cho mọi thứ trong phim.
- **Màu:** giấy + mực + **một accent đỏ cam duy nhất**. Accent cho vật chính, điểm nhấn, hoặc trạng thái quan trọng. Không thêm màu.
- **Chữ:** font hình học rõ ràng (vd Jost), viết/vẽ theo nét. Tiêu đề và nhãn ngắn, rõ. Chữ không sôi; chữ hiện bằng cách viết hoặc pop nhẹ trên beat.
- **Nhịp:** 60 fps mượt; vật lý **lò xo giảm chấn** cho mọi chuyển động (người que nghiêng, bật, dừng có overshoot nhẹ rồi ổn định). Diễn xuất bằng thay thế tư thế theo nhịp; hành động đáp trên beat nhạc. Anticipation → hành động → follow-through.
- **Camera:** camera đi theo người que; từ điển: follow ngang (người que đi/chạy), push-in (chi tiết/hành động), pull-back (toàn cảnh), khóa khung (người que diễn trong khung). Camera mượt, không rung.
- **Âm thanh:** tiếng bước chân/bật nhảy (thump nhẹ theo nhịp lò xo), nhạc nền vui, nhịp rõ (để hành động đáp trên beat), giọng kể (nếu có) đi cùng hành động. −14 LUFS.
- **Chiêu đặc trưng:** thân một nét cong liền mạch (không gấp khúc); tay nắm là đường cong tiếp tuyến; lò xo giảm chấn (overshoot nhẹ); người que là diễn viên (đi, chạy, nhảy, đẩy, kéo, ngã, đứng dậy).
- **Cạm bẫy:** thân gấp khúc (đọc như que diêm, không phải người que); tay là đoạn thẳng rời (mất liền mạch); chuyển động không có lò xo (đọc như robot); quá nhiều chi tiết trên người que (mất tối giản).

### 6. iPad Sketch — vẽ số trên iPad

- **Bản chất:** vẽ minh họa trên **một trang giấy số** (iPad): nét chì trước, màu tô sau **lệch khỏi nét** 5–12 đơn vị canvas xuống-phải (như tô màu bằng tay, không khớp hoàn toàn với nét). Chỉ có bút stylus trong khung hình — không có tay người. Trang giấy số là mặt phẳng làm việc; camera đi trên trang.
- **Vật liệu:** giấy số `#f3eadb`, graphite `#43362e` (nét chì), coral `#dc6a4c` (màu chính), mustard `#f1c04f` (màu phụ). Nét chì: mỏng, hơi rung, như chì thật; màu tô: mảng màu phẳng, lệch khỏi nét 5–12 đơn vị xuống-phải, mép hơi nhám. **Đổi màu bằng re-register block**: khi đổi màu, một khối màu mới được đăng ký lại (không phải tô đè lên màu cũ).
- **Màu:** giấy + graphite + coral + mustard. Tối đa 2 màu tô (+ graphite). Không thêm màu. **Dải swatch** ghi từng trạng thái màu đã dùng (như palette trên trang).
- **Chữ:** chữ viết tay trên trang (bằng stylus), viết trái → phải. Tiêu đề và ghi chú bằng chữ viết tay. Không font in.
- **Nhịp:** 24 fps; nét chì vẽ trước (chậm, cẩn thận), màu tô sau (nhanh hơn, mảng lớn). Pause giữa các bước. Bút stylus di chuyển mượt, có easing.
- **Camera:** camera trên trang giấy số; từ điển: follow stylus (đang vẽ), push-in (chi tiết), pull-back (toàn trang), pan sang vùng mới. Không cắt giữa chừng khi stylus đang vẽ.
- **Âm thanh:** tiếng stylus trên màn hình (tap/scratch nhẹ), tiếng tô màu (swish), nhạc nền nhẹ, giọng kể (nếu có). −14 LUFS.
- **Chiêu đặc trưng:** nét chì trước, màu tô sau lệch khỏi nét (tô tay không khớp); re-register block khi đổi màu; dải swatch ghi trạng thái; chỉ có stylus, không tay.
- **Cạm bẫy:** màu tô khớp hoàn toàn với nét (đọc như vector fill, không phải tô tay); tay người xuất hiện; đổi màu bằng tô đè (mất re-register); quá 2 màu tô.

### 7. Marker Paper — marker trên giấy

- **Bản chất:** giải một bài toán/bài tập trên **giấy trắng** bằng marker đầu tròn dày: đen dựng hình, xanh là dữ kiện cho trước, đỏ là ẩn số/đáp án (đỏ luôn là nét cuối cùng). **Một câu hỏi mỗi tờ** — hết một tờ là hết một bài. Chuyển cảnh bằng push-through (đẩy tờ cũ ra) và peel (bóc tờ).
- **Vật liệu:** giấy `#faf9f5`, marker đầu tròn dày 6–10 px, nét đậm, đều, hơi rung. Vẽ theo twos 12 fps (mỗi bức vẽ giữ 2 frame — cảm giác vẽ tay, không mượt như vector). Giấy là tờ riêng lẻ, có mép; tờ cũ được bóc/đẩy ra khi sang bài mới.
- **Màu:** đen `#1b1c20` = dựng hình (vẽ hình, trục, khung); xanh `#2456d6` = dữ kiện cho trước (số đã biết, điều kiện); đỏ `#e23b2e` = ẩn số/đáp án (câu hỏi, kết quả). **Đỏ luôn là nét cuối cùng** trong mỗi tờ — đáp án xuất hiện cuối cùng, bằng đỏ. Không thêm màu. Màu không bao giờ đổi nghĩa.
- **Chữ:** chữ viết tay bằng marker, viết trái → phải với tốc độ bút thật. Số và công thức viết bằng marker đen (dữ kiện) hoặc đỏ (đáp án). Chữ lớn, rõ, đọc được từ xa.
- **Nhịp:** vẽ theo twos 12 fps; nét vẽ với tốc độ bút thật; pause giữa các bước giải. Đáp án đỏ xuất hiện cuối cùng, có pause trước đó để người xem tự nghĩ. Chuyển tờ bằng push-through/peel với easing.
- **Camera:** camera khóa trên tờ giấy; từ điển: khóa tờ (đang giải), push-in (chi tiết/công thức), pull-back (toàn tờ), push-through/peel (sang tờ mới). Không di chuyển camera nhiều — tờ giấy là sân khấu.
- **Âm thanh:** tiếng marker trên giấy (squeak/swish theo tốc độ nét), tiếng bóc giấy (peel), nhạc nền nhẹ, giọng giảng đi cùng bước giải. −14 LUFS.
- **Chiêu đặc trưng:** đỏ luôn là nét cuối (đáp án xuất hiện cuối cùng); một câu hỏi mỗi tờ; push-through và peel (bóc tờ sang bài mới); vẽ theo twos 12 fps.
- **Cạm bẫy:** đỏ xuất hiện giữa chừng (mất ý nghĩa "đáp án cuối"); nhiều câu hỏi trên một tờ (mất tổ chức); chữ hiện bằng fade thay vì viết; màu đổi nghĩa giữa chừng.

## Hệ màu / bảng chất liệu bất biến (tóm tắt theo style)

| Style | Giấy & bút | Màu (bất biến) | Nhịp vẽ |
|---|---|---|---|
| one-line | Giấy `#f4efe4`, mực `#1d1a17`, một nét liền | Tối đa 1 accent, dùng 1 lần | 24 fps, camera bám bút lag −0,55…+0,4 s |
| whiteboard | Bảng 8000×4500, marker, ghost mark 5–10% | Tối đa 3 màu, mỗi màu một nghĩa | Tốc độ bút thật, camera theo bút |
| chalkboard | Bảng xanh đậm sạch, phấn trắng + 1 nhấn + 1 nhạt | Trắng + 1 nhấn + 1 nhạt | 30 fps, viết–xóa–viết lại, ~0,1 s/nét |
| sketchnote | Giấy chấm lưới 26 px, fineliner + marker xám | Đen + xám 3 độ + 1 vàng `rgba(255,205,40,.80)` | Khối ý xuất hiện theo thứ tự nói |
| stick-explainer | Giấy `#f3f0ea`, mực `#24242c`, nét ~8 px | Mực + accent `#eb4a2a` duy nhất | 60 fps, lò xo giảm chấn |
| ipad-sketch | Giấy số `#f3eadb`, graphite `#43362e` | Graphite + coral `#dc6a4c` + mustard `#f1c04f` | 24 fps, chì trước màu sau lệch 5–12 đv |
| marker-paper | Giấy `#faf9f5`, marker 6–10 px | Đen `#1b1c20` + xanh `#2456d6` + đỏ `#e23b2e` (đỏ cuối) | Vẽ theo twos 12 fps |

## Quy trình sản xuất

1. **Chốt brief trước.** Chủ đề, câu hỏi/bài toán (nếu có), bảng màu theo nghĩa (mỗi style có quy tắc màu riêng — chọn từ brief, không lấy màu của demo gốc). Hỏi user có tư liệu tham chiếu của mình không (bài toán, bài giảng, sơ đồ cần giải thích).
2. **Treatment ngắn trước khi dựng:** chọn 1 style (không trộn 2 style trong một phim trừ khi brief yêu cầu rõ và có điểm chuyển), chọn 3 chiêu đặc trưng sẽ dùng (xem từng style), mỗi chiêu: nó nói ý gì, xuất hiện khi nào. Một phim 20–60 s thường dùng 2–4 chiêu. Với marker-paper/chalkboard: liệt kê trước các bước giải/viết theo thứ tự.
3. **Look test trước:** render frame tĩnh/đoạn ngắn bằng đúng cách vẽ của style (nét liền, marker, phấn, fineliner, người que, stylus) và đối chiếu với `STYLE.md` gốc: nét có đúng vật lý không (rung tay, overshoot, ghost mark, lệch màu tô), chữ có đọc được không.
4. **Timeline là nguồn sự thật duy nhất:** một bảng beat (mốc giây → nét nào được vẽ → sự kiện âm) mà hình, phụ đề, nhạc, mix đều đọc từ đó. Nhịp bút và cue âm lệch nhau là lỗi, không phải "cảm tính".
5. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi nét vẽ là hàm của `t` với seed cố định; nét xuất hiện đúng thứ tự tay viết; chữ viết/vẽ theo đúng thứ tự tay.
6. **Render thử các frame hero của từng beat** → contact sheet soát: nét vẽ, độ đọc của chữ, bố cục giấy/bảng, trước khi render full.
7. **Âm thanh theo bảng âm của style** (xem từng style), mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng (chung cho nhóm)

- Nét xuất hiện bằng cách được vẽ (draw-on theo thứ tự tay), không fade-in, không pop-in (trừ stick-explainer pop nhẹ trên beat và chữ viết tay).
- Một màu, một nghĩa — không đổi nghĩa màu giữa chừng; không thêm màu ngoài quy tắc của style.
- Một tờ/bảng = một ý; lật trang/bóc tờ/panel trượt = đổi ý. Không nhồi nhiều ý lên một tờ.
- Chữ bắt buộc đọc giữ ≥ 1,8 s (hoặc ≥ câu nói + 0,6 s); công thức đọc chung: CJK ÷ 4,5 + Latin ÷ 15 + 1,5 s tính từ lúc khối chữ hoàn chỉnh.
- Bút dẫn camera: camera đi theo ngòi bút; khi bút dừng, camera dừng. Không để camera đi trước bút.
- Số liệu (nếu có) phải thật và có nguồn ghi lại; không bịa số trong bài giải.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; mọi jitter/rung tay phải suy từ seed cố định theo index của nét), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Seed và sôi:** mọi nét có seed cố định; random chỉ được tiêu thụ cùng một cách ở mọi tiến độ (nét vẽ dở và nét vẽ xong là cùng một nét). Chỉ phần style cho phép mới sôi (sketchnote: wobble fineliner boil chu kỳ 2 frame, 3 bản; one-line: rung nét; marker-paper: vẽ theo twos 12 fps) và sôi theo chu kỳ cố định.
- **Nét vẽ theo thời gian:** mỗi nét có thời gian vẽ trên mỗi pixel (bake vào texture) để shader phát lại thứ tự nét; nét xuất hiện dọc chiều dài, không hiện nguyên nét cùng lúc.
- **Giấy/bảng neo vào thế giới:** texture giấy/bảng neo vào trang (world space), pan/zoom cùng camera; không bao giờ cố định theo màn hình.
- **Chữ viết:** chữ hiện bằng cách viết dọc skeleton glyph hoặc stroke-by-stroke (không wipe, không fade); chữ Hoa (chalkboard) là stroke data tự viết, không dùng outline font.
- **Cache:** nội dung đã viết xong cache thành sprite/texture; chỉ vẽ stroke-by-stroke thứ đang được viết.
- **Âm thanh:** master −14 LUFS, true peak ≤ −1 dBTP; giọng đọc kiểm tra bằng ASR trên giọng sạch và trên phim hoàn chỉnh. Chalkboard: mix ~−16 LUFS trước mastering.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1280×720 hoặc 1920×1080, 30 fps; stick-explainer 60 fps nếu brief chốt; chalkboard 30 fps), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) nét vẽ đúng vật lý của style (rung tay, overshoot, ghost mark, lệch màu tô, lò xo); (b) chữ đọc được, đủ thời gian đọc, không bị nét vẽ cắt ngang; (c) bố cục giấy/bảng đủ lề (không viết tới mép); (d) màu đúng nghĩa của style (không thêm màu, không đổi nghĩa).
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn, nhãn nằm trên vùng giấy/bảng trống, không đè lên chủ thể.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Bản quyền: ghi rõ nguồn tham chiếu/hình ảnh trong QA.md; không dùng artwork, tên phim demo, nhân vật hay nhãn hiệu thật của repo gốc.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: nguồn tham chiếu, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.

## Phân biệt với các nhóm skill opuscar khác

- `opuscar-painting-illustration`: cũng vẽ tay, nhưng là **hội họa** (chất liệu sơn/sáp/màu nước là nhân vật chính, kể chuyện bằng tranh) — nhóm này là **giải thích** (ý tưởng là nhân vật chính, nét vẽ là cách ý tưởng hiện ra).
- `opuscar-edit-documentary`: sắp xếp tư liệu thật, không vẽ ra thế giới — ngược với nhóm này.
- `opuscar-traditional-crafts`: vật liệu thủ công truyền thống (thủy mặc, rối bóng, tranh khắc) với chuyển động cứng theo mảnh/lớp — nhóm này là bút/phấn/marker hiện đại trên bảng/giấy.
- `opuscar-printmaking`: in ấn là luật (bản in riêng, halftone, lệch đăng ký) — hình là bản in; nhóm này hình là nét vẽ trực tiếp.
- Các nhóm còn lại (graphic & type, line diagrams, cartoons, games, film & tape, screens & interfaces, light & lines, 3D & miniature, instruments & evidence, data & maps): khi brief nói "giải thích bằng cách vẽ ra trên bảng/giấy" thì nhóm này là đáp án.
