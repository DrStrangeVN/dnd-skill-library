---
name: remotion-general
description: Pipeline tổng quát dựng showreel, promo và explainer bằng Remotion (React) từ chất liệu thật của sản phẩm — storyboard theo mốc giờ, một camera liên tục, trạng thái là hàm thuần của thời gian, spring dạng đóng, lưới nhịp, QA bằng khung tĩnh. Dùng khi brief yêu cầu Remotion cho showreel/promo/explainer/portfolio/app film mà không thuộc composition truyện tranh dọc, không thuộc video dọc có giọng đọc, và không thuộc pipeline HTML seek(t) của hệ Opus55.
---

# Remotion tổng quát — showreel / promo / explainer

Skill này chưng cất cấu trúc làm việc chung của 10 mục đã xác minh trên
prompt-motion.com có ghi dùng Remotion (xem mục Nguồn tham khảo). Mọi nội dung
dưới đây diễn đạt lại cấu trúc bằng lời của người tổng hợp; không chép nguyên
văn prompt, câu chữ hay artwork của tác giả nào. Credit thuộc về từng tác giả
và prompt-motion.com.

## 1. Khi nào dùng

Dùng khi cả ba điều kiện sau đúng:

- Đầu ra là video dựng bằng **Remotion** (React, render bằng Remotion CLI),
  thuộc một trong các dạng: showreel giới thiệu năng lực, promo sản phẩm/
  dịch vụ, explainer khái niệm, portfolio, app film.
- Có **chất liệu thật** để lấy làm nguồn chân lý: repo/codebase, website
  đang chạy, ảnh chụp màn hình mới nhất, hệ thống thiết kế, logo, font,
  màu, số liệu demo của chính sản phẩm đó.
- Brief cần một dòng chuyển động liền mạch (camera liên tục, chuyển cảnh
  bằng vật thể chung) thay vì chuỗi cảnh cắt rời, và cần kiểm chứng được
  bằng khung hình tĩnh trước khi render đủ.

## 2. Khi nào KHÔNG dùng — ranh giới với skill gần nhất

| Trường hợp | Dùng skill khác | Vì sao không phải skill này |
|---|---|---|
| Quảng cáo dọc kiểu truyện tranh: sunburst, halftone, bong bóng starburst, caption hộp vàng, năng lượng hype | `motion-comic-hype-video` | Skill đó khóa cứng một composition comic dọc duy nhất; skill này không có skin comic và không khóa một bố cục nào. |
| Video dọc 1080×1920, kịch bản tiếng Việt có giọng đọc, 5 variant A–E, karaoke captions | `motion-video` | Stack lõi của skill đó là HyperFrames + GSAP, không phải Remotion; phạm vi dọc-có-voice của nó nằm ngoài skill này. |
| Motion graphics bằng một file HTML duy nhất, hàm `seek(t)` + chụp khung headless, thuộc một trong bốn kỹ thuật Canvas 2D / SVG+GSAP / Shader / Three.js | Router `opus55-motion-graphics` và skill con `opus-motion-canvas`, `opus-motion-svg-gsap`, `opus-motion-shader`, `opus-motion-threejs` | Hệ Opus55 dựng bằng HTML/JS thuần và chụp khung bằng trình duyệt headless, không qua Remotion. Skill này chỉ dùng Remotion; không mượn pipeline render của hệ đó. |
| Chỉ cần tra cứu API Remotion, quy tắc từng mảng (3D, caption, chart, transition…), tạo project, nâng cấp, Studio, render, bản đồ | `remotion`, `remotion-video-creation`, `remotion-create`, `remotion-docs`, `remotion-render`, `remotion-studio`, `remotion-upgrade`, `remotion-maps`, `remotion-captions`, `remotion-markup`, `remotion-best-practices` và các skill `remotion-*` còn lại | Các skill đó là tài liệu tham khảo theo mảng; skill này là pipeline sản xuất đầu-cuối, không thay thế chúng. Khi cần chi tiết API, tra cứu ở đó rồi quay lại pipeline này. |
| Explainer mà chữ là diễn viên chính, hiểu trọn khi tắt tiếng, từ bài nói/speech | `opus-explainer-kinetic-type` | Phạm vi explainer/speech bằng chữ động đã có skill chuyên trách; skill này chỉ nhận kinetic type khi nó là một lớp trong phim Remotion (ví dụ tiêu đề theo nhịp), không nhận phim chữ-động thuần. |
| Chỉ chiến lược chart/sequencing, không dựng thành phẩm | `video-data-visualization` | Skill đó không dựng; nếu chart là một phần của phim Remotion thì dựng theo pipeline này. |
| Game/interactive chơi được, PRD game, telestrator thể thao | `opus55-interactive`, `opus-game-*`, `opuscar-telestrator` | Không phải video Remotion tuyến tính. |
| Video dọc có voice thuộc kênh Học Bóng Rổ / các kênh có chuẩn riêng (giọng API, độ dài, engine bắt buộc) | Chuẩn riêng của kênh đó | Skill này không ghi đè chuẩn kênh. Khi brief thuộc một kênh đã có chuẩn khóa, chuẩn kênh thắng. |

