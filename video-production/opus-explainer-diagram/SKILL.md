---
name: opus-explainer-diagram
description: Kỹ thuật explainer bằng sơ đồ hoạt hình SVG/Canvas — diagram tự vẽ, chart tự dựng, data story, timeline, mô phỏng chạy thật (nhóm SVG+GSAP 33 mục + Canvas 16 mục trong kho opus5.5 Explainer). Dùng khi brief là "vẽ sơ đồ giải thích", "biểu đồ chuyển động kể số liệu", "giải thích quy trình/hệ thống bằng hình", "data story", "video kiểu The Pudding", hoặc explainer sản phẩm bằng UI states. Luôn đi cùng pipeline explainer chung của opus55-explainers (learning objective trước, reveal-on-cue, mô phỏng thật, sound-off test).
---

# Opus Explainer — Diagram (Sơ đồ & Data Story)

Archetype đông nhất của nhóm Explainer: khái niệm được biến thành một sơ đồ sống — đường tự vẽ, cột tự mọc, nút sáng lên đúng lúc được gọi tên. Engine: SVG + GSAP (chính xác, sắc nét, dễ gắn nhãn) hoặc Canvas 2D (khi cần hàng nghìn phần tử/mô phỏng liên tục).

Mẫu đại diện trong corpus (đọc trước khi làm — `~/workspace/opus55-videos/prompts/<slug>.md`):
- `astrothewizard-618782` (Canvas, full) — explainer khoa học 60s kiểu studio: mô phỏng thật (random walk chạy thật), số thật + ghi rõ độ không chắc chắn, gag thị giác giữ nhịp, voice + phụ đề đốt.
- `verbove-268381` (Canvas, full) — explainer sản phẩm bằng UI states: một element morph qua 12 trạng thái kể câu chuyện, dữ liệu thật từng state, con trỏ dẫn dắt.
- `deedydas-252537` (SVG+GSAP, full) · `alex-prompter-997524` (SVG+GSAP, full) — sơ đồ/infographic SVG có timeline GSAP.
- `retropunkai-277590` (Canvas/SVG/GSAP, full) — explainer lịch sử dạng timeline: kiến trúc dựng dần theo mốc thời gian, hình thật lồng vào sơ đồ.

## Khi nào dùng

- Giải thích quy trình, hệ thống, luồng dữ liệu, cấu trúc quan hệ (ai nối với ai, cái gì chảy đi đâu).
- Kể chuyện bằng số liệu: chart mọc theo lập luận, so sánh trước/sau, phân rã một con số lớn thành phần dễ hình dung.
- Mô phỏng hiện tượng có quy luật rõ (lan truyền, xếp hàng, tăng trưởng, random walk...) — Canvas chạy mô phỏng thật.
- Explainer sản phẩm: UI states nối tiếp, mỗi state chứng minh một luận điểm (biến thể của `verbove-268381`).

## Nguyên lý cốt lõi

1. **Sơ đồ là lập luận, không phải minh họa.** Thứ tự vẽ = thứ tự lập luận. Người xem phải "đi" theo nét vẽ như đi theo câu nói; vẽ xong toàn cảnh ngay từ đầu rồi mới thuyết minh là thất bại kinh điển.
2. **Một lớp thông tin mới mỗi beat.** Nền/khung được giới thiệu một lần rồi giữ ổn định; mỗi beat chỉ thêm đúng một lớp (một nhánh, một cột, một mũi tên). Não người xem cộng dồn bản đồ tư duy theo từng lớp.
3. **Nhãn gắn liền vật, không có chú thích rời.** Chữ nằm cạnh phần tử nó gọi tên, xuất hiện cùng phần tử. Không bắt người xem đối chiếu legend ở góc màn hình.
4. **Số phải thật và "cân" được.** Chart đúng tỉ lệ thật; trục/đơn vị ghi rõ; số ước tính ghi "ước tính". Mô phỏng dùng thuật toán thật với seed xác định (để `seek(t)` vẫn thuần).
5. Kế thừa kỷ luật chung: reveal-on-cue theo lời, một ý hình mỗi scene, sound-off test (sơ đồ + nhãn phải tự kể được ý chính), spring dạng đóng, cấm easing nảy.

