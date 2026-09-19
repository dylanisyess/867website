import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import vm from 'node:vm';
const root=path.resolve('dist');
const routes=JSON.parse(fs.readFileSync('docs/routes.json','utf8'));
const origin=JSON.parse(fs.readFileSync('content/team.json','utf8')).url.replace(/[/]+$/,'');
const ogImage=`${origin}/assets/og-image.png`;
let references=0;
for(const route of routes){
 const file=route==='/'?'dist/index.html':route==='/404.html'?'dist/404.html':`dist${route}index.html`;
 const html=fs.readFileSync(file,'utf8');
 assert.equal((html.match(/<h1[ >]/g)||[]).length,1,`${route}: exactly one h1`);
 assert.match(html,/<title>[^<]+<\/title>/);
 assert.match(html,/<html lang="en">/);
 assert(!/Tiger Ho(?:[<\s]|&)|around 15|Barcelona|Paris|Milan|2029|2030|insert pictures|Project Name 0|BUY TICKETS|connect with other FRC teams to \./.test(html),`${route}: unfinished or template content`);
 for(const match of html.matchAll(/(?:href|src)="([^"#]*)/g)){
  const url=match[1];if(!url.startsWith('/'))continue;
  const clean=url.split(/[?#]/)[0];let target=path.join(root,clean);if(clean.endsWith('/'))target=path.join(target,'index.html');
  assert(fs.existsSync(target),`${route}: missing ${url}`);references++;
 }
 assert(html.includes(`<meta property="og:image" content="${ogImage}">`),`${route}: link preview image`);
 assert(html.includes(`<meta property="og:title" content="`)&&html.includes(`<meta name="twitter:card" content="summary_large_image">`),`${route}: link preview title and card type`);
 if(route!=='/404.html')assert(html.includes(`<link rel="canonical" href="${origin}${route}">`),`${route}: canonical URL`);
 for(const match of html.matchAll(/<img\b[^>]*>/g))assert.match(match[0],/alt="[^"]*"/,`${route}: image missing alt`);
}
new vm.Script(fs.readFileSync('dist/assets/site.js','utf8'));
const tiers=JSON.parse(fs.readFileSync('content/sponsors.json','utf8')).tiers;
assert.deepEqual(tiers.map(t=>[t.name,t.inherits,t.benefits.length]),[['Wood',null,5],['Brick','Wood',4],['Steel','Brick',4],['Carbon Fiber','Steel',6]]);
assert(fs.readFileSync('dist/downloads/absolute-value-867-sponsorship.pdf').subarray(0,5).equals(Buffer.from('%PDF-')));
const preview=fs.readFileSync('dist/assets/og-image.png');
assert(preview.subarray(0,8).equals(Buffer.from('89504e470d0a1a0a','hex')),'preview image is a PNG');
assert.deepEqual([preview.readUInt32BE(16),preview.readUInt32BE(20)],[1200,630],'preview image is 1200x630');
console.log(`PASS: ${routes.length} pages, ${references} local references, metadata, link previews, alternative text, copy safeguards, tier inheritance, JavaScript syntax, and PDF signature.`);
