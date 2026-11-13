---
name: opuscar-printmaking
description: Kỹ thuật phim in ấn (spin-out từ bộ Lemo-Opuscar) — risograph, hồ sơ halftone, khắc gỗ, khắc đồng, lụa poster, long-take khắc bản, pop-art, collage cổ. Dùng khi brief là "phim trông như in riso", "hồ sơ điều tra bằng chấm halftone", "khắc gỗ kể chuyện", "khắc đồng minh họa", "poster lụa", "một cú máy dài khắc bản", "pop-art", hoặc "collage giấy cũ". Mọi nội dung (chủ đề, câu chuyện, bảng màu) do brief quyết định — skill chỉ giữ vật lý in ấn và kỷ luật dựng.
---

# Opuscar Print & Printmaking — In ấn

Mỗi style trong nhóm là một **quy trình in** được dựng lại thành máy làm phim: bản in riêng (plate), chấm halftone, lệch đăng ký, dao khắc, mực đục, chấm Ben-Day, giấy cắt dán. Điểm chung: **hình là bản in** — không phải nét vẽ trực tiếp, không phải ảnh thật. Màu đến từ bản in (spot color), không phải từ blend pixel. Lệch đăng ký và hạt in là chữ ký, không phải lỗi.

Kỹ thuật chưng cất từ Lemo-Opuscar by Lemomo (LemoLab) — https://github.com/lemomo-ai/lemo-opuscar. Code gốc MIT, tài liệu gốc CC BY-NC 4.0; phim do mình làm ra thuộc về mình. Xem `LICENSE` và `LICENSE-MIT.txt` trong thư mục skill này.

Nguồn kỹ thuật: các style `risograph`, `halftone-dossier`, `woodcut`, `engraving`, `silkscreen-poster`, `printed-long-take`, `pop-art`, `vintage-collage` trong repo Lemo-Opuscar — đọc `STYLE.md` gốc để tra chi tiết thông số khi cần, không sao chép câu chữ, không dùng lại câu chuyện, tên phim demo, nhân vật hay nhãn hiệu thật trong demo của repo.

## Khi nào dùng

- Phim trông như **in riso**: 2–3 mực spot, overprint multiply, lệch đăng ký, halftone (risograph).
- **Hồ sơ điều tra** bằng chấm halftone, tem, dấu đóng (halftone-dossier).
- Kể chuyện bằng **khắc gỗ**: đen là gỗ, trắng là dao gọt (woodcut).
- Minh họa bằng **khắc đồng**: tông màu chỉ bằng đường kẻ (engraving).
- **Poster lụa**: mực đục, ≤6 màu, reveal bằng squeegee (silkscreen-poster).
- **Một cú máy dài** liên tục trong thế giới khắc bản (printed-long-take).
- **Pop-art**: 4 bản đỏ/vàng/xanh/key đen, chấm Ben-Day (pop-art).
- **Collage giấy cũ**: cut-out có viền giấy trắng rách, data engraving (vintage-collage).

## Khi nào KHÔNG dùng

- Không dùng nhóm này cho phim hội họa (sáp, màu nước, sơn dầu — đó là `opuscar-painting-illustration`), cho phim giải thích bằng bảng trắng/marker (`opuscar-sketch-board`), hay cho phim tư liệu thật (`opuscar-edit-documentary`).
- Không dùng nhóm này cho phim cần chuyển động mượt kiểu 3D/photoreal: hình là bản in — chuyển động là bản in di chuyển, lật, bóc, đóng dấu, không phải vật 3D mềm.
- Không dùng risograph cho poster cần màu chính xác (đó là silkscreen-poster); không dùng woodcut cho minh họa cần đường kẻ tinh tế (đó là engraving); không dùng pop-art cho chuyện cần trầm lặng (đó là woodcut hoặc engraving).
- Không dùng nhóm này khi brief cần hình ảnh sắc nét kiểu vector: chấm halftone, lệch đăng ký, hạt in là một phần của style — làm "sạch" chúng là giết style.

## Nguyên lý cốt lõi

1. **Hình là bản in.** Mỗi màu là một bản in riêng (plate); hình được tạo bằng cách in các bản chồng lên nhau, không phải vẽ trực tiếp. Bản in là diễn biến truyện (mỗi bản in là một bước trong câu chuyện).
2. **Màu spot, không blend pixel.** Màu đến từ mực spot (2–3 mực riso, ≤6 mực lụa, 4 bản pop-art). Overprint (chồng mực) bằng multiply, không phải blend màu trong Photoshop. Gradient cấm — thay bằng dải bậc thang hoặc chấm halftone.
3. **Lệch đăng ký là chữ ký.** Mỗi bản in lệch 1–3 px khỏi bản khác (như in tay không khớp hoàn toàn). Lệch là một phần của style, không phải lỗi cần sửa.
4. **Chấm halftone là ngôn ngữ.** Tông màu (sáng/tối) được tạo bằng chấm (halftone, Ben-Day), không phải bằng màu xám. Kích thước chấm = độ tối; góc screen khác nhau cho mỗi màu.
5. **Giấy là nền.** Giấy (kem, trắng ngà, washi) là nền và là sáng. Không bao giờ tô trắng lên trên.

