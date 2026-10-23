---
name: real-estate-video
description: Sản xuất video bất động sản dọc 9:16 kiểu "An Hồ Residence" (mẫu user gửi 2026-10-22) — ảnh AI + bản đồ OSM dark + route chấm trắng vẽ dần (mọi route) + số liệu vị trí THẬT (OSRM/Overpass) + giọng Nam - Nhật Phong (VieNeu). Không phụ đề đáy. Dùng khi user gửi mẫu + địa chỉ/tên dự án và nói "làm video bất động sản", "video BĐS", "video dự án như mẫu".
---

# Real Estate Video — công thức từ video mẫu An Hồ Residence

Học từ mẫu 2026-10-22: 720×1280 (bản sản xuất: **1080×1920**), 9:16, 30fps,
**36.9s**, h264+aac 48kHz stereo, loudness đo được **−14.19 LUFS, TP −1.24**
(khớp chuẩn nhà −14 LUFS). Cấu trúc 8 scene cố định, mỗi scene = 1 câu voice.

## Intake — user chỉ cần gửi
1. **Địa chỉ** (hoặc pin/tọa độ) của dự án/khu đất — bắt buộc duy nhất.
2. Tên dự án (thiếu → Muse tự đặt tên minh hoạ và ghi rõ).
3. Tuỳ chọn: diện tích, loại hình, landmark muốn nhấn. Thiếu → tự suy từ bản đồ.

## Cấu trúc 8 scene (timing theo mẫu)
| # | Thời gian | Visual | Headline (trắng + dòng 2 xanh lime) | Câu voice (mẫu) |
|---|-----------|--------|--------------------------------------|-----------------|
| 1 | 0–3.7s | Ảnh AI mặt tiền dự án, bình minh, Ken Burns nhẹ | `<TÊN>` / `RESIDENCE` | "<Tên> — một dự án … gần <điểm nổi bật>, <thành phố>." |
| 2 | 3.7–6.8s | Ảnh AI cảnh đẹp gần địa chỉ (ven hồ/sông/biển/công viên) | `<HOẠT ĐỘNG>` / `<THỜI ĐIỂM>` | "Ảnh do AI tạo, chỉ để minh hoạ không khí …" |
| 3 | 6.8–11s | Map dark zoom vào khu đất, pin kim cương lime | `KHU ĐẤT MINH HOẠ` / `≈ <DIỆN TÍCH> M²` | "Khu đất … rộng khoảng <…> m², phía <hướng> <landmark>." |
| 4 | 11–13.3s | Map, route chấm trắng vẽ dần tới bờ hồ/sông/gần nhất | `<ĐIỂM GẦN NHẤT>` / `<X> PHÚT ĐI BỘ` | "Đi bộ chừng <X> phút là ra tới …" |
| 5 | 13.3–17.5s | Map zoom out, route chấm trắng vẽ dần tới trung tâm thương mại lớn | `<LANDMARK>` / `≈ <X> PHÚT LÁI XE` | "<Landmark> cách khoảng <…> km, chừng <X> phút lái xe." |
| 6 | 17.5–21.5s | Map, route rẽ nhánh tới 2 điểm văn hoá/du lịch | `<A> · <B>` / `<X–Y> PHÚT LÁI XE` | "<A> và <B> cách chừng <X> đến <Y> phút lái xe." |
| 7 | 21.5–25.7s | Map zoom out toàn tuyến tới trung tâm thành phố | `<TRUNG TÂM>` / `≈ <X> PHÚT · <…> KM` | "<Trung tâm> cách khoảng <…> km, chừng <X> phút khi đường thông thoáng." |
| 8 | 25.7–30.5s | Map + vòng tròn bán kính 1km, chấm tiện ích hiện dần + chip đếm | `TIỆN ÍCH` / `TRONG BÁN KÍNH 1 KM` | "Trong bán kính 1 km, bản đồ ghi nhận hơn <…> nhà hàng, quán cà phê và hơn <…> trường học." |
| 9 | ~+7s | Ảnh mặt tiền tối dần + Ken Burns — **GIÁ + CTA** (user yêu cầu bổ sung 2026-10-22: demo cũng phải khiến người xem muốn liên hệ/đặt mua) | Chip `GIÁ DEMO THAM KHẢO` (dự án thật: giá user cung cấp) / chữ lime lớn `TỪ <X> TỶ/CĂN` / nút pill lime `LIÊN HỆ NGAY` / `HOTLINE (DEMO): <số>` / dòng urgency "SỐ CĂN ĐẸP CÒN RẤT ÍT — ƯU TIÊN GIỮ CHỖ SỚM" | "Giá tham khảo demo từ <X> tỷ đồng một căn. Liên hệ ngay qua hotline trên màn hình để nhận tư vấn và bảng giá chi tiết." |
| Outro | cuối | Quay lại ảnh scene 1, tối dần | Tên dự án + `DỰ ÁN … · <KHU VỰC>` + disclaimer (thêm dòng: giá/hotline là demo minh họa nếu dùng số demo) | (không voice — nhạc kết) |

## Design system (khớp mẫu)
- Font: sans bold, uppercase, headline trắng; **dòng nhấn màu lime `#A6F135`**.
- Thanh trên cùng mọi scene: chữ nhỏ trắng 70%:
  `VIDEO DEMO • DỰ ÁN MINH HOẠ • ẢNH TẠO BẰNG AI` (dự án thật: thay bằng tên CĐT/thương hiệu, vẫn giữ "ẢNH TẠO BẰNG AI" nếu dùng ảnh AI).
