"""Draw the 1200x630 link-preview card from the team logo and site palette."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
INDIGO, MUTED, PEACH, LINE = '#393a74', '#626574', '#ffa68e', '#e9eaf0'
assets = Path('dist/assets')

card = Image.new('RGB', (W, H), 'white')
draw = ImageDraw.Draw(card)
# The same 32px grid the hero and page banners use.
for x in range(0, W, 32): draw.line([(x, 0), (x, H)], fill=LINE)
for y in range(0, H, 32): draw.line([(0, y), (W, y)], fill=LINE)

logo = Image.open(assets / 'logo.webp').convert('RGBA')
logo = logo.crop(logo.getbbox())
logo_h = 300
logo = logo.resize((round(logo.width * logo_h / logo.height), logo_h), Image.LANCZOS)

title_font = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 78)
sub_font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 27)
title, subtitle = 'Absolute Value 867', 'ARCADIA HIGH SCHOOL · FRC TEAM 867'

def spaced(text, font, tracking):
    """Width of text drawn with per-character tracking, matching the site's heading spacing."""
    return sum(font.getlength(c) for c in text) + tracking * (len(text) - 1)

def write(x, y, text, font, tracking, fill):
    for c in text:
        draw.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + tracking

title_w = spaced(title, title_font, -2.7)
sub_w = spaced(subtitle, sub_font, 1.4)
gap = 54
text_w = max(title_w, sub_w)
left = (W - (logo.width + gap + text_w)) / 2
card.paste(logo, (round(left), (H - logo_h) // 2), logo)

text_x = round(left + logo.width + gap)
draw.rectangle([text_x, 243, text_x + 80, 249], fill=PEACH)
write(text_x, 281, title, title_font, -2.7, INDIGO)
write(text_x, 385, subtitle, sub_font, 1.4, MUTED)

card.save(assets / 'og-image.png')
print(f'Wrote dist/assets/og-image.png ({W}x{H}, {(assets / "og-image.png").stat().st_size} bytes).')