## Tám style trong nhóm

### 1. Risograph — in riso

- **Bản chất:** phim trông như **in riso** (máy in stencil Nhật): 2–3 mực spot, overprint multiply (mực chồng lên nhau tối dần), lệch đăng ký ±1–3 px, halftone chu kỳ 6–8 px, góc screen cách nhau ≥15° (mỗi màu một góc screen khác nhau để không tạo moiré). **Các bản in (plate) làm diễn biến truyện**: mỗi bản in là một bước trong câu chuyện (bản 1 in nền, bản 2 in nhân vật, bản 3 in chi tiết — câu chuyện tiến triển qua các lần in).
- **Vật liệu:** giấy ~`#f4eee2` (giấy kem ấm); mực spot (mực riso thật, có hạt, không đều); halftone: chấm tròn, chu kỳ 6–8 px, góc screen mỗi màu cách nhau ≥15°. Overprint: mực chồng lên nhau bằng multiply (chỗ hai mực chồng tối hơn, tạo màu thứ ba).
- **Màu:** 2–3 mực spot. Ví dụ: Blue `#0078bf` + Yellow `#ffe800` + Fluorescent Pink `#ff48b0` (xanh + vàng + hồng huỳnh quang — ba mực tạo ra nhiều màu khi overprint). Không thêm mực thứ tư. Màu thứ ba (khi overprint) là màu "miễn phí" — dùng nó.
- **Chữ:** chữ in (font in, không viết tay), chữ lớn, đậm; tiêu đề là chữ in riso (có hạt, lệch đăng ký nhẹ). Phụ đề (nếu có) trên giấy, font in.
- **Nhịp:** nhân vật 12 fps (chuyển động cứng, như in động); bản in hiện lần lượt (mỗi bản in là một beat). Camera mượt.
- **Camera:** camera trên tờ giấy in; từ điển: khóa tờ (đang in từng bản), push-in (chi tiết halftone), pull-back (toàn tờ), pan (sang bản in mới). Không cắt giữa chừng khi đang in một bản.
- **Âm thanh:** tiếng máy in riso (quay, in, giấy chạy), tiếng bản in ấn xuống, nhạc nền nhẹ (indie, lo-fi), giọng kể (nếu có). −14 LUFS.
- **Chiêu đặc trưng:** bản in làm diễn biến truyện (mỗi plate là một bước); overprint multiply (mực chồng tạo màu thứ ba); lệch đăng ký ±1–3 px; halftone 6–8 px, góc screen ≥15°.
- **Cạm bẫy:** quá 3 mực (mất riso); các bản khớp hoàn toàn (mất lệch đăng ký); gradient mượt bằng blend (không phải halftone); góc screen quá gần nhau (tạo moiré).

### 2. Halftone Dossier — hồ sơ halftone

- **Bản chất:** **hồ sơ điều tra** bằng chấm halftone: giấy kem, chấm halftone lớn (step 20–26 px), mực tối + 4–5 mực spot, tem (stamp), dấu đóng (stamp slam), dot wipe (chấm xóa). Phim là một hồ sơ đang được mở ra: tài liệu, ảnh, tem, dấu — mỗi thứ là một bằng chứng.
- **Vật liệu:** giấy kem; chấm halftone: step 20–26 px (chấm lớn, thấy rõ), k 0,6–0,72 (hệ số chấm); mực tối (đen/nâu đậm) + 4–5 mực spot (đỏ, xanh, vàng, xanh lá, tím — chọn theo hồ sơ). Tem: tem giấy (có răng cưa, có chữ); dấu đóng: dấu tròn/vuông đóng lên giấy.
- **Màu:** mực tối + 4–5 mực spot. Màu spot cho tem, dấu, highlight. Không thêm màu.
- **Chữ:** chữ đánh máy (typewriter) hoặc chữ in hồ sơ; tiêu đề là chữ hồ sơ lớn; nhãn tài liệu là chữ đánh máy. Phụ đề (nếu có) trên giấy hồ sơ.
- **Nhịp:** line boil ~10 fps (nét rung nhẹ, như phim cũ); **dot wipe 0,44 s** (chấm halftone xóa cảnh cũ trong 0,44 s — chuyển cảnh bằng chấm); **stamp slam 0,09 s từ 2,6×** (dấu đóng xuống trong 0,09 s, từ kích thước 2,6× thu về 1× — dấu đập xuống giấy). Nhịp phim là nhịp mở hồ sơ.
- **Camera:** camera trên hồ sơ; từ điển: khóa hồ sơ (đang xem tài liệu), push-in (chi tiết tem/dấu), pull-back (toàn hồ sơ), pan (sang tài liệu mới). Không cắt giữa chừng khi dấu đang đóng.
- **Âm thanh:** tiếng giấy (lật hồ sơ), tiếng tem (dán), tiếng dấu đóng (slam — thump mạnh), tiếng đánh máy (nếu có chữ đánh máy), nhạc trinh thám nhẹ (jazz, noir). −14 LUFS.
- **Chiêu đặc trưng:** dot wipe 0,44 s (chấm xóa cảnh); stamp slam 0,09 s từ 2,6× (dấu đập xuống); tem và dấu là bằng chứng; line boil ~10 fps.
- **Cạm bẫy:** chấm halftone quá nhỏ (mất cảm giác hồ sơ cũ); dấu đóng chậm (mất slam); quá nhiều mực spot (mất kỷ luật hồ sơ); chữ hiện bằng fade (phải đánh máy hoặc đóng dấu).

