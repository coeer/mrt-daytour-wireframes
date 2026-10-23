# -*- coding: utf-8 -*-
# 三主题批量生成 HTML（设计干员 2026-10-23）
import os, sys
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'themes'))
from content import ZH, KO
from courses import courses
import magazine, refined, swiss
from base import theme_dir

THEMES = [('A-magazine', magazine), ('B-refined', refined), ('C-swiss', swiss)]

for name, mod in THEMES:
    d = theme_dir(name)
    for lang in ('zh', 'ko'):
        CS = courses(lang)
        for c in CS:
            c['hltxt'] = {'zh': '高光时刻', 'ko': '하이라이트'}[lang]
            c['pilltxt'] = {'zh': '预计', 'ko': '예정'}[lang]
        C = ZH if lang == 'zh' else KO
        html = mod.build(lang, C, CS)
        out = os.path.join(d, f'page_{lang}.html')
        open(out, 'w', encoding='utf-8').write(html)
        print(name, lang, len(html), '->', out)
