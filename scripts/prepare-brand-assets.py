"""Extract original decorative artwork and self-host the requested accent font."""
from pathlib import Path
import io, json, re, urllib.request, urllib.parse
import pymupdf
from PIL import Image

assets = Path('dist/assets')
pdf = pymupdf.open('dist/downloads/absolute-value-867-sponsorship.pdf')
icons = {
    'pixel-star-yellow': (46, 1),
    'pixel-star-purple': (50, 1),
    'pixel-wrench': (151, 5),
    'pixel-bolt': (1946, 5),
    'pixel-flowers': (2056, 7),
    'pixel-gear': (4023, 9),
    'pixel-trophy': (2380, 10),
    'pixel-people': (540, 15),
    'pixel-handshake': (3078, 15),
    'pixel-chain': (3231, 16),
    'pixel-envelope': (620, 17),
}
for name, (xref, page) in icons.items():
    pix = pymupdf.Pixmap(pdf, xref)
    mask = pdf.xref_get_key(xref, 'SMask')
    if mask[0] == 'xref':
        pix = pymupdf.Pixmap(pix, pymupdf.Pixmap(pdf, int(mask[1].split()[0])))
    image = Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGBA')
    image = image.crop(image.getbbox())
    image.thumbnail((360, 360), Image.Resampling.NEAREST)
    image.save(assets / f'{name}.webp', lossless=True)

# This narrow cover region contains only the original stacked pixel 867 artwork.
pdf[0].get_pixmap(matrix=pymupdf.Matrix(1.5,1.5), clip=pymupdf.Rect(37,42,186,746), alpha=False).save(str(assets/'pixel-867.png'))

fonts = assets / 'fonts'
fonts.mkdir(exist_ok=True)
characters = ''.join(chr(n) for n in range(32,127)) + '\u2013\u2014\u00b7\u2192'
url = 'https://fonts.googleapis.com/css2?family=DotGothic16&display=swap&text=' + urllib.parse.quote(characters)
css = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})).read().decode()
font_url = re.search(r'url\((https://[^)]+)\)', css).group(1)
data = urllib.request.urlopen(font_url).read()
extension = 'woff2' if data[:4] == b'wOF2' else 'woff' if data[:4] == b'wOFF' else 'ttf'
(fonts/f'dotgothic16-latin.{extension}').write_bytes(data)
license_url = 'https://raw.githubusercontent.com/google/fonts/main/ofl/dotgothic16/OFL.txt'
(fonts/'DotGothic16-OFL.txt').write_bytes(urllib.request.urlopen(license_url).read())
Path('docs/brand-assets.json').write_text(json.dumps({
    'icons': {name: {'pdfImageId': xref, 'packetPage': page} for name,(xref,page) in icons.items()},
    'pixel867': {'packetPage':1,'clip':[37,42,186,746]},
    'font': {'family':'DotGothic16','source':url,'license':license_url,'file':f'dotgothic16-latin.{extension}'}
},indent=2))
print(f'Extracted {len(icons)} original packet icons and cover artwork. Font: {extension}, {len(data)} bytes.')
