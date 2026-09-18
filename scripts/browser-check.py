from pathlib import Path
import json
from playwright.sync_api import sync_playwright

base='http://127.0.0.1:8670'
routes=json.loads(Path('docs/routes.json').read_text())
Path('tmp/qa').mkdir(parents=True,exist_ok=True)
errors=[];checks=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='chrome',headless=True)
    page=browser.new_page()
    page.on('pageerror',lambda error:errors.append(str(error)))
    for width,height in [(1440,1000),(768,1024),(390,844),(320,740)]:
        page.set_viewport_size({'width':width,'height':height})
        for route in routes:
            response=page.goto(base+route)
            assert response.status==200,(route,response.status)
            page.wait_for_load_state('networkidle')
            overflow=page.evaluate('document.documentElement.scrollWidth > innerWidth')
            assert not overflow,('overflow',width,route)
            broken=page.locator('img[src]').evaluate_all('(imgs)=>imgs.filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src)')
            # Lazy images load after scrolling through the document.
            for image in page.locator('img[src]').all():
                image.scroll_into_view_if_needed()
            page.wait_for_function('Array.from(document.images).filter(i=>i.hasAttribute("src")).every(i=>i.complete&&i.naturalWidth>0)')
        checks.append(f'{len(routes)} routes: {width}px, no overflow or broken images')
        for route,name in [('/','home'),('/sponsor/','sponsor'),('/team-leads/','leads'),('/join/','join'),('/gallery/','gallery')]:
            page.goto(base+route)
            page.locator('img[src]').evaluate_all('(imgs)=>imgs.forEach(i=>i.loading="eager")')
            page.wait_for_function('Array.from(document.images).filter(i=>i.hasAttribute("src")).every(i=>i.complete&&i.naturalWidth>0)')
            page.screenshot(path=f'tmp/qa/{name}-{width}.png',full_page=True)
    page.set_viewport_size({'width':390,'height':844})
    page.goto(base)
    toggle=page.get_by_role('button',name='Menu',exact=True)
    assert not page.locator('#navigation').is_visible()
    toggle.click();assert page.locator('#navigation').is_visible()
    page.locator('summary').filter(has_text='About').click()
    page.locator('.dropdown').get_by_role('link',name='Team Leads',exact=True).click()
    assert page.url.endswith('/team-leads/')
    page.get_by_role('button',name='Menu',exact=True).click();page.keyboard.press('Escape')
    assert page.get_by_role('button',name='Menu',exact=True).get_attribute('aria-expanded')=='false'
    checks.append('Mobile menu, submenu navigation, Escape, and focus return')
    page.set_viewport_size({'width':1440,'height':1000});page.goto(base)
    page.keyboard.press('Tab');assert page.locator('.skip').evaluate('(e)=>e===document.activeElement')
    assert page.locator('.skip').evaluate('(e)=>getComputedStyle(e).outlineStyle')!='none'
    page.keyboard.press('Enter');assert page.locator('#main').evaluate('(e)=>e===document.activeElement')
    summary=page.locator('summary').filter(has_text='Projects');summary.focus();page.keyboard.press('Enter')
    assert summary.evaluate('(e)=>e.parentElement.open')
    page.keyboard.press('Escape');assert not summary.evaluate('(e)=>e.parentElement.open')
    checks.append('Keyboard skip link, visible focus, dropdown Enter/Escape')
    page.goto(base+'/gallery/')
    page.select_option('#gallery-category','Team');assert page.locator('.gallery figure:visible').count()==1
    photo=page.locator('.photo-open:visible').first;photo.click();assert page.locator('dialog').is_visible()
    page.keyboard.press('Tab');assert page.locator('dialog').evaluate('(d)=>d.contains(document.activeElement)')
    page.keyboard.press('Escape');assert not page.locator('dialog').is_visible()
    assert photo.evaluate('(e)=>e===document.activeElement')
    photo.click();page.get_by_role('button',name='Close',exact=True).click();assert not page.locator('dialog').is_visible()
    checks.append('Gallery filters; dialog opens, traps focus, closes by Escape/button, restores focus')
    page.goto(base+'/projects/frc/');page.select_option('#frc-year','2026');assert page.locator('.project-item:visible').count()==1
    page.goto(base+'/projects/jpl/');page.select_option('#jpl-category','Other');assert page.locator('.project-item:visible').count()==1
    page.select_option('#jpl-year','2025');assert page.locator('[data-filter-empty]').is_visible()
    checks.append('Project year/category filters and no-results state')
    pdf=page.request.get(base+'/downloads/absolute-value-867-sponsorship.pdf');assert pdf.status==200 and pdf.body()[:5]==b'%PDF-'
    page.goto(base+'/contact/');assert page.locator('a[href="mailto:arcadiaedd.team867@gmail.com"]').count()>0
    checks.append('Packet download returns PDF; mailto and Instagram destinations match supplied contact')
    for route in ['/','/join/','/sponsor/']:
        page.goto(base+route);page.add_style_tag(content='html{font-size:200%}')
        assert not page.evaluate('document.documentElement.scrollWidth > innerWidth'),('text resize overflow',route)
    checks.append('200% root text size: homepage, join, sponsor; no horizontal overflow')
    browser.close()
assert not errors,errors
report={'checks':checks,'pageErrors':errors,'routes':len(routes)}
Path('docs/browser-checks.json').write_text(json.dumps(report,indent=2))
print(json.dumps(report,indent=2))
