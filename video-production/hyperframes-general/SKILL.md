---
name: hyperframes-general
description: "HyperFrames tổng quát ngoài video dọc có voice: phim motion ngắn khổ vuông hoặc ngang, KHÔNG voice, chỉ nhạc/SFX tổng hợp đồng bộ beat, vòng lặp kín seek(0)=seek(cuối). Dùng khi brief yêu cầu HyperFrames nhưng không phải video dọc 1080x1920 có giọng đọc tiếng Việt — ví dụ vòng lặp biến hình một hình khối, phim giấy, video hỏi-đáp theo ngày, promo ngắn, showreel 15 giây, phim lấy nhạc làm trung tâm. Không dùng cho video dọc có voice (đó là motion-video), không dùng cho giao diện web không xuất video."
---

# HyperFrames tổng quát — khổ vuông/ngang, không voice, vòng lặp kín

Skill này sở hữu quy trình dựng phim motion ngắn bằng HyperFrames cho mọi brief
**không thuộc phạm vi video dọc có voice**. Mọi nội dung trong skill này diễn
đạt lại cấu trúc bằng lời của người tổng hợp; không chép nguyên văn prompt,
copy hay artwork của tác giả trên prompt-motion.com. Credit thuộc về từng tác
giả, link nguồn ghi ở mục 8.

## 1. Khi nào dùng / không dùng

### Dùng skill này khi đồng thời có cả ba điều kiện

1. Stack là HyperFrames (thường đi cùng GSAP), hình vẽ bằng code trong một
   trang HTML tự chứa, render xác định bằng `seek(t)`.
2. Khổ **vuông** (ví dụ 1080×1080, 1440×1440) **hoặc ngang** (ví dụ
   1280×720, 1920×1080). Không có khổ dọc trong skill này.
3. **Không voice**: không giọng đọc, không phụ đề lời đọc. Âm thanh chỉ là
   nhạc và SFX tự tổng hợp, đồng bộ theo lưới beat. Phim phải hiểu được khi
   tắt tiếng, hoặc câu trả lời phải đọc được trọn vẹn trên hình.

### Không dùng — chuyển sang skill đúng phạm vi

| Yêu cầu | Đi đâu |
|---|---|
| Video dọc 1080×1920, kịch bản tiếng Việt + giọng đọc, karaoke caption, 5 variant A–E | `motion-video` — skill này KHÔNG được dùng để dựng lại phạm vi đó dưới tên khác |
| Chỉ cần hợp đồng composition, thuộc tính `data-*`, track, sub-composition, quy tắc render xác định | `hyperframes-core` (đọc trước khi viết HTML) |
| Chỉ cần quy tắc motion nguyên tử, blueprint cảnh, transition, adapter runtime | `hyperframes-animation` |
| Chỉ cần mix nhạc/SFX đã đặt sẵn (fade, ducking, EQ, bus) | `hyperframes-audio` — skill này chỉ định thiết kế âm thanh, không thay phần mix chuyên sâu |
| Chỉ cần lệnh CLI, chẩn đoán render, batch render, publish | `hyperframes-cli` |
| Chỉ cần tìm/cài block, component có sẵn trong registry | `hyperframes-registry` |
| Motion cho giao diện web, không xuất video | Các skill `motion-*` (UI demo) |
| Explainer dài có voice, cần lập luận sư phạm, reveal theo cue nói | Các skill `opus55-explainers` / `opus-explainer-*` |
| Game hoặc trải nghiệm tương tác chơi được | `opus55-interactive` / `opus-game-*` |
| Showreel/promo/explainer bằng Remotion tổng quát, chất liệu thật từ repo/website | Skill Remotion tổng quát (dự án riêng, không thuộc skill này) |
| Thế giới 3D thật, shader làm cả cảnh | `opus-3d-worlds`, `opus-3d-shader`, `opus-motion-threejs`, `opus-motion-shader` |

### Ranh giới với skill gần nhất (`motion-video`)

