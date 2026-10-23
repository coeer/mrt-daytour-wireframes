# -*- coding: utf-8 -*-
# v45 三主题批量渲染+切片（设计干员 2026-10-23）
# 每主题：probe 实测高度 -> Chrome 2x 整图 -> 尾部裁剪 -> DOM 边界贪心切片(<=2850 CSS px)
# 切片与整图母版直落 03_交付，命名 winter_<tag>_<lang>_segN.jpg
import os, re, json, html as ihtml, subprocess, sys
from PIL import Image
import numpy as np

CHROME = r'C:/Program Files\Google\Chrome\Application\chrome.exe'
ROOT = os.path.dirname(os.path.abspath(__file__))            # 02_施工/
DELIV = os.path.normpath(os.path.join(ROOT, '..', '03_交付'))
THEMES = [('A-magazine', 'v45a'), ('B-refined', 'v45b'), ('C-swiss', 'v45c')]
SCALE = int(os.environ.get('SHOOT_SCALE', '2'))
MAXH_CSS, MAXH_DEV, MINH_CSS, QUALITY = 2850, 5700, 700, 95

PROBE = '<script>window.addEventListener("load",function(){setTimeout(function(){document.title="H="+Math.ceil(document.body.getBoundingClientRect().height)+"px"},800)})</script>'

JS = r'''<script>window.addEventListener("load",function(){setTimeout(function(){
var sels=[["section",3],[".card",2],[".hkcard",2],[".hkline",1],[".hkrow",1],[".evrow",1],[".figure",1],["figure",1],[".tl",1],[".notice",1],[".note",1],[".kick",3],[".sechead",3],[".breath",3],[".bandimg",3],[".bandwrap",3],[".trustpickup",3],[".cost-grid",1],[".cost-box",1],[".fbody",2],[".qa",1],[".fend",1],[".end",3],[".copyright",3],[".cover",3],[".cover-img",3],[".cover-title",1]];
var out=[];var bodyTop=document.body.getBoundingClientRect().top;
sels.forEach(function(sp){document.querySelectorAll(sp[0]).forEach(function(el){
var r=el.getBoundingClientRect();out.push([Math.round(r.top-bodyTop),sp[1]]);out.push([Math.round(r.bottom-bodyTop),sp[1]]);});});
document.title=JSON.stringify(out);},900)})</script>'''


def height(td, lang):
    src = os.path.join(td, f'page_{lang}.html')
    h = open(src, encoding='utf-8').read().replace('</body>', PROBE + '</body>')
    pr = os.path.join(td, f'probe_{lang}.html')
    open(pr, 'w', encoding='utf-8').write(h)
    out = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
        '--virtual-time-budget=12000', '--window-size=780,1200', '--dump-dom', 'file:///' + pr.replace('\\', '/')],
        capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=180)
    m = re.search(r'<title>H=(\d+)px</title>', out.stdout or '')
    return int(m.group(1)) if m else None


def shoot(td, lang, H):
    src = os.path.join(td, f'page_{lang}.html')
    png = os.path.join(td, f'out_{lang}.png')
    subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
        f'--force-device-scale-factor={SCALE}', '--virtual-time-budget=25000',
        f'--window-size=780,{H}', '--screenshot=' + png, 'file:///' + src.replace('\\', '/')],
        capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=300)
    return png


def trim_tail(png, bg=(240, 240, 240), tol=16, guard=400):
    im = Image.open(png).convert('RGB')
    a = np.asarray(im).astype(int)
    h = a.shape[0]
    cut = 0
    while cut < guard and cut < h - 1:
        row = a[h - 1 - cut]
        if all(abs(row.mean(axis=0)[i] - bg[i]) <= tol for i in range(3)):
            cut += 1
        else:
            break
    if cut:
        im.crop((0, 0, im.size[0], h - cut)).save(png)
    return cut


