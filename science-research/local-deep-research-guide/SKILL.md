---
name: local-deep-research-guide
description: Guide to Local Deep Research, the local research app shown in the Facebook Reel "MỘT NỘI DUNG NHIỀU ĐẦU RA". Use when the user asks about Local Deep Research, running deep research locally with Ollama/SearXNG, or setting up that app. This is a guide skill only; the app itself is not installed here and its code was not copied into the skill library.
---

# Local Deep Research — hướng dẫn

## Nguồn đã xác minh (kiểm tra 02/11/2026)

- Repo: `LearningCircuit/local-deep-research`, giấy phép MIT, khoảng 9.478 sao, đẩy lần cuối 02/11/2026.
- Đây là một ứng dụng nghiên cứu hoàn chỉnh, KHÔNG phải skill. Không đổ code của ứng dụng vào thư viện skill.
- Trong video, tên này xuất hiện ở giai đoạn "Nghiên cứu — TỪ Ý TƯỞNG ĐẾN BÁO CÁO", cùng nhóm với Social Media Research Skills. Video không cho link repo; repo trên được xác định bằng tìm kiếm theo tên và đối chiếu mô tả.

## Ứng dụng làm gì

Ứng dụng nghiên cứu chạy cục bộ, có giao diện web, cho phép nghiên cứu sâu bằng mô hình ngôn ngữ chạy local hoặc qua API tương thích OpenAI, kết hợp tìm kiếm web qua SearXNG và kho tài liệu riêng. Cơ sở dữ liệu được mã hóa bằng SQLCipher theo README của repo.

## Khi nào dùng, khi nào không

- Dùng khi Trí muốn một công cụ nghiên cứu chạy local, dữ liệu ở trên máy mình, thay vì chỉ dùng tìm kiếm web của trợ lý.
- Không dùng thay cho quy trình nghiên cứu đã có của các skill `deep-research`, `blog-*`, hay các skill ScrapeCreators khi cần dữ liệu mạng xã hội — Local Deep Research không lấy dữ liệu mạng xã hội theo kiểu ScrapeCreators.
- Mọi kết quả nghiên cứu dùng cho bài đăng công khai vẫn phải kiểm chứng nguồn trước khi dùng; ứng dụng không thay bước kiểm chứng đó.

## Cách chạy theo README (chưa cài thử trên máy này)

README của repo nêu 3 cách. Trên Mac của Trí, lưu ý cách 1:

1. **Docker Compose (khuyến nghị cho Mac/Windows):** tải `docker-compose.yml` của repo rồi chạy `docker compose up -d`, mở `http://localhost:5000`. README cảnh báo `--network host` chỉ chạy trên Linux thuần; trên Docker Desktop nó không xuất bản được cổng và không tới được Ollama/SearXNG, nên dùng Docker Compose.
2. **Docker Run (Linux):** chạy riêng Ollama, SearXNG, rồi chạy ứng dụng với biến môi trường trỏ tới SearXNG. Cần đọc kỹ mục Quick Start trong README vì có ghi chú về URL SearXNG được phê duyệt từ v1.10.3.
3. **pip install:** `pip install local-deep-research`, vẫn cần Ollama (hoặc endpoint tương thích OpenAI) và SearXNG đang chạy. Xem thêm `docs/install-pip.md` trong repo.

Ngoài ra repo có MCP server để tích hợp Claude (xem mục "MCP Server" trong README) và Python/HTTP API. Chưa cấu hình MCP này trên máy Trí; muốn dùng thì Trí duyệt trước.

## Giới hạn cần kiểm chứng trước khi dùng

- Chưa chạy thử, chưa đo chất lượng hay tốc độ trên máy Trí. Con số SimpleQA ~95% là tuyên bố của repo (với mô hình cụ thể trên GPU cụ thể), không phải kết quả đo của Trí.
- Cần Docker hoặc Python + Ollama + SearXNG; chi phí tài nguyên và thời gian cài đặt không nhỏ. Đọc `docs/faq.md` và `docs/docker-compose-guide.md` trong repo trước khi cài.
- Giấy phép MIT áp cho code của repo; mô hình và nguồn dữ liệu dùng kèm có điều khoản riêng, kiểm tra trước khi dùng cho công việc thương mại.
- Không ghi secret hay API key vào file skill, memory hay repo. Key (nếu dùng endpoint đám mây) đi qua Secure Vault / biến môi trường của máy chạy ứng dụng.