`motion-video` lấy HyperFrames làm stack lõi, nhưng phạm vi của nó khóa cứng:
dọc 1080×1920, giọng đọc tiếng Việt, caption karaoke, 5 variant chọn theo
routing. Skill này là phần bù đúng nghĩa: khổ vuông/ngang, không voice, không
caption karaoke, không variant A–E, không routing theo kịch bản nói. Một brief
vừa dọc vừa có voice thì thuộc `motion-video` dù chủ đề có giống mẫu trong
skill này; một brief vuông/ngang không voice thì thuộc skill này dù kỹ thuật
hình có giống `motion-video`. Không dựng cùng một chủ đề ở cả hai skill để
lách ranh giới.

### Ranh giới với các skill `hyperframes-*` còn lại

Các skill `hyperframes-*` là bộ phận chuyên môn (lõi, animation, âm thanh,
CLI, registry, studio, keyframes, creative). Skill này là skill **sở hữu quy
trình đầu–cuối** cho một lớp phim cụ thể; khi cần tra cứu chuyên sâu, đọc
skill bộ phận tương ứng và tuân theo nó, không viết lại quy tắc của nó tại
đây. Nếu yêu cầu chỉ nằm gọn trong một bộ phận (ví dụ chỉ hỏi lệnh CLI), dùng
trực tiếp skill bộ phận đó, không mở quy trình đầy đủ của skill này.

## 2. Đầu vào bắt buộc

Không bắt đầu dựng khi thiếu một trong các mục sau; hỏi đúng một lần, gọn,
rồi mới dựng:

1. **Khổ + fps + thời lượng**: vuông hay ngang, số pixel cụ thể, fps (mặc
   định 30), thời lượng giây (mặc định 14–15 giây cho vòng lặp/showreel;
   10 giây cho promo ngắn; 30 giây cho mẫu hỏi-đáp theo ngày nếu giữ đúng
   khung gốc — ghi rõ lựa chọn này là của người dựng khi trang nguồn không
   ghi thời lượng).
2. **Câu hỏi hoặc ý trung tâm duy nhất** mà phim trả lời, viết bằng tiếng
   Việt, cùng **đáp án thật có thể kiểm chứng** (ngày, giờ, tên, trạng thái).
   Không bịa số liệu, tỉ lệ, tên khách hàng, kết quả.
3. **Lưới beat**: BPM (mặc định 120 → beat 0,5 giây, bar 2 giây), mốc bắt
   đầu của từng beat, mốc nào là điểm nhấn (downbeat, đổi trạng thái, SFX).
   Nếu trang nguồn không ghi BPM, ghi rõ BPM là lựa chọn của người dựng.
4. **Bảng màu khóa cứng**: nền, mực/chữ, tối đa 2 màu nhấn, màu của trạng
   thái tối (nếu có chuyển sáng/tối). Không thêm màu ngoài bảng trong lúc
   dựng.
5. **Font chữ**: chữ lớn tiếng Việt dùng Be Vietnam Pro Black (kiểm glyph
   dấu tiếng Việt ở khổ lớn trước khi render); font phụ cho ghi chú/chữ nhỏ
   ghi rõ trong brief. Không dùng font render dấu nặng sai vị trí ở khổ lớn.
6. **Thiết kế âm thanh**: nhạc tổng hợp theo hợp âm nào, SFX nào ở mốc nào,
   có vòng lặp âm thanh kín tới mức nào. Không voice, không giọng clone,
   không gọi VieNeu API, không nhạc có bản quyền, không tải track ngoài.
7. **Tiêu chí vòng lặp**: phim có phải vòng lặp kín không. Mặc định trong
   skill này là **có**: `seek(0)` phải bằng `seek(thời lượng)`. Nếu brief
   yêu cầu phim có mở đầu/kết thúc rõ ràng (không lặp), ghi rõ ngoại lệ đó
   trong brief và bỏ kiểm tra vòng lặp ở mục 7 — không tự ý biến phim tuyến
   tính thành vòng lặp.

## 3. Quy trình

1. **Chốt beat grid trước khi viết code.** Liệt kê từng beat: khoảng thời
   gian, ý duy nhất, chữ trên hình, hình minh họa, mốc SFX. Một beat = một
   ý. Không beat nào mang hai ý, không ý nào trải qua hai beat.
2. **Vẽ storyboard tĩnh.** Chụp hoặc phác 1 khung đại diện cho mỗi beat.
   Kiểm tra: chữ không tràn, không chồng, không cấn viền; hình minh họa đọc
   được ở kích thước thật; trạng thái đầu và trạng thái cuối của vòng lặp
   giống nhau.