- Phụ đề: **BỎ HOÀN TOÀN** (quy tắc user 2026-10-22, từ bản Sun Fours Tower): không thanh phụ đề ở đáy trong MỌI scene, kể cả scene 9. Chỉ giữ headline, chip, nhãn đích, footnote bản đồ, text outro/disclaimer.
- Map: nền dark navy sát mẫu. **LƯU Ý KỸ THUẬT (rút kinh nghiệm v1→v2, 2026-10-22):** tile CARTO dark hiện trả "API KEY REQUIRED" (không dùng được, đừng thử lại) → dùng **OSM tiles supersample zoom+1 (retina) + dark transform** (invert → hue-rotate → giảm saturation → tint lạnh), nhãn đường nhỏ/mờ. Framing map phải đủ rộng (scene khu đất ~900m bề ngang) — zoom quá gần sẽ blur và nhãn đường khổng lồ.
- Route: **MỌI route (đi bộ VÀ lái xe) đều là chấm trắng vẽ dần** (quy tắc user 2026-10-22, từ bản Sun Fours Tower — thay cho route neon lime đặc trước đây): chấm trắng + glow nhẹ, mask-reveal để chấm vẽ dần trong ~70% thời lượng voice, ease mượt. KHÔNG dùng route neon lime đặc nữa. Map + route + pin nằm trong **cùng một wrapper transform**: mỗi scene map zoom-out nhẹ 1.16→1.05 kèm pan về hướng route (route không bao giờ lệch map). Điểm đích: dot trắng viền lime + 2 vòng pulse lan tỏa + chip nhãn (tên + thời gian/khoảng cách). Pin dự án = kim cương lime + hộp nhãn đen viền lime. **Scrim gradient đen mờ trên/dưới** để headline/phụ đề luôn đọc rõ (v1 bị nhãn đường chồng headline — không lặp lại). Ô đất scene 3: polygon tô lime mờ + viền đứt nét marching-ants. Chip scene 8: dots pop-in nảy (back.out) lần lượt theo nhóm.
- Góc dưới map: `Bản đồ © OpenStreetMap contributors`; cạnh route ghi chú:
  `THỜI GIAN ƯỚC TÍNH • ĐI BỘ 5 KM/H • Ô TÔ 25 KM/H, CHƯA TÍNH KẸT XE`.
- Chip tiện ích (scene 8): pill viền màu theo nhóm — công viên (xanh lá), nhà hàng·cà phê (hồng), siêu thị (cam), trường học (xanh dương), y tế (đỏ) — số đếm **chạy số (counter)** khi hiện.
- Outro bắt buộc disclaimer trung thực: dự án hư cấu/minh hoạ thì ghi rõ "không có thật, không phải tin rao bán"; dự án thật thì dùng thông tin pháp lý user cung cấp, không tự bịa.

## Số liệu — PHẢI THẬT, không bịa (chuẩn nhà)
1. **Geocode** địa chỉ → tọa độ: Nominatim (OSM), free, không key.
2. **Route + khoảng cách + thời gian**: OSRM public API — `foot` cho đi bộ, `driving` cho lái xe. Chọn 4–5 landmark: điểm gần nhất đi bộ được, 1 TTTM lớn, 2 điểm văn hoá/du lịch, trung tâm hành chính/hồ trung tâm của thành phố đó.
3. **Tiện ích 1km**: Overpass API đếm POI theo nhóm (amenity=restaurant/cafe, shop=supermarket, amenity=school, leisure=park, amenity=hospital/clinic/pharmacy). Ghi nguồn OSM trên hình như mẫu.
4. Số trên headline làm tròn kiểu mẫu: `≈`, thời gian nguyên phút, khoảng cách 1 chữ số thập phân (dấu phẩy kiểu VN: `6,3 KM`).

## Sản xuất — dùng skill hiện có
- **Kịch bản**: theo bảng 8 scene trên; ~85–95 từ voice cho ~37s (nới dài tuỳ chọn 45–60s nếu nhiều landmark — hỏi user nếu >60s).
- **Ảnh AI**: 2 ảnh (mặt tiền + cảnh quan gần địa chỉ) bằng media/image generation; phong cách photoreal, ánh bình minh, cây xanh — ghi nhãn AI như mẫu.
- **Giọng**: skill `local-motion-video` + `local-vieneu-tts` — VieNeu API, voice **`Nam - Nhật Phong`**, speed **1.1**, chia file theo từng scene để sync map animation. Cấm thay giọng khác rồi gọi là Nhật Phong; bản clone local `nhat-phong` chỉ là phương án dự phòng và phải nói rõ là clone.
- **Composition**: HyperFrames + GSAP (skill `local-hyperframes`, `local-hyperframes-animation`): map render từ tile OSM dark tĩnh theo bbox từng scene (pre-render PNG), route SVG overlay vẽ dần, headline vào kiểu fade+rise, Ken Burns nhẹ ở scene ảnh.
- **Audio**: theo `local-motion-video` bước 6 — nhạc warm pad tự tổng hợp ~28dB dưới voice, ducking nhẹ, `alimiter` + loudnorm **−14 LUFS**.
- **QA bắt buộc** (chuẩn motion-video): ffprobe 1080×1920/30fps, loudness/peak, screenshot từng scene, kiểm glyph tiếng Việt, đối chiếu mọi số liệu với kết quả OSRM/Overpass đã lưu, contact sheet.
- **Giao**: MP4 + link tải + duration/size + bảng số liệu nguồn (route nào, bao nhiêu km/phút, đếm tiện ích) để user kiểm chứng. **Không đăng công khai khi chưa được user duyệt** (quy tắc cứng).

## Output contract
User gửi mẫu + địa chỉ → trả MP4 hoàn chỉnh đúng công thức này. Chỉ hỏi lại khi địa chỉ không geocode được hoặc trùng nhiều kết quả.
