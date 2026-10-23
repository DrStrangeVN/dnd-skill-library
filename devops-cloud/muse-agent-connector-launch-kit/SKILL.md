---
name: muse-agent-connector-launch-kit
description: Starter kit để build custom connector cho Meta Muse (và các AI-agent platform khác): Cloudflare Worker mẫu với OpenAPI, health check, test tự động, connector-readiness checker, và kinh nghiệm submit thật lên Muse.
---

# Agent Connector Launch Kit

Starter kit tối giản, tái sử dụng được — để expose một capability có API thành connector cho các AI-agent platform qua HTTPS/OpenAPI. Dùng Cloudflare Worker, Web API chuẩn, không runtime dependency.

- Repo gốc: https://github.com/camirian/agent-connector-launch-kit
- Source đã clone: `~/workspace/skill-repos/agent-connector-launch-kit`

## Có gì trong kit

- Cloudflare Worker mẫu: `GET /health`, `GET /openapi.json`, endpoint action JSON có cấu trúc.
- Connector metadata, test tự động, **connector-readiness checker**.
- URL-safety helpers, security defaults.
- Template privacy/terms/support/icon.
- Hướng dẫn deploy + **ghi chú submit lên Meta Muse dựa trên kinh nghiệm submit thật (09/2026)**.
- Test live an toàn qua pinned Connector Testbench release (tùy chọn).

## Quick start

```bash
git clone https://github.com/camirian/agent-connector-launch-kit.git
cd agent-connector-launch-kit
npm install && npm test && npm run connector-check
npx wrangler dev
```

Tùy biến logic trong `src/index.js`, OpenAPI schema, và `connector.json`; thay mọi giá trị `YOUR_*` và text contact/policy mẫu trước khi deploy.

## Khi nào dùng

- Muốn biến một dịch vụ/API nội bộ (vd: TaskDND, hệ thống CLB Dragons) thành connector mà Muse có thể gọi.
- Muốn học "chuẩn" Meta yêu cầu ở một connector submission (form hỏi gì, tiêu chí nào).

## Không phải

- Không phải project chính thức của Meta, không phải chứng nhận, không bảo đảm được duyệt.
- Không phải SaaS dashboard/billing/database.