Nghi ngờ thì hỏi một câu duy nhất trước khi dựng: "Brief này thuộc
composition khóa, video dọc có voice, hay pipeline HTML?" — trả lời rơi vào
hàng nào thì giao cho skill hàng đó.

## 3. Đầu vào bắt buộc

Không dựng khi thiếu mục 1 hoặc mục 2. Thiếu mục 3 thì dựng bản không
nhạc có bản quyền, kèm bảng cue âm thanh (mục 7).

1. **Chất liệu thật (nguồn chân lý duy nhất).** Một trong: URL website/
   trang đích đang chạy; repo/codebase; bộ ảnh chụp màn hình mới nhất;
   file hệ thống thiết kế + logo + font + bảng màu. Ghi rõ đường dẫn/URL
   và ngày lấy. Mọi nút, tính năng, số liệu, câu chữ trên hình phải đối
   chiếu được với chất liệu này. Không có chất liệu thật thì chỉ được
   dựng khi brief giao toàn quyền và toàn bộ nội dung trên hình là hư
   cấu có ghi rõ là hư cấu — khi đó lập một file `SOURCE.md` hư cấu
   trong dự án, liệt kê đúng những gì được phép hiện, và không thêm
   bất cứ nút/tính năng/số liệu nào ngoài file đó.
2. **Mục đích + một câu đo được.** Ví dụ: người xem hiểu được ba ý nào,
   nhớ được tên sản phẩm nào, bấm vào đâu sau khi xem. Brief chỉ nêu
   "làm cho đẹp" thì phải chốt một câu đo được trước khi viết storyboard.
3. **Âm thanh hợp pháp.** Nhạc/SFX tự tổng hợp bằng mã, hoặc tài sản có
   quyền dùng rõ ràng. Không dùng nhạc/SFX có bản quyền, không dùng
   nhạc lấy từ video của người khác.
4. **Khổ, fps, thời lượng mục tiêu.** Mặc định của skill này: ngang
   1920×1080, 30 fps, 15 giây cho mẫu ngắn; 1920×1080, 30 fps,
   90–100 giây cho mẫu dài. Mọi con số khác phải do brief ghi, không
   suy đoán rồi ghi như đã xác minh.

## 4. Quy trình

### Bước 1 — Thu thập và đóng băng chất liệu

- Tải/chụp đúng chất liệu ở mục 3.1 vào thư mục dự án (`assets/`).
  Với website thật: chụp các trang/mục sẽ dùng, đặt trong khung trình
  duyệt/điện thoại khi lên hình, không vẽ lại giao diện từ trí nhớ.
- Trích ra một bảng duy nhất: tên sản phẩm, slogan (ghi đúng từng chữ),
  màu, font, logo (vẽ lại thành SVG để giữ nét khi phóng to), các màn
  hình/số liệu được phép hiện. Bảng này là nguồn chân lý; storyboard
  và code chỉ được lấy từ bảng này.
- Ghi rõ thỏa hiệp: màn hình nào không có thì không hiện, không bịa
  màn hình thay thế; số liệu nào không có thì không hiện số.

### Bước 2 — Storyboard theo mốc giờ, chốt trước khi code

- Viết storyboard dạng bảng: mỗi hàng một đoạn, ghi mốc bắt đầu–kết
  thúc (giây), ý duy nhất của đoạn, chữ trên hình (cực ít, rất ngắn),
  vật thể chung nối sang đoạn sau, vị trí camera. Mỗi đoạn một ý.
  Không đoạn nào mang hai ý.
