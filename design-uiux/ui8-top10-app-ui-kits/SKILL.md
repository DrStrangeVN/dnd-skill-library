---
name: ui8-top10-app-ui-kits
description: 10 mẫu UI kit app/webapp tốt nhất trên UI8 (khảo sát 16/11/2026) — chưng cất cấu trúc, màn hình chính, component và cách dựng lại từng mẫu bằng code. Dùng khi cần chọn nhanh một mẫu dashboard/app để dựng giao diện thật.
---

# UI8 Top 10 App/Webapp UI Kits

Chưng cất từ khảo sát trực tiếp danh mục https://ui8.net/category/ui-kits ngày 16/11/2026
(6.418 kit, đã xem 92 sản phẩm, mở chi tiết 12 kit). 10 mẫu dưới đây là bản đánh giá
tốt nhất cho app/webapp theo tiêu chí: đủ màn hình thật, đủ component, đúng nhu cầu
dùng (dashboard SaaS, CRM, analytics, HR, quản lý dự án, e-commerce, fintech, AI,
observability), giá hợp lý lúc khảo sát (đang Black Friday Sale).

> Ranh giới bản quyền: 10 mẫu này đều là file Figma trả phí trên UI8. Skill này chỉ
> chưng cất cấu trúc, bố cục và pattern từ preview công khai — KHÔNG kèm file Figma
> gốc, KHÔNG tải/chia sẻ lại file trả phí. Khi dùng thật, mua đúng kit trên UI8
> (link từng mẫu ở dưới) hoặc dựng lại giao diện theo pattern đã chưng cất.
> Demo tương tác 10 mẫu (dựng lại bằng code): artifact "10 Template UI/UX cho
> App/Webapp" (slug `10-template-ui-ux-cho-app-webapp`).

## Chọn nhanh theo nhu cầu

| Nhu cầu | Mẫu nên dùng | Vì sao |
|---|---|---|
| Dashboard SaaS / admin tổng quát | Junctly, Oxtra, Garavelle | Nhiều màn nhất, đủ Light & Dark |
| AI agent / AI workspace | Nakko, Junctly | Workspace agent + workflow automation |
| CRM / bán hàng B2B | Northwind | 116 màn, có AI assistant dự báo |
| Analytics sản phẩm | Cohort | Web + mobile, đủ 5 loại biểu đồ |
| HR / quản trị nhân sự | HumaniZen | 186 màn, 17 module HR |
| Quản lý dự án | Garavelle | Kanban, timeline, calendar, team |
| E-commerce / quản lý bán hàng | Oxtra | 180+ màn, đa kênh, giá đang giảm |
| Fintech mobile | Moola | 103 màn iOS, ví crypto |
| Fintech dashboard + AI | Viola UI | Dashboard fintech có AI |
| DevOps / sự cố hệ thống | Vigil | Incident & observability, rẻ nhất |

Tổng giá 10 kit lúc khảo sát (giá sale): **$318**.

## 1. Junctly — AI Workflow Automation Dashboard

- Tác giả: Artena Nagara — Giá: **$34** (gốc $69) — Figma + PNG, 9,5 MB
- Quy mô: **244 màn** (122 màn riêng Light & Dark: 112 desktop 1440px + 10 iPhone),
  20 flow, 77 bộ component
- Link: https://ui8.net/artena-nagara/products/junctly-ai-workflow-automation-dashboard-ui-kit-dark--light
- Màn hình chính: workflow canvas (kéo-thả node), AI dispatcher, danh sách lần chạy
  (run history), màn phê duyệt (approval), quản lý agent, analytics, billing.
- Pattern dựng lại: sidebar tối + canvas lưới chấm; node workflow dạng thẻ bo tròn có
  trạng thái (chạy/xong/lỗi); bảng run có cột thời gian, trạng thái, nút chạy lại;
  toggle Light/Dark đổi toàn bộ token màu.
- Dùng khi: làm dashboard tự động hoá, AI agent ops, trung tâm điều phối workflow.

## 2. Nakko — AI Agent Workspace UI Kit

- Tác giả: HeyGar — Giá: **$20** (gốc $40) — Figma, 18,0 MB
- Quy mô: **91 màn** dashboard 1440px, light mode + responsive iPhone 16,
  15 flow, 37 component
- Link: https://ui8.net/heygar/products/nakko--ai-agent-workspace-ui-kit
- Màn hình chính: workspace agent (chat + công cụ), danh sách agent, chi tiết agent,
  lịch sử hội thoại, cài đặt workspace.