### 3. Woodcut — khắc gỗ

- **Bản chất:** kể chuyện bằng **khắc gỗ**: đen là gỗ (phần gỗ còn lại), trắng là dao gọt (phần gỗ bị gọt đi). Hình được tạo bằng cách gọt gỗ: chỗ nào gọt đi thì trắng, chỗ nào giữ lại thì đen. Dao khắc có 4 loại: knife 1,2–2 px (dao nhọn, nét mảnh), V-gouge 2–8 px (dao chữ V, nét vừa), U-gouge 10–22 px (dao chữ U, nét to), stab r 3–8 px (dao đâm, chấm tròn). Tối đa 1 bản màu, chỉ in lên phần trắng đã khắc.
- **Vật liệu:** gỗ (bản khắc gỗ); dao khắc 4 loại (xem trên); giấy (giấy in khắc gỗ, hơi vàng); mực đen (in từ bản gỗ). **Khối khắc bị soi gương**: bản khắc in ra giấy bị lật ngược (như in thật) — chữ và hình trên bản khắc phải vẽ ngược.
- **Màu:** đen (gỗ) + trắng (giấy, phần gọt) + tối đa **1 bản màu** (chỉ in lên phần trắng đã khắc — màu chỉ xuất hiện ở chỗ đã gọt, không tô lên gỗ đen). Không thêm màu.
- **Chữ:** chữ khắc gỗ (chữ là nét khắc, không phải font in); tiêu đề là chữ khắc lớn; phụ đề (nếu có) trên giấy.
- **Nhịp:** nhân vật 12 fps (chuyển động cứng, như khắc gỗ động); chuyển cảnh bằng **peel** (bóc giấy — tờ giấy in được bóc khỏi bản khắc để lộ hình mới). Nhịp phim là nhịp khắc và in.
- **Camera:** camera trên bản khắc/giấy in; từ điển: khóa bản (đang khắc), push-in (chi tiết dao khắc), pull-back (toàn bản), peel (bóc giấy sang hình mới). Không cắt giữa chừng khi đang khắc.
- **Âm thanh:** tiếng dao khắc gỗ (cạo, gọt), tiếng in (bản ấn xuống giấy), tiếng bóc giấy (peel), nhạc dân gian nhẹ. −14 LUFS.
- **Chiêu đặc trưng:** đen là gỗ, trắng là dao gọt; 4 loại dao khắc (knife, V-gouge, U-gouge, stab); 1 bản màu chỉ trên phần trắng đã khắc; peel (bóc giấy); khối khắc bị soi gương.
- **Cạm bẫy:** màu tô lên gỗ đen (mất luật); dao khắc không phân biệt loại (mất chi tiết); hình không bị soi gương (mất cảm giác in thật); quá 1 bản màu.

### 4. Engraving — khắc đồng

