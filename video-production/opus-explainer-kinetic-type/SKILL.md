---
name: opus-explainer-kinetic-type
description: Kỹ thuật explainer bằng kinetic typography — chữ làm diễn viên: phim từ bài nói/speech, từ mang vai trò thị giác, chữ phản ứng với "trường lực" của lập luận, hiểu trọn khi tắt tiếng (archetype của gdgtify-130294 trong kho opus5.5 Explainer). Dùng khi brief là "làm video chữ chuyển động cho bài phát biểu", "kinetic typography", "speech visualization", "video tuyên ngôn/manifesto bằng chữ", "chữ nhảy theo lời đọc", hoặc nội dung là lập luận/slogan cần chữ gánh toàn bộ hình ảnh. Luôn đi cùng pipeline explainer chung của opus55-explainers.
---

# Opus Explainer — Kinetic Type (Chữ làm diễn viên)

Ở archetype này không có hình minh họa: **chữ là diễn viên, là đạo cụ, là bối cảnh**. Mỗi từ khóa được gán một *vai trò thị giác* (field role) và toàn bộ khung hình tổ chức lại quanh nó — câu trước dọn sân cho câu sau, khung hình cuối là kết quả tích lũy của mọi câu đã nói. Đỉnh cao của corpus là phim speech mà tắt tiếng vẫn hiểu trọn vẹn từng chữ.

Mẫu đại diện trong corpus (đọc trước khi làm — `~/workspace/opus55-videos/prompts/<slug>.md`):
- `gdgtify-130294` (full, prompt essay) — mẫu mực của archetype: bài nói 5 câu/20s, mỗi từ khóa (WAIT, WAITING, VOICE, ROOM, FLOOR) có vai trò trong một "trường từ" nhất quán; storyboard chốt theo từng khoảng giây; yêu cầu tuyệt đối "hiểu trọn bài nói khi không có audio".
- `koushikde-937635` (full, prompt essay) — kinetic type theo beat nhạc 128 BPM: một từ chuyển từ thin → black đúng nhịp, chữ đổi typeface như đổi luận điểm, mọi thay đổi trạng thái rơi đúng beat.
- `dotey-927166` (full, prompt essay) — biên niên sử bằng chữ: mỗi thời kỳ một đại tự khóa xuất hiện theo cụm từ, hệ chữ/HUD nhất quán xuyên suốt như một "bộ máy kể chuyện" bằng typography.

## Khi nào dùng

- Nội dung gốc là một bài nói, tuyên ngôn, lập luận, thơ, slogan — thứ mà sức nặng nằm ở câu chữ.
- Brief yêu cầu video chạy tốt trên feed tắt tiếng (X/TikTok/Reels): chữ trên hình chính là phụ đề + hình ảnh hợp nhất.
- Muốn cảm giác "văn bản vật lý": chữ có trọng lượng, bị nén, bị kéo, đứng thẳng dậy, san phẳng — ẩn dụ lập luận được diễn bằng chính letterform.
- Không có (hoặc không muốn) footage/sơ đồ: toàn bộ sản xuất nằm trong typography + chuyển động.

## Nguyên lý cốt lõi

1. **Nguyên văn là bất khả xâm phạm.** Nếu brief có bài nói gốc: đúng chữ, đúng thứ tự, không thêm slogan, không gán cho người thật. Chữ nào không có trong nguyên văn thì không xuất hiện như "lời".
2. **Mỗi từ khóa một vai trò thị giác duy nhất, giữ nhất quán toàn phim.** Vai trò phải *suy ra từ nghĩa* (WAIT = vật cản/nén ép; FLOOR = sự san phẳng/ổn định) và được diễn bằng chính letterform (nghiêng, nén kerning, võng, đứng thẳng) — cấm minh họa trang trí bên cạnh chữ để "giải thích thay" chữ.
3. **Khung hình là tích lũy.** Mỗi câu nói tổ chức lại toàn bộ trường chữ; trạng thái cuối của câu này là điểm xuất phát của câu sau. Cấm cắt cảnh "reset" về khung trống — sự liên tục của trường chính là mạch lập luận.
4. **Tĩnh lặng là một nhịp.** Một khoảng đứng yên tuyệt đối (≥ 400ms, kể cả hạt trang trí cũng dừng) đặt đúng khoảnh khắc lập luận "chốt" có sức nặng hơn mọi chuyển động. Dùng tối đa 1–2 lần/phim.
5. **Chữ luôn đọc được.** Letterform biến dạng trong giới hạn đọc được: câu bị "ép" vẫn phải đọc trọn. Mọi hiệu ứng dừng lại trước ngưỡng làm mất chữ.
6. Kế thừa kỷ luật chung: `seek(t)` xác định (hạt/bụi dùng hash-seed theo id + thời gian), spring dạng đóng, sự kiện rơi đúng beat/cụm từ, cấm easing nảy.

