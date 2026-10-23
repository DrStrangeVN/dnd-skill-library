---
name: event-operations-pro
description: "Biến event brief, email, meeting notes, Word, PDF, Excel hoặc quy trình rời rạc thành bộ Event Operations hoàn chỉnh: run sheet, timeline, manpower, checklist, suppliers, guest list, contingency plan, contacts và event-day command sheet; ưu tiên Excel làm command center và có thể tạo DOCX/PDF/PPTX để briefing." 
---

# Event Operations Pro

## Mục tiêu
Biến thông tin sự kiện rời rạc thành một hệ thống vận hành có thể dùng thật trước, trong và sau event.

Plugin phải giúp Event Lead/GM trả lời nhanh:
- Event diễn ra khi nào, ở đâu, mục tiêu là gì?
- Mốc quan trọng trước event là gì?
- Ai phụ trách từng hạng mục?
- Supplier nào đang ở trạng thái nào?
- Khách/VIP/Sponsor/Media nào cần xử lý đặc biệt?
- Trong ngày event, từng phút ai làm gì?
- Nếu trễ, mất điện, mưa, supplier fail, talent trễ, crowd issue... thì xử lý thế nào?
- Ai là decision owner và escalation contact?
- Checklist nào phải hoàn tất trước khi mở cửa / bắt đầu chương trình?

## Nguồn đầu vào hỗ trợ
Có thể làm việc từ:
- event brief bằng chat;
- email / email thread;
- Word / DOCX;
- PDF hoặc PDF scan;
- Excel / Google Sheet;
- meeting notes / minutes;
- proposal / quotation;
- supplier list;
- guest list;
- venue plan / floor plan / image / screenshot;
- agenda / script / MC script;
- nhiều nguồn cùng lúc.

Khi nhiều nguồn mâu thuẫn, không tự chọn một phiên bản. Đánh dấu `Needs Confirmation` và chỉ rõ nguồn nào khác nhau.

## Nguyên tắc vận hành
1. Không tự bịa thời gian, địa điểm, số lượng khách, ngân sách, supplier, hotline, người chịu trách nhiệm hoặc quyền phê duyệt.
2. Nếu chưa có dữ kiện nhưng vẫn xây được bộ khung, dùng `TBD` hoặc `Needs Confirmation`.
3. Phân biệt rõ:
   - Confirmed = đã được nguồn xác nhận;
   - Planned = kế hoạch hiện tại;
   - Recommended = đề xuất tối ưu;
   - Contingency = phương án dự phòng.
4. Mỗi hạng mục quan trọng phải có Owner, Deadline/Time, Status và Next Action khi phù hợp.
5. Trong event-day run sheet, thời gian là nguồn sự thật chính; không để hai hoạt động xung đột tài nguyên mà không cảnh báo.
6. Những việc ảnh hưởng an toàn, crowd, điện, y tế, venue, talent/VIP, sponsor commitment hoặc pháp lý phải có escalation rõ.
7. Không làm tài liệu đẹp nhưng không dùng được. Ưu tiên thao tác nhanh, filter được, tick được và đọc tốt trên laptop/điện thoại.
8. Giữ một nguồn dữ liệu chính. Không lặp guest list, supplier info hoặc timeline ở nhiều file nếu có thể tránh.

# DEFAULT OUTPUT — EVENT OPERATIONS PACK

Nếu người dùng không chỉ định format, ưu tiên tạo:

1. `01_Event_Command_Center.xlsx` — file vận hành trung tâm
2. `02_Event_Day_Command_Sheet.docx` — bản 1–2 trang cho Event Lead/GM
3. `03_Event_Team_Brief.pptx` — tùy chọn, dùng khi cần briefing/training trước event

Nếu event nhỏ, có thể chỉ cần XLSX + Command Sheet.
Nếu event lớn/phức tạp, nên tạo đủ cả 3.

# 1. EVENT COMMAND CENTER — XLSX

Workbook mặc định nên có các sheet sau; chỉ tạo sheet có giá trị thực tế.

## 00_Dashboard
Tóm tắt:
- Event name
- Date / time
- Venue
- Event Lead
- Days to event nếu biết
- Overall readiness % nếu có đủ checklist để tính
- Open critical issues
- Pending approvals
- Critical suppliers
- VIP / sponsor / media alerts
- Weather / venue / access alerts nếu nguồn có

Không giả tạo readiness % nếu không có dữ liệu đủ để tính.

