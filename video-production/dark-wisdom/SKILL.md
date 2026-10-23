---
name: "dark-wisdom"
description: "Dark Wisdom: sản xuất video kể chuyện triết lý 'dark' kiểu TĨNH ĐAO — kịch bản dài tiếng Việt (tâm lý, tư duy tầng lớp, binh pháp ứng xử), giọng Đời - Nam (VieNeu, nam miền Bắc) kể chuyện chậm, visual tĩnh nền tối + waveform + subtitle lớn căn giữa, bản dài 6–9 phút + bản cắt reels 60–90s, nhạc ambient u ám, QA và link tải. Dùng khi user nói 'Dark Wisdom', 'kênh triết lý', 'video kể chuyện dark', 'làm video kiểu Tĩnh Đao', 'Ngầm Đời', hoặc gửi một chủ đề triết lý/tâm lý/tư duy/làm giàu cần dựng thành video dài + reels."
metadata: { "includeInPrompt": true, "version": "1.3.7" }
---

# Dark Wisdom

## Purpose
Biến một chủ đề triết lý/tâm lý (ví dụ: bản chất bi kịch gia đình, tư duy kẻ
mạnh, quy luật tiền bạc, quan hệ nam–nữ) thành **video kể chuyện "dark"**
hoàn chỉnh: kịch bản dài tiếng Việt → giọng nam trầm kể chuyện chậm →
composition tĩnh nền tối + waveform + subtitle lớn → **bản dài 6–9 phút**
(feed) + **bản cắt reels 60–90s** (9:16) → nhạc ambient → QA → link tải.
**Không trả kế hoạch suông.**

Điểm khác biệt cốt lõi so với `motion-video`: nội dung này dẫn dắt bằng
**lời đọc**, không phải bằng hình. Hình ảnh gần như tĩnh, tối giản, u ám —
vai trò của visual là tạo không khí và giữ mắt người xem, không phải giải
thích.

## Workflow
1. **Intake**: nhận chủ đề + góc nhìn (sự thật phũ phàng nào muốn nói?) từ user.
   Tự dựng narrative theo `references/narrative.md` nếu user không đưa kịch bản.
   Kịch bản bản dài: 900–1.400 từ (~6–9 phút đọc ở tốc độ chậm).
2. **Voice**: đọc `references/voice.md`. VieNeu API (skill `vieneu-api-client`),
   voice `Đời - Nam` (VieNeu, nam miền Bắc — user chốt 09/10/2026), speed
   **0.95** (chậm, trầm, kể chuyện).
   **Cấm thay giọng khác.**
3. **Scaffold**: `python3 bin/new_project.py --slug <ten> --title "<tieu de>"`
   → project mới. (Có thể tái dùng template tại
   `~/workspace/motion-video-template/`.)
