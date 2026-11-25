---
name: apple-liquid-glass-ui
description: >-
  True translucent Apple Liquid Glass design system (T-VPN v4 / Loon Mac standard)
  for macOS SwiftUI/AppKit, iOS, Electron, and Web apps. Use whenever the user asks
  for Liquid Glass UI, translucent macOS glass like Loon/T-VPN, frosted Bento cards
  with real desktop wallpaper bleed-through, adjustable glass transparency (0-100%),
  unified glass modals/inputs, or fixing flat/opaque/mismatched UI.
---

# Apple Liquid Glass UI — True Translucent Design Standard (T-VPN / Loon Grade)

Use this skill whenever building or upgrading a macOS, iOS, Electron, or Web app that requires **true translucent Liquid Glass** (real blurred desktop wallpaper shining smoothly through sidebar, canvas, and floating frosted Bento cards — identical to Loon Mac and T-VPN v4).

## 1. The 5 Fatal Anti-Patterns That Ruin Liquid Glass (NEVER DO THESE)

If an app looks "flat grey", "opaque white", or "inconsistent", one of these 5 mistakes caused it:

| Anti-Pattern (Breaks Glass) | Required True Liquid Glass Solution |
|---|---|
| Wrapping main content in an opaque `#FFFFFF` / `#101217` "Inset Sheet" | Keep `outerChromeBg = .clear` and `insetSheetBg = .clear` above `45%` transparency so behind-window vibrancy flows unobstructed across the entire window. |
| Using `NSVisualEffectView` with `.followsWindowActiveState` or `.underWindowBackground` / `.sidebar` | **ALWAYS** use `blendingMode = .behindWindow`, **`state = .active`**, and **`material = .hudWindow`** (only fall back to `.windowBackground` when `reduceTransparency` is on or user sets `transparency <= 0.04`). |
| Stacking 3+ high-alpha overlays (`0.75 + 0.85 + 0.88` white) | Keep total card fill translucent (`white@0.42` Light / `#1B2232@0.48` Dark at default `56%` transparency) with a crisp specular rim (`white@0.68` Light / `white@0.13` Dark) and subtle hairline outer border. |
| Leaving native macOS `.textFieldStyle(.roundedBorder)`, raw `TextEditor`, bright-blue native segmented `Picker`, or stark-white default `.sheet` modals | Replace **100%** of sheets, popovers, inputs, and editors with unified glass primitives (`GlassModalContainer`, `GlassTextField`, `GlassSecureField`, `GlassTextEditor` with `.scrollContentBackground(.hidden)`, `GlassSegmentedControl`). |
| Putting fixed wide `.frame(minWidth: 420)` inside mounted tabs without clamping the tab container | Clamp the persistent tab `ZStack` with `.frame(minWidth: 0, maxWidth: .infinity).clipped()`, keep split-pane `minWidth <= 260`, and wrap toolbars/headers in `ViewThatFits` so `900×760` split-screen never clips or wraps mid-word. |

---

## 2. Core Surface & Adjustable Transparency Formula (`0% – 100%`)

Every Liquid Glass app MUST provide **both** instant presets (`Crystal 86%` | `Clear 74%` | `Loon 56%` | `Solid 0%`) **and** a live **`0% – 100%` Transparency Slider** (updating live at 120fps while dragging, persisting on release, plus a quick-access header popover icon `drop.halffull` so users can tune glass directly over their desktop wallpaper).

Anchor the piecewise-linear alpha curve (`tr` in `0.0...1.0`, forced to `0.0` when `reduceTransparency == true`):

| Token | Solid (`tr = 0.00`) | Default Loon (`tr = 0.56`) | Crystal (`tr = 1.00`) |
|---|---|---|---|
| **Light `outerChromeBg`** | `#E2E6EC` (96%) | `.clear` (`tr >= 0.45`) | `.clear` |
| **Light `sidebarBg`** | `white@0.88` | `white@0.08` | `white@0.01` |
| **Light `bentoCardBg`** | `white@0.95` | `white@0.42` | `white@0.16` |
| **Light `fieldBg`** | `white@0.90` | `white@0.40` | `white@0.18` |
| **Dark `outerChromeBg`** | `#0C111C@0.96` | `#0C111C@0.20` | `#0C111C@0.04` |
| **Dark `sidebarBg`** | `#101522@0.94` | `#101522@0.28` | `#101522@0.08` |
| **Dark `bentoCardBg`** | `#1B2232@0.95` | `#1B2232@0.48` | `#1B2232@0.20` |
| **Dark `fieldBg`** | `white@0.20` | `white@0.065` | `white@0.04` |