## 01_Master_Timeline
Dùng cho giai đoạn chuẩn bị trước event.

Columns khuyến nghị:
| ID | Phase | Task | Owner | Start | Deadline | Dependency | Priority | Status | Approval | Notes |

Phase ví dụ:
- Planning
- Procurement
- Production
- Marketing/Comms
- Guest/VIP
- Venue
- Rehearsal
- Event Day
- Post Event

## 02_Run_Sheet
Đây là sheet quan trọng nhất cho ngày event.

Columns khuyến nghị:
| Time | Duration | Activity | Location | Owner | Supporting Team | Vendor/Talent | Cue / Trigger | Required Asset | Status | Backup Plan | Notes |

Quy tắc:
- Sắp theo thời gian tăng dần.
- Có load-in / setup / soundcheck / rehearsal / doors open / program / breakdown nếu phù hợp.
- Cảnh báo overlap bất hợp lý của Owner, location hoặc resource.
- Nếu có hard cue, đánh dấu rõ.
- Không tự thêm thời gian nếu chưa có cơ sở; dùng TBD.

## 03_Manpower
Columns:
| Person / Role | Team | Responsibility | Call Time | Shift Start | Shift End | Zone | Supervisor | Backup | Phone/Contact | Status |

Nếu chưa có tên người, dùng role thay vì bịa tên.

Phải kiểm tra:
- vị trí chưa có người;
- ca chồng chéo;
- khoảng thời gian không có coverage;
- một người bị giao quá nhiều critical task cùng lúc;
- thiếu backup cho vị trí quan trọng.

## 04_Checklists
Có thể chia theo category hoặc phase.

Columns:
| Category | Checklist Item | Owner | Due | Critical? | Status | Evidence / Link | Notes |

Category ví dụ:
- Venue
- Production
- AV / LED / Sound / Light
- Branding
- Registration
- VIP / Guest
- Sponsor
- Security
- Medical / Safety
- F&B
- Transport
- Staff
- Content / Media
- Finance / Payment
- Breakdown / Return

## 05_Suppliers
Columns:
| Supplier | Category | Contact | Scope | PO/Contract | Cost | Deposit | Balance | Delivery Time | On-site Contact | Status | Risk | Backup Supplier | Notes |

Chỉ đưa số tiền khi nguồn có.

Kiểm tra:
- supplier chưa confirm;
- chưa có hợp đồng/PO khi cần;
- còn balance / payment milestone;
- delivery time xung đột;
- thiếu on-site contact;
- chưa có backup cho critical vendor.

## 06_Guest_List
Columns khuyến nghị:
| Guest Name | Organization | Category | VIP Level | Invitation Status | RSVP | +1 | Contact | Arrival Time | Seating/Zone | Host/Owner | Special Requirement | Check-in Status | Notes |

Category có thể gồm:
- VIP
- Sponsor
- Partner
- Media
- Speaker/Talent
- Staff
- General Guest

Không suy đoán VIP level nếu không có nguồn.

## 07_Contingency
Columns:
| Risk / Scenario | Likelihood | Impact | Trigger | Prevention | Immediate Action | Decision Owner | Escalation Contact | Backup Resource | Status |

Scenario cần cân nhắc khi phù hợp:
- rain / extreme weather
- power outage
- AV / LED / sound failure
- internet / check-in failure
- talent/speaker late or no-show
- supplier delay/no-show
- transport delay
- crowd congestion
- medical incident
- security incident
- venue access issue
- lost item / missing asset
- sponsor deliverable missed
- program running late
- guest/VIP complaint

Không gán mức Likelihood/Impact chắc chắn nếu thiếu dữ liệu; có thể dùng `To Assess`.

## 08_Contacts
Một nguồn liên lạc duy nhất:
| Function | Name | Company/Team | Role | Phone | Backup Contact | Radio/Channel | Notes |

Ưu tiên nhóm:
- Event Lead
- Venue
- Production
- AV
- Security
- Medical
- Registration
- Guest/VIP
- Transport
- Supplier leads
- Client/Sponsor decision maker

## 09_Approvals_Decisions
Columns:
| Decision ID | Issue | Decision Needed | Options | Recommended Option | Decision Owner | Deadline | Status | Decision / Evidence |

`Recommended Option` chỉ dùng nếu có cơ sở; phải phân biệt đề xuất với quyết định đã duyệt.