- Vẽ storyboard bằng khung tĩnh (ảnh chụp màn hình đã có, phác bố cục
  bằng hình khối) nếu brief phức tạp; trình storyboard trước khi code
  khi có người duyệt.
- Chốt nhịp: chọn BPM (mặc định 120), tính lưới beat (`beat = 60/BPM`
  giây). Mọi sự kiện hình ảnh quan trọng rơi đúng beat hoặc đúng nửa
  beat; không để beat trống (dead time) mà không có chuyện gì xảy ra.
- Chốt camera: **một thế giới duy nhất, một camera liên tục.** Camera
  chỉ có một chuyển động tại một thời điểm (pan, zoom, hoặc dolly —
  không hai thứ cùng lúc trừ khi đã tính sẵn trong hàm camera). Chuyển
  đoạn bằng vật thể chung: một chi tiết ở đoạn trước nở ra thành khung
  của đoạn sau, hoặc camera lao vào một ô rồi ô đó nở phủ kín khung
  (cắt khớp vị trí: khung cuối của đoạn trước trùng khung đầu của
  đoạn sau). Cấm cắt cứng không lý do nhịp điệu.

### Bước 3 — Dựng composition Remotion

- Một composition, một file gốc (`src/`), không state tích lũy:
  mọi trạng thái hình ảnh là hàm thuần của thời gian (mục 5).
- Dựng theo thứ tự: thế giới tĩnh (bố cục, chữ, vật thể) →
  camera → chuyển động vào/ra theo beat → âm thanh theo beat.
- Render khung tĩnh ở mọi mốc cắt và mốc giữa đoạn **trước** khi
  render đủ (dùng `remotion still` hoặc render ảnh). Sửa mọi lỗi
  chồng lấn, cắt xén, tràn chữ, vật thể trôi vào vùng biên rồi mới
  render video.
- Bản dọc (nếu brief yêu cầu thêm): tái bố cục có chủ đích, không
  cắt xén bản ngang.

### Bước 4 — Âm thanh theo beat, trộn đúng mức

- Nhạc tự tổng hợp bằng mã hoặc tài sản có quyền; đặt sự kiện âm
  thanh theo lưới beat và theo đỉnh đã đo của bản nhạc.
- SFX kiềm chế: một tiếng nhẹ cho mỗi yếu tố xuất hiện quan trọng,
  còn lại giữ im lặng; tránh tiếng nổ lớn, riser, tiếng vút rải khắp.
- Trộn ở **−14 LUFS** (mục tiêu), đo bằng `loudnorm`/`volumedetect`
  trên file bàn giao cuối. Không giọng đọc trừ khi brief ghi rõ giọng
  và nguồn giọng hợp lệ; khi có giọng đọc, giọng là một track riêng,
  nhạc nằm dưới giọng và không át giọng.
- Nếu không có tài sản âm thanh an toàn: giao bản hình kèm bảng cue
  (vị trí, loại nhạc/SFX cần đặt), không gắn nhạc không rõ quyền.

### Bước 5 — QA và bàn giao

- Chạy checklist ở mục 8. Chỉ báo xong khi mọi mục đạt.
- Bàn giao gồm: storyboard cuối, mã nguồn composition, MP4, khung
  cuối/poster, contact sheet, thời lượng chính xác, danh sách tài
  sản/màn hình thật đã dùng, giải thích ngôn ngữ chuyển động, các
  thỏa hiệp còn lại, lệnh render lại. Không triển khai, không sửa dữ
  liệu production, không merge — trừ khi brief ghi rõ việc đó.

## 5. Cấu trúc bắt buộc: hàm thuần của thời gian, spring dạng đóng, lưới nhịp

### 5.1. Mọi trạng thái là hàm thuần của `t`

Trong component Remotion, lấy `frame` bằng `useCurrentFrame()`,
đổi ra giây `t = frame / fps`. Mọi vị trí, tỉ lệ, độ mờ, độ dài
nét vẽ đều tính từ `t` bằng hàm thuần — không `useState`,
không `useEffect` tích lũy, không timer, không đọc trạng thái
frame trước. Cùng một frame render hai lần phải cho cùng một
hình (kiểm chứng ở mục 8).

