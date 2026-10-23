# -*- coding: utf-8 -*-
# ============================================================
# 主题 A · 雪国杂志风（设计干员 2026-10-23）
# 整页当冬季旅行杂志排：纸底 + 衬线大标题 + 满幅图出血 + 细线分层，无卡片堆叠
# ============================================================
from base import img, shell, strip_emoji

CSS = r'''
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:780px}
body{background:#f6f3ec;color:#202a33;
 font-family:"Noto Sans SC","Noto Sans KR","Microsoft YaHei","Malgun Gothic",sans-serif;
 -webkit-font-smoothing:antialiased;font-size:15px;line-height:1.75}
img{display:block;width:100%;height:100%;object-fit:cover}
.page{width:780px;overflow:hidden;background:#f6f3ec}
section{position:relative}
.serif{font-family:"Noto Serif SC","Noto Serif KR",serif}
.rule{height:1px;background:#d8d2c4}

/* ---------- COVER ---------- */
.cover{height:980px;background:#202a33}
.cover img{object-position:center 30%}
.cover .shade{position:absolute;inset:0;
 background:linear-gradient(180deg,rgba(20,30,40,.42) 0%,rgba(20,30,40,.06) 26%,rgba(20,30,40,.16) 48%,rgba(18,26,34,.86) 82%,#141d26 100%)}
.cover .brand{position:absolute;top:0;left:28px;background:#fff;padding:16px 24px 14px;
 box-shadow:0 6px 18px rgba(10,18,26,.22)}
.cover .brand img{height:42px;width:auto;object-fit:contain}
.cover .issue{position:absolute;top:24px;right:30px;color:#fff;font-size:11.5px;letter-spacing:.3em;
 font-family:"Cormorant Garamond",serif;font-style:italic;text-shadow:0 1px 4px rgba(10,18,26,.5)}
.cover .txt{position:absolute;left:0;right:0;bottom:70px;text-align:center;color:#fff;padding:0 50px}
.cover .eyebrow{font-size:15px;letter-spacing:.42em;color:#d9e6f2;margin-bottom:18px;
 font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:600}
.cover h1{font-family:"Noto Serif SC","Noto Serif KR",serif;font-size:47px;line-height:1.32;
 font-weight:900;letter-spacing:.015em;text-shadow:0 2px 18px rgba(8,16,24,.45)}
.cover .sub{margin-top:16px;font-size:16px;color:#d5e0ea;line-height:1.8}
.cover .chips{margin-top:26px;display:flex;justify-content:center;gap:10px;flex-wrap:wrap}
.cover .chips span{font-size:12.5px;padding:7px 15px;border:1px solid rgba(255,255,255,.5);
 color:#f2f6fa;letter-spacing:.05em;background:rgba(255,255,255,.07)}

/* ---------- 杂志分节头 ---------- */
.kick{padding:56px 48px 0;display:flex;align-items:baseline;gap:14px}
.kick .no{font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:700;font-size:30px;color:#b06a3b}
.kick .t{font-size:12px;font-weight:700;letter-spacing:.34em;color:#3e7cb1}
.kick .hr{flex:1;height:1px;background:#d8d2c4;align-self:center}
.wkick{padding:0 48px}

/* ---------- HOOK ---------- */
.hkintro{margin:30px 48px 0;font-family:"Noto Serif SC","Noto Serif KR",serif;
 font-size:18.5px;line-height:2;color:#2a3642}
.hkline{display:flex;gap:16px;padding:20px 48px 0}
.hkline .n{flex:0 0 34px;font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:700;
 font-size:22px;color:#b06a3b;padding-top:1px}
.hkline .tx{flex:1;font-size:14.5px;line-height:1.85;color:#3c4a56;border-top:1px solid #ddd6c8;padding-top:14px}
.hkline .tx b{color:#22303d}

/* ---------- COURSE ---------- */
.chead{padding:20px 48px 0}
.chead .ctagline{display:flex;align-items:baseline;gap:13px;flex-wrap:wrap}
.chead h2{font-family:"Noto Serif SC","Noto Serif KR",serif;font-size:31px;font-weight:900;line-height:1.34}
.chead .ctag{font-size:12.5px;font-weight:700;color:#fff;background:#3e7cb1;padding:4px 12px;letter-spacing:.04em;white-space:nowrap}
.chead .cs{margin-top:10px;font-size:14px;color:#6d7c8a}
.chead .sub{margin-top:6px;font-size:13.5px;color:#8b96a1}
.chead .tagline{margin:22px 0 0;text-align:center;font-size:13px;letter-spacing:.4em;font-weight:600;
 color:#a2947f;padding:10px 0;border-top:1px solid #d8d2c4;border-bottom:1px solid #d8d2c4}
figure{margin:30px 0 0;position:relative;background:#e2ddd2}
figure .cap{position:absolute;left:0;right:0;bottom:0;padding:26px 20px 13px;color:#fff;font-size:12.5px;
 letter-spacing:.05em;background:linear-gradient(180deg,rgba(15,24,32,0),rgba(15,24,32,.72))}
.evrow{display:flex;gap:20px;padding:26px 48px 0}
.evrow .time{flex:0 0 92px;font-family:"Noto Serif SC","Noto Serif KR",serif;font-weight:900;
 font-size:20px;line-height:1.3;color:#3e7cb1}
.evrow .time small{display:block;font-family:"Noto Sans SC","Noto Sans KR",sans-serif;
 font-size:10.5px;font-weight:700;letter-spacing:.22em;color:#a2947f;margin-top:4px}
.evrow .body{flex:1;border-top:1px solid #ddd6c8;padding-top:12px}
.evrow h4{font-size:16.5px;font-weight:900;line-height:1.5}
.evrow h4 .dur{font-size:12px;font-weight:600;color:#93a0ab;margin-left:8px;letter-spacing:.02em}
.evrow p{font-size:13.8px;color:#46545f;line-height:1.85;margin-top:6px}
.evrow.hl .body{border-top:2px solid #b06a3b}
.evrow .star{display:inline-block;font-size:10.5px;font-weight:800;letter-spacing:.14em;color:#fff;
 background:#b06a3b;padding:3px 10px;margin-left:8px;vertical-align:2px}
.evrow figure{margin:14px 0 2px}
.note{margin:34px 48px 0;padding:16px 20px 16px 22px;background:#efeadf;border-left:2px solid #3e7cb1;
 font-size:13px;line-height:1.85;color:#55636e}
.note b{color:#2c3944}
.note.warn{border-left-color:#b06a3b;background:#f2e9de}

/* ---------- BREATH + BAND ---------- */
.breath{text-align:center;padding:60px 48px 8px}
.breath .t{font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:600;
 font-size:19px;letter-spacing:.26em;color:#a2947f;display:flex;align-items:center;justify-content:center;gap:18px}
.breath .t:before,.breath .t:after{content:'';width:70px;height:1px;background:#d8d2c4}
.bandimg{height:400px;margin-top:34px}
.bandimg .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,26,36,.14),rgba(16,26,36,.6))}
.bandimg .txt{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
 color:#fff;text-align:center;padding:0 44px}
.bandimg .txt b{font-family:"Noto Serif SC","Noto Serif KR",serif;font-size:25px;font-weight:900;
 text-shadow:0 2px 14px rgba(0,0,0,.5)}
.bandimg .txt span{font-size:13px;color:#e4ecf3;margin-top:11px;letter-spacing:.1em;text-shadow:0 1px 8px rgba(0,0,0,.5)}

/* ---------- TRUST + PICKUP（官方整图原样） ---------- */
.trustpickup{background:#f6f3ec}
.trustpickup img{width:780px;height:auto;display:block}
.trustpickup .wrap{padding:0}
.trustpickup .note{margin:26px 48px 0}

/* ---------- COST ---------- */
.costwrap{padding:0 48px}
.cost-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:34px}
.cost-box{background:#fff;border:1px solid #e0dacb;padding:22px 22px 16px}
.cost-box h5{font-size:12px;font-weight:800;letter-spacing:.3em;margin-bottom:12px}
.cost-box.inc h5{color:#3e7cb1}.cost-box.exc h5{color:#b06a3b}
.cost-box li{font-size:13px;line-height:1.8;color:#46545f;list-style:none;
 padding-left:18px;position:relative;margin-top:7px}
.cost-box.inc li:before{content:"—";position:absolute;left:0;color:#3e7cb1;font-weight:900}
.cost-box.exc li:before{content:"—";position:absolute;left:0;color:#b06a3b;font-weight:900}

/* ---------- FAQ ---------- */
.faqzone{padding-bottom:8px}
.fhead{padding:56px 48px 6px;display:flex;gap:16px;align-items:baseline}
.fhead .ic{font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:700;font-size:30px;color:#b06a3b}
.fhead b{font-size:12px;font-weight:700;letter-spacing:.34em;color:#3e7cb1}
.fbody{margin:20px 48px 0;border-top:1px solid #d8d2c4}
.qa{padding:20px 0;border-bottom:1px solid #ddd6c8;display:flex;gap:18px}
.qa .qn{flex:0 0 44px;font-family:"Cormorant Garamond",serif;font-style:italic;font-weight:700;
 font-size:26px;color:#b06a3b;line-height:1.1}
.qa .qc{flex:1}
.qa .q{font-family:"Noto Serif SC","Noto Serif KR",serif;font-size:16.5px;font-weight:900;line-height:1.55;color:#22303d}
.qa .a{font-size:13.6px;line-height:1.9;color:#46545f;margin-top:9px}
.fend{margin:26px 48px 0;text-align:center;font-size:13.5px;color:#7c6a4f;line-height:1.8;
 padding:16px 20px;border:1px solid #e0dacb;background:#fff}

/* ---------- END ---------- */
.end{height:470px;margin-top:60px;background:#141d26}
.end .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(16,24,32,.3),rgba(16,24,32,.42) 45%,rgba(12,19,26,.88))}
.end .txt{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
 color:#fff;text-align:center;padding:0 48px}
.end .eyebrow{font-family:"Cormorant Garamond",serif;font-style:italic;font-size:16px;letter-spacing:.36em;color:#d9c9a8}
.end h3{font-family:"Noto Serif SC","Noto Serif KR",serif;font-size:27px;font-weight:900;margin-top:16px;line-height:1.55}
.end p{font-size:13.5px;color:#c8d4de;margin-top:13px;line-height:1.8}
.end .line{width:56px;height:1px;background:#d9c9a8;margin:20px auto 0}
.copyright{background:#f6f3ec;color:#9aa294;text-align:center;font-size:11.5px;padding:22px 30px;line-height:1.8}
'''


