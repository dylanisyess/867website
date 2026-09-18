from pathlib import Path
import pymupdf, io, urllib.request, shutil
from PIL import Image

pdf=pymupdf.open(r'C:\Users\dylan\Downloads\EDD Sponsorship Packet (1).pdf')
assets=Path('dist/assets')
mapping={3877:'workshop',150:'mechanical-workshop',1943:'controls-workshop',184:'team-collaboration',185:'robot-assembly',190:'robot-testing',2025:'hands-on',2067:'cad-work',157:'dylan-lin',155:'iris-shi',156:'cyrus-chow',181:'amanda-hang',201:'tiger-hou',231:'kay-singhal',623:'team-photo',45:'logo',44:'pixel-star'}
for xref,name in mapping.items():
    pix=pymupdf.Pixmap(pdf,xref)
    smask=int(pdf.xref_get_key(xref,'SMask')[1].split()[0]) if pdf.xref_get_key(xref,'SMask')[0]=='xref' else 0
    if smask:pix=pymupdf.Pixmap(pix,pymupdf.Pixmap(pdf,smask))
    im=Image.open(io.BytesIO(pix.tobytes('png'))).convert('RGBA')
    if name in ('logo','pixel-star'):im=im.crop(im.getbbox())
    im.thumbnail((1400,1000))
    im.save(assets/f'{name}.webp',quality=85)
    if name=='logo':im.save(assets/'favicon.png')
pdf[0].get_pixmap(matrix=pymupdf.Matrix(.6,.6)).save(str(assets/'packet-cover.png'))
shutil.copyfile(r'C:\Users\dylan\Downloads\EDD Sponsorship Packet (1).pdf','dist/downloads/absolute-value-867-sponsorship.pdf')
for name,key in [('biocore','473aab_d52d9ebb5cb84728820015e7be632532~mv2.png'),('jpl-device','473aab_6a73d80bb80f4d378ed8039c8ea82cea~mv2.png'),('frc-render','473aab_0741bf2f03ff4058b73ef7ed6d77e442~mv2.png')]:
    raw=urllib.request.urlopen('https://static.wixstatic.com/media/'+key).read()
    im=Image.open(io.BytesIO(raw));im.thumbnail((1400,1000));im.save(assets/f'{name}.webp',quality=86)
    print(name,im.size)
