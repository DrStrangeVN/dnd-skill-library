---
name: "motion-video"
description: "Motion Video: sản xuất video motion-graphics dọc 1080x1920 phong cách Beeknoee — kịch bản tiếng Việt, giọng Nhật Phong (VieNeu), HyperFrames+GSAP, karaoke captions, nhạc/SFX tự tổng hợp, QA và link tải. Dùng khi user nói 'Motion Video', 'làm video', 'làm motion video', 'dựng video', 'làm reel', 'video explainer', hoặc gửi chủ đề/link cần dựng thành video."
metadata: { "includeInPrompt": true, "version": "2.4.0" }
---

# Motion Video

## Purpose
Biến một yêu cầu của user (chủ đề, repo, ý tưởng) thành **video MP4 hoàn chỉnh**:
kịch bản nói tiếng Việt → giọng đọc Nhật Phong → composition HyperFrames+GSAP
→ render 1080x1920/30fps → nhạc/SFX → QA → link tải. **Không trả kế hoạch suông.**

## Workflow
1. **Intake**: nhận chủ đề + độ dài mục tiêu + điểm chính từ user. Tự dựng
   narrative theo `references/narrative.md` nếu user không đưa kịch bản.
2. **Voice**: đọc `references/voice.md`. Ưu tiên VieNeu API
   (skill `vieneu-api-client`, voice `Nam - Nhật Phong`, speed mặc định 1.1);
   studio local `https://vieneu-studio.vercel.app` khi API không dùng được.
   **Cấm thay giọng khác.**
3. **Scaffold**: `python3 bin/new_project.py --slug <ten> --title "<tieu de>"`
   → project mới từ template tại `~/workspace/motion-video-template/`.
4. **Composition**: chọn variant trong `references/style-variants.md`
   (A=Tutorial, B=Editorial, C=Minimal Premium, D=Analyst, E=Punchline) theo
   bảng routing — trúng trường hợp nào dùng variant đó, không khóa cứng một
   kiểu cho mọi video. Dựng scenes theo `references/style-system.md`
   (archetypes tương ứng). Xem demo render sẵn tại `assets/style-demos/`.
5. **Render**: `TMPDIR=<project>/tmprender npx hyperframes@0.8.127 render`
   (/tmp chỉ 512MB). Render lại từ đầu nếu VM bị replace giữa chừng.
6. **Audio**: voice atempo (giữ pitch) → đặt đúng timeline → nhạc nền NHẸ stereo
   tự tổng hợp (warm pad Am–F–C–G, detune ±1.5Hz tạo width, sub root mono;
   chuẩn đối thủ @escbase 2026-10-10: bed liên tục, năng lượng 250–2000Hz +
   low-end mềm, side ~-45dBFS tức ~28dB dưới voice, ducking NHẸ dưới VO để
   nhạc vẫn nghe được) + SFX (whoosh/click/pop/shimmer, bus 0.45) → mix stereo
   (voice center) → `alimiter=limit=0.95` → loudnorm -14 LUFS. Triển khai tại
   `~/workspace/ai60giay-gen/make_audio.py` (ducking bằng numpy — KHÔNG dùng
   ffmpeg sidechaincompress+amix vì build này gộp stereo thành mono).
7. **QA** (bắt buộc trước khi báo xong): ffprobe 1080x1920/30fps/h264+aac;
   loudness + peak (không clip); screenshots 8 scenes + midpoints;
   caption karaoke khớp voice; verify 0 missing glyph bằng fontTools;
   số liệu on-screen khớp nguồn.
8. **Deliver**: upload lấy URL (kèm expiry), báo duration/size/version/changelog,
   source project path, contact sheet QA. Không dùng từ "xong/hoàn thành"
   khi chưa đủ tiêu chí.

## Output Contract
Mỗi lần user gọi skill (dù chỉ gửi 1 câu chủ đề), trả về: file MP4 thật +
URL tải được + duration + changelog + QA tóm tắt. Không hỏi lại những gì
đã có chuẩn; chỉ hỏi khi thiếu thông tin quyết định (độ dài, góc nhìn).

## Operating Rules
1. Đọc README/nguồn gốc của chủ đề trước khi dựng kịch bản; số liệu on-screen
   phải khớp nguồn, không bịa performance claims.
2. Không copy asset có bản quyền — chỉ học pacing, edit density, hierarchy,
   bố cục từ video tham khảo.
3. Không `opacity:0` trên `[data-start]` clip; không `backdrop-filter`
   (crash headless Chromium); `filter: blur()` thường thì an toàn.
4. Giọng đọc: đúng `Nam - Nhật Phong`; đổi tempo bằng `atempo`, không nâng pitch.
5. Nhạc/SFX tự tổng hợp (numpy/ffmpeg) — không dùng nhạc có bản quyền.
6. API key giọng đọc: **chỉ** từ env `VIENEU_AGENT_KEY` / Secure Vault connector
   `vieneu`; không hardcode, không in, không commit.
7. Subtitle: **tối đa 2 dòng** (ưu tiên 1 dòng), mỗi dòng 6–10 từ — cấm sub dài
   che màn hình (user 2026-10-10). Kiểu sub (punchline/karaoke/chip) đi theo
   variant đã chọn trong style-variants.md; không ép một kiểu cho mọi video.
8. Độ dài video kênh AI 60 Giây: chuẩn 90s, tối đa 150s (user 2026-10-10:
   60s không đủ thông tin).
9. Thanh/lines trang trí (accent bars): KHÔNG để cấn vào chữ — phải chừa padding
   rõ ràng quanh text, hoặc bỏ hẳn (user 2026-10-10: 2 thanh màu trong video v13
   đè lên chữ "LẤY LẠI"). Kiểm tra bằng screenshot QA trước khi giao.
