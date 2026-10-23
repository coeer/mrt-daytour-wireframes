# -*- coding: utf-8 -*-
# ============================================================
# 主题 C · 瑞士网格风（设计干员 2026-10-23）
# 白底黑字 + 国际克莱因蓝单点强调 + 网格点阵，全部直角细线，数据优先
# ============================================================
from base import img, shell, strip_emoji

CSS = r'''
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:780px}
body{background:#ffffff;color:#10151a;
 font-family:"Noto Sans SC","Noto Sans KR","Microsoft YaHei","Malgun Gothic",sans-serif;
 -webkit-font-smoothing:antialiased;font-size:15px;line-height:1.7}
img{display:block;width:100%;height:100%;object-fit:cover}
.page{width:780px;overflow:hidden;background:#fff}
section{position:relative}
.micro{font-size:11px;font-weight:700;letter-spacing:.3em}

/* ---------- COVER ---------- */
.cover-top{background:#fff;padding:26px 36px 0}
.cover-top .row{display:flex;justify-content:space-between;align-items:baseline;
 border-bottom:2px solid #10151a;padding-bottom:10px}
.cover-top .row .l{color:#10151a}
.cover-top .row .r{color:#002FA7}
.cover-title{padding:34px 36px 0}
.cover-title h1{font-size:52px;line-height:1.22;font-weight:900;letter-spacing:-.01em}
.cover-title h1 em{font-style:normal;color:#002FA7}
.cover-title .sub{margin-top:16px;font-size:14.5px;color:#3d4750;line-height:1.8;max-width:560px}
.cover-title .chips{margin-top:22px;display:flex;gap:8px;flex-wrap:wrap}
.cover-title .chips span{font-size:12px;font-weight:700;padding:6px 12px;border:1px solid #10151a;letter-spacing:.04em}
.cover-title .chips span:first-child{background:#002FA7;color:#fff;border-color:#002FA7}
.cover-img{height:430px;margin-top:30px;position:relative;background:#10151a}
.cover-img .bar{position:absolute;left:0;bottom:0;right:0;height:6px;background:#002FA7}

/* ---------- 节头 ---------- */
.sechead{padding:52px 36px 0;display:flex;align-items:center;gap:14px}
.sechead .micro{color:#002FA7}
.sechead .idx{font-size:26px;font-weight:900;line-height:1}
.sechead .ln{flex:1;height:1px;background:#10151a}
.sechead .dots{width:74px;height:12px;
 background-image:radial-gradient(#c4ccd4 1.1px,transparent 1.1px);background-size:9px 9px}

/* ---------- HOOK ---------- */
.hkintro{margin:26px 36px 0;font-size:17px;line-height:1.9;font-weight:700;color:#10151a;max-width:640px}
.hkrow{display:flex;gap:18px;margin:0 36px;padding:18px 0 0}
.hkrow .n{flex:0 0 40px;font-size:15px;font-weight:900;color:#002FA7;padding-top:2px}
.hkrow .tx{flex:1;border-top:1px solid #10151a;padding-top:12px;font-size:14px;line-height:1.8;color:#3d4750}
.hkrow .tx b{color:#10151a}

/* ---------- COURSE ---------- */
.chead{padding:18px 36px 0}
.chead .ctagline{display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.chead h2{font-size:29px;font-weight:900;line-height:1.3;letter-spacing:-.005em}
.chead .ctag{font-size:11.5px;font-weight:700;letter-spacing:.08em;color:#fff;background:#002FA7;padding:4px 11px}
.chead .cs{margin-top:8px;font-size:13px;color:#5a6570}
.chead .sub{margin-top:4px;font-size:12.5px;color:#8b95a0}
.chead .tagline{margin:18px 0 0;font-size:11px;letter-spacing:.4em;font-weight:700;color:#002FA7;
 padding:9px 0;border-top:1px solid #10151a;border-bottom:1px solid #10151a;text-align:center}
figure{margin:28px 0 0;position:relative;background:#e8ebee}
figure .cap{position:absolute;left:0;bottom:0;right:0;padding:24px 18px 11px;color:#fff;font-size:12px;
 font-weight:700;letter-spacing:.06em;background:linear-gradient(180deg,rgba(10,14,18,0),rgba(10,14,18,.78))}
.evrow{display:flex;gap:18px;margin:0 36px;padding:20px 0 0}
.evrow .time{flex:0 0 96px;font-size:16px;font-weight:900;line-height:1.25;color:#10151a}
.evrow .time small{display:block;font-size:10px;font-weight:700;letter-spacing:.24em;color:#002FA7;margin-top:5px}
.evrow .body{flex:1;border-top:1px solid #10151a;padding-top:11px}
.evrow h4{font-size:16px;font-weight:900;line-height:1.5}
.evrow h4 .dur{font-size:11.5px;font-weight:700;letter-spacing:.06em;color:#8b95a0;margin-left:8px}
.evrow p{font-size:13.5px;color:#3d4750;line-height:1.8;margin-top:5px}
.evrow.hl{border-left:4px solid #002FA7;padding-left:14px;margin-left:36px;margin-right:36px}
.evrow.hl .body{border-top:2px solid #002FA7}
.evrow .star{display:inline-block;font-size:10px;font-weight:900;letter-spacing:.16em;color:#fff;
 background:#002FA7;padding:3px 9px;margin-left:8px;vertical-align:2px}
.evrow figure{margin:12px 0 2px}
.note{margin:30px 36px 0;border:1px solid #10151a;border-left:4px solid #002FA7;
 padding:14px 18px;font-size:12.8px;line-height:1.8;color:#3d4750}
.note b{color:#10151a}
.note.warn{border-left-color:#10151a;background:#f4f6f8}

/* ---------- BREATH + BAND ---------- */
.breath{padding:48px 36px 4px;display:flex;align-items:center;gap:16px}
.breath .ln{flex:1;height:1px;background:#10151a}
.breath .t{font-size:12px;font-weight:700;letter-spacing:.34em;color:#002FA7;white-space:nowrap}
.bandwrap{margin-top:30px}
.bandwrap .ph{height:330px;position:relative}
.bandwrap .blue{background:#002FA7;color:#fff;padding:22px 36px;display:flex;flex-direction:column;gap:6px}
.bandwrap .blue b{font-size:21px;font-weight:900}
.bandwrap .blue span{font-size:12.5px;letter-spacing:.08em;color:#cfdcf7}

/* ---------- TRUST + PICKUP（官方整图原样） ---------- */
.trustpickup img{width:780px;height:auto;display:block}
.trustpickup .note{margin:26px 36px 0}

/* ---------- COST ---------- */
.costwrap{padding:0 36px}
.cost-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:32px;border:1px solid #10151a}
.cost-box{padding:20px 22px 14px}
.cost-box.inc{border-right:1px solid #10151a}
.cost-box h5{font-size:11px;font-weight:900;letter-spacing:.3em;margin-bottom:11px}
.cost-box.inc h5{color:#002FA7}.cost-box.exc h5{color:#10151a}
.cost-box li{font-size:12.8px;line-height:1.75;color:#3d4750;list-style:none;
 padding-left:18px;position:relative;margin-top:6px}
.cost-box.inc li:before{content:"+";position:absolute;left:0;color:#002FA7;font-weight:900}
.cost-box.exc li:before{content:"−";position:absolute;left:0;color:#10151a;font-weight:900}

/* ---------- FAQ ---------- */
.faqzone{padding-bottom:4px}
.fbody{margin:18px 36px 0;border-top:2px solid #10151a}
.qa{display:flex;gap:18px;padding:18px 0;border-bottom:1px solid #d7dce2}
.qa .qn{flex:0 0 56px;font-size:30px;font-weight:900;color:#002FA7;line-height:1}
.qa .qc{flex:1}
.qa .q{font-size:15.5px;font-weight:900;line-height:1.5}
.qa .a{font-size:13.2px;line-height:1.85;color:#3d4750;margin-top:8px}
.fend{margin:24px 36px 0;border:1px solid #10151a;padding:14px 18px;text-align:center;
 font-size:13px;font-weight:700;color:#10151a}

/* ---------- END ---------- */
.end{height:460px;margin-top:56px;background:#10151a}
.end .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,16,22,.24),rgba(12,16,22,.5) 50%,rgba(12,16,22,.9))}
.end .txt{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
 color:#fff;text-align:center;padding:0 44px}
.end .eyebrow{font-size:11px;font-weight:700;letter-spacing:.4em;color:#7ea0f5}
.end h3{font-size:26px;font-weight:900;margin-top:15px;line-height:1.5}
.end p{font-size:13.5px;color:#c9d2dc;margin-top:12px;line-height:1.75}
.end .line{width:64px;height:3px;background:#002FA7;margin:20px auto 0}
.copyright{background:#10151a;color:#8b95a0;text-align:center;font-size:11.5px;padding:18px 24px;line-height:1.75}
'''


