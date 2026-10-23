# v45 · 富良野冬季详情页三主题管线

2026-10-23 设计干员（KimiWork 侧）施工。三个视觉主题共用同一份 v3 文案（`copy/`，唯一真源），各出中韩整页：
扁平展示页在上一级目录：`v45a-magazine-{ko,zh}.html` / `v45b-refined-{ko,zh}.html` / `v45c-swiss-{ko,zh}.html`（GitHub Pages 直开）。

## 目录

```
v45/
├── copy/    文案唯一真源（改文案先改这里，韩文禁止手敲）
├── docs/    设计说明（三主题设计决策 + QA 记录）
└── src/
    ├── content.py / courses.py   文案与行程数据（逐字映射 copy/）
    ├── css.py                    K3 原藏青样式（主题 B 基底）
    ├── build_all.py              生成 themes/<主题>/page_{lang}.html
    ├── render_all.py             probe 测高 → Chrome 2x 截图 → 切片
    ├── verify_copy.py            文案 QA：79 项与 copy/ 真源比对，改文案必跑全绿
    └── themes/                   base / magazine(A) / refined(B) / swiss(C)
```

## 复现（Windows，需本机 Chrome）

```bash
cd furano/winter/v45/src
set ASSETS_REL=../../../assets        # 素材在上一级 winter/assets/
python build_all.py                   # 生成 6 张 page_{lang}.html
python render_all.py                  # 渲染+切片，落 v45/03_交付/
python verify_copy.py                 # 文案 QA
```

切片规格：1560 px 宽母版（2x），≤5700 设备 px/张，JPG q95。
本地施工目录（线路详情页/furano/winter/02_施工）与本市为同一管线的两处分身，改任一处后记得同步。

## 选型状态

三主题待香菜选一上线 MRT（挂账 #19）。选定后 ko 版切片上传平台，其余两主题 HTML 留档。
