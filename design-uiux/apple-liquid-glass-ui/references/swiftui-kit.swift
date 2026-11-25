// Production Drop-In Apple Liquid Glass Kit (macOS 14+ / iOS 17+, SwiftUI 6)
// Proven in T-VPN v4 / Loon Mac side-by-side translucency parity.

import SwiftUI
#if os(macOS)
import AppKit

/// True behind-window macOS vibrancy. ALWAYS uses `.active` + `.hudWindow` so
/// desktop wallpaper shines vibrantly even when inactive or compared side-by-side.
public struct LiquidGlassBackground: NSViewRepresentable {
    public let isLight: Bool
    public let transparency: Double // 0.0 (solid) .. 1.0 (crystal clear)
    public let reduceTransparency: Bool

    public init(isLight: Bool, transparency: Double = 0.56, reduceTransparency: Bool = false) {
        self.isLight = isLight
        self.transparency = transparency
        self.reduceTransparency = reduceTransparency
    }

    public func makeNSView(context: Context) -> NSVisualEffectView {
        let v = NSVisualEffectView()
        v.blendingMode = .behindWindow
        v.state = .active
        apply(to: v)
        return v
    }

    public func updateNSView(_ nsView: NSVisualEffectView, context: Context) {
        apply(to: nsView)
    }

    private func apply(to view: NSVisualEffectView) {
        view.appearance = NSAppearance(named: isLight ? .aqua : .darkAqua)
        view.state = .active
        if reduceTransparency || transparency <= 0.04 {
            view.material = isLight ? .windowBackground : .underWindowBackground
        } else {
            view.material = .hudWindow
        }
    }
}

/// Call in `.onAppear` of your root WindowGroup view.
@MainActor
public func configureLiquidGlassWindow() {
    for win in NSApp.windows {
        win.isOpaque = false
        win.backgroundColor = .clear
        win.titlebarAppearsTransparent = true
        win.titleVisibility = .hidden
        win.styleMask.insert(.fullSizeContentView)
    }
}
#endif

public struct LiquidGlassTokens: Sendable {
    public let isLight: Bool
    public let transparency: Double // 0.0 = Solid, 0.56 = Loon Balanced, 1.0 = Crystal Clear
    public let reduceTransparency: Bool

    public init(isLight: Bool, transparency: Double = 0.56, reduceTransparency: Bool = false) {
        self.isLight = isLight
        self.transparency = min(1.0, max(0.0, transparency))
        self.reduceTransparency = reduceTransparency
    }

    public var effectiveTransparency: Double { reduceTransparency ? 0.0 : transparency }

    private static func lerp(_ a: Double, _ b: Double, _ t: Double) -> Double {
        let c = min(1.0, max(0.0, t))
        return a + (b - a) * c
    }

    private func alpha(solid: Double, balanced: Double, crystal: Double) -> Double {
        let tr = effectiveTransparency
        return tr <= 0.56
            ? Self.lerp(solid, balanced, tr / 0.56)
            : Self.lerp(balanced, crystal, (tr - 0.56) / 0.44)
    }

    // Surfaces
    public var outerChromeBg: Color {
        let tr = effectiveTransparency
        if tr <= 0.02 { return isLight ? Color(hex: 0xE2E6EC) : Color(hex: 0x151923) }
        if isLight {
            if tr >= 0.45 { return .clear }
            return Color(hex: 0xE2E6EC, alpha: Self.lerp(0.96, 0.0, tr / 0.45))
        }
        return Color(hex: 0x0C111C, alpha: alpha(solid: 0.96, balanced: 0.20, crystal: 0.04))
    }

    public var sidebarBg: Color {
        let tr = effectiveTransparency
        if tr <= 0.02 { return isLight ? Color(hex: 0xDDE1E8) : Color(hex: 0x171C27) }
        return isLight
            ? Color.white.opacity(alpha(solid: 0.88, balanced: 0.08, crystal: 0.01))
            : Color(hex: 0x101522, alpha: alpha(solid: 0.94, balanced: 0.28, crystal: 0.08))
    }

    public var insetCanvasBg: Color {
        let tr = effectiveTransparency
        if tr <= 0.02 { return isLight ? Color(hex: 0xE4E8EE) : Color(hex: 0x141822) }
        return isLight ? .clear : Color.black.opacity(Self.lerp(0.18, 0.02, tr))
    }

    public var bentoCardBg: Color {
        let tr = effectiveTransparency
        if tr <= 0.02 { return isLight ? Color(hex: 0xEFF2F6) : Color(hex: 0x1E2331) }
        return isLight
            ? Color.white.opacity(alpha(solid: 0.95, balanced: 0.42, crystal: 0.16))
            : Color(hex: 0x1B2232, alpha: alpha(solid: 0.95, balanced: 0.48, crystal: 0.20))
    }

    public var fieldBg: Color {
        let tr = effectiveTransparency
        if tr <= 0.02 { return isLight ? Color(hex: 0xE6EAF0) : Color(hex: 0x161B27) }
        return isLight
            ? Color.white.opacity(alpha(solid: 0.90, balanced: 0.40, crystal: 0.18))
            : Color.white.opacity(alpha(solid: 0.20, balanced: 0.065, crystal: 0.04))
    }