- **Bản chất:** minh họa bằng **khắc đồng** (engraving): tông màu **chỉ bằng đường kẻ** — không có màu xám, không có wash, chỉ có đường kẻ dày/mỏng, thưa/dày tạo ra sáng/tối. Đường kẻ là ngôn ngữ duy nhất. **Swell law**: `width × (0,2 + 0,8·sin(πu)^0,7)` — bề rộng đường kẻ thay đổi theo vị trí trên đường (đầu mỏng, giữa dày, cuối mỏng — như nét khắc bằng burin).
- **Vật liệu:** đồng (bản khắc đồng); burin (dao khắc đồng); giấy ~`#f1e8d2` (giấy kem); mực ~`#1c1510` (mực nâu đen). Đường kẻ: họ đường khác nhau cho tông khác nhau (ngưỡng đổi họ đường ~0,14 / 0,5 / 0,75 — từ sáng tới tối, đổi kiểu đường kẻ ở 3 ngưỡng).
- **Màu:** mực nâu đen `#1c1510` + giấy kem `#f1e8d2` + **tô màu tay bằng wash trong suốt** (tô màu nước trong lên trên bản khắc — màu nhạt, trong, không che đường kẻ). Màu wash chỉ là tint nhẹ, không phải màu chính.
- **Chữ:** chữ khắc đồng (chữ là nét khắc, tinh tế); tiêu đề là chữ khắc; phụ đề (nếu có) trên giấy.
- **Nhịp:** đường kẻ hiện stroke-by-stroke (như đang khắc); **roundel phóng đại** (hình tròn phóng đại chi tiết khắc — như kính lúp xem bản khắc); **proof** (bóc giấy — tờ proof được bóc khỏi bản đồng để xem hình). Nhịp phim là nhịp khắc.
- **Camera:** camera trên bản khắc; từ điển: khóa bản (đang khắc), push-in (chi tiết đường kẻ), roundel (phóng đại chi tiết), pull-back (toàn bản), proof (bóc giấy). Không cắt giữa chừng khi đang khắc một đường.
- **Âm thanh:** tiếng burin khắc đồng (scratch kim loại), tiếng in (bản ấn xuống giấy), tiếng bóc giấy (proof), nhạc cổ điển nhẹ. −14 LUFS.
- **Chiêu đặc trưng:** tông màu chỉ bằng đường kẻ (không xám, không wash); swell law (đường kẻ dày/mỏng theo vị trí); ngưỡng đổi họ đường 0,14/0,5/0,75; roundel phóng đại; proof (bóc giấy).
- **Cạm bẫy:** dùng màu xám/wash để tạo tông (mất engraving); đường kẻ đều nhau (mất swell); không đổi họ đường theo tông (mất chiều sâu); wash đục che đường kẻ.

### 5. Silkscreen Poster — poster lụa

- **Bản chất:** **poster lụa** (silkscreen): mực đục (opaque — mực lụa không trong, che hoàn toàn lớp dưới), ≤6 màu, lệch đăng ký 1–3 px, gradient cấm (thay bằng dải bậc thang — gradient mượt không in được bằng lụa, phải làm bằng các dải màu bậc thang). **Reveal bằng squeegee**: poster hiện ra khi cây gạt mực (squeegee) kéo qua — mực được gạt qua lưới lụa lên giấy. **Palette re-ink 0,35 s**: đổi bảng màu trong 0,35 s (như thay mực mới).
- **Vật liệu:** lưới lụa (screen); squeegee (cây gạt mực); mực đục (≤6 màu); giấy poster (dọc 1000×1500 u hoặc full-bleed 16:9). Mực đục: lớp mực trên che hoàn toàn lớp dưới (không trong như màu nước).
- **Màu:** ≤6 màu, mực đục. Ví dụ palette: dawn `#f6cd98 #ee9a73 #9a7fa8 #3e7079 #1e3b3f #fbe6b4` (bình minh); harbour `#e8f0f2 #7fb3c8 #d9c7a3 #2f6e8e #173247 #e8553d` (bến cảng); winter `#eef1f4 #b8c9d9 #8b9bb0 #4a5d78 #1f2a3c #f2b134` (mùa đông). Gradient cấm — thay bằng dải bậc thang.
- **Chữ:** chữ poster lớn, đậm, in lụa (có hạt, lệch đăng ký nhẹ); tiêu đề là chữ poster; phụ đề (nếu có) trên poster.
- **Nhịp:** reveal bằng squeegee (poster hiện theo cây gạt); palette re-ink 0,35 s (đổi màu nhanh); poster dọc 1000×1500 u hoặc full-bleed 16:9. Nhịp phim là nhịp gạt mực.
- **Camera:** camera trên poster; từ điển: khóa poster (đang gạt mực), push-in (chi tiết mực), pull-back (toàn poster), pan (sang poster mới). Không cắt giữa chừng khi squeegee đang gạt.
- **Âm thanh:** tiếng squeegee gạt mực (swish), tiếng lưới lụa, nhạc nền (indie, pop), giọng kể (nếu có). −14 LUFS.
- **Chiêu đặc trưng:** reveal bằng squeegee (gạt mực hiện poster); palette re-ink 0,35 s; mực đục (che hoàn toàn); gradient cấm, dải bậc thang thay thế; lệch đăng ký 1–3 px.
- **Cạm bẫy:** gradient mượt (không in được bằng lụa); mực trong (mất đục); quá 6 màu; squeegee không phải là reveal (mất hành động in).

