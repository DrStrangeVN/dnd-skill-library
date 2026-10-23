---
name: muse-dowser
description: Read-only MCP connector "tìm tiền đang bị bỏ quên": class action settlements còn mở, thu hồi sản phẩm (CPSC), credit thẻ chưa dùng, điểm thưởng sắp hết hạn, quà sinh nhật. Chạy local hoặc deploy Vercel, không cần tài khoản.
---

# Dowser — Finds the money hiding in your life

MCP connector **chỉ đọc** cho AI assistant như Meta Muse: quét các khoản tiền/quyền lợi user có thể đang bỏ lỡ, mỗi kết quả kèm link chính thức.

- Repo gốc: https://github.com/harris-ryder/dowser
- Source đã clone: `~/workspace/skill-repos/dowser`

## Các tool

| Tool | Trả lời câu hỏi | REST |
|---|---|---|
| `search_settlements` | Vụ kiện tập thể (U.S.) nào còn mở khớp với brand tôi dùng? Deadline, số tiền, bằng chứng cần, link claim | `GET /api/v1/settlements` |
| `match_recalls` | Đồ tôi sở hữu có bị thu hồi 3 năm qua không, cách khắc phục? | `GET /api/v1/recalls` |
| `card_benefits` | Credit/perk thẻ nào sắp reset, dùng thế nào? | `GET /api/v1/cards` |
| `points_expiry` | Dặm/điểm khi nào hết hạn, làm gì để giữ? | `GET /api/v1/points` |
| `birthday_freebies` | Chuỗi cửa hàng gần tôi tặng gì vào sinh nhật? | `GET /api/v1/freebies` |
| `check_for_new` | Có gì mới từ lần check trước? (sweep hàng tuần) | `GET /api/v1/updates` |

Kèm một MCP prompt `find_my_money` dẫn assistant đi hết quy trình sweep.

## Chạy

```bash
npm install
npm run build:data   # ~30s: scrape settlements + 3 năm CPSC recalls
npm run dev          # http://localhost:3000 (MCP tại /mcp)
```

Hoặc deploy Vercel (repo đã cấu hình sẵn `vercel.json`).

## Đặc điểm dữ liệu

- Không database, không tài khoản, không lưu dữ liệu cá nhân. Matching bằng TF-IDF index trên tiêu đề/tên sản phẩm.
- Dữ liệu settlements/recalls refresh hàng ngày qua GitHub Action; catalog thẻ/điểm quà tặng do người duy trì thủ công.
- Lưu ý: dữ liệu thiên về thị trường Mỹ — với user ở Việt Nam, giá trị thực tế chủ yếu ở phần recall sản phẩm quốc tế và brand toàn cầu.
