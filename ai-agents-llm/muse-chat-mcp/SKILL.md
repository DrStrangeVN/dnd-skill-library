---
name: muse-chat-mcp
description: Dùng Meta Muse (muse.ai) từ bất kỳ MCP client hay OpenAI-compatible client nào qua Chrome đã đăng nhập của chính bạn. Gồm MCP server 7 tools, HTTP shim tương thích OpenAI, và CLI.
---

# Muse-Chat-MCP

Muse không có public API — chat của nó là WebSocket mã hóa. Project này **không re-implement protocol** mà điều khiển Chrome đã đăng nhập thật của bạn bằng Playwright: gõ vào composer và đọc câu trả lời đã render.

- Repo gốc: https://github.com/duclm1x1/Muse-Chat-MCP
- Source đã clone: `~/workspace/skill-repos/muse-chat-mcp`

## Hai cửa dùng

| Cửa | Là gì | Dùng từ |
|---|---|---|
| **MCP server** (stdio) | 7 tools: `muse_status`, `muse_login`, `muse_new_chat`, `muse_chat`, `muse_read_last`, `muse_dump_dom`, `muse_close` | Claude Desktop, opencode, Cursor, bất kỳ MCP host nào |
| **OpenAI-compatible shim** (HTTP) | `GET /v1/models`, `POST /v1/chat/completions` (stream SSE + non-stream, tool calling) | Mọi OpenAI SDK / `@ai-sdk/openai-compatible` |
| **CLI** | `muse-cli.mjs` — one-shot generation từ script | shell |

## Cài đặt & đăng nhập

```bash
git clone https://github.com/duclm1x1/Muse-Chat-MCP.git && cd Muse-Chat-MCP
npm install          # chỉ kéo playwright-core, KHÔNG tải browser
npm run selftest     # mở Chrome, in trạng thái login/browser, rồi đóng
```

- Lần đầu chạy: đăng nhập tài khoản Meta của chính bạn trong Chrome được mở ra. Dùng Chrome profile riêng, hoặc attach vào Chrome đang chạy với `--remote-debugging-port=9222`. Không bao giờ kill browser của bạn — chỉ disconnect khi đóng.
- Hỗ trợ gửi ảnh/video kèm prompt; lấy media Muse đã tạo (link + download); tool calling qua prompt-injection.

## Cảnh báo quan trọng

- Chạy trên **tài khoản và quota Muse của chính user** — tự động hóa tài khoản cá nhân có thể vi phạm ToS của Meta; dùng ở mức cá nhân, không lạm dụng tần suất.
- Tuyệt đối không chia sẻ Chrome profile / session đã login cho người khác.