### 6. Printed Long Take — long-take khắc bản

- **Bản chất:** **một cú máy dài liên tục** trong một thế giới khắc bản (scratchboard/print): cảnh dựng 3D nhưng mọi giá trị (sáng/tối, màu, chi tiết) là **nét cào neo theo world space** (nét khắc gắn vào thế giới 3D, không phải phủ lên màn hình). ≥3 lớp mỗi frame giữ (mỗi frame giữ ít nhất 3 lớp nét — để nét không nhấp nháy khi camera di chuyển). Một cú máy dài liên tục, không cắt. 30 fps, print flicker 12 Hz (nhấp nháy in 12 lần/giây — cảm giác bản in động).
- **Vật liệu:** mực `#16171b` (mực gần đen), giấy `#ede5cd` (giấy kem), đỏ `#c4332b` (đỏ gạch), vàng `#dfa443` (vàng hổ phách). Nét cào: nét trắng cào trên nền đen (scratchboard) hoặc nét đen khắc trên giấy; nét neo theo world space (gắn vào vật 3D, di chuyển cùng vật khi camera đi).
- **Màu:** mực `#16171b` + giấy `#ede5cd` + đỏ `#c4332b` + vàng `#dfa443`. Chỉ 4 màu. Không thêm màu.
- **Chữ:** chữ khắc (chữ là nét cào/khắc); tiêu đề là chữ khắc; phụ đề (nếu có) trên giấy.
- **Nhịp:** một cú máy dài liên tục (không cắt); 30 fps; print flicker 12 Hz; **bầu trời khắc mở** (bầu trời là nét khắc thưa, mở — không tô kín); **xuyên hơi nước** (camera xuyên qua hơi nước/sương — hơi nước là nét khắc mờ). Nhịp phim là nhịp của cú máy dài.
- **Camera:** **một cú máy dài liên tục**: camera di chuyển không ngừng qua thế giới khắc bản (đi qua các khu vực, lên/xuống, vào/ra). Không cắt. Camera là nhân vật chính — nó dẫn người xem qua thế giới.
- **Âm thanh:** nhạc nền theo cú máy (nhạc dài, liền mạch, không ngắt quãng); tiếng môi trường (gió, nước, bước chân) theo vị trí camera; im lặng ở những đoạn camera đi qua khoảng trống. −14 LUFS.
- **Chiêu đặc trưng:** một cú máy dài liên tục (không cắt); nét cào neo theo world space; ≥3 lớp mỗi frame; print flicker 12 Hz; bầu trời khắc mở; xuyên hơi nước.
- **Cạm bẫy:** cắt giữa chừng (mất long-take); nét cào cố định theo màn hình (mất neo world space — nét sẽ trượt khi camera di chuyển); <3 lớp mỗi frame (nét nhấp nháy); bầu trời tô kín (mất khắc mở).

### 7. Pop Art — pop-art

- **Bản chất:** **pop-art**: 4 bản (đỏ/vàng/xanh/key đen), chấm Ben-Day 45° neo theo page space (chấm halftone nghiêng 45°, gắn vào trang — không di chuyển khi vật di chuyển), lặp lại = ý nghĩa (một hình lặp lại nhiều lần, mỗi lần một màu khác nhau — sự lặp lại chính là thông điệp). **Dot pull**: chấm Ben-Day kéo dài khi vật di chuyển (chấm bị kéo theo hướng di chuyển). **Stamped copies**: bản sao đóng dấu (hình được đóng dấu nhiều lần, mỗi lần lệch một chút).
- **Vật liệu:** chấm Ben-Day (chấm halftone tròn, 45°, neo theo page space); 4 bản in (đỏ, vàng, xanh, key đen — mỗi màu một bản); giấy `#f8f2e2` (giấy kem).
- **Màu:** đỏ `#e4232b` + vàng `#ffd21f` + xanh `#1e62b0` + key đen `#141414` + giấy `#f8f2e2`. Chỉ 4 màu + giấy. Không thêm màu. Mỗi hình lặp lại đổi màu (đỏ → vàng → xanh → đen).
- **Chữ:** chữ pop-art lớn, đậm, có viền; tiêu đề là chữ pop (chữ lớn, màu rực, có bóng); phụ đề (nếu có) trên giấy. Chữ có thể lặp lại (như hình).
- **Nhịp:** 24 fps; lặp lại là nhịp (hình lặp lại theo nhịp nhạc); dot pull khi vật di chuyển; stamped copies (đóng dấu nhiều lần). Nhịp phim là nhịp lặp lại.
- **Camera:** camera trên trang pop-art; từ điển: khóa trang (đang xem hình lặp), push-in (chi tiết chấm Ben-Day), pull-back (toàn trang lặp), pan (sang hình lặp mới). Không cắt giữa chừng khi hình đang lặp.
- **Âm thanh:** nhạc pop/rock nhịp rõ (để hình lặp theo beat); tiếng đóng dấu (stamp); giọng kể (nếu có) ngắn, mạnh. −14 LUFS.
- **Chiêu đặc trưng:** lặp lại = ý nghĩa (hình lặp nhiều lần, mỗi lần một màu); chấm Ben-Day 45° neo theo page space; dot pull (chấm kéo dài khi di chuyển); stamped copies (đóng dấu nhiều lần).
- **Cạm bẫy:** chấm Ben-Day không neo theo page space (chấm di chuyển cùng vật — mất neo); hình lặp cùng màu (mất ý nghĩa lặp); quá 4 màu; chấm không nghiêng 45°.