```tsx
import { useCurrentFrame } from "remotion";

// t tính bằng giây, suy ra từ frame — không có trạng thái nào khác.
export const useT = (fps: number) => useCurrentFrame() / fps;
```

### 5.2. Spring dạng đóng (critically damped, không nảy)

Mọi chuyển động vào/ra dùng đáp ứng bước của spring tắt dần tới
hạn — công thức đóng, không dùng easing nảy/đàn hồi, không dùng
spring mặc định có overshoot khi brief cấm nảy. Một giá trị đổi
đích nhiều lần bằng tổng các spring con, mỗi spring con bắt đầu
tại thời điểm đổi đích của nó.

```tsx
// Đáp ứng bước của spring tắt dần tới hạn: 0 tại t=0, tiến tới 1, không vượt 1.
export const springClosed = (t: number, omega = 6): number => {
  if (t <= 0) return 0;
  return 1 - (1 + omega * t) * Math.exp(-omega * t);
};

// Giá trị đổi đích tại các mốc t1..tn: cộng dồn từng spring con.
export const stepped = (
  changes: { at: number; from: number; to: number }[],
  t: number,
  omega = 6,
): number => {
  let value = changes.length ? changes[0].from : 0;
  for (const c of changes) {
    value += (c.to - c.from) * springClosed(t - c.at, omega);
  }
  return value;
};
```

Quy ước: phần tử phụ (ghi chú, chi tiết nhỏ) dùng `omega` nhỏ hơn
(chậm hơn) phần tử chính trong cùng một beat — lệch nhịp có chủ
đích, không đồng loạt.

### 5.3. Lưới nhịp (beat grid)

```tsx
export const BPM = 120;
export const BEAT = 60 / BPM; // 0,5 giây
export const beatAt = (beatIndex: number) => beatIndex * BEAT;
```

- Sự kiện quan trọng đặt tại `beatAt(n)` hoặc giữa hai beat.
- Khi nhạc có đoạn lên cao điểm, đoạn cao điểm đó phải trùng với
  đoạn hình dồn dập nhất; ghi rõ mốc cao điểm trong storyboard.
- Vòng lặp kín (chỉ khi brief yêu cầu loop): khung cuối phải trùng
  khung đầu — cả vị trí, tỉ lệ và pha của mọi phần tử.

### 5.4. Camera liên tục trên một thế giới

Đặt toàn bộ nội dung trong một "thế giới" có tọa độ cố định; camera
là một phép biến đổi duy nhất (dịch + tỉ lệ) tính từ `t`, áp lên
thế giới. Không đặt camera riêng cho từng đoạn; không dùng hai
camera. Kiểm tra khung cuối của mỗi lần camera tiến vào: không để
phần đầu trang/hàng thông tin trôi vào vùng biên.

```tsx
// camera(t) trả về {x, y, scale} — một chuyển động tại một thời điểm.
export const cameraAt = (t: number) => {
  const cx = stepped(
    [
      { at: 0, from: 0, to: 0 },
      { at: 5, from: 0, to: 320 },
      { at: 10, from: 320, to: 0 },
    ],
    t,
    2.2,
  );
  const scale = stepped(
    [
      { at: 0, from: 1, to: 1 },
      { at: 2.5, from: 1, to: 1.35 },
      { at: 10, from: 1.35, to: 1 },
    ],
    t,
    2.2,
  );
  return { x: cx, y: 0, scale };
};
```

Áp camera bằng một `div` bọc ngoài thế giới với `transform`
tính từ `cameraAt(t)`. Mọi đoạn đều sống trong cùng thế giới đó.

## 6. Luật cấm

Lấy từ các luật cấm đã ghi rõ trong nguồn (đặc biệt mục 110 và 183),
diễn đạt lại và áp cho mọi phim theo skill này:

- Không bịa nút, tính năng, màn hình, số liệu, slogan. Chỉ dùng
  những gì có trong chất liệu thật hoặc trong `SOURCE.md` hư cấu
  đã đóng băng.
- Không liệt kê tính năng. Mỗi đoạn một ý; chữ trên hình cực ít,
  rất ngắn; phim phải xem được cả khi tắt tiếng.
