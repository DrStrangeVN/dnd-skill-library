---
name: opus55-explainers
description: Router + pipeline chung cho video explainer (giải thích/dạy một khái niệm bằng motion) học từ kho awesome-opus5-5-videos (nhóm Explainer, 116 prompt). Dùng khi user nói "làm video giải thích", "explainer video", "video dạy/giảng về X", "giải thích khái niệm bằng animation", "làm video kiểu 3Blue1Brown/Pudding", "kinetic typography cho bài nói", hoặc gửi chủ đề cần giải thích mà chưa chốt kỹ thuật (diagram / kinetic type / 3D). Skill này chọn kỹ thuật, giao việc cho skill con tương ứng và sở hữu pipeline explainer + chuẩn đầu ra dùng chung.
---

# Opus55 Explainers — Master (Router + Pipeline chung)

Học từ nhóm **Explainer** của repo `awesome-opus5-5-videos` (703 video toàn repo, 116 mục explainer: 75 prompt full, 41 partial).
Thư viện prompt gốc: `~/workspace/opus55-videos/prompts/<slug>.md`; catalogue đã xếp nhóm: `~/workspace/opus55-videos/EXPLAINER-INDEX.md`.
Prompt thuộc về tác giả gốc — **chỉ học kỹ thuật và cấu trúc sư phạm, nội dung luôn làm mới**, không sao chép nguyên văn brief/kịch bản của người khác thành sản phẩm của mình.

Khác biệt cốt lõi so với nhóm Motion: motion graphics **trang trí/thuyết phục**, còn explainer **dạy** — thước đo thành công là người xem *hiểu và nhớ được một điều cụ thể*, không phải "đẹp". Mọi quyết định hình ảnh đều phải trả lời được: nó giúp hiểu thêm điều gì?

## Khi nào dùng

- User yêu cầu video giải thích một khái niệm, quy trình, cơ chế, dữ kiện: khoa học, công nghệ, tài chính, lịch sử, cách một sản phẩm/hệ thống vận hành.
- User nói "kiểu 3Blue1Brown", "kiểu The Pudding", "video giảng bài", "kinetic typography cho speech/bài phát biểu", "data story".
- Brief chưa rõ kỹ thuật → skill này phân loại rồi chuyển cho 1 trong 3 skill con:
  - `opus-explainer-diagram` — sơ đồ/chart hoạt hình, data story (SVG/Canvas)
  - `opus-explainer-kinetic-type` — chữ làm diễn viên, phim từ bài nói/speech, hiểu được khi tắt tiếng
  - `opus-explainer-3d` — Three.js/GLSL cho khái niệm không gian/vật lý

## Chọn kỹ thuật theo brief (bảng router)

| Dấu hiệu trong brief | Chọn | Lý do |
|---|---|---|
| Khái niệm là quan hệ/cấu trúc/luồng: quy trình, hệ thống, biểu đồ, số liệu, so sánh, timeline | `opus-explainer-diagram` | Sơ đồ tự vẽ theo lời giảng; archetype đông nhất corpus (SVG+GSAP 33 + Canvas 16) |
| Nội dung là một bài nói/slogan/lập luận; chữ là nhân vật chính; phải hiểu khi tắt tiếng; nhịp câu chữ dẫn dắt | `opus-explainer-kinetic-type` | Chữ mang vai trò thị giác, mỗi từ/cụm xuất hiện đúng lúc ý nó xuất hiện trong lời |
| Khái niệm là vật thể/cấu trúc 3D, hiện tượng vật lý, không gian: thấu kính, động cơ, phân tử, quỹ đạo, sóng | `opus-explainer-3d` | Cần mô hình 3D thật, cắt lớp, nổ tung (explode) có nhãn, ánh sáng đi qua vật |
| Sản phẩm/app giải thích bằng UI states nối tiếp | `opus-explainer-diagram` (biến thể UI-story) | Một element morph qua các states kể câu chuyện, dữ liệu thật |
| Brief trộn nhiều kỹ thuật | Kỹ thuật của "khoảnh khắc aha" làm skill chủ; phần còn lại mượn kỹ thuật phụ, ghi rõ trong storyboard | Explainer thắng ở 1–2 khoảnh khắc hiểu sáng tỏ, không thắng ở dàn trải |