### 8. Vintage Collage — collage cổ

- **Bản chất:** **collage giấy cũ**: cut-out có viền giấy trắng mỏng rách (mảnh giấy cắt ra có viền trắng rách ở mép — như xé giấy ra khỏi tờ cũ), giấy `#ecdfc2`, card `#f6eedb`, mực `#221c17`, ochre `#c65f3a`, teal `#2f7f7a`, mustard `#e1ab3b`. Mảnh giấy chạy theo twos 12 fps (mỗi mảnh giữ 2 frame — cảm giác giấy động, không mượt). **Data engraving**: biểu đồ khắc (biểu đồ vẽ bằng nét khắc đồng — dữ liệu thành hình khắc). **Ransom letters**: chữ cắt từ báo (chữ ransom — mỗi chữ cái cắt từ một tờ báo khác nhau, dán lại thành câu).
- **Vật liệu:** giấy cũ (giấy vàng, có vết thời gian); cut-out (mảnh giấy cắt/xé, có viền trắng rách); card (thẻ giấy); mực (viết/vẽ trên giấy cũ); data engraving (biểu đồ khắc).
- **Màu:** giấy `#ecdfc2` + card `#f6eedb` + mực `#221c17` + ochre `#c65f3a` + teal `#2f7f7a` + mustard `#e1ab3b`. Màu giấy cũ, ấm, trầm. Không thêm màu rực.
- **Chữ:** **ransom letters** (chữ cắt từ báo — mỗi chữ một font/kích thước khác nhau, dán lại); tiêu đề là ransom letters hoặc chữ viết tay trên giấy cũ; phụ đề (nếu có) trên card giấy.
- **Nhịp:** mảnh giấy chạy theo twos 12 fps; camera mượt; data engraving hiện stroke-by-stroke. Nhịp phim là nhịp dán giấy (mỗi mảnh dán là một beat).
- **Camera:** camera trên bàn collage; từ điển: khóa bàn (đang dán mảnh), push-in (chi tiết mảnh giấy/viền rách), pull-back (toàn collage), pan (sang mảnh mới). Không cắt giữa chừng khi mảnh đang được dán.
- **Âm thanh:** tiếng giấy (xé, cắt, dán), tiếng card (lật), nhạc jazz cổ/vintage nhẹ, giọng kể (nếu có). −14 LUFS.
- **Chiêu đặc trưng:** cut-out có viền giấy trắng mỏng rách; mảnh giấy chạy theo twos 12 fps; data engraving (biểu đồ khắc); ransom letters (chữ cắt từ báo).
- **Cạm bẫy:** mảnh giấy không có viền trắng rách (mất cảm giác xé giấy); mảnh giấy mượt 24 fps (mất twos); ransom letters cùng font (mất cảm giác cắt báo); màu quá rực (mất giấy cũ).

## Hệ màu / bảng chất liệu bất biến (tóm tắt theo style)