- Không chuyển cảnh chung chung: không mờ chồng (crossfade) cho mọi
  thứ, không quét ngẫu nhiên, xoay, nhiễu, lia máy liên tục, trượt
  sang trái kiểu mẫu chung, phóng to mờ. Chuyển đoạn chỉ bằng vật
  thể chung hoặc camera liên tục.
- Không easing nảy/đàn hồi, không rải hạt, không lạm dụng kính mờ/
  blur, không xoay thẻ 3D vô nghĩa, không phóng to liên tục, không
  thẻ kính, không dải màu chuyển sắc trang trí trên chrome giao diện,
  không chữ nảy.
- Không dùng nhiều phong cách animation khác nhau trong một phim;
  không bắt chước một quảng cáo cụ thể từng shot.
- Không khoảng lặng chết: mỗi beat có chuyện xảy ra; khung cuối giữ
  đủ lặng để ghi nhận (ít nhất khoảng 1 giây) trước khi hết phim.
- Không âm thanh có bản quyền; không SFX rải khắp; không để lớp phủ
  che mất phần tử thật của chất liệu (giao diện, tên tác giả, nhãn).
- Không dùng số cứng rải trong từng đoạn cho timeline/chuỗi chữ:
  timeline và chuỗi chữ tách riêng khỏi nội dung đoạn, tính từ
  lưới beat và storyboard.

## 7. Mẫu 15 giây

Khung mẫu cho showreel/promo 15 giây, 1920×1080, 30 fps, 120 BPM
(30 beat, mỗi đoạn 5 beat = 2,5 giây). Đây là khung, không phải
kịch bản cố định — thay nội dung, giữ nhịp và cơ chế.

| Mốc | Đoạn (một ý) | Camera / vật thể chung | Chữ trên hình |
|---|---|---|---|
| 0,0–2,5 s (beat 0–4) | Mở: dấu hiệu thương hiệu hé lộ, camera đi xuyên qua nó | Camera tiến chậm vào dấu hiệu; dấu hiệu là vật thể chung | Tên sản phẩm + một dòng mô tả ngắn |
| 2,5–5,0 s (beat 5–9) | Màn hình/tổng quan thật đầu tiên, con số chính hiện rõ | Một chi tiết từ đoạn mở nở thành khung màn hình | Con số chính + nhãn của nó (chỉ số có trong chất liệu) |
| 5,0–7,5 s (beat 10–14) | Chi tiết thứ hai: một phần tử từ màn hình trước nở thành đối tượng mới, đối tượng được sắp xếp gọn vào đúng vị trí | Chuyển bằng vật thể chung, không cắt cứng | Một câu ngắn nêu việc đang diễn ra |
| 7,5–10,0 s (beat 15–19) | Màn hình thật thứ hai, một khoảnh khắc trạng thái/con số vào đúng vị trí | Camera giữ, phần tử vào lệch nhịp theo spring | Trạng thái + con số (chỉ số có trong chất liệu) |
| 10,0–12,5 s (beat 20–24) | Nhịp chậm lại: nhiều tín hiệu thu về một khung nhìn có cấu trúc | Camera lùi dần, các tín hiệu thu về | Một câu chốt ngắn |
| 12,5–15,0 s (beat 25–29) | Kết: giao diện thu lại thành khối sản phẩm, dấu hiệu thương hiệu hiện rõ, giữ lặng | Camera kéo ra rồi đứng yên từ beat 28 | Tên sản phẩm + địa chỉ/slogan đúng từng chữ |

Âm thanh mẫu 15 giây: nhạc 120 BPM tự tổng hợp; một tiếng nhẹ
ở mỗi lần hé lộ lớn (beat 0, 5, 10, 15, 20, 25); tiếng kết ở
beat 28; còn lại im lặng. Trộn −14 LUFS.

## 8. Mẫu dài 90–100 giây (khung trong skill, không làm demo dài)

Khung cho showreel dài, theo mẫu mục 133 (90–100 giây,
1920×1080, khoảng 120 BPM, cắt theo nhịp, nhịp tổng thể lúc
nhanh lúc chậm theo câu chuyện). Chỉ là khung/mẫu trong skill;
không dựng demo dài theo skill này nếu chưa có brief riêng.

