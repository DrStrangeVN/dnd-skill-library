# Pipeline — Dark Wisdom

## Tổng quan
1 kịch bản → 2 sản phẩm: **LONG** (6–9 phút, đăng feed + YouTube) và
**REELS** (60–90s cắt từ LONG, đăng reels/tiktok).

## Bước chi tiết
1. **Script** (`script.md`): viết theo `references/narrative.md`, chia 6 beat,
   đánh số B1..B6. Mục tiêu 900–1.400 từ.
2. **TTS per beat**: mỗi beat 1 request VieNeu (≤20k chars là dư dả), lưu
   `audio/beat-N.wav`. Strip 37-byte ID3 tag nếu dùng CLI tts. ffprobe từng
   beat lấy duration thật.
3. **Timings**: `timings.json` — beat N: start/end (giây). Subtitle split theo
   cụm từ trong từng beat; mỗi cụm có start/end ước lượng = duration_beat ×
   (số từ cụm / tổng từ beat), rồi chỉnh tay khi QA.
4. **Composition** (HyperFrames+GSAP): 1 scene/beat, visual tĩnh + waveform
   (vẽ bằng canvas theo amplitude giả lập từ duration — không cần FFT thật,
   nhưng phải đồng bộ nhịp với voice: dùng `atempo` timeline).
5. **Render LONG**: `TMPDIR=<project>/tmprender npx hyperframes@0.8.127 render`.
6. **Cutdown REELS**: chọn beat 1 + đoạn mạnh nhất của beat 4 (tổng 60–90s),
   cắt bằng ffmpeg `-ss/-t` (giữ nguyên audio track), burn lại subtitle cụm
   từ cho đoạn cắt, thêm caption file.
7. **Audio mix** (theo `references/voice.md` mục "Âm thanh v1.2"): voice beat
   nối với gap 0.4s → nhạc pad ambient tự tổng hợp theo **dynamic arc**
   (nền −22dB; swell +3dB ở beat 4, drop về −28dB ở beat 5, nốt trầm 2s dưới
   câu chốt beat 6) → sidechain ducking → `alimiter=limit=0.95`. Thêm **sonic
   sting 2s** (drone 55Hz + chuông 880Hz decay) ngay trước hook 0.5s.
   Target −14 LUFS ±1 (chuẩn reels/feed).
8. **Caption**: `[TIÊU ĐỀ IN HOA GIẬT GÂN…]` + link funnel
   `?utm_source=facebook&utm_campaign=YYYYMMDD-slug` — không hashtag.

## QA checklist (bắt buộc — 4 cửa, thiếu 1 là chưa xuất xưởng)

**Cửa 1 — Nội dung (references/narrative.md):**
- [ ] Script qua đủ 6 tiêu chí XỊN, mọi beat ≥4/5 điểm
- [ ] Hook dùng 1 trong 8 công thức đã kiểm chứng
- [ ] Đã qua red-team pass ("người lướt 23h có dừng lại không? có lý do để share không?")
- [ ] 1 video = 1 sự thật duy nhất, không cliché self-help, facts có nguồn

**Cửa 2 — Giọng đọc (references/voice.md):**
- [ ] Đúng giọng `Đời - Nam`, speed 0.95, pitch-locked
- [ ] Nghe lại toàn bộ 1 lần: không lỗi phát âm, ngắt nghỉ đúng chỗ, hook có trọng lượng
- [ ] Không rè, không cắt cụt, không khoảng lặng chết >1.2s

**Cửa 3 — Visual (references/style.md):**
- [ ] Nhất quán font/cỡ/vị trí/watermark suốt video; đúng palette 4 màu
- [ ] Hook scene 3–4s đủ choáng; subtitle ≤2 dòng, keyword tô đúng từ đinh
- [ ] Waveform đồng bộ voice; không beat nào trơ chữ >10s hay nhồi >2 visual
- [ ] Soi screenshot ở 3 cỡ: đầy đủ, mobile, thumbnail

**Cửa 4 — Kỹ thuật:**
- [ ] ffprobe: 1080×1920, 30fps, h264+aac, cả 2 bản
- [ ] Loudness −14 LUFS ±1, peak không clip
- [ ] 8 screenshots LONG + 4 screenshots REELS: subtitle khớp voice, 0 tofu
- [ ] fontTools: 0 missing glyph (latin+vietnamese subsets)
- [ ] Waveform chạy đồng bộ với voice
- [ ] Facts/trích dẫn on-screen khớp nguồn

**Chuẩn xuất xưởng:** cả 4 cửa phải tick đủ. Một ô chưa tick = video chưa
xong = không báo "xong", không đăng. Không có ngoại lệ "tạm được", không
có "để lần sau sửa". Đây là quy chuẩn chất lượng cao nhất của kênh.

## Deliver
2 MP4 + URL tải (kèm expiry) + duration/size từng bản + changelog + contact
sheet QA. Báo rõ: bản LONG (feed/YouTube) và bản REELS (reels/tiktok).
