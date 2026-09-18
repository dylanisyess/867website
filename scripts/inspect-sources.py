from pathlib import Path
from html.parser import HTMLParser
import urllib.request, json, concurrent.futures

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.skip=0; self.text=[]; self.links=[]; self.images=[]
    def handle_starttag(self,t,a):
        d=dict(a)
        if t in ('script','style'): self.skip+=1
        if t=='a' and d.get('href'): self.links.append(d['href'])
        if t=='img': self.images.append(d)
    def handle_endtag(self,t):
        if t in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self,s):
        if not self.skip and s.strip(): self.text.append(s.strip())

base='https://dylanlin2009.wixstudio.com/867-absolute-value'
def fetch(item):
    name,path=item
    s=urllib.request.urlopen(base+path).read().decode()
    Path(f'docs/sources/wix-{name}.html').write_text(s,encoding='utf8')
    p=Parser();p.feed(s)
    Path(f'docs/sources/wix-{name}.txt').write_text('\n'.join(p.text),encoding='utf8')
    Path(f'docs/sources/wix-{name}-media.json').write_text(json.dumps(p.images,indent=2),encoding='utf8')
    return name,p
with concurrent.futures.ThreadPoolExecutor() as pool:
    for name,p in pool.map(fetch,[('home',''),('history','/home-1'),('projects','/projects'),('sponsors','/home-2')]):
        print('\nPAGE '+name+'\n'+'\n'.join(p.text).encode('ascii','replace').decode())
        print('LINKS',list(dict.fromkeys(p.links)))
