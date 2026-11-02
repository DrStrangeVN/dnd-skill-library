---
name: ai-youtube-shorts-generator-guide
description: Guide to the AI YouTube Shorts Generator, the open-source clipping tool shown in the Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA". Use when the user asks about turning a long-form video into ranked 9:16 shorts with LLM highlight detection and Whisper transcription. This is a guide skill only; the tool itself is not installed here and its code was not copied into the skill library.
---

# AI YouTube Shorts Generator — hướng dẫn

## Nguồn đã xác minh (kiểm tra 02/11/2026)

- Repo: `SamurAIGPT/AI-Youtube-Shorts-Generator`, giấy phép MIT, khoảng 5.721 sao, đẩy lần cuối 24/10/2026, bản v0.1.
- Đây là một công cụ Python hoàn chỉnh (CLI + thư viện), KHÔNG phải skill. Không đổ code của công cụ vào thư viện skill.
- Trong video, tên này xuất hiện ở giai đoạn "DỰNG VIDEO CẮT SHORTS". Video không cho link repo; repo trên được xác định bằng tìm kiếm theo tên và đối chiếu mô tả.

## Công cụ làm gì

Từ một video dài (URL YouTube hoặc file local), công cụ dùng mô hình ngôn ngữ để chọn đoạn nổi bật, dùng Whisper để chép lời, rồi cắt dọc 9:16 có theo dõi khuôn mặt, trả về các short đã xếp hạng. README tự giới thiệu là lựa chọn thay thế mã nguồn mở cho Opus Clip, Vidyo.ai, Klap, SubMagic.

## Khi nào dùng, khi nào không

- Dùng khi Trí muốn thử cắt short từ video dài sẵn có của chính mình, ngoài quy trình cắt clip đang chạy.
- Chỉ xử lý video Trí sở hữu hoặc có quyền xử lý. Không tải/cắt video của người khác để đăng lại; kiểm tra điều khoản của YouTube và quyền của chủ sở hữu trước.
- Mọi clip cắt ra vẫn phải qua kiểm tra trùng lặp trước khi xếp lịch (`recut_overlap_replace_guard`) và qua QA/duyệt như mọi video khác. Không xếp lịch clip trùng nội dung với clip đã lên lịch.
- Không dùng thay cho pipeline sản xuất video của Trí khi cần mô phỏng động tác, giọng VieNeu API, hay phong cách đã chốt theo kênh.

## Cách dùng theo README (chưa cài thử trên máy này)

Yêu cầu: Python 3.10+, và ở chế độ local cần `ffmpeg` trên PATH cùng key của nhà cung cấp mô hình ngôn ngữ.

Hai chế độ, theo README:

- **API (mặc định, nhanh, không cần cài đặt nhiều):** dùng dịch vụ MuAPI cho tải/xử lý/cắt; trả phí theo clip thay vì thuê bao tháng. Lệnh mẫu trong README: `python main.py "https://www.youtube.com/watch?v=VIDEO_ID"`.
- **Local (chạy trên máy, trừ bước gọi mô hình ngôn ngữ):** dùng `yt-dlp`, `faster-whisper` và `ffmpeg`/`opencv`, chọn OpenAI hoặc Gemini để xếp hạng đoạn nổi bật. Lệnh mẫu: `python main.py "https://www.youtube.com/watch?v=VIDEO_ID" --mode local`. Cũng nhận file local hoặc `file://` URL.

Cấu hình qua biến môi trường (tên và giá trị mặc định theo README): `LLM_PROVIDER=openai|gemini`, `OPENAI_API_KEY` hoặc `GEMINI_API_KEY`, `OPENAI_MODEL` (mặc định `gpt-4o-mini`), `LOCAL_WHISPER_MODEL` (tiny/base/small/medium/large-v3), `LOCAL_WHISPER_DEVICE` (auto/cpu/cuda). Đọc mục "Installation (Self-Hosted)", "Configuration" và "Troubleshooting" trong README trước khi chạy.

## Giới hạn cần kiểm chứng trước khi dùng

- Chưa cài, chưa chạy thử, chưa đo chất lượng chọn đoạn hay cắt dọc. README nêu chế độ API của MuAPI có thể đổi giá/tính năng; kiểm tra trang của MuAPI trước khi dùng cho việc thật.
- Key API không ghi vào file skill, memory hay repo; dùng Secure Vault / biến môi trường của máy chạy công cụ.
- Chế độ local vẫn gọi mô hình ngôn ngữ từ xa (OpenAI/Gemini) cho bước xếp hạng đoạn nổi bật, nên không hoàn toàn offline.
- Bản v0.1, repo có thể đổi cờ dòng lệnh; luôn đọc README của bản đang dùng, không tin hoàn toàn vào bản tóm tắt này.