## Quy trình sản xuất

1. Rút learning objective + danh sách số liệu/nguồn từ pipeline master; nếu số liệu chưa có nguồn → dừng, không vẽ.
2. Phác sơ đồ tĩnh trước (trên giấy/HTML tĩnh): chốt layout cuối cùng mà mọi thứ sẽ "mọc" tới — layout này phải tự nó đã rõ ràng khi đứng yên.
3. Chia storyboard theo beat: beat nào vẽ thêm lớp nào, nhãn nào hiện, con số nào chạy (counter) — khớp mốc từ khóa trong script voice/phụ đề.
4. Dựng HTML: SVG (path vẽ bằng dash-offset, cột scale từ gốc, counter nội suy theo `t`) hoặc Canvas (mô phỏng seeded chạy trong `draw(t)`). Mọi trạng thái suy ra từ `seek(t)`.
5. Render thử 1 frame/beat → contact sheet: soát thứ tự lập luận trên ảnh tĩnh; sửa layout/storyboard trước khi render full.
6. Render full + ghép voice/phụ đề/nhạc theo pipeline master, QA đầy đủ (đặc biệt: đồng bộ reveal và kiểm tỉ lệ chart).

## Công thức & kỹ thuật đặc thù

- **Path tự vẽ:** `stroke-dasharray = pathLength`, `dashoffset` nội suy từ 1 → 0 theo cửa sổ beat của nét đó; đầu bút có thể gắn một chấm accent chạy theo để mắt bám theo.
- **Cột/điểm mọc có thứ tự lập luận:** stagger theo thứ tự được nhắc trong lời, không theo vị trí trái→phải một cách máy móc.
- **Counter & nhãn số:** số chạy bằng cùng easing spring như hình để mắt cảm thấy "cùng một sự kiện"; số cuối dừng đúng giá trị nguồn, làm tròn nhất quán (ghi rõ nếu đã làm tròn).
- **Highlight dẫn mắt:** phần đang được nói tới giữ accent/full opacity; phần đã qua hạ xuống 40–60% (không biến mất — người xem vẫn cần bản đồ tổng).
- **Mô phỏng Canvas xác định:** seed cố định (hash theo id phần tử), trạng thái tại `t` tính khép kín hoặc tiền tính (precompute) vào mảng theo frame — tuyệt đối không tích lũy state qua các lần gọi `seek`.
- **UI-story (biến thể sản phẩm):** một element không bao giờ cắt — morph size/radius/màu qua các state, nội dung vào sau khi container bắt đầu morph và ra trước morph tiếp theo để chữ không bao giờ chồng nhau; con trỏ (click/gõ/kéo) là "người dẫn chuyện".

## QA bắt buộc

- Đứng yên ở frame cuối của mỗi scene: sơ đồ hoàn chỉnh có tự nó rõ ràng không (đọc được như một infographic tĩnh)?
- Tỉ lệ chart đối chiếu số nguồn từng cột/điểm; counter dừng đúng số.
- Reveal khớp từ khóa trong voice/phụ đề (lệch > 0.3s là lỗi); nhãn không chồng nét vẽ, không tràn khung ở cỡ điện thoại.
- Sound-off test: chỉ nhìn hình + nhãn + phụ đề có hiểu trọn lập luận không.
- Thêm các mục QA chung của `opus55-explainers` (ffprobe, contact sheet, loudness, xem trọn bản phát).

## Output contract

Theo output contract của `opus55-explainers`, cộng: bảng số liệu đã dùng kèm nguồn (để đối chiếu về sau) và ghi rõ phần nào của sơ đồ là mô phỏng thật, phần nào là minh họa đơn giản hóa.
