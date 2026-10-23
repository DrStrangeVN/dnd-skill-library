---
name: web-liquid-glass-landing
description: Landing page "liquid glass" nền đen gần như tuyệt đối: pill/card kính mờ bắt sáng ở viền, headline serif khổ lớn có đúng một từ italic, panel xem trước sản phẩm sống (app view + chart nhỏ), form hứng email xác nhận ngay trong trang. Dùng khi làm trang chờ (waitlist), private beta, ra mắt sản phẩm, newsletter trả phí hoặc SaaS nhỏ cần một trang chuyển đổi duy nhất, sang và tĩnh, mở offline trong một file HTML tự chứa. Không dùng cho brand sáng màu/có màu nhấn riêng, site nội dung nhiều tầng, hay trang cần gửi email thật ngay (form chỉ confirm trong trang tới khi nối dịch vụ).
---

# Web — Liquid Glass Landing

Chưng cất từ dữ liệu công khai của Skillry `bs-liquid-glass-landing` (mô tả + 3 ảnh preview, 23/10/2026) theo quy ước bộ web (master `web-studio`): một ngôn ngữ thị giác khóa cứng, một file HTML tự chứa, tương tác chạy thật trong trang. Đây là bản dựng lại độc lập — brand, nội dung và code đều làm mới, chỉ giữ hệ phong cách.

## Khi nào dùng

- **Trang chuyển đổi một mục tiêu:** việc chính của trang là hứng email (waitlist, beta kín, launch, newsletter trả phí) hoặc một CTA duy nhất tương đương.
- Sản phẩm **cho xem được bằng một màn hình thật** (app view, hộp thư, changelog, dashboard thu nhỏ) thay vì ảnh stock.
- User muốn gu "premium minimalist dark glass" mà không muốn tự căn blur/viền/highlight.
- Không dùng khi: brand sáng màu, nhiều màu, minh họa-led (hệ này **dark-only, không màu nhấn**); site nội dung sâu nhiều cấp điều hướng; cần SEO content dày.

## Nguyên lý cốt lõi

1. **Một file, offline, style-locked.** Toàn bộ CSS/JS inline trong một `index.html`, mở bằng `file://` chạy đủ. Font qua Google Fonts + fallback hệ thống (serif: Georgia; sans: system-ui) — mất mạng trang vẫn đúng dáng.
2. **Kính là vật liệu duy nhất.** Mọi bề mặt nổi (nav, form, card, panel) đều là kính mờ trên nền đen: fill trắng 4–8%, viền 1px trắng ~16%, blur 14–20px, và **rim light** — highlight mảnh ở cạnh trên (`inset 0 1px 0 rgba(255,255,255,.28)`) khiến pill "bắt sáng" đúng nghĩa liquid glass. Không bề mặt đặc nào ngoài nút CTA trắng.
3. **Monochrome tuyệt đối.** Đen – trắng – xám, không màu nhấn. Thứ bậc tạo bằng cỡ chữ, độ mờ và khoảng trắng, không bằng màu. Nút chính là pill trắng chữ đen; nút phụ là pill kính chữ trắng.
4. **Serif gánh trang, sans gánh việc.** Headline serif khổ lớn (clamp 56–120px), mỗi headline **đúng một từ italic** — đó là "điểm rơi" thị giác duy nhất của cả section. Body/label/form dùng sans nhỏ, xám, tracking thoáng.
5. **Sản phẩm xuất hiện như đang sống.** Panel preview là một cửa sổ app thu nhỏ dựng bằng HTML/CSS thật (không ảnh chụp): có chrome cửa sổ, hàng dữ liệu, chart SVG nhỏ và một chi tiết "live" (chấm pulse, số liệu cập nhật bằng JS). Người xem tin vì nó *vận hành*, không vì nó đẹp.
6. **Form confirm trong trang, nói thật.** Mọi form (hero, closing, sign-in nếu có) validate tại chỗ và chuyển sang trạng thái đã xác nhận trong trang; không giả vờ đã gửi đi đâu. Nối dịch vụ email thật là bước riêng, ghi rõ trong bàn giao.

## Quy trình sản xuất

1. **Khóa nội dung trước khi khóa kính:** một câu hứa (headline), một CTA, 3 section truyện/tính năng, bảng giá, FAQ 4–6 câu. Trang này là funnel một cột — nội dung thừa cắt ngay từ brief.
2. **Dựng design token** theo bảng ở mục kỹ thuật (nền, kính, viền, radius, type scale) — sửa token là sửa toàn trang, không sửa tay từng chỗ.
3. **Dựng section theo nhịp cố định:** nav pill → hero (headline + capture) → panel preview sống → 3 section story/features (xen kẽ bố cục: stat rows / card grid / editorial split) → pricing (toggle tháng/năm) → FAQ accordion → closing capture → footer wordmark ma.
4. **Cài tương tác thật:** form validate + trạng thái confirm; toggle giá đổi số và ghi chú chu kỳ; accordion mở một mục một lúc; nav anchor cuộn mượt tới đúng section.
5. **QA theo mục QA bắt buộc** rồi mới giao: chụp ≥4 vị trí cuộn ở bề ngang 1280, lái thử toggle/accordion/form bằng headless và assert trạng thái đổi thật.

