---
name: muse-mac-connector
description: Cho Meta Muse thao tác trên máy Mac qua app menu-bar (file, terminal, app, clipboard, screenshot, click/type, Apple Shortcuts). Có Full Computer Mode cần chủ máy phê duyệt thủ công.
---

# Muse Mac Connector

App macOS (menu bar) mã nguồn mở, cộng đồng phát triển — cho Meta Muse một bộ công cụ an toàn, có xác thực để làm việc trên máy Mac của user.

- Repo gốc: https://github.com/dkm90x/muse-mac-connector (MIT, v0.5.0-alpha)
- Source đã clone: `~/workspace/skill-repos/muse-mac-connector`

## Cài đặt

1. Tải build từ GitHub Releases (ad-hoc signed — macOS có thể hiện cảnh báo Gatekeeper, dùng Finder's **Open** / **Open Anyway** sau khi xác minh tải đúng từ repo này).
2. Mở app — biểu tượng tròn xuất hiện trên menu bar.
3. Chờ trạng thái **Ready** (app tự tạo Cloudflare Quick Tunnel miễn phí và copy cấu hình Muse hiện tại).
4. Mở Muse, nhấn **Command-V** để dán cấu hình; nếu Muse hỏi access key qua credential flow, dùng **Copy Muse Access Key** trong menu app.

## Khả năng (capability index, `GET /capabilities`)

- **Files:** liệt kê/đọc/ghi/tạo/di chuyển/xóa file (Restricted Mode giới hạn trong thư mục đã cấu hình).
- **Developer commands:** chạy lệnh terminal có kiểm soát; Full Computer Mode cho phép lệnh shell đầy đủ (pipe, redirect).
- **Processes:** start/inspect/đọc output/stop tiến trình nền.
- **Apps:** mở app macOS đã cài. **Clipboard:** đọc/ghi. **Screen:** chụp màn hình.
- **UI:** inspect app đang focus, activate, click, gõ phím, hotkey.
- **Shortcuts:** chạy Apple Shortcuts theo tên. **Web:** mở URL. **Scripts:** chạy script trong thư mục connector. **Settings:** đổi giá trị macOS defaults (string).

## An toàn

- **Full Computer Mode** phải được chủ máy bật thủ công trong menu app (đọc cảnh báo và approve). Kể cả khi bật, macOS privacy controls (Accessibility, Screen Recording, Full Disk Access, SIP...) vẫn áp dụng; thao tác phá hoại/đặc quyền/credential vẫn giữ approval gate cục bộ.
- Nếu Mac restart hoặc tunnel đổi, mở lại app để reconnect và copy cấu hình mới.