| Phần | Thời lượng gợi ý | Nội dung |
|---|---|---|
| Mở | ~10 giây | Tên + một câu về người làm/chủ thể; camera trên chất liệu thật đầu tiên |
| Chất liệu thật theo trình tự | ~55–65 giây | Chụp các trang/mục thật trong khung trình duyệt và khung điện thoại; mỗi shot một ý, vật thể chính đặt giữa, chừa khoảng thở; khóa ba màu và font của chính website/sản phẩm |
| Đoạn hỏi–đáp chữ lớn | ~10–15 giây | Câu hỏi và câu trả lời thật hiển thị lớn, đậm; chỉ dùng sự thật và con số có trên chất liệu thật |
| Kết | ~10 giây | Quay lại trang chủ/màn hình chính; tên + thông tin liên hệ đúng như chất liệu thật; giữ lặng cuối |

Luật riêng của mẫu dài: chuyển động mượt thay vì cắt cứng (trừ
điểm nhấn theo nhịp); không thêm SFX phụ; kiểm tra khung tĩnh ở
mọi điểm cắt trước khi render đủ; nhịp nhanh/chậm theo câu
chuyện, không đều đều suốt 90 giây.

## 9. Checklist QA (bắt buộc, ghi số đo thật)

- [ ] **Nguồn chân lý:** mọi nút/tính năng/số liệu/slogan trên hình
      đối chiếu được với chất liệu thật hoặc `SOURCE.md`; không có
      mục nào ngoài bảng.
- [ ] **Storyboard:** bảng mốc giờ khớp với video; mỗi đoạn một ý;
      vật thể chung nối các đoạn đã ghi rõ.
- [ ] **Khung tĩnh:** đã render và xem khung ở mọi mốc cắt + giữa
      đoạn; không chồng lấn, không cắt xén, không tràn chữ, không
      vật thể trôi vào vùng biên; chữ tiếng Việt đủ glyph, dấu
      đúng vị trí (chữ lớn dùng font có glyph tiếng Việt đầy đủ,
      ví dụ Be Vietnam Pro Black cho tiêu đề lớn).
- [ ] **Hàm thuần:** render cùng một frame hai lần cho cùng hình;
      render toàn bộ hai lần cho cùng MD5 (phần hình, trước khi
      gắn âm thanh) — ghi cả hai MD5.
- [ ] **Kỹ thuật:** `ffprobe` xác nhận khổ/fps/thời lượng/codec;
      `blackdetect` không có đoạn đen ngoài ý đồ; không crossfade,
      không easing nảy, không hạt/glow/shake trong code (grep
      kiểm tra).
- [ ] **Âm thanh:** đo loudness trên file bàn giao cuối
      (`loudnorm`/`volumedetect`); mục tiêu −14 LUFS; sự kiện âm
      thanh rơi đúng beat; ghi rõ nguồn nhạc/SFX và quyền dùng.
- [ ] **Xem/nghe:** ghi rõ đã xem/nghe trọn liên tục hay chưa; nếu
      chưa thì ghi rõ hạn chế đó, không báo "đã xem trọn" khi
      chỉ kiểm khung tĩnh.
- [ ] **Bàn giao:** đủ các mục ở bước 5, mục 5 của quy trình; không
      commit/push khi chưa được duyệt (cổng demo-trước-khi-duyệt).

## 10. Khung code tự viết (bộ khung tối thiểu)

```tsx
// src/Root.tsx — đăng ký composition, không chứa logic hình ảnh.
import React from "react";
import { Composition } from "remotion";
import { Film } from "./Film";

export const Root: React.FC = () => (
  <Composition
    id="RemotionGeneralFilm"
    component={Film}
    durationInFrames={450} // 15 giây x 30 fps
    fps={30}
    width={1920}
    height={1080}
  />
);
```

