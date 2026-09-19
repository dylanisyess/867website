"""Draw the 1200x630 link-preview card from the team logo and site palette."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
INDIGO, MUTED, LINE = '#393a74', '#626574', '#e9eaf0'
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
title, subtitle = 'Absolute Value 867', 'ARCADIA HIGH SCHOOL FRC TEAM 867'

def spaced(text, font, tracking):
    """Width of text drawn with per-character tracking, matching the site's heading spacing."""
    return sum(font.getlength(c) for c in text) + tracking * (len(text) - 1)

def write(x, y, text, font, tracking, fill):
    for c in text:
        draw.text((x, y), c, font=font, fill=fill)
        x += font.getlength(c) + tracking

TITLE_TRACK, SUB_TRACK, LINE_GAP = -2.7, 1.4, 30
title_w = spaced(title, title_font, TITLE_TRACK)
sub_w = spaced(subtitle, sub_font, SUB_TRACK)
gap = 54
left = (W - (logo.width + gap + max(title_w, sub_w))) / 2
card.paste(logo, (round(left), (H - logo_h) // 2), logo)

# Centre the two lines of type on the card by their inked height, not their line boxes.
_, title_top, _, title_bottom = title_font.getbbox(title)
_, sub_top, _, sub_bottom = sub_font.getbbox(subtitle)
block_h = (title_bottom - title_top) + LINE_GAP + (sub_bottom - sub_top)
block_y = (H - block_h) / 2

text_x = round(left + logo.width + gap)
write(text_x, block_y - title_top, title, title_font, TITLE_TRACK, INDIGO)
write(text_x, block_y + (title_bottom - title_top) + LINE_GAP - sub_top, subtitle, sub_font, SUB_TRACK, MUTED)

card.save(assets / 'og-image.png')
print(f'Wrote dist/assets/og-image.png ({W}x{H}, {(assets / "og-image.png").stat().st_size} bytes).')
