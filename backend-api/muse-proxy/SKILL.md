---
name: muse-proxy
description: API-key gateway triển khai trên Cloudflare Worker cho các dịch vụ cần username/password (hiện hỗ trợ CalDAV/CardDAV). Chủ tài khoản lưu credential upstream một lần, cấp key có giới hạn (scoped) cho agent như Meta Muse.
---

# Muse Proxy

Gateway API key cho các dịch vụ vốn yêu cầu username + password — sinh ra cho Meta Muse, vốn bị cấm lưu password dạng plaintext. Chủ tài khoản lưu credential upstream một lần (mã hóa), đặt "connection ceiling" (điều không bao giờ được phép), rồi tạo API key có phạm vi hẹp cho agent.

- Repo gốc: https://github.com/NeedsChloesure/muse-proxy
- Source đã clone: `~/workspace/skill-repos/muse-proxy`

## Dịch vụ hỗ trợ hiện tại

- **CalDAV / CardDAV** (lịch và danh bạ tự host). Có thể thêm dịch vụ khác bằng pull request hoặc fork.

## Triển khai (Cloudflare)

1. Nút **Deploy to Cloudflare** trong README: clone repo về tài khoản GitHub của user, tự tạo D1 database, hỏi `CREDENTIAL_ENCRYPTION_KEY` (tạo bằng `openssl rand -base64 32`).
2. Hoặc thủ công: `npm install`, `npx wrangler d1 create muse-proxy`, `npm run db:migrate:local`, copy `.dev.vars.example` → `.dev.vars` và điền key mã hóa thật.
3. Mở `/user/`, tạo account đầu tiên (luôn là admin).

## Cấp quyền cho agent

- Tạo API key trong dashboard, gắn scope (vd: chỉ đọc lịch, không ghi).
- Đưa key cho agent qua **credential flow an toàn** (Secure Vault / credential prompt) — không dán key vào chat, không hardcode vào file/repo.

## Lưu ý

- Repo ghi rõ "written by agents, for agents — limited review". Đọc code trước khi deploy production, đặc biệt phần mã hóa credential và phân quyền key.