3. **Dựng trang HTML tự chứa.** Toàn bộ hình là SVG/HTML/CSS vẽ bằng code;
   không ảnh ngoài, không footage, không asset của mẫu gốc. Mọi trạng thái
   đều là hàm thuần của `t` qua `window.seek(t)` — không vòng lặp tự chạy,
   không `requestAnimationFrame` tự động, không trạng thái lưu giữa các lần
   gọi `seek` (xem mục 4).
4. **Tổng hợp âm thanh trong code.** Nhạc + SFX đều sinh từ dao động/nhiễu
   trong script (xem mục 5). Đặt SFX đúng mốc beat đã chốt ở bước 1. Chuẩn
   hóa về −14 LUFS trước khi encode.
5. **Render xác định.** Chụp từng subframe bằng trình duyệt headless, gọi
   `seek(t)` cho từng mốc, ghép bằng `tmix` để có motion blur (xem mẫu khung
   ở mục 6). Render lại từ đầu nếu môi trường bị thay giữa chừng; không vá
   nửa chừng bằng frame cũ.
6. **QA theo checklist ở mục 7.** Chưa đạt checklist thì chưa giao. Ghi rõ
   mọi điểm còn khác mẫu gốc và mọi lựa chọn suy định (khổ, fps, BPM, âm
   thanh) trong file QA.
7. **Bàn giao.** File MP4 + sheet ảnh tĩnh + file QA. Không commit, không
   push lên repo skill khi chưa có duyệt demo (cổng demo-trước-khi-duyệt);
   không dùng từ "xong/hoàn thành" khi chưa đủ tiêu chí QA.

## 4. Kỹ thuật hình — kỷ luật bắt buộc

- **`seek(t)` thuần.** Mọi thuộc tính thị giác (vị trí, tỉ lệ, xoay, độ
  mờ, độ dài nét vẽ) đều tính trực tiếp từ `t`. Không dùng easing của
  timeline chạy ngầm, không dùng trạng thái tích lũy. Gọi `seek` hai lần
  với cùng `t` phải cho cùng một khung hình; gọi ngược thời gian không
  được để lại dư trạng thái.
- **Spring dạng đóng.** Mọi chuyển động vào/ra dùng hàm spring tắt dần
  dạng đóng, ví dụ dạng chuẩn: `s(u) = 1 − (1 + w·u)·e^(−w·u)` với `u`
  là thời gian đã chuẩn hóa trong beat, `w` là độ cứng. Không dùng easing
  nảy (bounce), không dùng easing có vượt quá rồi dao động không tắt.
  Phần tử phụ (ghi chú, vật đi sau) dùng cùng họ spring nhưng `w` nhỏ hơn
  để tạo follow-through — vẫn là hàm đóng của `t`.
- **Beat grid.** Mọi lần đổi trạng thái rơi đúng mốc beat (bội số của
  `60/BPM`). Chuyển trạng thái bằng **cắt cứng + trượt vào bằng spring**.
  Cấm crossfade giữa hai trạng thái; cấm dissolve; cấm morph mờ dần từ
  trạng thái này sang trạng thái khác.
- **Vòng lặp kín.** Với thời lượng `D`, đặt pha `p = (t mod D) / D` và
  tính mọi chuyển động theo `p`. Điều kiện nghiệm thu: khung hình ở
  `seek(0)` và khung hình ở `seek(D)` trùng khớp từng pixel (kiểm tra bằng
  so sánh ảnh, xem mục 7). Một hình khối biến hình qua các trạng thái phải
  quay về đúng trạng thái đầu ở cuối vòng; một vòng quay phải quay đúng
  360° (hoặc bội số) trong `D`.
- **Một chuyển động chính mỗi lần chuyển.** Mỗi lần đổi beat chỉ có một
  chuyển động vào chính (thường là tiêu đề/hình khối chính trượt + co giãn
  nhẹ). Các chuyển động còn lại trong beat phải là phụ và thuộc cùng một ý.
- **Không hiệu ứng trang trí gây nhiễu.** Cấm particles, cấm glow
  (không `filter: blur()` làm quầng sáng, không drop-shadow phát sáng),
  cấm shake/rung màn hình, cấm hạt ăn mừng. Nét vẽ tay (nếu có) vẽ dần
  bằng `stroke-dashoffset` theo spring, không vẽ bằng hiệu ứng mờ.
