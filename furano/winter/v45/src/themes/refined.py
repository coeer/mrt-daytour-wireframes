# -*- coding: utf-8 -*-
# ============================================================
# 主题 B · 深化现有骨架（设计干员 2026-10-23）
# 保留 K3 时代藏青+金字骨架与信息结构，只做版式精修：
# 统一圆角/间距/字阶、收敛阴影、时间轴细化、新增 C14/C15 段
# ============================================================
import os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 02_施工/
sys.path.insert(0, ROOT)
from css import CSS as CSS_ORIG
from base import img, shell

# 精修覆盖层（后写优先）
CSS = CSS_ORIG + r'''
/* ---- v45-B 精修覆盖 ---- */
.card{border-radius:18px;box-shadow:0 3px 10px rgba(20,40,60,.05),0 10px 26px rgba(20,40,60,.05)}
.hkcard{border-radius:18px;box-shadow:0 3px 10px rgba(20,40,60,.05),0 10px 26px rgba(20,40,60,.05)}
figure{border-radius:12px}
.tl:before{left:71px;border-left:1.6px solid #d5dfe9}
.ev .dot{width:13px;height:13px;left:65.5px;border-width:3px}
.ev .pill{width:60px;border-radius:7px}
.cost-box{border-radius:14px;border-color:#e6edf5;box-shadow:0 2px 8px rgba(20,40,60,.04)}
.qa .q .n{background:#3a6ea5;border-radius:8px}
.fbody{border-radius:18px}
.chead .badge{border-radius:11px}
.cover h1{font-size:43px;letter-spacing:.015em}
.cover .sub{font-size:16px}
.notice{border-radius:12px}
.drvveh{padding:0 38px}
.drvveh .notice{margin:0 0 12px}
'''


def build(lang, C, CS):
    P = []
    A = P.append
    cv = C['cover']

    # COVER
    A('<section class="cover"><img src="../../assets/cover.jpg" alt=""><div class="shade"></div>')
    A('<div class="brand"><img src="../../assets/logo.png" alt="%s"></div>' % cv['brand_alt'])
    A('<div class="tag">%s</div>' % cv['tag'])
    A('<div class="txt"><div class="eyebrow">%s</div>' % cv['eyebrow'])
    A('<h1>%s</h1><div class="sub">%s</div>' % (cv['h1'], cv['sub']))
    A('<div class="chips">%s</div>' % ''.join('<span>%s</span>' % x for x in cv['chips']))
    A('</div></section>')

    # HOOK
    H = C['hook']
    A('<section class="hook"><div class="hkcard">')
    A('<div class="hkintro">%s</div>' % H['intro'])
    for ic, tx in H['lines']:
        A('<div class="hkline"><div class="hkic">%s</div><div class="hktx">%s</div></div>' % (ic, tx))
    A('</div></section>')

    # COURSE
    for c in CS:
        A('<section class="coursewrap"><div class="card %s">' % c['cls'])
        A('<div class="chead"><div class="badge">%s</div><div><h2>%s</h2><div class="ctag">%s</div><div class="cs">%s</div></div></div>' % (c['lb'], c['title'], c['tag'], c['sub']))
        A('<div class="tagline">%s</div>' % c['tagline'])
        A(img(c['hero'][0]))
        A('<div class="tl">')
        for e in c['ev']:
            cls = 'ev' + (' hl' if e.get('hl') else '')
            star = '<span class="star">⭐ %s</span>' % c.get('hltxt', '') if e.get('hl') else ''
            dur = '<span class="dur">%s</span>' % e['d'] if e.get('d') else ''
            A('<div class="%s"><div class="pill">%s<br>%s</div><div class="dot"></div>' % (cls, c['pilltxt'], e['t']))
            A('<h4>%s%s%s</h4><p>%s</p>' % (e['ti'], dur, star, e['b']))
            if e.get('img'):
                A(img(e['img'][0]))
            A('</div>')
        A('</div>')
        A('<div class="notice">%s</div>' % c['note'])
        if c.get('warn'):
            A('<div class="notice warn" style="margin-top:-12px">%s</div>' % c['warn'])
        A('</div></section>')

    # BREATH + BAND
    A('<section class="breath"><div class="t">SNOW COVERS EVERYTHING BUT WARMTH.</div></section>')
    if lang == 'zh':
        bt, bs = '冬天的北海道，值得一整天', '企鹅散步 · 雪原孤树 · 冰蓝瀑布 · 森林灯火 —— 一条线走完'
    else:
        bt, bs = '겨울 홋카이도는 온종일 걸릴 가치가 있습니다', '펭귄 산책 · 설원의 나무 · 얼음 폭포 · 숲속 불빛 — 한 코스로'
    A('<section class="bandimg"><img src="../../assets/band.jpg"><div class="shade"></div>'
      '<div class="txt"><b>%s</b><span>%s</span></div></section>' % (bt, bs))

    # TRUST + PICKUP（官方整图原样嵌入）
    A('<section class="trustpickup"><img src="../../assets/trust_full.jpg" style="display:block;width:780px;height:auto">'
      '<div style="padding:18px 38px 4px"><div class="notice" style="margin:0">%s</div></div>'
      '<img src="../../assets/pickup_full.jpg" style="display:block;width:780px;height:auto"></section>' % C['pickup_note'])

    # C14/C15 司机与车辆（v3 新增）
    A('<section class="drvveh"><div class="notice">%s</div><div class="notice">%s</div></section>' % (C['drv'], C['veh']))

    # COST
    CO = C['cost']
    A('<section class="coursewrap" style="padding-top:0"><div class="cost-grid">')
    A('<div class="cost-box inc"><h5>%s</h5><ul>%s</ul></div>' % (CO['inc_h'], ''.join('<li>%s</li>' % x for x in CO['inc'])))
    A('<div class="cost-box exc"><h5>%s</h5><ul>%s</ul></div>' % (CO['exc_h'], ''.join('<li>%s</li>' % x for x in CO['exc'])))
    A('</div></section>')

    # FAQ
    F = C['faq']
    A('<section class="faqzone"><div class="fhead"><div class="ic">💬</div><div><b>%s</b><span>%s</span></div></div>' % (F['b'], F['s']))
    A('<div class="fbody">')
    for i, (q, a) in enumerate(F['items'], 1):
        A('<div class="qa"><div class="q"><div class="n">Q%d</div><b>%s</b></div><div class="a">%s</div></div>' % (i, q, a))
    A('<div class="fend">%s</div>' % F['end'])
    A('</div></section>')

    # END
    E = C['end']
    A('<section class="end"><img src="../../assets/closing.jpg"><div class="shade"></div><div class="txt">')
    A('<div class="eyebrow">%s</div><h3>%s</h3><div class="line"></div><p>%s</p>' % (E['eyebrow'], E['h3'], E['p']))
    A('</div></section>')
    A('<div class="copyright">%s</div>' % C['copyright'])

    title = '札幌出发富良野美瑛冬季小团1日游 · v45-B 藏青精修' if lang == 'zh' else '삿포로 출발 비에이·후라노 겨울 소그룹 1일 투어 · v45-B 리파인드'
    return shell(lang, CSS, '\n'.join(P), title)
