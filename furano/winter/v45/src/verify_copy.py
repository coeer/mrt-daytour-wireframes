# -*- coding: utf-8 -*-
# 文案 QA：content.py / courses.py 全部客人可见文字逐条与 v3 真源 md 比对
# （去掉所有空白与 HTML 标签后做子串检查；emoji 前缀的设计元素单独剥离）
import os, re, io, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

WORK = os.path.dirname(os.path.abspath(__file__))
MDP = os.path.normpath(os.path.join(WORK, '..', 'copy', '冬季MRT详情页_中韩文案_v3_去AI味.md'))
md_raw = io.open(MDP, encoding='utf-8').read()
md = re.sub(r'\s+', '', md_raw.replace('**', ''))

def norm(s):
    s = re.sub(r'<[^>]+>', '', s)      # HTML 标签
    s = re.sub(r'[\s]+', '', s)
    return s

import importlib
import content, courses
importlib.reload(content); importlib.reload(courses)

fails, checks = [], 0
def ck(label, s):
    global checks
    checks += 1
    if norm(s) not in md:
        fails.append((label, s[:60]))

for L in ('ZH', 'KO'):
    C = getattr(content, L)
    ck(L+'.cover.h1', C['cover']['h1'])
    ck(L+'.cover.sub', C['cover']['sub'])
    for ch in C['cover']['chips']:
        ck(L+'.chip', re.sub(r'^[\U0001F000-\U0001FAFF☃❄️⭐✔✘💬■]+\s*', '', ch))
    ck(L+'.hook.intro', C['hook']['intro'])
    for ic, tx in C['hook']['lines']:
        ck(L+'.hook.line', tx)
    for it in C['cost']['inc'] + C['cost']['exc']:
        ck(L+'.cost', it)
    ck(L+'.pickup_note', C['pickup_note'])
    ck(L+'.drv', C['drv'])
    ck(L+'.veh', C['veh'])
    for q, a in C['faq']['items']:
        if not (L == 'KO'):   # v3 真源 md 的 FAQ 标题只有中文，KO 问句沿 v2 译文，不参与比对
            ck(L+'.faq.q', q)
        ck(L+'.faq.a', a)
    ck(L+'.end.h3', C['end']['h3'])
    ck(L+'.end.p', C['end']['p'])

for lang in ('zh', 'ko'):
    for c in courses.courses(lang):
        ck(lang+'.note', c['note'])
        for e in c['ev']:
            ck(lang+'.ev', e['b'])

print('checks:', checks, 'fails:', len(fails))
for lb, s in fails:
    print('FAIL', lb, '->', s)
sys.exit(1 if fails else 0)