- Pattern dựng lại: layout 3 cột (sidebar agent / khung chat chính / panel công cụ);
  thẻ agent có avatar, trạng thái online, mô tả nhiệm vụ; khung chat có gợi ý lệnh
  nhanh; nền sáng, chữ sans đậm, điểm nhấn màu đơn.
- Dùng khi: làm workspace AI agent, trợ lý ảo, trung tâm chat đa agent.

## 3. Northwind — CRM Dashboard UI Kit

- Tác giả: nizarali — Giá: **$24** (gốc $49) — Figma, 42,2 MB
- Quy mô: **116 màn** desktop 1440px, 14 flow, 370+ component, 98 biến màu/tỷ lệ
- Link: https://ui8.net/nizarali/products/northwind---crm-dashboard-ui-kit
- Màn hình chính: tổng quan deal, pipeline bán hàng (kéo-thả theo giai đoạn), liên hệ,
  công ty, hoá đơn, AI assistant (cảnh báo rủi ro, dự báo doanh số).
- Pattern dựng lại: pipeline dạng cột theo giai đoạn với thẻ deal có giá trị + ngày
  chốt; bảng liên hệ có avatar, công ty, trạng thái; panel AI assistant gợi ý hành
  động tiếp theo; Light & Dark.
- Dùng khi: CRM B2B, quản lý pipeline, theo dõi deal và dự báo bán hàng.

## 4. Cohort — Product Analytics Dashboard (Web + Mobile)

- Tác giả: Bblast — Giá: **$59** — Figma, 3,7 MB
- Quy mô: **100 màn** Dark & Light (200 frame): 70 web 1440px + 30 iOS 393pt,
  61 component, 5 loại biểu đồ (funnel, line, bar, donut, retention), 4 tông màu nhấn
- Link: https://ui8.net/bblast/products/cohort---product-analytics-dashboard-ui-kit-web--mobile
- Màn hình chính: tổng quan sản phẩm, funnel chuyển đổi, retention cohort, phân tích
  theo sự kiện, báo cáo theo khoảng ngày (7d/30d/90d).
- Pattern dựng lại: nền tối mặc định; KPI lớn ở đầu trang; funnel dạng bậc thang có
  % rớt từng bước; heatmap retention theo cohort tuần; bộ chọn khoảng ngày đổi toàn
  bộ số liệu; mobile giữ cùng cấu trúc, xếp dọc.
- Dùng khi: analytics sản phẩm, theo dõi funnel/retention, dashboard dữ liệu tối.

## 5. HumaniZen — HR Management SaaS Dashboard

- Tác giả: Gandaria — Giá: **$30** — Figma
- Quy mô: **186 màn** desktop, 17 module HR, Light & Dark, kèm Design System
- Link: https://ui8.net/gandaria-studio-46bb3b/products/humanizen---hr-management-saas-dashboard-ui-kit
- Màn hình chính: tổng quan nhân sự, danh sách nhân viên (lọc theo phòng ban),
  chấm công, lương, tuyển dụng (pipeline ứng viên), analytics nhân sự.
- Pattern dựng lại: sidebar theo module HR; bảng nhân viên có avatar, phòng ban,
  chức danh, trạng thái; thẻ KPI (tổng nhân viên, nghỉ phép, tuyển mới); lịch chấm
  công dạng lưới tháng; nền sáng.
- Dùng khi: HR SaaS, quản trị nhân sự, chấm công/lương/tuyển dụng.

## 6. Garavelle — SaaS Project Management UI Kit

- Tác giả: Gandaria — Giá: **$30** — Figma, 19,3 MB
- Quy mô: **50+ màn** desktop + mobile, Light & Dark
- Link: https://ui8.net/gandaria-studio-46bb3b/products/garavelle---saas-project-management-ui-kit
- Màn hình chính: tổng quan dự án, Kanban, danh sách task, timeline, calendar,
  team, file đính kèm.
- Pattern dựng lại: Kanban 4 cột (To do / In progress / Review / Done), thẻ task có
  nhãn ưu tiên, người phụ trách, ngày hết hạn; chuyển thẻ đổi cột; timeline dạng
  thanh Gantt gọn; calendar xem task theo ngày.
- Dùng khi: quản lý dự án SaaS, theo dõi task nhóm, làm việc nhóm.

## 7. Oxtra — E-Commerce Manager UI Kit

- Tác giả: Qrelab — Giá: **$24** (gốc $49) — Figma, 37 MB
- Quy mô: **180+ màn** desktop Light & Dark, 10 flow, 100+ component,
  responsive mobile web