## Công thức & kỹ thuật đặc thù

**Design token (mặc định, sửa một chỗ áp toàn trang):**

| Token | Giá trị |
|---|---|
| `--ground` | `#060607` (đen gần tuyệt đối, hơi ấm về phía dưới bằng radial-gradient rất nhẹ) |
| `--glass` | `background: rgba(255,255,255,.055)` |
| `--glass-strong` | `rgba(255,255,255,.09)` cho panel chính |
| `--rim` | `border: 1px solid rgba(255,255,255,.16)` + `box-shadow: inset 0 1px 0 rgba(255,255,255,.28), 0 24px 60px rgba(0,0,0,.45)` |
| `--blur` | `backdrop-filter: blur(18px) saturate(140%)` |
| `--ink` / `--ink-2` / `--ink-3` | `#f5f4f0` / `rgba(245,244,240,.62)` / `rgba(245,244,240,.38)` |
| `--hairline` | `rgba(255,255,255,.09)` |
| `--r-pill` / `--r-card` / `--r-panel` | `999px` / `24px` / `28px` |
| Serif | `"Playfair Display", "Fraunces", Georgia, serif` — headline 400/500, italic cho từ nhấn |
| Sans | `"Inter", system-ui, -apple-system, "Segoe UI", sans-serif` — body 15–17px, label 12–13px uppercase tracking .12em khi cần |

**Công thức kính (class dùng lại cho nav, form, card):**

```css
.glass{
  background:rgba(255,255,255,.055);
  border:1px solid rgba(255,255,255,.16);
  box-shadow:inset 0 1px 0 rgba(255,255,255,.28), 0 24px 60px rgba(0,0,0,.45);
  backdrop-filter:blur(18px) saturate(140%);
  -webkit-backdrop-filter:blur(18px) saturate(140%);
}
```

**Nhịp section (đừng đổi thứ tự):** hero căn giữa, các section sau trái-lề theo lưới 1120px; mỗi section mở bằng một headline serif có một từ italic; khoảng đệm dọc 120–160px; phân cách bằng hairline hoặc khoảng trắng, không bằng hộp màu.

**Panel preview sống:** cửa sổ kính bo 28px, thanh chrome 3 chấm xám + địa chỉ pill; bên trong là UI sản phẩm tối giản (3–5 hàng dữ liệu có hairline) và một chart SVG đường/cột nhỏ vẽ bằng path tĩnh + một chỉ số "live" cập nhật bằng `setInterval` (đếm giờ yên tĩnh, hàng đợi...) — chi tiết chuyển động duy nhất của trang, giữ dưới 1 yếu tố.

**Ghost wordmark footer:** tên brand serif cỡ ~17vw, màu `rgba(255,255,255,.05)` (hoặc stroke 1px trong suốt ruột), bị cắt ở mép dưới footer (`overflow:hidden`, dịch xuống ~18%) — chữ ký đóng trang của hệ này.

**Nền hero:** không ảnh stock; dùng lớp SVG/CSS trừu tượng tối (gợn sóng/địa hình bằng radial-gradient xếp lớp + blur lớn) để giữ rim light của vật kính là thứ sáng nhất trang. Nền càng tối, kính càng nổi.

## QA bắt buộc

- Mở bằng `file://`, tắt mạng: trang vẫn đúng layout, font fallback không phá nhịp.
- Headless (Chrome, viewport 1280): **không tràn ngang** (`scrollWidth ≤ innerWidth`), chụp ≥4 vị trí cuộn — hero, panel preview, pricing, FAQ/footer — soi: kính thấy rõ trên nền, rim light có mặt, chữ đọc được (body ≥ .62 opacity trên nền).
- **Lái thử tương tác bằng script và assert:** bấm toggle giá → số tiền + ghi chú chu kỳ đổi; bấm mục FAQ thứ hai → mục đó mở, mục đang mở đóng; submit email sai định dạng → báo lỗi tại chỗ, email đúng → hiện trạng thái confirm. Cả ba phải PASS mới giao.
- Mỗi headline đúng **một** từ italic; toàn trang không xuất hiện màu nào ngoài thang xám (trừ màu hệ thống của trình duyệt).
- Nội dung hư cấu ghi rõ là mẫu (số liệu, testimonial) để user thay bằng số thật — không trình bày số mẫu như fact.

## Output contract

- Một file `index.html` tự chứa duy nhất (CSS/JS inline), mở offline bằng `file://`, không request ngoài nào ngoài font (có fallback).
- Kèm: ảnh chụp QA ≥4 vị trí + contact sheet, và `QA.md` ghi kết quả từng mục kiểm, độ lệch so với mẫu tham chiếu (nếu có) và lý do.
- Form chỉ confirm trong trang; khi bàn giao phải nói rõ muốn thu email thật thì nối dịch vụ nào là bước tiếp theo.
