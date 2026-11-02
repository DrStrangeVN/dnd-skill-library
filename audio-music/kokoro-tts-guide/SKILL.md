---
name: kokoro-tts-guide
description: Guide to Kokoro-82M text-to-speech, the TTS model shown in the Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA". Use when the user asks about Kokoro TTS, Kokoro voices, or running Kokoro locally. Kokoro has no Vietnamese voice and must never replace the VieNeu API voice for Vietnamese production narration.
---

# Kokoro TTS — hướng dẫn

## Nguồn đã xác minh (kiểm tra 02/11/2026)

- Model: `hexgrad/Kokoro-82M` trên Hugging Face; thư viện suy luận: repo `hexgrad/kokoro`, giấy phép Apache-2.0, khoảng 9.856 sao.
- Kokoro-82M là model TTS 82 triệu tham số, xuất âm thanh 24 kHz, chạy được trên CPU hoặc GPU.
- Trong video, tên "Kokoro" xuất hiện ở giai đoạn "TỪ SCRIPT THÀNH MEDIA" mà không có nhãn phụ đọc được rõ. Video không cho link repo; repo trên được xác định bằng tìm kiếm theo tên và đối chiếu mô tả.

## Cảnh báo cứng — áp cho mọi việc của Trí

- **Kokoro KHÔNG có giọng tiếng Việt.** Các ngôn ngữ có giọng kèm theo là tiếng Anh (Mỹ, Anh), Tây Ban Nha, Pháp, Hindi, Ý, Nhật, Bồ Đào Nha (Brazil), Trung (Quan thoại). Không dùng Kokoro để đọc lời tiếng Việt.
- **Không thay giọng khác rồi gọi là "Nam - Nhật Phong".** Lời đọc sản xuất tiếng Việt của Trí dùng giọng VieNeu Studio API "Nam - Nhật Phong". Kokoro chỉ dùng cho thử nghiệm/demo tiếng Anh hoặc ngôn ngữ được hỗ trợ khác, nếu Trí yêu cầu.
- Kokoro dùng thư viện giọng cố định, không có nhân bản giọng (voice cloning). Không hứa tạo giọng giống một người cụ thể bằng Kokoro.

## Khi nào dùng

- Thử nghiệm TTS tiếng Anh (hoặc ngôn ngữ được hỗ trợ khác) chạy local, nhẹ, nhanh, giấy phép Apache-2.0 cho phép dùng thương mại theo giấy phép đó.
- Demo kỹ thuật, so sánh chất lượng TTS, hoặc làm giọng đọc cho nội dung không phải tiếng Việt.

## Cách dùng theo README (chưa cài thử trên máy này)

Cài đặt theo README của repo `hexgrad/kokoro`: `pip install kokoro` (phiên bản từ 0.9.4 trở lên trong ví dụ của README), cài `soundfile`, và cài `espeak-ng` cho dự phòng ngoài từ điển tiếng Anh và một số ngôn ngữ khác.

Mẫu tối thiểu trong README:

```python
from kokoro import KPipeline
pipeline = KPipeline(lang_code='a')
generator = pipeline("Your text here", voice='af_heart')
```

Mã ngôn ngữ (`lang_code`) theo README: `a` tiếng Anh Mỹ, `b` tiếng Anh Anh, `e` Tây Ban Nha, `f` Pháp, `h` Hindi, `i` Ý, `j` Nhật (cần `misaki[ja]`), `p` Bồ Đào Nha Brazil, `z` Quan thoại (cần `misaki[zh]`). Mã ngôn ngữ phải khớp với giọng chọn; ví dụ giọng `af_heart` dùng với `a`. Tốc độ đọc điều chỉnh bằng tham số của pipeline; kiểm tra README của bản đang dùng vì tên tham số có thể đổi.

Chất lượng và tốc độ thực tế chưa đo trên máy Trí. Nghe thử trước khi dùng cho việc thật, và kiểm tra phát âm tên riêng, số, từ viết tắt bằng tai.
