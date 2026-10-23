---
name: muse-gadget-sdk
description: SDK chính thức của Meta để tự build thiết bị phần cứng Muse (gadget): firmware ESP32 và Linux SDK — màn hình, nút bấm, cảm biến, loa/mic, actuator. Cần SDK token và bật Developer mode trong app Muse.
---

# Muse Gadget SDK (chính thức từ Meta)

**Muse Gadgets** là thiết bị mã nguồn mở bạn tự build: lập trình board ESP32 có sẵn hoặc biến Raspberry Pi/Linux thành gadget, rồi kết nối Muse với màn hình, nút bấm, cảm biến, actuator...

- Repo gốc: https://github.com/facebookincubator/muse-gadget-sdk (Apache-2.0)
- Source đã clone: `~/workspace/skill-repos/muse-gadget-sdk`

## Hai SDK

| SDK | Dùng cho |
|---|---|
| **ESP32 Device SDK** (`esp32/`) | Kết nối board ESP32 với Muse: hiển thị ảnh, audio in/out, cảm biến. Có simulator. |
| **Linux Device SDK** (`linux/`) | Biến Raspberry Pi/Linux box thành gadget; tự viết command để Muse làm sysadmin hoặc điều khiển Home Assistant. |

## Bắt đầu

1. Lấy **SDK token** tại https://gadgets.muse.ai/settings/sdk-tokens và đọc [Gadget SDK Terms](https://gadgets.muse.ai/sdk-terms). Mỗi gadget cần một token để pair — **giữ token bí mật, không build sẵn vào firmware chia sẻ cho người khác**.
2. Trong app Muse (iOS/Android): bật **Developer mode** (Settings), vào Settings > Devices, tìm thiết bị có tiền tố `MuseGadget` để pair.
3. Mỗi thư mục `esp32/` và `linux/` có `README.md` hướng dẫn và `AGENTS.md` cho coding agent.

## Cộng đồng & ví dụ build

- Discord cộng đồng builder; các build tiêu biểu: Muse Pocket (e-paper Xteink X4 Pro — đã có skill `muse-pocket`), Muse trên M5Stack StackChan, PSP, Rabbit r1, router OpenWrt, Home Assistant bridge.
- Lưu ý bản quyền: Apache-2.0 **không** cover Jollybot avatar; một số file third-party giữ license gốc (xem README repo).