- Link: https://ui8.net/qrelab/products/oxtra---e-commerce-manager-ui-kit
- Màn hình chính: tổng quan bán hàng đa kênh (webstore, marketplace, mạng xã hội),
  đơn hàng (lọc theo kênh), sản phẩm, kho, khuyến mãi, khách hàng, báo cáo.
- Pattern dựng lại: KPI doanh thu theo kênh; bảng đơn hàng có cột kênh bán, trạng
  thái giao, tổng tiền; bộ lọc kênh (Shopee/Lazada/Website...); biểu đồ doanh thu
  theo ngày; Light & Dark.
- Dùng khi: quản lý bán hàng đa kênh, admin thương mại điện tử, theo dõi đơn/kho.

## 8. Moola — Fintech & Crypto Wallet App UI Kit

- Tác giả: YLAB — Giá: **$29** — Figma, 17,2 MB
- Quy mô: **103 màn** iOS 393×852, 11 chương, 163 component, 14 flow prototype,
  Dark & Light
- Link: https://ui8.net/ylab/products/moola--fintech--crypto-wallet-app-ui-kit
- Màn hình chính: tổng số dư ví, danh sách coin (BTC/ETH/SOL...), chi tiết coin,
  gửi/nhận, lịch sử giao dịch, đổi coin.
- Pattern dựng lại: khung điện thoại 393×852; số dư lớn ở đầu, danh sách coin có
  icon, giá, % tăng/giảm 24h; chạm coin mở chi tiết có biểu đồ giá; phong cách
  acid-lime/collage (điểm nhấn xanh lime trên nền tối/sáng).
- Dùng khi: app ví crypto/fintech mobile, theo dõi tài sản số.

## 9. Viola UI — Fintech Dashboard & AI UI Kit

- Tác giả: kaasusha — Giá: **$49** — Figma
- Quy mô: dashboard fintech + AI (xem chi tiết số màn trên trang sản phẩm)
- Link: https://ui8.net/kaasusha/products/viola-ui--fintech-dashboard--ai-ui-kit
- Màn hình chính: tổng quan tài chính, giao dịch, AI insight (gợi ý tiết kiệm/đầu tư),
  báo cáo theo kỳ.
- Pattern dựng lại: dashboard desktop nền sáng/tối; biểu đồ dòng tiền; thẻ AI insight
  có nút áp dụng gợi ý; bảng giao dịch có phân loại; bộ chọn kỳ (5N/1N/1T...).
- Dùng khi: dashboard fintech desktop, quản lý tài chính có AI gợi ý.

## 10. Vigil — Incident & Observability UI Kit (Web + Mobile)

- Tác giả: Bblast — Giá: **$19** (gốc $39) — Figma
- Quy mô: web + mobile (xem chi tiết số màn trên trang sản phẩm)
- Link: https://ui8.net/bblast/products/vigil---incident--observability-ui-kit-web--mobile
- Màn hình chính: tổng quan hệ thống, danh sách sự cố (lọc theo mức độ Critical/
  Warning/Info), chi tiết sự cố, timeline xử lý, xác nhận xử lý.
- Pattern dựng lại: trạng thái hệ thống dạng đèn (xanh/vàng/đỏ); bảng sự cố có mức
  độ màu, dịch vụ ảnh hưởng, thời gian; lọc Critical chỉ còn sự cố nặng; nút xác
  nhận xử lý đổi trạng thái sự cố.
- Dùng khi: giám sát hệ thống, quản lý sự cố, dashboard DevOps/SRE.

## Quy trình dùng skill

1. Xác định nhu cầu (bảng chọn nhanh ở trên) → chốt 1 mẫu chính.
2. Mở link UI8 của mẫu đó, xem preview đầy đủ (gallery trên trang sản phẩm).
3. Lấy cấu trúc ở mục tương ứng trong skill này: màn hình chính, component, pattern.
4. Dựng lại bằng code (HTML/Tailwind hoặc Remotion tuỳ dự án): sidebar, KPI, bảng,
   biểu đồ SVG, trạng thái Light/Dark — bám pattern, không sao chép file Figma.
5. Nếu cần mua file gốc để dùng trong Figma: mua đúng kit trên UI8 theo link,
   giá lúc khảo sát 16/11/2026 (đang sale, kiểm tra lại giá lúc mua).

## Ghi chú

- Giá và số màn hình là giá trị lúc khảo sát 16/11/2026; UI8 đang chạy Black Friday
  Sale nên giá có thể đổi — kiểm tra lại trên trang sản phẩm trước khi mua.
- Tất cả 12 kit mở chi tiết đều là Figma; không thấy Sketch/XD trong nhóm này.
- Nguồn: UI8 — https://ui8.net/category/ui-kits (6.418 UI Kits).