- **Chữ.** Chữ lớn tiếng Việt dùng Be Vietnam Pro Black; kiểm glyph bằng
  công cụ font trước khi render (0 glyph thiếu). Tối đa 2 dòng cho chữ
  phụ; không để chữ cấn viền, chồng nhau, hoặc bị thanh trang trí đè.
  Không chrome giao diện trên hình: không thanh tiến trình, không timecode,
  không fps, không header giả.
- **Không bịa.** Không phần trăm, hệ số, tên khách hàng, con số kết quả
  trên hình trừ khi có nguồn kiểm chứng được ghi trong QA. Logo (nếu có)
  chỉ là wordmark bằng chữ, không đóng hộp file logo.

## 5. Kỹ thuật âm thanh — nhạc/SFX tổng hợp, không voice

- **Không voice dưới mọi hình thức.** Không giọng đọc, không giọng tổng
  hợp, không giọng clone, không gọi VieNeu API hay bất kỳ API giọng đọc
  nào. Thiết kế âm thanh của skill này không có bước kiểm tra giọng đọc.
- **Nhạc tổng hợp trong code.** Pad/bass/arp sinh từ dao động sine/tam
  giác, nhiễu lọc mềm; tiến trình hợp âm viết rõ theo bar, bar cuối quay về
  hợp âm mở đầu để vòng lặp âm thanh càng kín càng tốt. Mọi nốt đều rơi
  đúng lưới beat đã chốt.
- **SFX tổng hợp, đặt đúng mốc.** Mỗi điểm nhấn hình ảnh có tối đa một
  SFX (tick, pop, chime, sweep). SFX phải decay xong trước khi vòng lặp
  quay lại mốc đó; không SFX nào có đuôi vang cắt ngang qua điểm nối vòng
  lặp. Ghi bảng mốc SFX trong QA.
- **Vòng lặp âm thanh.** Mục tiêu: mẫu âm thanh ở đầu và cuối vòng lặp
  khớp nhau (cùng hợp âm, cùng pha lưới beat, biên độ đầu/cuối gần bằng
  nhau). Đo và ghi chênh lệch RMS của 50 ms đầu/cuối trong QA; nếu chênh
  lệch nghe được, ghi rõ là điểm còn khác, không ghi "vòng lặp kín tuyệt
  đối" cho âm thanh khi chưa đo được.
- **Trộn và chuẩn hóa.** Nhạc nền nhẹ, không lấn SFX; không clip (đỉnh
  dưới 0 dBFS); chuẩn hóa 2-pass về **−14 LUFS**, true peak ≤ −1 dBTP.
  Đo lại loudness trên file MP4 cuối sau khi encode AAC, vì encode có thể
  làm loudness dịch chuyển; ghi cả hai số đo trong QA.

## 6. Mẫu khung code (tự viết, không sao chép từ mẫu gốc)

Khung dưới đây là cấu trúc tối thiểu; mỗi dự án tự viết tiếp phần vẽ của
mình theo beat grid đã chốt. Không dùng CSS `transition`/`animation` — mọi
trạng thái suy ra từ `seek(t)`.