Không chắc → mặc định `opus-explainer-diagram`: phần lớn khái niệm giải thích tốt nhất bằng sơ đồ đơn giản vẽ đúng lúc.

## Nguyên lý cốt lõi (chất sư phạm của corpus — áp dụng cho MỌI explainer)

1. **Một video = một mục tiêu học (learning objective).** Viết được thành 1 câu: "Xem xong, người xem hiểu được ___." Mọi scene phải phục vụ câu đó; cảnh nào không phục vụ thì cắt, dù đẹp.
2. **Hình đi cùng lời, không đi trước lời.** Phần tử xuất hiện đúng khoảnh khắc khái niệm được nhắc tới (reveal-on-cue). Hiển thị trước = người xem đọc lan man; hiển thị sau = hụt. Đây là kỷ luật quan trọng nhất của explainer.
3. **Một ý tưởng hình thức mạnh cho mỗi scene (one strong formal idea).** Mỗi scene chỉ có một phép ẩn dụ thị giác chính (sơ đồ võng xuống dưới tải trọng, trường lực phẳng thành mặt sàn, thấu kính nổ tung...). Hai ẩn dụ trong một scene = không hiểu cả hai.
4. **Mô phỏng thật khi có thể, không vẽ giả.** Random walk thì chạy random walk thật; số liệu thật, ghi rõ ước tính/khoảng không chắc chắn. Explainer bịa số là explainer hỏng, kể cả khi đẹp.
5. **Hiểu được khi tắt tiếng (sound-off test).** Đa số người xem feed không bật âm. Phụ đề/chữ trên hình phải đủ để hiểu trọn ý chính mà không cần voice.
6. **Kế thừa toàn bộ nguyên lý motion của `opus55-motion-graphics`:** animation là hàm thuần của thời gian qua `seek(t)` xác định; spring dạng đóng `1 − (1 + ωt)·e^(−ωt)`; lưới nhịp ~120 BPM (hoặc theo nhịp đọc của voice); không dead time; cấm easing nảy/elastic và vẻ template.

## Quy trình sản xuất (pipeline explainer — skill này sở hữu)

1. **Chốt learning objective + kiểm chứng sự thật:** 1 câu mục tiêu học; liệt kê các khẳng định/số liệu sẽ nói và nguồn của chúng. Chưa rõ đúng/sai thì không đưa vào video.
2. **Viết script/storyboard theo beat:** kịch bản lời (hoặc cấu trúc chữ nếu không voice) chia thành các beat ý — mỗi beat = 1 ý nhỏ + 1 hành động hình duy nhất. Storyboard dạng bảng: `thời gian · lời/chữ · hình làm gì · điểm nhấn`. Một beat không ôm hai ý.
3. **Dựng hệ thống hình (visual system):** palette giới hạn (nền + chữ + 1 accent dẫn chuyển cảnh), 1–2 font, quy ước nhất quán (accent = điều đang được nói tới; mờ = bối cảnh). Hệ thống phải đủ đơn giản để người xem "học" trong 10 giây đầu.
4. **Âm thanh (nếu có voice):** ghi voice VieNeu (giọng theo chuẩn nhà của từng kênh), phụ đề theo cụm từ (phrase-level, không tràn 2 dòng) đốt vào hình hoặc track riêng; nhạc nền lùi dưới voice (~−28 dB), loudness tổng ≈ −14 LUFS. Không có voice → kinetic-type hoặc chữ dẫn chuyện phải tự đứng vững (sound-off test ở bước 6 vẫn áp dụng).
5. **Dựng single-file HTML + render:** một file HTML chứa toàn bộ scene + `seek(t)`; render frame-by-frame bằng headless Chromium (3–5 subframes + ffmpeg `tmix` khi cần motion blur), ghép MP4. Theo đúng skill con đã chọn.
6. **QA sư phạm + kỹ thuật rồi mới giao** (xem mục QA bắt buộc). Chỉ báo "xong" sau khi render + QA thật đạt.

