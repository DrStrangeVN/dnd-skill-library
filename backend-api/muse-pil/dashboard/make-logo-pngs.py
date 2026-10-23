#!/usr/bin/env python3
"""Render the PIL bookmark logo to PNGs (Pillow — no SVG rasterizer on this box).

Geometry mirrors pil-logo.svg: 96x120 unit bookmark, 9-unit stroke, ribbon notch.
Two colorways:
  app      dark tile, orange outline bookmark, bone PIL   (PWA / apple-touch)
  favicon  transparent, solid orange bookmark, dark PIL    (browser chrome)
"""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ORANGE = (255, 90, 31, 255)
BONE = (236, 231, 219, 255)
BLACK = (20, 18, 16, 255)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def arc_points(cx, cy, r, a0, a1, n=16):
    pts = []
    for i in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * i / n)
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def centerline():
    """The bookmark's center path (as in the SVG), closed."""
    pts = []
    pts += arc_points(22.5, 22.5, 18, 180, 270)   # top-left corner
    pts.append((73.5, 4.5))                        # top edge
    pts += arc_points(73.5, 22.5, 18, 270, 360)   # top-right corner
    pts.append((91.5, 106))                        # right edge
    pts.append((48, 82))                           # ribbon cut
    pts.append((4.5, 106))                         # left edge
    pts.append(pts[0])                             # close the loop
    return pts


def silhouette():
    """Solid bookmark silhouette (centerline polygon, minus the closing dup)."""
    return centerline()[:-1]


def render(size, style):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    pad = size * 0.14
    lw = size - 2 * pad
    k = lw / 96.0
    ox, oy = pad, (size - 120 * k) / 2

    def X(p):
        return (p[0] * k + ox, p[1] * k + oy)

    font = ImageFont.truetype(FONT, max(8, int(31 * k)))
    cx, cy = size / 2, oy + 56 * k
    if style == "app":
        d.rectangle([0, 0, size, size], fill=BLACK)
        d.line([X(p) for p in centerline()], fill=ORANGE,
               width=max(2, int(9 * k)), joint="curve")
        d.text((cx, cy), "PIL", font=font, fill=BONE, anchor="mm")
    else:  # favicon: solid bookmark, dark letters
        d.polygon([X(p) for p in silhouette()], fill=ORANGE)
        d.text((cx, cy), "PIL", font=font, fill=BLACK, anchor="mm")
    return img


def main():
    jobs = [
        ("pil-icon-512.png", 512, "app"),
        ("pil-icon-192.png", 192, "app"),
        ("pil-apple-touch-180.png", 180, "app"),
        ("pil-favicon-32.png", 32, "favicon"),
        ("pil-favicon-16.png", 16, "favicon"),
    ]
    for name, size, style in jobs:
        path = os.path.join(HERE, name)
        render(size, style).save(path)
        print("wrote", path, os.path.getsize(path), "bytes")


if __name__ == "__main__":
    main()
