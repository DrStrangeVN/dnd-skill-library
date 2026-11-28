# Demo skill-design-review — Review SKILL.md `magic-moment-video`

Ngày: 28/11/2026. Skill: `skill-design-review` (mới chưng cất, chưa push).
Đối tượng review: `~/workspace/custom-skills/magic-moment-video/SKILL.md`
(6.888 byte sau khi sửa, chưng cất cùng đợt 28/11/2026).

## Bảng checklist 12 điểm

| # | Điểm | Kết quả | Ghi chú |
|---|---|---|---|
| 1 | Description nói rõ làm gì + khi nào dùng | ✅ pass | Có trigger: clip talking-head/selfie, "kể lại việc AI đã làm" |
| 2 | Scope một việc hẹp | ✅ pass | Một việc: talking-head → video dọc kể chuyện công việc thật |
| 3 | Body nói "làm gì tiếp theo", không giải thích lĩnh vực | ✅ pass | 6 bước quy trình, không lan man |
| 4 | Tài liệu cồng kềnh dồn references/ | ✅ pass | Không có tài liệu cồng kềnh cần tách; không có references/ thừa |
| 5 | Template chỉ ở assets/ khi output dùng tới | ✅ pass | Không có assets/ thừa |
| 6 | Không trùng lặp SKILL.md ↔ references | ✅ pass | Không có references/ nên không trùng |
| 7 | Lệnh/path tồn tại thật | ✅ pass | `~/workspace/video-kit/demos/`, `deliverables/` đã `ls` thấy; `ffmpeg` có tại `/usr/bin/ffmpeg` |
| 8 | Auth/flow theo helper thật, không bịa | ✅ pass | Tool `mm` chỉ được nhắc để nói "không có, không dùng" (dòng 13, 113) — không bịa flow |
| 9 | Helper có sẵn được ưu tiên | ✅ pass | Remotion + VieNeu + QA frame thay cho `mm` |
| 10 | Ví dụ ngắn, chạy được | ⚠️ nên sửa | Lúc review: chưa có ví dụ beat cụ thể |
| 11 | Output contract rõ | ✅ pass | Mục Output liệt kê video + script/fact sheet + QA.md |
| 12 | Tên chưa trùng, không trùng scope | ✅ pass | Đã kiểm tra local + repo ngày 28/11: tên mới; scope khác motion-video / rea-video / local-real-estate-video (kể chuyện talking-head, không phải explainer hay phân tích) |

## Lỗi tìm thấy: 0 chặn push, 2 nên sửa

1. **Thiếu ví dụ beat cụ thể** (điểm 10) — đã sửa trực tiếp: thêm mục
   "Ví dụ beat (ngắn)" với transcript thật từ vụ BINA 21/11 + mapping 3 beat
   + bằng chứng đối chiếu.
2. **Chưa nói rõ cách giữ giọng gốc** (điểm 8, mức nên sửa) — đã sửa trực
   tiếp: bước render ghi rõ "tách audio gốc khỏi clip bằng ffmpeg, giữ
   nguyên làm narration track — không thu lại giọng khác".

Cả hai sửa đều nhỏ và rõ ràng nên đã áp dụng trực tiếp vào SKILL.md (theo
quy tắc của skill-design-review). File sau sửa: 6.888 byte.

## Kết luận: PASS — đủ điều kiện push (sau khi Trí duyệt demo)

Không còn điểm "chặn push". Skill `magic-moment-video` đạt 12/12 điểm sau
2 sửa nhỏ. Gate này chứng minh skill `skill-design-review` chạy được
end-to-end trên một SKILL.md thật: checklist đầy đủ, kiểm chứng kỹ thuật
bằng lệnh thật, sửa trực tiếp lỗi nhỏ, báo cáo rõ ràng.