## 10_Incident_Log
Dùng trong ngày event khi cần:
| Time | Incident | Location | Severity | Reported By | Immediate Action | Owner | Escalated To | Resolution | Closed Time | Follow-up |

## 11_Post_Event
Có thể gồm:
- returned assets;
- supplier reconciliation;
- outstanding payments;
- incident follow-up;
- sponsor deliverables;
- content handover;
- lessons learned;
- post-event report actions.

# 2. EVENT-DAY COMMAND SHEET — DOCX/PDF

Mục tiêu: Event Lead/GM có thể mở trên điện thoại hoặc in 1–2 trang và nắm ngay event.

Nội dung mặc định:

## Event Header
- Event name
- Date
- Venue
- Event Lead
- Doors Open / Start / End

## Critical Timeline
Chỉ đưa các mốc then chốt, không copy cả run sheet.

## Command Structure
- Event Lead
- Production Lead
- Venue Lead
- Guest/VIP Lead
- Security
- Medical
- Client/Sponsor contact

## Critical Contacts
Chỉ số cần gọi trong event day.

## Critical Checks Before Go-Live
5–15 check quan trọng nhất.

## Top Risks & Backup Actions
3–8 rủi ro quan trọng nhất.

## Pending Decisions / Red Flags
Chỉ các mục còn mở có thể ảnh hưởng chương trình.

## Emergency / Escalation Flow
Ai gọi ai và ai có quyền quyết định.

Command Sheet phải ngắn, ưu tiên scan trong 30–60 giây.

# 3. EVENT TEAM BRIEF — PPTX

Chỉ tạo nếu người dùng cần briefing, training hoặc event có nhiều team/supplier.

Khuyến nghị 7–12 slides:
1. Event Overview
2. Objective / Success Criteria
3. Venue / Zones
4. Team Structure
5. Master Timeline
6. Event-Day Run of Show
7. Guest / VIP Journey
8. Supplier / Production Readiness
9. Safety + Contingency
10. Key Do / Don't
11. Escalation & Contacts
12. Final Checklist / Call Time

Slide phải trực quan, không copy nguyên bảng Excel lên slide.

# WORKFLOW XỬ LÝ

## Bước 1 — Intake & Extract
Trích xuất:
- Event objective
- Date/time/venue
- Audience / guest type
- Expected attendance nếu có
- Stakeholders
- Program / agenda
- Production needs
- Venue constraints
- Suppliers
- Guest/VIP requirements
- Budget/payment items nếu có
- Approval points
- Existing risks

## Bước 2 — Build Event Structure
Tạo workstreams:
- Program
- Venue
- Production
- Guest/VIP
- Staff/Manpower
- Supplier
- Security/Safety
- Transport
- F&B
- Branding
- Sponsor/Partner
- Media/Content
- Finance/Payment
- Post-event

Chỉ giữ workstream phù hợp.

## Bước 3 — Build Timeline & Dependencies
Xác định:
- deadline;
- dependency;
- handoff;
- approval;
- critical path;
- hard deadline.

Nếu thấy task deadline sau dependency hoặc logic thời gian sai, cảnh báo.

## Bước 4 — Build Event-Day Run Sheet
Kết hợp agenda + setup + operation + breakdown.
Kiểm tra:
- gap;
- overlap;
- thiếu owner;
- thiếu location;
- thiếu cue;
- thiếu buffer cho các điểm chuyển giao quan trọng.

Không tự thêm buffer cụ thể nếu chưa đủ cơ sở; có thể đề xuất `Recommended Buffer`.

## Bước 5 — Build Manpower & Coverage
Map role với timeline và zone.
Phát hiện thiếu coverage, owner xung đột hoặc thiếu backup.

## Bước 6 — Supplier & Guest Readiness
Supplier:
- scope;
- delivery;
- contact;
- confirmation;
- payment/contract nếu có;
- backup.

Guest:
- invite;
- RSVP;
- arrival;
- check-in;
- seating/zone;
- owner/host;
- special requirement.

## Bước 7 — Contingency & Escalation
Ưu tiên các rủi ro có thể phá chương trình hoặc gây safety/reputation impact.
Mỗi risk cần Trigger + Immediate Action + Decision Owner.

## Bước 8 — Generate Outputs
Tạo XLSX command center trước.
Sau đó tạo Command Sheet và PPTX nếu phù hợp.

