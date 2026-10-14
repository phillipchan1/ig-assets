from playwright.sync_api import sync_playwright
F='<link href="https://fonts.googleapis.com/css2?family=Spectral:wght@600;700&family=IBM+Plex+Sans:wght@400;600&family=IBM+Plex+Mono:wght@400;500&display=block" rel="stylesheet">'
P='#F6F4EF';L='#16191C';S='#3A4045';B='#9C7B3F';ST='#8A8C87';LW='#EEEAE1'
def wrap(inner): return f'<html><head>{F}</head><body style="margin:0"><div style="position:relative;width:1456px;height:1048px;background:{P};overflow:hidden;font-family:\'IBM Plex Sans\'">{inner}<div style="position:absolute;right:112px;top:100px;font:600 32px Spectral;letter-spacing:-0.4px;color:{L}">Made for Goodness</div></div></body></html>'
q=wrap(f'''<div style="position:absolute;left:112px;top:108px;font:500 22px 'IBM Plex Mono';letter-spacing:4px;color:{ST}">WHAT I MOSTLY DO AS A LEADER</div>
<div style="position:absolute;left:112px;top:250px;width:4px;height:300px;background:{B}"></div>
<div style="position:absolute;left:170px;top:240px;width:1120px;font:600 72px/1.16 Spectral;color:{L};letter-spacing:-0.8px">The interruptions aren’t the tax you pay on your leadership. Most of the time, they are your leadership.</div>
<div style="position:absolute;left:170px;top:680px;width:1100px;font:400 34px/1.4 'IBM Plex Sans';color:{S}">What you do most as a leader is notice. Everything you produce comes after that.</div>''')
def col(x,t,o,empty=False):
  bd=f'2px solid {B}' if empty else f'1px solid {ST}'
  out=f'<div style="font:400 30px \'IBM Plex Sans\';color:{ST}">Nothing to show for it</div>' if empty else f'<div style="font:600 30px \'IBM Plex Sans\';color:{L}">{o}</div>'
  return f'''<div style="position:absolute;left:{x}px;top:330px;width:380px;height:470px;background:{LW};border:{bd};border-radius:4px;box-sizing:border-box;padding:44px 40px">
<div style="font:500 20px 'IBM Plex Mono';letter-spacing:3px;color:{ST}">WHEN I</div>
<div style="font:600 42px/1.15 Spectral;color:{L};margin-top:14px;height:150px">{t}</div>
<div style="height:1px;background:{ST};margin:10px 0 34px"></div>
<div style="font:500 20px 'IBM Plex Mono';letter-spacing:3px;color:{ST};margin-bottom:14px">IT LEAVES</div>{out}</div>'''
d=wrap(f'''<div style="position:absolute;left:112px;top:84px;font:700 62px Spectral;color:{L};letter-spacing:-0.6px">Attention leaves no artifact</div>
<div style="position:absolute;left:112px;top:180px;font:400 32px 'IBM Plex Sans';color:{S}">The time that matters most feels wasted.</div>
{col(112,'Write a plan','A document')}{col(538,'Run a meeting','Action items')}{col(964,'Sit with someone and notice','',True)}
<div style="position:absolute;left:112px;top:870px;width:1232px;font:400 30px/1.4 'IBM Plex Sans';color:{S}">It looks like nothing because the work happened inside another person.</div>''')
with sync_playwright() as p:
  b=p.chromium.launch(executable_path='/usr/bin/google-chrome');pg=b.new_page(viewport={'width':1456,'height':1048},device_scale_factor=2)
  for n,h in (('img-1',q),('img-2',d)):
    pg.set_content(h);pg.wait_for_load_state('networkidle');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(500);pg.screenshot(path=n+'.png')
  b.close()
