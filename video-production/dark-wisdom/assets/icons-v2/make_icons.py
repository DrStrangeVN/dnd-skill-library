#!/usr/bin/env python3
"""Vẽ 12 icon SVG neon line-art cho dark-wisdom v1.3 (assets/icons-v2/)."""
import os

OUT = os.path.expanduser("~/workspace/skills/dark-wisdom/assets/icons-v2")
os.makedirs(OUT, exist_ok=True)

GOLD = "#D8B36A"
BLUE = "#A8C8E8"
HEAD = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" '
        'fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round" '
        'stroke-linejoin="round">\n')
TAIL = "</svg>\n"

def svg(color, body):
    return HEAD.format(c=color) + body + TAIL

ICONS = {
    # 1. Đồng xu nứt vỡ — tiền bạc mong manh
    "coin-crack": (GOLD,
     '<circle cx="100" cy="100" r="62"/>\n'
     '<circle cx="100" cy="100" r="47" stroke-width="5"/>\n'
     '<polyline points="100,42 86,68 104,92 88,118 100,158"/>\n'),
    # 2. Cán cân: tim vs đồng xu — tình vs tiền
    "scale-heart-coin": (GOLD,
     '<line x1="100" y1="28" x2="100" y2="148"/>\n'
     '<line x1="42" y1="44" x2="158" y2="44"/>\n'
     '<line x1="42" y1="44" x2="26" y2="88"/>\n'
     '<line x1="42" y1="44" x2="58" y2="88"/>\n'
     '<line x1="158" y1="44" x2="142" y2="88"/>\n'
     '<line x1="158" y1="44" x2="174" y2="88"/>\n'
     '<path d="M42 96 c-6,-8 -20,-4 -20,6 c0,8 10,14 20,22 c10,-8 20,-14 20,-22 c0,-10 -14,-14 -20,-6"/>\n'
     '<circle cx="158" cy="106" r="18"/>\n'
     '<circle cx="158" cy="106" r="10" stroke-width="5"/>\n'
     '<line x1="72" y1="148" x2="128" y2="148"/>\n'
     '<line x1="100" y1="148" x2="100" y2="164"/>\n'
     '<line x1="82" y1="164" x2="118" y2="164"/>\n'),
    # 3. Đồng hồ cát, cát là đồng xu — thời gian = tiền
    "hourglass-coins": (GOLD,
     '<line x1="62" y1="28" x2="138" y2="28"/>\n'
     '<line x1="62" y1="172" x2="138" y2="172"/>\n'
     '<path d="M62 28 C62 76 92 82 92 100 C92 118 62 124 62 172"/>\n'
     '<path d="M138 28 C138 76 108 82 108 100 C108 118 138 124 138 172"/>\n'
     '<line x1="100" y1="100" x2="100" y2="126" stroke-width="5"/>\n'
     '<circle cx="100" cy="136" r="6" stroke-width="5"/>\n'
     '<circle cx="86" cy="152" r="9"/>\n'
     '<circle cx="104" cy="157" r="9"/>\n'
     '<circle cx="121" cy="150" r="9"/>\n'),
    # 4. Mặt nạ hai mặt — giả tạo
    "mask-twoface": (BLUE,
     '<path d="M58 72 Q100 48 142 72 Q142 132 100 152 Q58 132 58 72 Z"/>\n'
     '<line x1="100" y1="54" x2="100" y2="152" stroke-width="5"/>\n'
     '<path d="M70 84 Q82 80 94 84" stroke-width="5"/>\n'
     '<line x1="106" y1="88" x2="130" y2="80" stroke-width="5"/>\n'
     '<path d="M72 96 Q82 89 94 96" stroke-width="5"/>\n'
     '<path d="M106 96 Q118 89 128 96" stroke-width="5"/>\n'
     '<path d="M74 122 Q86 130 98 124" stroke-width="5"/>\n'
     '<line x1="104" y1="126" x2="126" y2="126" stroke-width="5"/>\n'),
    # 5. Con mắt với dấu hỏi — đọc vị
    "eye-question": (BLUE,
     '<path d="M36 100 Q100 58 164 100 Q100 142 36 100 Z"/>\n'
     '<circle cx="100" cy="100" r="24"/>\n'
     '<path d="M93 96 Q93 86 103 86 Q112 86 112 94 Q112 100 103 103 L103 107" stroke-width="5"/>\n'
     '<circle cx="103" cy="113" r="3" fill="'+BLUE+'" stroke="none"/>\n'),
    # 6. Bóng người đơn độc dưới đèn đường — cô độc
    "lone-lamp": (GOLD,
     '<line x1="132" y1="36" x2="132" y2="168"/>\n'
     '<line x1="132" y1="36" x2="88" y2="36"/>\n'
     '<path d="M78 36 h20 l-4 12 h-12 z"/>\n'
     '<line x1="80" y1="52" x2="64" y2="120" stroke-width="4" stroke-dasharray="6 8"/>\n'
     '<line x1="96" y1="52" x2="112" y2="120" stroke-width="4" stroke-dasharray="6 8"/>\n'
     '<circle cx="88" cy="108" r="9"/>\n'
     '<line x1="88" y1="117" x2="88" y2="148"/>\n'
     '<line x1="88" y1="148" x2="78" y2="168"/>\n'
     '<line x1="88" y1="148" x2="98" y2="168"/>\n'
     '<line x1="88" y1="126" x2="78" y2="142"/>\n'
     '<line x1="40" y1="168" x2="160" y2="168"/>\n'),
    # 7. Bàn tay buông đồng xu rơi — mất mát
    "hand-coin-drop": (GOLD,
     '<path d="M60 60 Q100 48 140 60"/>\n'
     '<line x1="70" y1="58" x2="70" y2="86"/>\n'
     '<line x1="90" y1="54" x2="90" y2="84"/>\n'
     '<line x1="110" y1="54" x2="110" y2="84"/>\n'
     '<line x1="130" y1="58" x2="130" y2="86"/>\n'
     '<path d="M60 60 Q55 75 70 86"/>\n'
     '<circle cx="100" cy="120" r="11"/>\n'
     '<circle cx="112" cy="150" r="11"/>\n'
     '<circle cx="96" cy="178" r="9"/>\n'),
    # 8. Ngọn lửa trong lồng kính — tham vọng bị nhốt
    "flame-cage": (GOLD,
     '<line x1="70" y1="62" x2="70" y2="150"/>\n'
     '<line x1="86" y1="62" x2="86" y2="150"/>\n'
     '<line x1="114" y1="62" x2="114" y2="150"/>\n'
     '<line x1="130" y1="62" x2="130" y2="150"/>\n'
     '<path d="M62 62 Q100 38 138 62"/>\n'
     '<line x1="62" y1="150" x2="138" y2="150"/>\n'
     '<circle cx="100" cy="30" r="6"/>\n'
     '<path d="M100 132 Q86 112 93 96 Q97 106 101 100 Q105 90 101 76 Q116 96 109 116 Q106 126 100 132 Z"/>\n'),
    # 9. Chiếc ghế trống — vắng mặt
    "empty-chair": (BLUE,
     '<line x1="72" y1="36" x2="72" y2="100"/>\n'
     '<line x1="112" y1="36" x2="112" y2="100"/>\n'
     '<line x1="72" y1="54" x2="112" y2="54"/>\n'
     '<line x1="72" y1="72" x2="112" y2="72"/>\n'
     '<line x1="72" y1="90" x2="112" y2="90"/>\n'
     '<line x1="72" y1="100" x2="132" y2="100"/>\n'
     '<line x1="72" y1="100" x2="72" y2="162"/>\n'
     '<line x1="132" y1="100" x2="132" y2="162"/>\n'
     '<line x1="72" y1="132" x2="132" y2="132"/>\n'),
    # 10. Mũi tên đâm xuyên trái tim giấy — tổn thương
    "arrow-heart": (GOLD,
     '<path d="M100 132 C72 108 56 88 61 68 C65 53 81 51 91 63 C99 52 115 53 119 68 C124 88 108 108 100 132 Z"/>\n'
     '<line x1="36" y1="152" x2="152" y2="56"/>\n'
     '<polyline points="152,56 134,58 146,72"/>\n'
     '<line x1="36" y1="152" x2="54" y2="148" stroke-width="5"/>\n'
     '<line x1="36" y1="152" x2="40" y2="134" stroke-width="5"/>\n'),
    # 11. Bẫy chuột với pho mát vàng — cạm bẫy lợi dụng
    "mousetrap": (GOLD,
     '<rect x="42" y="124" width="116" height="16" rx="5"/>\n'
     '<line x1="62" y1="132" x2="140" y2="66"/>\n'
     '<circle cx="62" cy="132" r="8"/>\n'
     '<path d="M118 124 L158 124 L158 96 Z"/>\n'
     '<circle cx="146" cy="114" r="4" stroke-width="4"/>\n'
     '<circle cx="133" cy="118" r="3" stroke-width="4"/>\n'),
    # 12. Cánh cửa hé sáng trong bóng tối — hy vọng
    "door-light": (GOLD,
     '<rect x="66" y="36" width="68" height="128"/>\n'
     '<path d="M66 36 L104 52 L104 164 L66 164 Z"/>\n'
     '<circle cx="96" cy="104" r="4" fill="'+GOLD+'" stroke="none"/>\n'
     '<path d="M104 52 L152 78 L152 146 L104 164" stroke-dasharray="9 8"/>\n'),
}

for name, (color, body) in ICONS.items():
    path = os.path.join(OUT, f"{name}.svg")
    with open(path, "w") as f:
        f.write(svg(color, body))
    print("wrote", path)
print(f"total: {len(ICONS)} icons")
