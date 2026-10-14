from playwright.sync_api import sync_playwright
V={'a':dict(bg='#F6F1E8',ink='#141311',mut='#5C574F',acc='#B8844F',line='#E2D9C8'),
   'b':dict(bg='#1B1916',ink='#F6F1E8',mut='#B9B0A2',acc='#C9A06A',line='#3A352E')}
import sys
T,S,SLUG=sys.argv[1],sys.argv[2],sys.argv[3]
LBL=sys.argv[4] if len(sys.argv)>4 else 'NEW ESSAY'
ST=sys.argv[6] if len(sys.argv)>6 else '860'
TS=sys.argv[5] if len(sys.argv)>5 else '124px/1.04'
def html(c,mock):
  m=f'<div style="position:absolute;left:290px;top:1250px;width:500px;height:120px;border-radius:24px;background:#9a9a9a;color:#fff;font:600 38px Inter;display:flex;align-items:center;justify-content:center">Read on Substack</div>' if mock else ''
  return f'''<html><body style="margin:0"><div style="position:relative;width:1080px;height:1920px;background:{c['bg']};overflow:hidden">
<div style="position:absolute;right:120px;top:0;width:2px;height:470px;background:{c['acc']}"></div>
<div style="position:absolute;right:107px;top:462px;width:28px;height:52px;background:{c['acc']};clip-path:polygon(50% 0,100% 45%,50% 100%,0 45%)"></div>
<div style="position:absolute;left:110px;top:300px;font:500 26px 'IBM Plex Mono';letter-spacing:4px;color:{c['acc']}">{LBL}</div>
<div style="position:absolute;left:104px;top:420px;width:780px;font:600 {TS} 'EB Garamond';color:{c['ink']};letter-spacing:-1px">{T}</div>

<div style="position:absolute;left:110px;top:{ST}px;width:800px;font:400 50px/1.3 'EB Garamond';color:{c['mut']};">{S}</div>
<div style="position:absolute;left:110px;right:110px;top:1500px;height:1px;background:{c['line']}"></div>
<div style="position:absolute;left:0;width:1080px;top:1522px;text-align:center;font:400 26px 'IBM Plex Mono';letter-spacing:1px;color:{c['mut']}">@thisisphilchan</div>
{m}</div></body></html>'''
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1920})
  for k,c in V.items():
    for mock in (0,1):
      pg.set_content(html(c,mock)); pg.wait_for_timeout(400)
      pg.screenshot(path=f'{SLUG}-{k}{"-mock" if mock else ""}.png')
  b.close()