def build(lang, C, CS):
    P = []
    A = P.append
    cv = C['cover']

    # COVER
    A('<section class="cover"><img src="../../assets/cover.jpg" alt=""><div class="shade"></div>')
    A('<div class="brand"><img src="../../assets/logo.png" alt="%s"></div>' % cv['brand_alt'])
    A('<div class="issue">WINTER COURSE · No.01</div>')
    A('<div class="txt"><div class="eyebrow">%s</div>' % cv['eyebrow'])
    A('<h1>%s</h1><div class="sub">%s</div>' % (cv['h1'], cv['sub']))
    A('<div class="chips">%s</div>' % ''.join('<span>%s</span>' % strip_emoji(x) for x in cv['chips']))
    A('</div></section>')

    # HOOK
    H = C['hook']
    A('<section class="hook"><div class="kick"><span class="no">i</span><span class="t">%s</span><span class="hr"></span></div>'
      % ('为什么是这条路线' if lang == 'zh' else '왜 이 코스인가'))
    A('<div class="hkintro">%s</div>' % H['intro'])
    for i, (ic, tx) in enumerate(H['lines'], 1):
        A('<div class="hkline"><div class="n">%d</div><div class="tx">%s</div></div>' % (i, tx))
    A('</section>')

    # COURSE
    for c in CS:
        A('<section class="coursewrap">')
        A('<div class="kick"><span class="no">ii</span><span class="t">%s</span><span class="hr"></span></div>'
          % ('今日行程' if lang == 'zh' else '오늘의 일정'))
        A('<div class="chead"><div class="ctagline"><h2>%s</h2><span class="ctag">%s</span></div>'
          '<div class="cs">%s</div><div class="sub">%s</div></div>' % (c['title'], c['tag'], c['hero'][1], c['sub']))
        A('<div class="tagline">%s</div>' % c['tagline'])
        A(img(c['hero'][0]))
        for e in c['ev']:
            hl = ' hl' if e.get('hl') else ''
            star = '<span class="star">%s</span>' % ('高光时刻' if lang == 'zh' else '하이라이트') if e.get('hl') else ''
            dur = '<span class="dur">%s</span>' % e['d'] if e.get('d') else ''
            tm = e['t'].replace(' → ', '<br>')
            A('<div class="evrow%s"><div class="time">%s<small>%s</small></div><div class="body">' % (hl, tm, c['pilltxt']))
            A('<h4>%s%s%s</h4><p>%s</p>' % (e['ti'], dur, star, e['b']))
            if e.get('img'):
                A(img(e['img'][0]))
            A('</div></div>')
        A('<div class="note">%s</div>' % c['note'])
        if c.get('warn'):
            A('<div class="note warn">%s</div>' % strip_emoji(c['warn']))
        A('</section>')

    # BREATH + BAND
    A('<section class="breath"><div class="t">SNOW COVERS EVERYTHING BUT WARMTH.</div></section>')
    if lang == 'zh':
        bt, bs = '冬天的北海道，值得一整天', '企鹅散步 · 雪原孤树 · 冰蓝瀑布 · 森林灯火 —— 一条线走完'
    else:
        bt, bs = '겨울 홋카이도는 온종일 걸릴 가치가 있습니다', '펭귄 산책 · 설원의 나무 · 얼음 폭포 · 숲속 불빛 — 한 코스로'
    A('<section class="bandimg"><img src="../../assets/band.jpg"><div class="shade"></div>'
      '<div class="txt"><b>%s</b><span>%s</span></div></section>' % (bt, bs))

    # TRUST + PICKUP（官方整图原样嵌入）
    A('<section class="trustpickup"><img src="../../assets/trust_full.jpg" alt="">'
      '<img src="../../assets/pickup_full.jpg" alt="">'
      '<div class="note">%s</div>' % C['pickup_note'])
    A('<div class="note">%s</div><div class="note">%s</div></section>' % (C['drv'], C['veh']))

    # COST
    CO = C['cost']
    A('<section class="costwrap"><div class="cost-grid">')
    A('<div class="cost-box inc"><h5>%s</h5><ul>%s</ul></div>' % (CO['inc_h'], ''.join('<li>%s</li>' % x for x in CO['inc'])))
    A('<div class="cost-box exc"><h5>%s</h5><ul>%s</ul></div>' % (CO['exc_h'], ''.join('<li>%s</li>' % x for x in CO['exc'])))
    A('</div></section>')

    # FAQ
    F = C['faq']
    A('<section class="faqzone"><div class="fhead"><span class="ic">Q&amp;A</span><b>%s</b></div>' % F['s'])
    A('<div class="fbody">')
    for i, (q, a) in enumerate(F['items'], 1):
        A('<div class="qa"><div class="qn">%02d</div><div class="qc"><div class="q">%s</div><div class="a">%s</div></div></div>' % (i, q, a))
    A('<div class="fend">%s</div></div></section>' % F['end'])

    # END
    E = C['end']
    A('<section class="end"><img src="../../assets/closing.jpg"><div class="shade"></div><div class="txt">')
    A('<div class="eyebrow">%s</div><h3>%s</h3><div class="line"></div><p>%s</p>' % (E['eyebrow'], E['h3'], E['p']))
    A('</div></section>')
    A('<div class="copyright">%s</div>' % C['copyright'])

    title = '札幌出发富良野美瑛冬季小团1日游 · v45-A 雪国杂志' if lang == 'zh' else '삿포로 출발 비에이·후라노 겨울 소그룹 1일 투어 · v45-A 매거진'
    return shell(lang, CSS, '\n'.join(P), title)