```html
<!DOCTYPE html>
<html lang="vi">
<head><meta charset="utf-8"><style>
  /* Font: Be Vietnam Pro (Black cho chữ lớn). Không transition/animation CSS. */
  html, body { margin: 0; overflow: hidden; }
  #stage { position: relative; }
</style></head>
<body>
<div id="stage"><!-- SVG/HTML vẽ bằng code, mỗi beat một nhóm riêng --></div>
<script>
(function () {
  "use strict";
  var DUR = 14; // giây — vòng lặp kín: seek(0) === seek(DUR)
  function clamp01(x) { return x < 0 ? 0 : (x > 1 ? 1 : x); }
  // Spring tắt dần dạng đóng: s(u) = 1 - (1 + w*u) * exp(-w*u).
  function spring01(u, w) {
    if (u <= 0) return 0;
    w = w || 6;
    return 1 - (1 + w * u) * Math.exp(-w * u);
  }
  function smooth01(u) { u = clamp01(u); return u * u * (3 - 2 * u); }
  // Lưới beat: BPM 120 -> beat 0.5s, bar 2s. BOUNDS là mốc bắt đầu mỗi beat.
  var BOUNDS = [0, 2, 4, 6, 8, 10, 12, 14];
  function beatIndex(phase) {
    var t = phase * DUR;
    for (var i = 0; i < BOUNDS.length - 1; i++) {
      if (t < BOUNDS[i + 1]) return i;
    }
    return BOUNDS.length - 2;
  }
  window.seek = function (t) {
    // Quấn vòng: t = DUR quay về đúng trạng thái t = 0.
    var wrapped = ((t % DUR) + DUR) % DUR;
    var phase = wrapped / DUR;
    var idx = beatIndex(phase);
    var lt = wrapped - BOUNDS[idx]; // thời gian trong beat hiện tại
    // ... đặt visibility + transform cho từng nhóm beat theo idx/lt,
    // mọi giá trị đều tính từ spring01/smooth01, không lưu trạng thái ...
    window.__ready = true;
  };
  window.seek(0);
})();
</script>
</body>
</html>
```

Render xác định: chụp subframe bằng trình duyệt headless, mỗi subframe gọi
`seek(t)` rồi chụp; ghép subframe bằng `tmix` (ví dụ 3 subframe → 30 fps)
để có motion blur; ghép nhạc/SFX đã chuẩn hóa ở bước encode cuối. Kiểm tra
tính xác định bằng cách render cùng một mốc `t` hai lần và so sánh ảnh.

## 7. Checklist QA (bắt buộc trước khi giao)

- [ ] `ffprobe`: đúng khổ, đúng fps, đúng thời lượng (sai số < 1 frame),
  có đủ stream video + audio (AAC stereo), codec đúng chuẩn bàn giao.
- [ ] `blackdetect`: không đoạn đen ngoài ý đồ (chạy 2 ngưỡng, ghi kết quả).
- [ ] Loudness: đo trên file MP4 cuối bằng `loudnorm` (ghi integrated,
  true peak, LRA) và `volumedetect`; mục tiêu −14 LUFS, không clip.
- [ ] Vòng lặp kín (hình): ảnh chụp ở `seek(0)` và `seek(DUR)` trùng khớp
  (ghi số pixel khác nhau và độ lệch trung bình; mục tiêu 0). Ảnh chụp ở
  `seek(0)` hai lần cũng phải trùng khớp (tính xác định).
- [ ] Vòng lặp âm thanh: ghi chênh RMS 50 ms đầu/cuối và nhận xét nghe được
  hay không; không ghi "kín tuyệt đối" nếu chưa đo.
- [ ] Chữ: 0 glyph thiếu (kiểm bằng fontTools trên đúng font đã dùng);
  xem sheet ảnh tĩnh, xác nhận không tràn, không chồng, không cấn viền ở
  mọi beat.
- [ ] Luật cấm: grep/đọc lại code, xác nhận không crossfade, không easing
  nảy, không particles/glow/shake, không voice, không nhạc ngoài, không
  nội dung bịa, không copy/artwork của mẫu gốc.
- [ ] Hạn chế ghi rõ: chưa xem/nghe trọn liên tục trong trình phát (nếu có);
  mọi thông số suy định (khổ, fps, BPM, âm thanh) ghi rõ là suy định, kèm
  căn cứ là trang nguồn không ghi.

## 8. Mẫu hình tái dùng (diễn đạt lại, theo nhóm mục nguồn)

Nguồn duy nhất là các trang công khai trên prompt-motion.com đã đọc trong
đợt khảo sát 04/11/2026. Mọi dòng dưới đây diễn đạt lại cấu trúc, không chép
nguyên văn. Các mục nguồn phần lớn chỉ ghi tiêu đề + tác giả + thời lượng;
khổ, fps, BPM, luật cấm thường không ghi trên trang — phần nào suy định phải
ghi rõ khi tái dùng.

### 8.1. Mẫu phim giấy (vị trí 132)