| Style | Chất liệu | Màu (bất biến) | Nhịp |
|---|---|---|---|
| risograph | Giấy `#f4eee2`, mực spot, halftone 6–8 px | 2–3 mực spot (vd Blue `#0078bf` + Yellow `#ffe800` + Pink `#ff48b0`) | Nhân vật 12 fps, plate làm truyện |
| halftone-dossier | Giấy kem, chấm step 20–26 px, tem, dấu | Mực tối + 4–5 mực spot | Boil ~10 fps, dot wipe 0,44 s, stamp slam 0,09 s từ 2,6× |
| woodcut | Gỗ, dao 4 loại, giấy in | Đen + trắng + tối đa 1 bản màu (chỉ trên phần trắng đã khắc) | Nhân vật 12 fps, peel |
| engraving | Đồng, burin, giấy `#f1e8d2`, mực `#1c1510` | Mực + giấy + wash trong suốt | Đường kẻ stroke-by-stroke, roundel, proof |
| silkscreen-poster | Lưới lụa, squeegee, mực đục ≤6 màu | Palette theo chủ đề (vd dawn/harbour/winter) | Reveal squeegee, re-ink 0,35 s |
| printed-long-take | Nét cào neo world space, ≥3 lớp/frame | Mực `#16171b`, giấy `#ede5cd`, đỏ `#c4332b`, vàng `#dfa443` | 30 fps, flicker 12 Hz, 1 cú máy dài |
| pop-art | Chấm Ben-Day 45° neo page space, 4 bản | Đỏ `#e4232b`, vàng `#ffd21f`, xanh `#1e62b0`, key `#141414`, giấy `#f8f2e2` | 24 fps, lặp lại = ý nghĩa |
| vintage-collage | Giấy cũ, cut-out viền trắng rách | Giấy `#ecdfc2`, card `#f6eedb`, mực `#221c17`, ochre `#c65f3a`, teal `#2f7f7a`, mustard `#e1ab3b` | Mảnh giấy twos 12 fps, camera mượt |

## Quy trình sản xuất

1. **Chốt brief trước.** Chủ đề, câu chuyện, bảng màu theo style (mỗi style có bảng màu riêng — chọn từ brief, không lấy màu của demo gốc). Hỏi user có tư liệu tham chiếu của mình không (poster cũ, hồ sơ, tranh khắc, báo cũ).
2. **Treatment ngắn trước khi dựng:** chọn 1 style (không trộn 2 style trong một phim trừ khi brief yêu cầu rõ và có điểm chuyển), chọn 3 chiêu đặc trưng sẽ dùng (xem từng style), mỗi chiêu: nó nói ý gì, xuất hiện khi nào. Một phim 20–60 s thường dùng 2–4 chiêu.
3. **Look test trước:** render frame tĩnh/đoạn ngắn bằng đúng cách in của style (halftone, lệch đăng ký, dao khắc, squeegee, chấm Ben-Day) và đối chiếu với `STYLE.md` gốc: hình có đúng là bản in không (chấm có đúng kích thước/góc không, lệch có đúng 1–3 px không).
4. **Timeline là nguồn sự thật duy nhất:** một bảng beat (mốc giây → sự kiện hình → sự kiện âm) mà hình, phụ đề, nhạc, mix đều đọc từ đó. Nhịp hình và cue âm lệch nhau là lỗi, không phải "cảm tính".
5. **Dựng page theo page contract** (xem Công thức): `render(t)` thuần, mọi nét/vật là hàm của `t` với seed cố định; bản in hiện theo thứ tự in; chữ in/khắc/cắt theo đúng cách của style.
6. **Render thử các frame hero của từng beat** → contact sheet soát: chất liệu in, độ đọc của chữ, bố cục giấy, trước khi render full.
7. **Âm thanh theo bảng âm của style** (xem từng style), mix xong đo loudness trên file cuối, QA đầy đủ rồi mới giao.

## Ngữ pháp dựng (chung cho nhóm)

- Hình là bản in: không vẽ trực tiếp, không phủ filter lên ảnh; màu đến từ bản in spot, không blend pixel.
- Lệch đăng ký là chữ ký: mỗi bản lệch 1–3 px; không sửa lệch thành khớp hoàn toàn.
- Gradient cấm (trừ bokashi trong ukiyoe — không thuộc nhóm này): gradient làm bằng dải bậc thang hoặc chấm halftone.
- Một style = một phim (trừ khi brief yêu cầu rõ và có điểm chuyển). Không trộn riso với pop-art trong một shot.
- Chữ bắt buộc đọc giữ ≥ 1,8 s (hoặc ≥ câu nói + 0,6 s); công thức đọc chung: CJK ÷ 4,5 + Latin ÷ 15 + 1,5 s tính từ lúc khối chữ hoàn chỉnh.
- Số liệu (nếu có) phải thật và có nguồn ghi lại; data engraving (vintage-collage) phải dùng số thật.

## Công thức & kỹ thuật đặc thù

