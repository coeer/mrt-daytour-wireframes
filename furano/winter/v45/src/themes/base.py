# -*- coding: utf-8 -*-
# 主题共享基座（设计干员 2026-10-23）：字体/素材路径/HTML 外壳
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # 02_施工/ 或 v45/src/
ASSETS_REL = os.environ.get('ASSETS_REL', '../../assets')            # themes/<name>/page.html 相对素材；仓库内跑设 '../../../assets'

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700;900'
         '&family=Noto+Sans+KR:wght@400;500;700;900'
         '&family=Noto+Serif+SC:wght@400;600;700;900'
         '&family=Noto+Serif+KR:wght@400;600;700;900'
         '&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&display=swap" rel="stylesheet">')

def img(name, cap=None, cls=''):
    c = f'<div class="cap">{cap}</div>' if cap else ''
    return f'<figure class="{cls}"><img src="{ASSETS_REL}/{name}.jpg">{c}</figure>'

def strip_emoji(s):
    return re.sub(r'^[\U0001F000-\U0001FAFF☃❄⭐✔✘💬■🐧💡👥🏨🎫]+\s*', '', s)

def shell(lang, css, body, title):
    return ('<!DOCTYPE html><html lang="%s"><head><meta charset="utf-8">'
            '<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">'
            '<title>%s</title>%s<style>%s</style></head><body><div class="page">%s</div></body></html>'
            % ('zh-CN' if lang == 'zh' else 'ko', title, FONTS, css, body))

def theme_dir(name):
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), name)
    os.makedirs(d, exist_ok=True)
    return d
