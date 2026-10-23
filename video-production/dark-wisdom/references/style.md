# Style System — Dark Wisdom v1.3.5

Tinh thần: **u ám, tĩnh, sang**. Visual không tranh spotlight với lời đọc.

## Canvas
- 1080×1920 (9:16), 30fps. Cả bản dài và reels.
- Nền: gradient tối (đen → xanh navy đậm #05070F), ambient particles rất mờ,
  chậm. Không hiệu ứng nhanh, không confetti, không màu neon rực tràn màn hình.

## Visual elements
- **Minh họa**: KHÔNG dùng icon (bỏ hẳn từ v1.3.4 — user thấy rối mắt).
  Chỉ còn chữ + nền B-roll điện ảnh — xem mục "Hệ layered cinematic
  (v1.3.5)" bên dưới.
- **Waveform** kiểu seed cũ: thanh dọc mảnh (3px), vàng gold #D8B36A, **ĐỘNG
  theo RMS audio** (v1.3.5 — user yêu cầu "phải động như cũ"), ở 1/4 dưới
  màn hình — dấu hiệu nhận biết của dòng video này.
- **Watermark** tên kênh ở đầu khung hình, mờ 40%, xuyên suốt.
- **Waveform** audio chạy ở 1/4 dưới màn hình — dấu hiệu nhận biết của dòng
  video voiceover, tạo cảm giác "đang nghe một bí mật được đọc lên".
- **Hook scene**: chữ IN HOA cỡ cực lớn (Anton 140–200px) căn giữa, nền gần
  như đen hoàn toàn. Giữ 3–4 giây.

## Subtitle (quan trọng nhất)
- Chữ trắng lớn (Plus Jakarta Sans 600, 64–76px), **căn giữa màn hình**,
  hiện theo **cụm từ** (2–6 từ), không karaoke từng chữ.
- **Keyword** (từ đinh của câu): phóng to 1.3x + tô màu đỏ (#FF3B5C) hoặc
  hồng — đây là signature của kênh tham khảo.
- Tối đa 2 dòng một lúc, không che waveform.

## Color semantics
- Trắng: lời kể trung lập. Đỏ/hồng: sự thật phũ / cảnh báo.
- Vàng mờ (#D8B36A): quy luật, "luật ngầm", câu chốt. Xanh nhạt: ví dụ/case.

## Fonts (bundle sẵn)
`~/workspace/skills/motion-video/assets/fonts/` — Anton (hook/display),
Plus Jakarta Sans 600/700 (subtitle/body). Luôn khai báo subset
latin+vietnamese + unicode-range, verify 0 missing glyph bằng fontTools.

## Những điều CẤM
- Không pill title trượt từ trái, không card bay từ phải (đó là DNA của
  motion-video/Beeknoee — kênh này phải khác).
- Không `backdrop-filter` (crash headless Chromium). `filter: blur()` ok.
- Không `opacity:0` trên `[data-start]` clip.
- Không chèn icon (bỏ hẳn từ v1.3.4) — mắt người xem nghỉ, chỉ tập trung
  vào chữ và nền.

## Tiêu chuẩn hoàn thiện visual — "sang, xịn, mịn"

Mọi video xuất xưởng phải qua vòng soi visual này. Một lỗi cũng không được
lọt:

1. **Nhất quán tuyệt đối:** cùng một font, cùng cỡ chữ, cùng vị trí subtitle
   suốt video. Watermark cùng độ mờ, cùng vị trí. Không frame nào "lạc tông".
2. **Hook scene phải choáng:** 3–4 giây đầu — chữ in hoa cực lớn, nền gần như
   đen, không chi tiết thừa. Người xem phải cảm thấy "có chuyện lớn sắp được
   nói".
3. **Subtitle đọc được trong 1 cái liếc mắt:** tối đa 2 dòng, cụm từ 2–6 từ,
   keyword phóng to + đỏ/hồng đúng từ đinh (không tô màu bừa). Không che
   waveform, không tràn viền.
4. **Nhịp thở visual:** mỗi beat 1–2 visual tĩnh, crossfade chậm. Không beat
   nào để màn hình trơ trụi chỉ có chữ quá 10 giây, không beat nào nhồi quá
   2 visual.
5. **Waveform CLASSIC — ĐỘNG, kiểu ảnh reference (v1.3.6):** ngang, **căn
   giữa** (~70% chiều rộng, strip 760×230 đặt y=1500), 70 thanh dọc 5px có
   khe hở, **đối xứng qua trục giữa** (kiểu waveform audio cổ điển), màu
   **trắng #F2F2F2** (alpha theo biên độ). Nhãn **"NGẦM ĐỜI · ĐANG KỂ"**
   nhỏ, letter-spacing rộng, xám trắng mờ #9AA0A6, ngay trên waveform.
   Animation: RMS audio thật (window 50ms, 30fps) + **EMA làm mượt**
   (attack 0.35 / release 0.90 theo từng thanh) → lên xuống êm, không giật;
   idle floor khi im lặng. Ngưỡng QA: diff pixel vùng waveform giữa 2 frame
   cách 1s ≥ 5; **max jump giữa 2 frame liên tiếp < 40%**.
6. **Kỷ luật màu sắc:** chỉ dùng palette đã định (trắng / đỏ-hồng / vàng mờ /
   xanh nhạt). Không màu lạ lọt vào bất kỳ frame nào.
7. **Soi 3 cỡ màn hình:** kiểm tra screenshot ở kích thước đầy đủ, thu nhỏ
   bằng điện thoại (xem trên mobile thật nếu được), và thumbnail — chữ vẫn
   đọc được, bố cục không vỡ.

## Nâng cấp v1.2 — vượt đối thủ (motion & finish)

Đối thủ giữ visual gần như tĩnh hoàn toàn. Mình giữ triết lý "tĩnh" nhưng
thêm 4 lớp sống động tinh tế — đủ để vượt, không đủ để phá nhịp chậm:

1. **Keyword pop:** khi voice đọc tới keyword (từ tô đỏ, cỡ 76px = 1.19x chữ
   trắng 64px, cùng baseline), keyword pop-in sau cụm trắng 0.12s qua 3 bước
   scale 0.82 → 0.91 → 1.0 (mỗi bước 0.1s, pre-render trong PIL). Một cú
   "nảy" duy nhất mỗi keyword — mắt người xem bị hút đúng chỗ cần nhớ.
2. **Ken Burns siêu chậm:** nền B-roll mỗi beat zoom 1.00 → 1.04 trong suốt
   thời lượng beat (linear, không ease). Gần như không nhận ra khi xem, nhưng
   video hết cảm giác "ảnh chết".
3. **Film grain:** overlay noise rất nhẹ (opacity 4–6%) toàn video. Tạo cảm
   giác điện ảnh, phân biệt với video dựng vội. Render rẻ, hiệu quả cao.
4. **End card (5s):** như narrative.md — nền đen tuyền, quote vàng #D8B36A
   (Plus Jakarta Sans 700, 72px, căn giữa), fade-in chậm 1s, giữ 3s, fade-out
   1s. Dưới quote: "NGẦM ĐỜI" nhỏ + dòng "Theo dõi để nghe sự thật mỗi ngày".

Cấm: không thêm quá 4 hiệu ứng này; không nhanh dần nhịp; không màu mới.

## Hệ layered cinematic (v1.3.5)

Từ v1.3.4, mỗi beat dựng theo 2 lớp chồng (bỏ hẳn lớp icon — user thấy rối
mắt, chữ + nền là đủ):

- **Lớp 1 (đáy) — B-roll điện ảnh:** clip từ `assets/broll/` (xem
  `assets/broll/manifest.json`). **LUẬT CỨNG (user 10/10): nền phải CHẠY ĐỦ
  THỜI LƯỢNG video — TUYỆT ĐỐI KHÔNG lấy clip ngắn rồi loop lại.** Mỗi video
  dùng clip dài ≥ thời lượng video; nếu không có clip đơn đủ dài, nối NHIỀU
  clip KHÁC NHAU thành montage (crossfade 0.8–1.2s giữa các clip) — cấm lặp
  lại cùng một cảnh. Thư viện `assets/broll/` phải luôn có bản full-duration
  (60–120s) cho mỗi mood; clip ngắn 10–15s chỉ dùng khi video ≤15s.
  Xử lý bắt buộc: phủ đen **35–45%** (KHÔNG blur, khử bão hòa nhẹ ~15%) →
  nền hiện **55–65%, đọc được chi tiết** (hẻm phố, dây điện, xe, người đi
  bộ) ở khoảng cách xem điện thoại. Thêm vignette vừa (PI/3.5) để đỉnh/đáy
  tối dần, chữ dễ đọc. Ngưỡng kiểm tra: pause frame bất kỳ giữa beat — nếu
  không nhận ra được cảnh đang quay gì thì overlay đang quá dày, phải giảm.
  **Nền KHÔNG bao giờ được sáng hơn subtitle** — nếu clip có vùng sáng
  chói, hạ brightness vùng đó hoặc đổi clip.
- **Lớp 2 — chữ (vua):** subtitle **kiểu seed cũ** + keyword pop + waveform +
  watermark + tagline. Quy tắc (áp dụng MỌI video, không chỉ demo):
  **mỗi lần chỉ hiện DUY NHẤT 1 cụm ngắn 4–7 từ (1–2 dòng)**, chữ thường
  (sentence case), font đậm; chữ **#FFFFFF 64px**, **từ khóa #FF4D6D
  (đỏ/hồng) 76px — TO HƠN 1.15–1.2x** so với chữ trắng để nổi bật;
  baseline căn khít (vẽ cùng baseline, anchor="ls"); KHÔNG hiện cụm xám
  trước/sau. Keyword pop: cụm trắng fade-in 0.25s, từ khóa pop-in sau
  0.12s (scale 0.82 → 0.91 → 1.0, mỗi bước 0.1s, pre-render trong PIL).
  Thêm viền chữ mỏng (`borderw=2, bordercolor=black@0.6`) để đọc được trên
  vùng nền sáng. Chữ luôn là lớp nổi bật nhất.
- **Waveform CLASSIC — ĐỘNG (v1.3.6):** ngang căn giữa (~70% rộng, strip
  760×230, y=1500), 70 thanh dọc 5px đối xứng qua trục giữa, trắng #F2F2F2,
  nhãn "NGẦM ĐỜI · ĐANG KỂ" (#9AA0A6, letter-spacing rộng) phía trên. RMS
  thật + EMA (attack 0.35 / release 0.90) → mượt; idle floor khi im lặng.
  KHÔNG dùng waveform full-width đáy hay màu vàng. Kỹ thuật: render 30
  frame PNG/giây bằng PIL → encode qtrle .mov giữ alpha → overlay
  x=(W-760)/2, y=1500. Lưu ý font: chỉ dùng font có đủ glyph Latin+Việt
  (PJS-700.ttf); các bản subset *-vi.ttf thiếu chữ Latin cơ bản → tofu.

**Quy tắc chọn nền theo beat** (map theo cảm xúc, không theo nghĩa đen):
- cô độc / sự thật phũ → `broll-pho-dem.mp4` (người đi một mình phố đêm)
- tiền / làm giàu / vật chất → `broll-bokeh-xe.mp4` (phố đêm bokeh đèn xe)
- gia đình / quan hệ / khoảng cách → `broll-mua-kinh.mp4` (mưa trên kính đêm)
- tầng lớp / quyền lực / khoảng cách giàu nghèo → `broll-toa-nha.mp4`
- bản chất con người / đám đông → `broll-dam-dong.mp4` (phố nhòe ẩn danh)
- cảm xúc mạnh / nội tâm dữ dội → `broll-bien-dem.mp4` (sóng biển đêm)
- beat kết / hy vọng le lói → `broll-nen.mp4` (nến trong bóng tối)
- **KHÔNG** dùng clip sáng/chói/lòe loẹt; nếu không có clip hợp cảm xúc
  beat → fallback về nền gradient tối thuần kiểu cũ (đen → navy #05070F).
- Chuyển beat: crossfade chậm 0.8–1.2s cả 2 lớp cùng lúc (không cắt khô).

**Giữ nguyên 4 nâng cấp v1.2:** keyword pop, Ken Burns siêu chậm, film grain
4–6%, end card 5s. End card vẫn nền đen tuyền (không B-roll) để chốt sang.