- **Page contract:** một trang HTML/Canvas duy nhất khai báo `window.DUR` (tổng thời lượng), `window.render(t)` — hàm thuần của `t` (cấm `Date.now()`, cấm `Math.random()` không seed; mọi jitter/lệch đăng ký phải suy từ seed cố định theo index của bản in/vật), `window.EV` — danh sách sự kiện âm thanh `{t, type}` để mix và đối chiếu cue, `window.TEXTS(t)` — mọi chữ người xem bắt buộc đọc tại thời điểm `t`, phục vụ kiểm tra thời gian đọc. Render bằng cách seek `t` qua headless Chrome (pipeline video-kit hiện có).
- **Seed và lệch:** mọi bản in/vật có seed cố định; lệch đăng ký suy từ seed (mỗi bản một offset cố định 1–3 px); random chỉ được tiêu thụ cùng một cách ở mọi tiến độ. Chỉ phần style cho phép mới động (line boil ~10 fps, print flicker 12 Hz) và theo chu kỳ cố định.
- **Halftone/Ben-Day:** chấm tính từ độ tối (kích thước chấm = độ tối); góc screen cố định theo màu (cách nhau ≥15° cho riso, 45° cho pop-art); chấm neo theo page space (pop-art) hoặc theo bản in (riso).
- **Chữ in/khắc/cắt:** chữ hiện bằng cách in/khắc/cắt/đóng dấu (không wipe, không fade); ransom letters dán từng chữ; stamp slam từ 2,6× trong 0,09 s.
- **Cache:** bản in đã in xong cache thành sprite; chỉ vẽ stroke-by-stroke thứ đang được in/khắc.
- **Âm thanh:** master −14 LUFS, true peak ≤ −1 dBTP; giọng đọc kiểm tra bằng ASR trên giọng sạch và trên phim hoàn chỉnh.

## QA bắt buộc

- ffprobe: đúng độ phân giải/tỉ lệ khung hình đã chốt trong brief (mặc định ngang 1280×720 hoặc 1920×1080, 30 fps; printed-long-take 30 fps; pop-art 24 fps nếu brief chốt), thời lượng khớp `window.DUR`.
- Contact sheet ≥ 6 frame phủ đủ các beat: kiểm (a) hình đúng là bản in (chấm halftone đúng kích thước/góc, lệch đăng ký 1–3 px, dao khắc đúng loại, mực đục, chấm Ben-Day 45°); (b) chữ đọc được, đủ thời gian đọc, không bị bản in che; (c) giấy đủ cho bố cục; (d) màu đúng bảng của style (không thêm màu, không gradient mượt).
- Đọc thử toàn bộ chữ tiếng Việt trên sheet: dấu đầy đủ, không tràn, nhãn nằm trên vùng giấy trống, không đè lên chủ thể.
- Đồng bộ cue: mọi mốc trong `window.EV` có sự kiện âm tương ứng trong mix, lệch ≤ 1 frame.
- Loudness đo trên file cuối: −14 LUFS ± 0,5; blackdetect: 0 đoạn đen ngoài chủ đích.
- Bản quyền: ghi rõ nguồn tham chiếu/hình ảnh trong QA.md; không dùng artwork, tên phim demo, nhân vật hay nhãn hiệu thật của repo gốc.

## Output contract

- File phim: `<slug>-demo.mp4` (H.264 + AAC, −14 LUFS) kèm contact sheet `<slug>-sheet.jpg` và `QA.md` ghi: nguồn tham chiếu, bảng beat đã thực hiện, kết quả đo (ffprobe, loudness, blackdetect), điểm lệch so với treatment nếu có.
- Source giữ cùng thư mục dự án: `index.html` (page contract đầy đủ DUR/render/EV/TEXTS), `render.js`, script sinh âm thanh, frames trung gian.
- Đi kèm `.srt` nếu phim có lời thoại/phụ đề chạy theo thời gian.

## Phân biệt với các nhóm skill opuscar khác

- `opuscar-painting-illustration`: hội họa (nét vẽ/cọ trực tiếp) — nhóm này là in ấn (hình là bản in, màu spot, halftone, lệch đăng ký).
- `opuscar-sketch-board`: bút/phấn/marker để giải thích — nhóm này là quy trình in để kể chuyện/trình bày.
- `opuscar-traditional-crafts`: thủ công truyền thống (thủy mặc, rối bóng, giấy cắt, đèn lồng, kính màu, vàng lá) — nhóm này có ukiyoe cũng là khắc gỗ, nhưng ukiyoe ở đó là một phần của truyền thống thủ công; nhóm này là cả một hệ in ấn hiện đại và cổ điển (riso, lụa, pop-art, halftone, khắc đồng).
- `opuscar-edit-documentary`: sắp xếp tư liệu thật, không dựng lại thế giới bằng bản in — ngược với nhóm này.
- Các nhóm còn lại (graphic & type, line diagrams, cartoons, games, film & tape, screens & interfaces, light & lines, 3D & miniature, instruments & evidence, data & maps): khi brief nói "in riso / halftone / khắc gỗ / khắc đồng / lụa / pop-art / collage" thì nhóm này là đáp án.