### Calm Low-Fatigue Nordic Palette (Zero Neon Glare)
- **Light**: Text `#262C36`, Muted `#545C6B`, Dim `#7A8292`, Primary CTA `#3D74CC`, Active Warm Sand `#BE7632` (soft `16%` bg), Green `#2B9367`, Rose `#C65165`, Indigo `#675FB8`.
- **Dark**: Text `#E3E8F2`, Muted `#9CA7BD`, Dim `#76819A`, Primary CTA `#5B8DEF`, Active Warm Sand `#E6B35A`, Green `#4CC99A`, Rose `#E87C8E`, Indigo `#9B92E8`.

### Concentric Corner Radii
- Window `20pt` → Bento Card `18pt` → Panel `16pt` → Sheet `14pt` → Tile `12pt` → Input/Control `9pt` → Pills/Segmented/Badges `999pt`.

---

## 3. macOS Window, Architecture & Performance Standards

1. **Window Setup (`AppKit` / `SwiftUI`)**:
   - `.windowStyle(.hiddenTitleBar)` + `win.isOpaque = false`, `win.backgroundColor = .clear`, `win.titlebarAppearsTransparent = true`, `win.titleVisibility = .hidden`, `win.styleMask.insert(.fullSizeContentView)`.
   - Set `NSApp.applicationIconImage` from bundled `AppIcon.icns` in `applicationDidFinishLaunching` and bump `CFBundleVersion` whenever updating the icon (plus `lsregister -f` + `killall Dock` on reinstall).
2. **120fps Zero-Lag Tab Switching**:
   - Mount tabs lazily inside a persistent `ZStack` (toggle `.opacity(visible ? 1 : 0)` + `.allowsHitTesting(visible)` + `.zIndex(visible ? 1 : 0)`). Never tear down/recreate heavy views on tab click.
   - Isolate high-frequency live metrics (speed/counters ticking every 1–2s) from structural app state so non-telemetry tabs never re-render during polling.
   - Cache remote icons in `NSCache<NSString, NSImage>` (never re-fetch `AsyncImage` on tab switch).
3. **Zero-Friction Responsive Split-Screen**:
   - Minimum window width `<= 860pt`.
   - Use `ViewThatFits(in: .horizontal)` on top control strips & mode bars (full wide → compact pills/icons → 2-row fallback) so words NEVER wrap mid-word (`Outboun\nd`).
4. **Menu Bar Popover**:
   - Mount fresh `NSHostingController` on open (0% CPU when closed), wrap root in `.background(.ultraThinMaterial)` + `.background(t.outerChromeBg)`, and bind to the exact same `transparency` token.

---

## 4. Drop-In Reference Implementations

Read only the reference matching your target stack:
- **macOS / iOS SwiftUI**: [references/swiftui-kit.swift](./references/swiftui-kit.swift) — complete drop-in `VisualEffectBackground`, `LiquidGlassTokens`, `GlassBentoCard`, `GlassModalContainer`, `GlassTextField`, `GlassTextEditor`, `GlassSegmentedControl`, and `GlassTransparencyPopover`.
- **Web / Electron / React / Tailwind**: [references/web-electron-tokens.css](./references/web-electron-tokens.css) — matching CSS variables, `--glass-tr` slider math, Electron `vibrancy: 'hud-window'` recipe, and `@supports` fallbacks.

---

## 5. Mandatory Visual & Technical QA Before Finishing

Never declare a Liquid Glass UI complete until ALL checks pass:
1. Grep codebase: **0** `.textFieldStyle(.roundedBorder)`, **0** raw unstyled `TextEditor` (missing `.scrollContentBackground(.hidden)`), **0** default stark-white macOS modal sheets.
2. Visually inspect Retina screenshots across **Light (`1240×840`)**, **Dark (`1240×840`)**, **Split-Screen (`900×760`)**, **Primary Modal Sheet**, and **Menu Bar Popover** (if applicable).
3. Verify the **Transparency Slider (`0% – 100%`)** smoothly scales translucency live with zero stutter and honors macOS **Reduce Transparency**.