    public var raisedBg: Color { isLight ? Color(hex: 0x182334, alpha: 0.06) : Color.white.opacity(0.075) }
    public var selectedPillBg: Color { isLight ? Color(hex: 0x3B76D6, alpha: 0.16) : Color(hex: 0x5B8DEF, alpha: 0.22) }
    public var menuBg: Color { isLight ? Color(hex: 0xF0F4F9, alpha: 0.86) : Color(hex: 0x171C29, alpha: 0.88) }
    public var cardShadow: Color { isLight ? Color.black.opacity(0.042) : Color.black.opacity(0.28) }

    // Borders & Specular Rim
    public var line: Color { isLight ? Color(hex: 0x182334, alpha: 0.08) : Color.white.opacity(0.09) }
    public var lineStrong: Color { isLight ? Color(hex: 0x182334, alpha: 0.15) : Color.white.opacity(0.17) }
    public var specularTop: Color { isLight ? Color.white.opacity(0.68) : Color.white.opacity(0.13) }

    // Typography & Calm Nordic Accents
    public var text: Color { isLight ? Color(hex: 0x262C36) : Color(hex: 0xE3E8F2) }
    public var muted: Color { isLight ? Color(hex: 0x545C6B) : Color(hex: 0x9CA7BD) }
    public var dim: Color { isLight ? Color(hex: 0x7A8292) : Color(hex: 0x76819A) }
    public var primaryCTA: Color { isLight ? Color(hex: 0x3D74CC) : Color(hex: 0x5B8DEF) }
    public var green: Color { isLight ? Color(hex: 0x2B9367) : Color(hex: 0x4CC99A) }
    public var amber: Color { isLight ? Color(hex: 0xBE7632) : Color(hex: 0xE6B35A) }
    public var rose: Color { isLight ? Color(hex: 0xC65165) : Color(hex: 0xE87C8E) }
}

private extension Color {
    init(hex: UInt32, alpha: Double = 1.0) {
        self.init(
            .sRGB,
            red: Double((hex >> 16) & 0xFF) / 255.0,
            green: Double((hex >> 8) & 0xFF) / 255.0,
            blue: Double(hex & 0xFF) / 255.0,
            opacity: alpha
        )
    }
}

/// Floating frosted Bento card with double specular + structural hairline rim.
public struct GlassBentoCard<Content: View>: View {
    let t: LiquidGlassTokens
    let padding: CGFloat
    let radius: CGFloat
    let content: Content

    public init(tokens: LiquidGlassTokens, padding: CGFloat = 16, radius: CGFloat = 18, @ViewBuilder content: () -> Content) {
        self.t = tokens
        self.padding = padding
        self.radius = radius
        self.content = content()
    }

    public var body: some View {
        content
            .padding(padding)
            .background(t.bentoCardBg)
            .clipShape(RoundedRectangle(cornerRadius: radius, style: .continuous))
            .overlay(RoundedRectangle(cornerRadius: radius, style: .continuous).strokeBorder(t.specularTop, lineWidth: 0.75))
            .overlay(RoundedRectangle(cornerRadius: radius, style: .continuous).strokeBorder(t.line, lineWidth: 0.5))
            .shadow(color: t.cardShadow, radius: 6, x: 0, y: 2)
    }
}

/// Unified translucent input well — replaces harsh white macOS `.roundedBorder`.
public struct GlassTextField: View {
    let t: LiquidGlassTokens
    let placeholder: String
    @Binding var text: String

    public init(tokens: LiquidGlassTokens, _ placeholder: String, text: Binding<String>) {
        self.t = tokens
        self.placeholder = placeholder
        self._text = text
    }

    public var body: some View {
        TextField(placeholder, text: $text)
            .textFieldStyle(.plain)
            .font(.system(size: 12.5))
            .foregroundStyle(t.text)
            .padding(.horizontal, 10)
            .frame(height: 30)
            .background(t.fieldBg)
            .clipShape(RoundedRectangle(cornerRadius: 9, style: .continuous))
            .overlay(RoundedRectangle(cornerRadius: 9, style: .continuous).strokeBorder(t.lineStrong, lineWidth: 0.75))
    }
}

/// Unified translucent code/multiline editor — ALWAYS hides default white scroll background.
public struct GlassTextEditor: View {
    let t: LiquidGlassTokens
    @Binding var text: String
    let minHeight: CGFloat

    public init(tokens: LiquidGlassTokens, text: Binding<String>, minHeight: CGFloat = 140) {
        self.t = tokens
        self._text = text
        self.minHeight = minHeight
    }

    public var body: some View {
        TextEditor(text: $text)
            .font(.system(size: 12, design: .monospaced))
            .foregroundStyle(t.text)
            .scrollContentBackground(.hidden)
            .padding(8)
            .frame(minHeight: minHeight)
            .background(t.fieldBg)
            .clipShape(RoundedRectangle(cornerRadius: 11, style: .continuous))
            .overlay(RoundedRectangle(cornerRadius: 11, style: .continuous).strokeBorder(t.lineStrong, lineWidth: 0.75))
    }
}