## Quy trình sản xuất — ghi chú máy này

- Render tuần tự, concurrency thấp (máy 2 core); explainer thường dài hơn motion (30–120s) → render thử 1 frame/beat thành contact sheet, soát storyboard trên ảnh tĩnh trước khi render full.
- Voice VieNeu: dùng helper/API theo chuẩn từng kênh; tốc độ và giọng do brief/kênh quy định, không tự đổi giọng rồi gọi bằng tên giọng khác.
- Font chữ tiếng Việt khổ lớn: **Be Vietnam Pro** (đã kiểm glyph). **Không** dùng Anton/Oswald cho chữ tiếng Việt lớn — dấu nặng (Ọ/Ị…) bị tách/sai vị trí.
- Mỗi dự án một thư mục riêng, giữ lại: script/storyboard, HTML nguồn, frames, file voice/nhạc, MP4 cuối, contact sheet QA, danh sách nguồn số liệu.

## Công thức & kỹ thuật đặc thù

- Reveal-on-cue: mốc xuất hiện của phần tử = mốc thời gian của từ khóa trong voice/phụ đề, trừ hao spring settle ~0.15–0.3s để phần tử "đứng yên" đúng lúc ý được nói trọn.
- Beat theo lời, không theo nhạc, khi có voice: beat grid = ranh giới cụm từ trong script; nhạc chỉ là nền, không được kéo hình lệch khỏi lời.
- Nhịp độ: 1 ý mới mỗi ~2–4 giây là trần; nhanh hơn thì người xem bỏ cuộc, chậm hơn thì sinh dead time — lấp bằng biến đổi có ý nghĩa trong cùng một ý, không bằng trang trí.
- Callback: lặp lại một motif hình ở đầu và cuối (cùng sơ đồ, nay đã "hiểu khác") để đóng vòng học — thủ pháp giữ chân mạnh nhất của corpus.

## QA bắt buộc

- **Sound-off test:** tắt tiếng, xem hết video — phải hiểu được ý chính. Không đạt → sửa chữ/phụ đề/hình, không sửa nhạc.
- **Kiểm sự thật:** đối chiếu từng số liệu/khẳng định trong bản final với danh sách nguồn ở bước 1; số ước tính phải có chữ "ước tính/khoảng" trên hình hoặc trong script.
- **Đồng bộ lời–hình:** rà các mốc reveal chính: phần tử có xuất hiện đúng từ khóa không (lệch > 0.3s là lỗi).
- ffprobe: đúng kích thước (1280×720 / 1920×1080 / 1080×1080 / dọc 9:16 theo brief), fps (30 hoặc 60), đúng thời lượng storyboard.
- Contact sheet (1 frame/beat + các điểm chuyển ý): chữ không chồng, không tràn, glyph tiếng Việt đúng, sơ đồ đọc được ở kích thước điện thoại.
- Loudness ≈ −14 LUFS, true peak ≤ −1 dBTP; voice rõ trên nhạc ở mọi đoạn.
- Xem lại bản phát trọn vẹn ít nhất 1 lượt (không chỉ ảnh tĩnh) trước khi giao.

## Output contract

Giao: **MP4 cuối** + **script/storyboard** + **file HTML nguồn** (sửa được) + thông số (kích thước/fps/thời lượng/dung lượng) + learning objective + danh sách nguồn số liệu + ghi chú prompt gốc đã tham khảo (slug). Không đăng công khai khi chưa có duyệt mới của user. Chưa render + QA xong thì không nói "xong".