def measure(td, lang):
    src = os.path.join(td, f'page_{lang}.html')
    h = open(src, encoding='utf-8').read().replace('</body>', JS + '</body>')
    pr = os.path.join(td, f'probe_{lang}.html')
    open(pr, 'w', encoding='utf-8').write(h)
    out = subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
        '--virtual-time-budget=12000', '--window-size=780,1200', '--dump-dom', 'file:///' + pr.replace('\\', '/')],
        capture_output=True, text=True, encoding='utf-8', errors='ignore', timeout=180)
    m = re.search(r'<title>(.*?)</title>', out.stdout or '', re.S)
    data = json.loads(ihtml.unescape(m.group(1)))
    cands = {}
    for y, p in data:
        if 0 < y:
            cands[y] = max(cands.get(y, 0), p)
    return sorted(cands.items())


def partition(cands, total_css):
    ys = [y for y, _ in cands]
    pts, last = [0], 0
    while total_css - last > MAXH_CSS:
        limit = last + MAXH_CSS
        pool = [(y, p) for y, p in cands if last + MINH_CSS < y <= limit]
        if pool:
            y = max(pool, key=lambda yp: yp[0] + yp[1] * 120)[0]
            pts.append(y); last = y
            continue
        nxt = min([y for y in ys if y > last] + [total_css])
        n = int(np.ceil((nxt - last) / MAXH_CSS))
        for k in range(1, n):
            pts.append(last + (nxt - last) * k // n)
        if nxt < total_css:
            pts.append(nxt)
        last = nxt
    pts.append(total_css)
    i = 1
    while i < len(pts) - 1:
        if pts[i] - pts[i - 1] < 600:
            if pts[i + 1] - pts[i - 1] <= MAXH_CSS:
                del pts[i]; continue
            pts[i] = (pts[i - 1] + pts[i + 1]) // 2
        i += 1
    if len(pts) > 2 and pts[-1] - pts[-2] < 600:
        if pts[-1] - pts[-3] <= MAXH_CSS:
            del pts[-2]
        else:
            pts[-2] = (pts[-3] + pts[-1]) // 2
    return pts


def blankest_row(a, target, win=120):
    h = a.shape[0]
    lo, hi = max(1, target - win), min(h - 1, target + win)
    seg = a[lo:hi].astype(np.float32)
    score = seg.std(axis=(1, 2)) + np.abs(np.diff(seg, axis=0, prepend=seg[:1])).mean(axis=(1, 2))
    return lo + int(np.argmin(score))


def slice_lang(td, lang, tag):
    im = Image.open(os.path.join(td, f'out_{lang}.png')).convert('RGB')
    a = np.asarray(im)
    W, H = im.size
    assert W == 1560, f'母版宽度异常: {W}（应为 1560=2x）'
    total_css = H // 2
    cands = measure(td, lang)
    pts_css = partition(cands, total_css)
    pts = [0]
    for y in pts_css[1:-1]:
        dev = y * 2
        snapped = blankest_row(a, dev, win=400)
        if snapped - pts[-1] > MAXH_DEV or snapped - pts[-1] < MINH_CSS * 2:
            snapped = dev
            if snapped - pts[-1] > MAXH_DEV:
                snapped = pts[-1] + MAXH_DEV
        pts.append(snapped)
    pts.append(H)
    heights = []
    for i in range(len(pts) - 1):
        out = os.path.join(DELIV, f'winter_{tag}_{lang}_seg{i+1}.jpg')
        im.crop((0, pts[i], W, pts[i + 1])).save(out, 'JPEG', quality=QUALITY, subsampling=0)
        heights.append(pts[i + 1] - pts[i])
    im.save(os.path.join(DELIV, f'winter_{tag}_{lang}_full.png'))
    im.convert('RGB').save(os.path.join(DELIV, f'预览_winter_{tag}_full_{lang}.jpg'), 'JPEG', quality=80)
    over = [h for h in heights if h > MAXH_DEV]
    print(lang, 'total', H, 'n=', len(heights), 'heights', heights, 'OVER!' if over else 'ok')


if __name__ == '__main__':
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for name, tag in THEMES:
        if only and only not in name:
            continue
        td = os.path.join(ROOT, 'themes', name)
        for lang in ('zh', 'ko'):
            H = height(td, lang)
            print(name, lang, 'height', H)
            if not H:
                continue
            png = shoot(td, lang, H)
            print(name, lang, 'trim', trim_tail(png))
            slice_lang(td, lang, tag)