## Bước 9 — QA
Trước khi giao, kiểm tra:
- timeline không mâu thuẫn;
- run sheet theo thứ tự thời gian;
- critical task có owner;
- contact critical không bị thiếu nếu nguồn có;
- guest/supplier không bị duplicate;
- manpower không xung đột obvious;
- status thống nhất;
- decision/approval chưa duyệt không bị ghi thành đã duyệt;
- risk có action và owner;
- file dễ filter / print / xem trên laptop;
- không có thông tin bịa.

# STATUS STANDARD
Ưu tiên dùng một bộ status thống nhất:
- Not Started
- In Progress
- Waiting / Pending
- Confirmed
- Blocked
- Done
- Cancelled
- Needs Confirmation

Có thể thay đổi theo hệ thống của người dùng nhưng phải thống nhất trong toàn workbook.

# PRIORITY STANDARD
- Critical — ảnh hưởng trực tiếp đến safety, start time, program, VIP/sponsor commitment hoặc event delivery
- High
- Medium
- Low

Không tự nâng mức Critical chỉ để làm nổi bật.

# FORMATTING PRINCIPLES

## Excel
- Freeze header / key columns khi phù hợp.
- Dùng Excel Table cho dữ liệu dạng danh sách nếu hợp lý.
- Có filter.
- Wrap text ở notes/action.
- Date/time nhất quán.
- Status / Priority có conditional formatting rõ ràng nhưng không lạm dụng màu.
- Không merge cell trong bảng dữ liệu chính.
- Dashboard đơn giản, phục vụ quyết định.
- Giữ cột vừa đủ để dùng trên laptop.

## DOCX/PDF Command Sheet
- 1–2 trang nếu có thể.
- Font dễ đọc.
- Critical info ở trang đầu.
- Không để đoạn văn dài.
- Contact và escalation dễ tìm.

## PPTX
- Visual, ít chữ.
- Mỗi slide một mục tiêu.
- Run-of-show nên dùng timeline/flow.
- Không nhồi nguyên worksheet vào slide.

# SPECIAL MODES

## Event Readiness Audit
Khi người dùng đã có file vận hành, kiểm tra:
- missing owner;
- overdue task;
- blocked task;
- duplicate guest;
- duplicate supplier;
- unpaid / unconfirmed critical vendor;
- schedule conflict;
- missing contact;
- manpower gap;
- missing contingency;
- unresolved decision;
- pre-opening checklist gaps.

Trả về:
- Red Flags
- Decisions Required
- Actions Today
- Actions Before Event

## Event-Day Mode
Ưu tiên cực ngắn và hành động được:
- Now
- Next 60 Minutes
- Critical Issues
- Decision Needed
- Who Owns It
- Backup Plan

## VIP / Sponsor Mode
Tập trung:
- arrival;
- host;
- parking/transport;
- check-in;
- seating;
- speaking/photo moment;
- branding/deliverables;
- hospitality;
- departure;
- special notes.

## Sports / Matchday Mode
Khi phù hợp có thể thêm:
- team arrival;
- accreditation;
- locker room;
- warm-up;
- court/field readiness;
- officials;
- security;
- sponsor activation;
- media;
- halftime/show flow;
- post-game obligations;
- transport/departure.

## Conference / Corporate Event Mode
Khi phù hợp có thể thêm:
- speaker management;
- presentation collection;
- stage cues;
- session timing;
- delegate registration;
- breakout rooms;
- catering;
- media;
- VIP protocol.

# OUTPUT SUMMARY TRONG CHAT
Khi hoàn tất, tóm tắt ngắn:
- Event và ngày tổ chức nếu đã biết;
- file nào là command center;
- số critical issues/open decisions;
- các mục Needs Confirmation;
- 3–7 việc ưu tiên tiếp theo.

# LỆNH GỌI NHANH
Ví dụ:
- "Biến brief này thành bộ Event Operations hoàn chỉnh. Tạo Run Sheet, Timeline, Manpower, Supplier, Guest List, Checklist, Contingency và Event-Day Command Sheet."
- "Đọc toàn bộ email và file này rồi tạo Event Command Center Excel cho tôi."
- "Audit file event hiện tại, tìm task thiếu owner, timeline conflict, supplier chưa confirm và các rủi ro trước event."
- "Tạo Event-Day Mode cho ngày mai: command sheet 1 trang + run sheet theo phút + escalation contacts."
- "Tạo bản PPT briefing cho toàn bộ staff và supplier từ Event Command Center này."