4. **Composition**: dựng scenes theo `references/style.md` — **hệ layered
   cinematic (v1.3.1)**: lớp 1 B-roll điện ảnh hiện rõ 55–65% (phủ đen
   35–45%, KHÔNG blur, desat nhẹ ~15% + vignette PI/3.5 — nền phải đọc được
   chi tiết ở khoảng cách xem điện thoại), lớp 2 icon neon từ `assets/icons-v2/`
   (380–460px, 1/3 trên, glow nhẹ), lớp 3 subtitle **karaoke** (in hoa đậm;
   cụm đang đọc #FFFFFF, cụm trước/sau #7A7F87, viền chữ mỏng) + keyword
   phóng to/tô màu đỏ-hồng + waveform + watermark + tagline. Mỗi beat map 1
   clip nền theo cảm xúc (`assets/broll/manifest.json`); không clip hợp →
   fallback gradient tối thuần. Font: Plus Jakarta Sans 600/700 (subtitle) +
   Anton (hook) — bundle tại
   `~/workspace/skills/motion-video/assets/fonts/`, luôn khai báo đủ subset
   latin+vietnamese + unicode-range.
5. **Render**: `TMPDIR=<project>/tmprender npx hyperframes@0.8.127 render`
   (/tmp chỉ 512MB). Render lại từ đầu nếu VM bị replace giữa chừng.
6. **Reels cutdown**: từ bản dài, chọn 1 đoạn 60–90s có hook mạnh nhất, cắt
   bằng ffmpeg (giữ nguyên audio), thêm caption giật gân in hoa.
7. **Audio**: voice giữ nguyên tempo chậm → nhạc ambient u ám pad tự tổng
   hợp (numpy) ở mức rất thấp, sidechain ducking dưới VO → `alimiter=limit=0.95`.
   **Không** dùng whoosh/click/pop dồn dập — nhịp của kênh này là chậm.
8. **QA** (bắt buộc trước khi báo xong): ffprobe 1080x1920/30fps/h264+aac;
   loudness + peak (không clip); screenshots 8 scenes + midpoints; subtitle
   khớp voice theo cụm từ; verify 0 missing glyph bằng fontTools; số liệu/
   trích dẫn on-screen khớp nguồn (nếu có).
9. **Deliver**: upload lấy URL (kèm expiry), báo duration/size/version/changelog
   (bản dài + bản reels), source project path, contact sheet QA. Không dùng từ
   "xong/hoàn thành" khi chưa đủ tiêu chí.

## Tiêu chuẩn chất lượng — quy chuẩn xuất xưởng (v1.1.0)

Mọi video của kênh Ngầm Đời, dù làm thủ công hay chạy tự động mỗi ngày, đều
phải vượt qua **4 cửa** dưới đây mới được coi là xong. Đây là cam kết chất
lượng cao nhất, không có ngoại lệ "tạm được":

1. **Cửa nội dung** (`references/narrative.md`): 6 tiêu chí XỊN + tự chấm
   điểm từng beat (≥4/5) + 8 công thức hook đã kiểm chứng + red-team pass.
2. **Cửa giọng đọc** (`references/voice.md`): đúng giọng/tốc độ, ngắt nghỉ
   có chủ đích, hook có trọng lượng, nghe lại toàn bộ không lỗi phát âm.
3. **Cửa visual** (`references/style.md`): nhất quán tuyệt đối, hook scene
   choáng, subtitle đọc được trong 1 liếc mắt, waveform sống, kỷ luật màu,
   soi 3 cỡ màn hình.
4. **Cửa kỹ thuật** (`references/pipeline.md`): ffprobe, loudness, font,
   screenshot, facts khớp nguồn.

Chi tiết từng cửa nằm trong file references tương ứng; checklist tổng hợp
nằm ở `references/pipeline.md` mục "QA checklist". Một ô chưa tick = video
chưa xong = không báo "xong", không đăng, không giao.

## Changelog v1.3.7 — luật nền full-duration, KHÔNG loop clip ngắn (10/10/2026)

User chốt: "chỗ video nền thì phải chạy đủ giờ nhé, k đc lấy video ngắn rồi loop lại".
- **Luật cứng:** B-roll nền phải chạy ĐỦ thời lượng video — cấm lấy clip ngắn
  10–15s loop lại. Mỗi video dùng clip dài ≥ thời lượng video; nếu không có
  clip đơn đủ dài, nối NHIỀU clip KHÁC NHAU thành montage (crossfade
  0.8–1.2s) — cấm lặp lại cùng một cảnh.
- Thư viện `assets/broll/` phải có bản full-duration (60–120s) cho mỗi mood;
  clip ngắn chỉ dùng khi video ≤15s.
- Visual giữ nguyên 100% v1.3.6 (chuẩn đã chốt).

## Changelog v1.3.6 — waveform CLASSIC theo ảnh reference của user (10/10/2026)

Mục tiêu: user gửi ảnh reference — "loại thanh này đâu sao k dùng, hãy dùng
thanh này và điều chỉnh cho mềm mượt lại là đẹp".
- **Waveform kiểu classic:** ngang, căn giữa (~70% chiều rộng, strip 760×230
  đặt y=1500), 70 thanh dọc 5px có khe hở, **đối xứng qua trục giữa** (kiểu
  waveform audio cổ điển), màu **trắng #F2F2F2** (alpha theo biên độ).
- **Nhãn "NGẦM ĐỜI · ĐANG KỂ":** nhỏ, letter-spacing rộng, xám trắng mờ
  #9AA0A6, đặt ngay trên waveform như ảnh.
- **Mềm mượt:** RMS audio thật (window 50ms, 30fps) + EMA attack 0.35 /
  release 0.90 theo từng thanh → thanh lên xuống êm, không giật cục; idle
  floor khi audio im lặng.
- QA: diff pixel vùng waveform giữa 2 frame cách 1s = 6.9 (động rõ, trên
  nhiễu nén ~2–3); max jump giữa 2 frame liên tiếp = 0.198 (< 0.40 ngưỡng);
  loudness −14.22 LUFS / true peak −0.77 dB; fontTools zero tofu.
- **Bài học font:** các file subset `*-vi.ttf` (PJS-600-vi, PlusJakartaSans-
  600-vietnamese) THIẾU cả chữ Latin cơ bản → nhãn render ra tofu; chỉ dùng
  font full-glyph (PJS-700.ttf) cho text có chữ Latin.
- Giữ nguyên 100% v1.3.5 còn lại: không icon, subtitle 1 cụm ngắn + từ khóa
  đỏ 1.19x + keyword pop, nền overlay 40%, brand + tagline đỉnh.

## Changelog v1.3.5 — waveform ĐỘNG theo RMS audio (10/10/2026)

Mục tiêu: sửa theo phản hồi duy nhất của user — "thanh nhạc phải ĐỘNG như cũ
chứ này tĩnh rồi".
- **Waveform ĐỘNG:** thanh dọc mảnh 3px, vàng gold #D8B36A, 270 thanh, chiều
  cao + alpha biến thiên theo RMS audio thật (window 50ms, 30fps), mỗi thanh
  có biến thiên mềm riêng → nhìn như visualizer sống. Seed gốc animate bằng
  envelope giọng nói đổi 9 lần/giây; bản này dùng RMS thật nên trung thực hơn.
- **Idle floor:** kể cả khi audio im lặng (pause giữa câu), thanh vẫn nhảy nhẹ
  (~15–25% chiều cao, nhịp chậm 0.4Hz) → waveform không bao giờ "chết"/phẳng.
- Kỹ thuật: render 30 frame PNG/giây bằng PIL → encode qtrle .mov (giữ alpha)
  → overlay y=1540. QA: diff pixel vùng waveform giữa 2 frame cách 1s = 26–32
  (bản tĩnh cũ chỉ 5.3).
- Giữ nguyên 100% v1.3.4: không icon, subtitle 1 cụm ngắn + từ khóa đỏ 1.19x
  + keyword pop, nền overlay 40%, brand + tagline.

## Changelog v1.3.4 — bỏ icon + từ khóa đỏ to hơn + waveform kiểu seed (10/10/2026)

Mục tiêu: sửa theo phản hồi của user ("bỏ luôn icon đi nhìn rối mắt quá",
"muốn nổi bật chỗ nào thì cho to lên một tí chỗ màu đỏ", "thanh nhạc quay
lại cái cũ sẽ đẹp hơn").
- **Bỏ hẳn icon** khỏi mọi video — chỉ còn 2 lớp: nền B-roll + chữ.
- **Từ khóa đỏ TO HƠN 1.19x:** chữ trắng 64px, từ khóa #FF4D6D 76px, cùng
  baseline (anchor="ls"), keyword pop giữ nguyên (PIL pre-render).
- **Waveform kiểu seed cũ:** thanh dọc mảnh 3px, vàng gold #D8B36A, vẽ từ
  RMS audio (270 thanh, alpha theo biên độ), tĩnh, y=1540. Seed thật gần
  như tĩnh (diff 5.3 giữa 2 frame cách 2s) nên không cần animate.
- Nền giữ nguyên v1.3.1 (overlay đen 40%, desat 0.85, vignette PI/3.5).

## Changelog v1.3.3 — subtitle ngắn kiểu seed + icon trắng mờ (10/10/2026)

Mục tiêu: sửa theo phản hồi của user ("lời dài quá", "icon không match,
nên để trắng mờ cho người ta tập trung vào nội dung").
- **Subtitle về kiểu seed 2/3 đã duyệt:** mỗi lần chỉ 1 cụm ngắn 4–7 từ
  (1–2 dòng), chữ thường, trắng #FFFFFF + từ khóa đỏ/hồng #FF4D6D.
  Bỏ hẳn cụm xám trước/sau của v1.3.1/v1.3.2.
- **Keyword pop render sẵn trong PIL** (không dùng filter animate của
  ffmpeg — `scale` với `eval=frame` không animate được, chữ kẹt ở 82% và
  lệch vị trí): cụm trắng fade-in 0.25s, từ khóa pop-in sau 0.12s qua
  3 bước scale 0.82 → 0.91 → 1.0 (mỗi bước 0.1s).
- **Icon trắng mờ:** stroke #FFFFFF, opacity 40–45%, KHÔNG glow, ~380px,
  1/3 trên — làm họa tiết nền, không tranh focus với chữ.
- Nền giữ nguyên v1.3.1 (overlay đen 40%, desat 0.85, vignette PI/3.5).
- Audio: dual-pass loudnorm về −14 LUFS (đo rồi normalize tuyến tính —
  cách volume=X dB trực tiếp sẽ vỡ true peak khi gain lớn).

## Changelog v1.3.1 — nền rõ + subtitle karaoke (10/10/2026)

Mục tiêu: sửa theo phản hồi của user ("của bạn mờ quá") sau khi so sánh trực
tiếp với đối thủ TĨNH ĐAO (nền video đêm hiện rõ ~60%, subtitle karaoke).
- **Overlay nền: 75–80% → 35–45%** (nền hiện 55–65%, đọc được chi tiết).
  Bỏ blur, desat chỉ còn ~15%, thêm vignette PI/3.5 để đỉnh/đáy tối dần.
  Ngưỡng QA mới: pause frame bất kỳ — phải nhận ra được cảnh đang quay gì.
- **Subtitle karaoke (áp dụng mọi video):** in HOA, font đậm; cụm đang đọc
  #FFFFFF, cụm trước/sau #7A7F87; cụm đang đọc căn giữa, cụm kề mờ ở
  trên/dưới; viền chữ mỏng (borderw=2, black@0.6) chống nền sáng.
- Giữ bản sắc NGẦM ĐỜI: icon vàng gold #D8B36A, brand + tagline đỉnh,
  waveform vàng mảnh đáy (không copy teal của đối thủ).

## Changelog v1.3.0 — hệ layered cinematic (10/10/2026)

Mục tiêu: nền có "hồn điện ảnh" mà chữ vẫn là vua (theo góp ý của user về
cách các kênh khác lồng video nền mờ nhạt).
- **Lớp B-roll:** 7 clip dọc 9:16 (`assets/broll/`, Pexels, manifest đầy đủ
  URL + tác giả) — phố đêm, bokeh xe, mưa kính, tòa nhà, đám đông nhòe,
  biển đêm, nến. Chuẩn hóa 1080×1920/30fps/10–15s. Map nền theo cảm xúc
  từng beat; fallback gradient tối thuần khi không có clip hợp.
- **Xử lý nền bắt buộc:** gradient đen 75–80% + blur 2–3px + desat 40% →
  nền chỉ hiện 20–25%, không bao giờ sáng hơn subtitle.
- **Bộ icon mới:** 12 icon SVG neon line-art (`assets/icons-v2/`,
  viewBox 200×200, stroke vàng #D8B36A / xanh nhạt #A8C8E8) giàu ẩn dụ hơn:
  đồng xu nứt, cán cân tim-xu, đồng hồ cát xu, mặt nạ hai mặt, mắt + dấu hỏi,
  người dưới đèn đường, tay buông xu, lửa trong lồng, ghế trống, tên xuyên tim,
  bẫy chuột, cửa hé sáng. Chọn icon qua `beat_map` trong manifest.
- **Giữ nguyên 4 nâng cấp v1.2** (keyword pop, Ken Burns, film grain, end card);
  end card vẫn nền đen tuyền.

## Changelog v1.2.0 — nâng cấp vượt đối thủ (09/10/2026)

Mục tiêu: không chỉ bắt kịp kênh tham khảo mà vượt ở 4 mặt.
- **Nội dung:** series hóa đánh số ("Luật ngầm #N"), bắt buộc kịch bản
  900–1.400 từ cho bản LONG, end card 5s (quote vàng + CTA), tease video
  tiếp theo ở câu cuối.
- **Hình thức:** keyword pop (scale punch khi voice tới từ đinh), Ken Burns
  siêu chậm trên icon, film grain 4–6%, end card fade-in/out.
- **Âm thanh:** dynamic music arc (swell beat 4, drop beat 5), sonic sting
  2s làm chữ ký kênh.
- **Phong cách:** giữ triết lý "tĩnh, u ám, sang" — mọi nâng cấp đều tinh tế,
  không phá nhịp chậm.

## Output Contract
Mỗi lần user gọi skill (dù chỉ gửi 1 câu chủ đề), trả về: **2 file MP4**
(bản dài 6–9 phút + bản reels 60–90s) + URL tải được + duration + changelog +
QA tóm tắt. Không hỏi lại những gì đã có chuẩn; chỉ hỏi khi thiếu thông tin
quyết định (chủ đề, góc nhìn sự thật muốn nói).

## Operating Rules
1. Kịch bản là vua: hook 3 giây đầu phải là một tuyên bố sốc/phũ phàng in hoa.
   Không mở đầu bằng giới thiệu kênh hay chào hỏi.
2. Không copy nội dung của kênh tham khảo — chỉ học pacing, nhịp dựng,
   hierarchy, công thức hook/caption từ họ.
3. Số liệu/trích dẫn on-screen phải khớp nguồn, không bịa. Triết lý là góc
   nhìn, nhưng facts phải đúng.
4. Không `opacity:0` trên `[data-start]` clip; không `backdrop-filter`
   (crash headless Chromium); `filter: blur()` thường thì an toàn.
5. Giọng đọc: đúng `Đời - Nam` (VieNeu, nam miền Bắc) speed 0.95; đổi tempo bằng
   `atempo`, không nâng pitch.
6. Nhạc/SFX tự tổng hợp (numpy/ffmpeg) — không dùng nhạc có bản quyền.
7. API key giọng đọc: **chỉ** từ env `VIENEU_AGENT_KEY` / Secure Vault connector
   `vieneu`; không hardcode, không in, không commit.
8. Caption reels: `[TIÊU ĐỀ IN HOA GIẬT GÂN…]` + link web/funnel của user,
   không hashtag (theo công thức kênh tham khảo).