- Credit: @ik_builds — https://prompt-motion.com/ik-builds-b8bdcf
- Cấu trúc diễn đạt lại: phim ra mắt sản phẩm ngắn, nền giấy sáng, chữ
  động khổ lớn, một lần chuyển dứt khoát sang nền tối rồi quay về nền
  sáng, nhịp ý nhanh (mỗi ý khoảng 1,5–2 giây), một âm thanh ở mỗi điểm
  nhấn, vật thể tuân theo vật lý thật (rơi, chạm, dẹp lại), ghi chú viết
  tay vẽ dần bằng nét, không chrome giao diện, không thuật ngữ làm phim
  trên hình, không kết quả bịa.
- Khi tái dùng: giữ khung nền giấy + chữ lớn + chuyển sáng/tối + nhịp ý
  nhanh; thay toàn bộ chủ đề, copy, hình minh họa, bảng màu cụ thể. Không
  dùng lại chữ hay hình của mẫu gốc.

### 8.2. Mẫu hỏi-đáp theo ngày (vị trí 81)

- Credit: @tankazunori0914 — https://prompt-motion.com/tankazunori0914-0fc886
- Cấu trúc diễn đạt lại: video tiện ích 30 giây, có nhạc nền làm khung
  nhịp, trả lời một câu hỏi đời thường mà đáp án thay đổi theo ngày/giờ,
  trong đúng một khung thời gian cố định; không yêu cầu giọng đọc. Trang
  không ghi khổ, fps, BPM, luật cấm.
- Khi tái dùng: giữ khung "một câu hỏi + đáp án thay đổi theo thời gian +
  nhạc nền làm nhịp"; thay câu hỏi và đáp án bằng câu hỏi/đáp án thật của
  người dùng, kiểm chứng đáp án theo ngày giờ thật; khổ/fps/BPM do người
  dựng chọn và ghi rõ là suy định.

### 8.3. Các mục còn lại trong nhóm 6 mục nguồn (ghi rõ độ thưa)

- Vị trí 118 — Credit: @jesscaroline7 —
  https://prompt-motion.com/jesscaroline7-1ff7cb — reel chuyển động cho
  một ứng dụng, trang không ghi thời lượng, khổ, fps, BPM hay âm thanh;
  điểm ghi nhận duy nhất là công cụ dựng. Tái dùng ở mức khung showreel
  chung, không suy đoán thêm chi tiết.
- Vị trí 122 — Credit: @reyzostyle —
  https://prompt-motion.com/reyzostyle-b55864 — promo sản phẩm 10 giây,
  sản phẩm chỉ định bằng đường link đính kèm, trang không ghi khổ, fps,
  BPM hay âm thanh. Tái dùng: biến thể promo ngắn hơn, đọc chất liệu từ
  link thật thay vì bịa.
- Vị trí 130 — Credit: @Rames_Jusso —
  https://prompt-motion.com/rames-jusso-589f80 — brief lấy nhạc làm trung
  tâm: chỉ khóa tempo 140 BPM và phong cách nhạc; yếu tố hình chỉ xuất
  hiện ở tiêu đề trang, không xuất hiện trong brief hiển thị. Tái dùng:
  khi brief lấy nhạc làm trung tâm, khóa tempo + phong cách, hình ảnh đi
  theo nhịp; ghi rõ phần nào suy định từ tiêu đề.
- Vị trí 186 — Credit: @danilowm —
  https://prompt-motion.com/danilowm-d3720d — showreel 15 giây phô diễn
  năng lực motion, gắn vào bối cảnh một dự án cụ thể đang làm; trang
  không ghi khổ, fps, BPM, cấu trúc beat hay âm thanh. Tái dùng: gắn
  showreel vào ngữ cảnh dự án thật thay vì showreel tách rời.

## 9. Luật cấm tổng hợp

1. Cấm video dọc, cấm voice/giọng clone/VieNeu, cấm caption karaoke theo
   lời đọc trong skill này.
2. Cấm crossfade/dissolve, easing nảy, particles, glow, shake.
3. Cấm chép nguyên văn prompt/copy/artwork của tác giả; cấm tải video/file
   gốc; cấm dùng nội dung ngoài các nguồn đã ghi.
4. Cấm bịa số liệu/kết quả; cấm dùng ảnh/footage ngoài; cấm thêm màu, font,
   hiệu ứng ngoài brief đã chốt.
5. Cấm commit/push repo skill khi chưa qua cổng demo-trước-khi-duyệt; cấm
   báo "xong" khi chưa đủ checklist QA ở mục 7.