```tsx
// src/Film.tsx — thế giới duy nhất + camera duy nhất + đoạn theo beat.
// Mọi giá trị đều là hàm thuần của t; xem springClosed/stepped/cameraAt ở mục 5.
import React from "react";
import { AbsoluteFill, useCurrentFrame } from "remotion";
import { springClosed, stepped, cameraAt, BEAT } from "./motion";

export const Film: React.FC = () => {
  const frame = useCurrentFrame();
  const fps = 30;
  const t = frame / fps;
  const cam = cameraAt(t);
  const titleIn = springClosed(t - 0, 6);

  return (
    <AbsoluteFill style={{ background: "#0E0F12", overflow: "hidden" }}>
      <div
        style={{
          position: "absolute",
          width: 1920,
          height: 1080,
          transform: `translate(${-cam.x}px, ${-cam.y}px) scale(${cam.scale})`,
          transformOrigin: "0 0",
        }}
      >
        {/* Thế giới: mọi đoạn sống trong cùng một tọa độ. */}
        <div
          style={{
            opacity: titleIn,
            transform: `translateY(${(1 - titleIn) * 40}px)`,
            fontFamily: '"Be Vietnam Pro", sans-serif',
            fontWeight: 900,
            fontSize: 120,
            color: "#FFFFFF",
          }}
        >
          TÊN SẢN PHẨM
        </div>
        {/* Các đoạn tiếp theo: hiện theo beatAt(n), vào bằng springClosed. */}
      </div>
    </AbsoluteFill>
  );
};
```

```bash
# Render khung tĩnh ở mốc cắt trước khi render đủ, rồi render video câm.
npx remotion still src/index.tsx RemotionGeneralFilm --frame=75  still-2-5s.png
npx remotion render src/index.tsx RemotionGeneralFilm silent.mp4
# Gắn âm thanh đã trộn ở -14 LUFS (file âm thanh tự tổng hợp, xem mục 4 bước 4).
ffmpeg -y -i silent.mp4 -i music.wav -c:v copy -c:a aac -b:a 192k -shortest out.mp4
```

## 11. Nguồn tham khảo (theo nhóm mục, diễn đạt lại — không chép nguyên văn)

Nhóm 10 mục Remotion đã xác minh, credit thuộc về từng tác giả,
link nguồn theo từng mục:

- Nhóm showreel 15 giây giao toàn quyền, ghi dùng Remotion:
  vị trí 45 (@tequilafunks) — https://prompt-motion.com/tequilafunks-97f6c9 ;
  vị trí 119 (@TheViableEdge) — https://prompt-motion.com/theviableedge-9065be .
- Nhóm brief mở cho promo/showreel ứng dụng, ghi dùng Remotion:
  vị trí 147 (@elliot_garreffa) — https://prompt-motion.com/elliot-garreffa-f334bc ;
  vị trí 170 (@gautam_mer1) — https://prompt-motion.com/gautam-mer1-2ae354 ;
  vị trí 176 (@francoxavier33) — https://prompt-motion.com/francoxavier33-d2dfd2 .
- Nhóm explainer lấy nhận diện/chất liệu thật làm thước đo, ghi dùng
  Remotion: vị trí 99 (@imthatcarlos) — https://prompt-motion.com/imthatcarlos-e04bfe ;
  vị trí 139 (@aschapmann) — https://prompt-motion.com/aschapmann-131210
  (đọc chất liệu thật trước khi dựng, chữ theo nhịp, kiểm khung tĩnh).
- Nhóm phim sản phẩm có storyboard theo mốc giờ, cấm bịa, QA khung
  tĩnh, ghi dùng Remotion: vị trí 110 (@daniel_haida) —
  https://prompt-motion.com/daniel-haida-8691d4 (nguồn chính cho
  luật cấm, camera liên tục, chuyển bằng vật thể chung ở mục 6).
- Nhóm showreel dài chụp website thật, ghi dùng Remotion: vị trí 133
  (@wani_shola) — https://prompt-motion.com/wani-shola-16ca7a (nguồn
  chính cho mẫu dài 90–100 giây ở mục 8).
- Nhóm promo trên giao diện thật, camera liên tục, lưới nhịp, trộn
  −14 LUFS, ghi dùng Remotion: vị trí 183 (@antonio_kodheli) —
  https://prompt-motion.com/antonio-kodheli-490109 (nguồn chính cho
  camera liên tục, cắt khớp vị trí, QA khung tĩnh, mức −14 LUFS).

Tổng hợp và đối chiếu bao phủ: `~/workspace/prompt-motion/SYNTHESIS-122.md`
(mục 5, 7, 8) và `~/workspace/prompt-motion/partials/skill-coverage-baseline.md`.
106 mục UNVERIFIED chưa được học, không dùng làm nguồn cho skill này.