## Quy trình sản xuất

1. Chốt nguyên văn + learning objective (thường là: người xem *cảm và nhớ* được tuyên ngôn/lập luận). Đếm câu, chia cụm từ (phrase groups) — đơn vị xuất hiện là cụm, không phải từng ký tự rời.
2. Bảng vai trò: liệt kê từ khóa → vai trò thị giác → cách letterform/trường phản ứng. Kiểm tra tính nhất quán: các vai trò phải thuộc cùng một "vật lý" (một trường, một hệ lực) — trộn hệ ẩn dụ là lỗi.
3. Storyboard theo khoảng giây cho từng câu: trường đang ở trạng thái nào → sự kiện chữ gì xảy ra → trạng thái chốt. Đánh dấu vị trí của 1–2 nhịp tĩnh lặng.
4. Hệ chữ: tối đa 3 vai — serif high-contrast cho lời nói, grotesque nặng cho từ "chịu lực" (từ khóa), mono cho nhãn/HUD phụ. Palette 3 màu: nền, chữ, accent của trường.
5. Dựng HTML (SVG cho letterform chính xác — xoay/nghiêng từng glyph bằng transform phân tích, không morph path; Canvas cho trường/hạt nền). Mọi thứ từ `seek(t)`.
6. Nếu có voice: voice đọc nguyên văn, mốc cụm từ trong voice là mốc sự kiện chữ (reveal-on-cue tuyệt đối). Render + QA theo pipeline master, thêm mục QA riêng dưới đây.

## Công thức & kỹ thuật đặc thù

- **Trường (field) bằng hàm phân tích:** độ nghiêng/nén của mỗi glyph = hàm của vị trí glyph so với "cực" hiện tại của scene (bản đồ vector viết tay theo storyboard) — tính trực tiếp từ `t` và vị trí, không mô phỏng tích lũy.
- **Dòng trường (streamlines):** vẽ bằng path có dash-offset rút/vẽ theo sự kiện "trường tổ chức lại"; filings/hạt trôi dọc streamline bằng hash-seed xác định.
- **Chuyển vai trò = sự kiện lớn nhất của scene:** khi từ khóa mới xuất hiện, trường cũ rút đi (dash-offset) và trường mới vẽ vào trong cùng một cửa sổ beat; glyph xoay về tư thế mới bằng phép quay toàn glyph (analytic rotation), không biến dạng path.
- **Nhịp câu chữ:** một cụm từ mỗi ~0.8–1.5s khi không voice; có voice thì khóa theo mốc cụm từ đo từ file âm thanh. Từ khóa "chịu lực" được giữ lâu hơn các từ nối ít nhất 2 lần.
- **Đóng phim bằng tích lũy:** khung cuối phải chứa dấu vết của mọi câu (trường đã phẳng, mọi chữ đứng thẳng...) — người xem nhìn frame cuối là "đọc" lại được toàn bộ lập luận.

## QA bắt buộc

- **Sound-off tuyệt đối:** tắt tiếng xem từ đầu — phải đọc/hiểu trọn 100% nguyên văn và mạch lập luận. Thiếu một cụm từ là lỗi chặn giao.
- Đối chiếu nguyên văn từng chữ với brief (thừa/thiếu/sai thứ tự = làm lại).
- Vai trò từ khóa: xem không tiếng, người kiểm tra có nói lại đúng "từ nào đóng vai gì" không; mỗi từ khóa chỉ một vai trò, không đổi giữa chừng.
- Nhịp tĩnh lặng: đo đúng vị trí và độ dài (≥ 400ms đứng yên thật, kể cả nền).
- Glyph tiếng Việt (nếu lời là tiếng Việt): dùng Be Vietnam Pro; cấm Anton/Oswald cho chữ lớn; kiểm dấu ở các từ khóa bị biến dạng mạnh nhất.
- Thêm các mục QA chung của `opus55-explainers` (ffprobe, contact sheet theo beat câu, loudness nếu có voice, xem trọn bản phát).

## Output contract

Theo output contract của `opus55-explainers`, cộng: nguyên văn đã dùng (toàn văn, ghi nguồn brief) và bảng vai trò từ khóa → hiệu ứng, để lần sau tái sử dụng cùng "vật lý" cho phần tiếp theo của series.
