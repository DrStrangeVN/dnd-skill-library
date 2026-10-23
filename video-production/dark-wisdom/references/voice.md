# Voice — Đời - Nam (VieNeu, nam miền Bắc)

## Primary: VieNeu API
Dùng skill `vieneu-api-client`: `~/workspace/skills/vieneu-api-client/vieneu_client.py`.

- Voice: `Đời - Nam` (Nam · VieNeu · Nam - Miền Bắc — giọng nam miền Bắc,
  user chọn ngày 09/10/2026 cho kênh Ngầm Đời). **Không thay giọng khác.**
- Speed: **0.95** (chậm, trầm, kể chuyện cho ngấm). Áp dụng bằng `atempo=`
  (pitch-locked), không pitch-shift.
- Key: chỉ từ env `VIENEU_AGENT_KEY` hoặc Secure Vault connector `vieneu`.
  Không hardcode, không in, không commit.
- Job protocol: POST `/v1/audio/speech` (header `X-Task-Id` UUID +
  `X-VieNeu-Worker: auto`) → poll `GET /jobs/{id}` mỗi 2s → `GET /jobs/{id}/audio`
  khi completed. Tối đa 20k ký tự/request — kịch bản dài chia nhiều request,
  nối bằng ffmpeg với khoảng lặng 0.4s giữa các đoạn.
- 401 = key hết hạn/thu hồi; 409 = task-id trùng (giữ nguyên task-id khi retry).

## Script rules (khác motion-video)
- Viết như **nói**, không như viết văn: câu ngắn vừa, có nhịp ngắt nghỉ.
  Đánh dấu pause bằng dấu câu — TTS sẽ ngấm theo.
- Số viết thành chữ ("chín mươi ba nghìn"), nhưng năm/giờ có thể đọc số.
- Hook đầu video: viết IN HOA trong kịch bản để nhấn giọng đọc mạnh.
- Chia narration theo beat (hook / bóc tách / chuyện / quy luật / cảnh tỉnh /
  kết) — mỗi beat 1 file audio riêng, dễ căn subtitle và cắt reels.
- Verify duration từng beat bằng `ffprobe` — không ước lượng.

## Env check (true/false only, never the value)
```bash
test -n "$VIENEU_AGENT_KEY" && echo true || echo false
```

## Tiêu chuẩn giọng đọc — "nghe là ngấm"

Audio là linh hồn của kênh này (visual chỉ làm nền). Mọi file voice phải đạt:

1. **Đúng giọng, đúng tốc độ:** `Đời - Nam`, speed 0.95, pitch-locked. Nghe
   thử 10 giây đầu — nếu nghe "vội" hay "robot" thì kiểm tra lại speed/tempo.
2. **Ngắt nghỉ có chủ đích:** dấu câu trong script phải trở thành khoảng
   lặng nghe được. Sau câu hook: lặng 0.5–0.8s cho ngấm. Trước câu chốt:
   lặng 0.6s. Không đọc đều đều một mạch.
3. **Hook đọc có trọng lượng:** 15 giây đầu đọc chậm hơn, trầm hơn, nhấn
   đúng từ đinh. Đây là 15 giây quyết định người xem ở lại hay lướt.
4. **Không lỗi phát âm:** kiểm tra từ Hán-Việt, tên riêng, số liệu trong
   script trước khi TTS. Nghe lại toàn bộ 1 lần, từ nào nghe sai/ngượng thì
   viết lại cách đọc (ví dụ: "TP.HCM" → "thành phố Hồ Chí Minh") rồi TTS lại.
5. **Sạch kỹ thuật:** không tiếng rè, không cắt cụt đầu/cuối câu, không
   khoảng lặng chết quá 1.2s giữa beats, nối beats bằng gap 0.4s đều nhau.

## Âm thanh v1.2 — dynamic arc & sonic branding (vượt đối thủ)

Đối thủ dùng nhạc nền phẳng đều từ đầu tới cuối. Mình cho nhạc "thở" theo
cảm xúc kịch bản:

1. **Dynamic music arc** (nhạc pad ambient tự tổng hợp, mức nền −22dB dưới
   voice):
   - Beat 1–2 (hook, bóc tách): nền thấp, căng — drone trầm + noise lọc nhẹ.
   - Beat 3 (câu chuyện): giữ nguyên, thêm một lớp pad ấm rất mờ.
   - Beat 4 (quy luật — cao trào): **swell** — tăng dần 3dB trong 8 giây đầu
     beat, giữ tới hết beat. Đây là lúc insight bùng nổ, nhạc phải nâng.
   - Beat 5 (cảnh tỉnh): **drop** — hạ về −28dB trong 3 giây, gần như im lặng.
     Tông trầm xuống, người xem nín thở.
   - Beat 6 (câu kết): trở về −22dB, thêm một nốt trầm dài 2s dưới câu chốt.
   - Sidechain ducking vẫn áp dụng suốt để voice luôn nổi.
2. **Sonic sting (2s, đầu video):** "chữ ký âm thanh" của kênh — tổng hợp bằng
   numpy: một cú drone trầm 55Hz swell 0.8s + một nốt chuông mờ (sine 880Hz,
   decay 1.2s, −18dB). Phát ngay trước hook 0.5s. Mục tiêu: nghe 2 giây là
   biết Ngầm Đời — như cách các kênh lớn có intro riêng.
3. Cấm: không whoosh/click/pop dồn dập; không nhạc có bản quyền; không để
   nhạc lấn voice ở bất kỳ beat nào.