def build(lang, C, CS):
    P = []
    A = P.append
    cv = C['cover']

    # COVER
    A('<section class="cover"><div class="cover-top"><div class="row">'
      '<span class="micro l">PGS WINTER COURSE A</span><span class="micro r">SAPPORO → BIEI → FURANO</span>'
      '</div></div>')
    h1 = cv['h1'].replace('<br>', '<br>')
    # 标题关键词强调：末行包蓝
    parts = h1.split('<br>')
    parts[-1] = '<em>%s</em>' % parts[-1]
    A('<div class="cover-title"><h1>%s</h1><div class="sub">%s</div>' % ('<br>'.join(parts), cv['sub']))
    A('<div class="chips">%s</div></div>' % ''.join('<span>%s</span>' % strip_emoji(x) for x in cv['chips']))
    A('<div class="cover-img"><img src="../../assets/cover.jpg"><div class="bar"></div></div></section>')

    # HOOK
    H = C['hook']
    A('<section class="hook"><div class="sechead"><span class="micro">%s</span><span class="idx">01</span><span class="ln"></span><span class="dots"></span></div>'
      % ('WHY THIS COURSE' if lang == 'ko' else '为什么是这条路线'))
    A('<div class="hkintro">%s</div>' % H['intro'])
    for i, (ic, tx) in enumerate(H['lines'], 1):
        A('<div class="hkrow"><div class="n">%02d</div><div class="tx">%s</div></div>' % (i, tx))
    A('</section>')

    # COURSE
    for c in CS:
        A('<section class="coursewrap">')
        A('<div class="sechead"><span class="micro">%s</span><span class="idx">02</span><span class="ln"></span><span class="dots"></span></div>'
          % ('TODAY SCHEDULE' if lang == 'ko' else '今日行程'))
        A('<div class="chead"><div class="ctagline"><h2>%s</h2><span class="ctag">%s</span></div>'
          '<div class="cs">%s</div><div class="sub">%s</div></div>' % (c['title'], c['tag'], c['hero'][1], c['sub']))
        A('<div class="tagline">%s</div>' % c['tagline'])
        A(img(c['hero'][0]))
        for e in c['ev']:
            hl = ' hl' if e.get('hl') else ''
            star = '<span class="star">%s</span>' % 'HIGHLIGHT' if e.get('hl') else ''
            dur = '<span class="dur">%s</span>' % e['d'] if e.get('d') else ''
            tm = e['t'].replace(' → ', ' →<br>')
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
    A('<section class="breath"><span class="ln"></span><span class="t">SNOW COVERS EVERYTHING BUT WARMTH.</span><span class="ln"></span></section>')
    if lang == 'zh':
        bt, bs = '冬天的北海道，值得一整天', '企鹅散步 · 雪原孤树 · 冰蓝瀑布 · 森林灯火 —— 一条线走完'
    else:
        bt, bs = '겨울 홋카이도는 온종일 걸릴 가치가 있습니다', '펭귄 산책 · 설원의 나무 · 얼음 폭포 · 숲속 불빛 — 한 코스로'
    A('<section class="bandwrap"><div class="ph"><img src="../../assets/band.jpg"></div>'
      '<div class="blue"><b>%s</b><span>%s</span></div></section>' % (bt, bs))

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
    A('<section class="faqzone"><div class="sechead"><span class="micro">%s</span><span class="idx">03</span><span class="ln"></span><span class="dots"></span></div>'
      % ('BOOKING FAQ' if lang == 'ko' else '预订前常见问题'))
    A('<div class="fbody">')
    for i, (q, a) in enumerate(F['items'], 1):
        A('<div class="qa"><div class="qn">%d</div><div class="qc"><div class="q">%s</div><div class="a">%s</div></div></div>' % (i, q, a))
    A('<div class="fend">%s</div></div></section>' % F['end'])

    # END
    E = C['end']
    A('<section class="end"><img src="../../assets/closing.jpg"><div class="shade"></div><div class="txt">')
    A('<div class="eyebrow">%s</div><h3>%s</h3><div class="line"></div><p>%s</p>' % (E['eyebrow'], E['h3'], E['p']))
    A('</div></section>')
    A('<div class="copyright">%s</div>' % C['copyright'])

    title = '札幌出发富良野美瑛冬季小团1日游 · v45-C 瑞士网格' if lang == 'zh' else '삿포로 출발 비에이·후라노 겨울 소그룹 1일 투어 · v45-C 스위스'
    return shell(lang, CSS, '\n'.join(P), title)
