# Hokkaido Winter Hub Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the existing Furano v56 detail into an extensible Hokkaido winter route collection that only displays confirmed routes.

**Architecture:** Retain the established Python HTML builders and segmented 2x screenshot pipeline. Add a versioned bilingual hub and a published-only route registry. Each confirmed route carries its own content, course and builder; route-specific facts through FAQ are wrapped in an independent detail section, while only brand and navigation are shared.

**Tech Stack:** Python 3, static HTML/CSS, Pillow, existing Chrome screenshot renderer, Playwright, GitHub Pages.

**Spec:** `docs/superpowers/specs/2026-10-28-hokkaido-winter-hub-design.md`

## Global Constraints

- All new Chinese copy is a precise translation of the Korean, not a new sales draft.
- Only confirmed routes appear; no future names, preparation labels or empty route numbers.
- Every route owns its content, course and builder; no service content is inherited by future routes.
- Create v57 files, never overwrite v56; retain all existing untracked files.
- Delivery is the online GitHub Korean/Chinese independent-long-image comparison.

## Review Focus

- Umbrella copy must not promise that future routes include the current route's hotel pickup, nine-person cap, or admission; assert these remain inside the Route 01 section.
- An unconfirmed registry entry must not render, and synthetic two-/three-route inputs must retain independent detail boundaries.
- The current-route transition must remain visible; inspect the hub/facts/course crop.
- The Chinese page must mirror every new Korean block; verify paired hub keys and visible text.
- Segmented screenshots must not lose the bottom of the page; verify dimensions, tail crop, and online natural image sizes.

---

### Task 1: Versioned bilingual hub and failing checks

**Files:**
- Create: `C:/Users/38185/ZCodeProject/线路详情页/furano/winter/02_施工/content_v57.py`
- Create: `C:/Users/38185/ZCodeProject/线路详情页/furano/winter/02_施工/routes_v57.py`
- Create: `C:/Users/38185/ZCodeProject/线路详情页/furano/winter/02_施工/verify_v57.py`

**Interfaces:**
- Consumes: unchanged `content_v56.ZH/KO`, `courses_v56.courses(lang)`, `v56.build`.
- Produces: `HUB = {'ko': {...}, 'zh': {...}}` and `published_routes(lang, registry=None)` returning confirmed routes with `id`, `number`, localized copy, `content`, `courses`, and `builder`.

- [ ] Write v57 assertions requiring one confirmed current route, no future placeholder, paired bilingual content, and extensible published-only registry behavior.
- [ ] Run `python -P "C:/Users/38185/ZCodeProject/线路详情页/furano/winter/02_施工/verify_v57.py"`; expect failure because the route registry does not exist.
- [ ] Add the bilingual hub and registry with the current route's independent content, course and builder references.

### Task 2: Theme, build, and static verification

**Files:**
- Create: `C:/Users/38185/ZCodeProject/线路详情页/furano/winter/02_施工/themes/v57.py`
- Create: `C:/Users/38185/ZCodeProject/线路详情页/furano/winter/02_施工/build_v57.py`

**Interfaces:**
- Consumes: `HUB`, `published_routes(lang)`, each route's `content`, `courses`, and `builder`.
- Produces: `v57-independent/page_{ko,zh}.html`, `03_交付/winter_v57_bilingual.html`, and repository `furano/winter/v57_bilingual.html`.

- [ ] Implement the magazine-style confirmed-route index and independent `main.route-detail` boundaries, using CSS grid `minmax(0, ...)`, intrinsic sizing, and no interactive route controls.
- [ ] Build both independent pages and the no-link comparison page.
- [ ] Run the v57 verifier; expect static HTML, route, bilingual-copy, and preserved-content checks to pass; image checks may remain pending until Task 3.
- [ ] Run `python -P "C:/Users/38185/ZCodeProject/线路详情页/furano/winter/02_施工/verify_copy.py"`; expect `79/79` unchanged-source checks to pass.

### Task 3: Render and inspect the deliverable

**Files:**
- Create: `C:/Users/38185/ZCodeProject/线路详情页/furano/winter/02_施工/render_v57.py`
- Create: `C:/Users/38185/ZCodeProject/tmp/v57qa/verify_online_v57.py`
- Create: `C:/Users/38185/ZCodeProject/线路详情页/furano/winter/03_交付/winter_v57_中韩对照校对稿.md`

**Interfaces:**
- Consumes: Task 2 HTML and existing `render_all` functions.
- Produces: both 1560px full images, slices, comparison assets, line-ID bilingual copy review, and QA evidence.

- [ ] Render both languages in 3000px segments and save full PNG/JPEG and slices without overwriting v56.
- [ ] Run all checks; inspect cover/hub/facts/course/footer crops and paired new-copy line IDs.
- [ ] Dispatch the required independent read-only reviewer for text, factual scope, and appearance; resolve blocking findings and rerun affected checks.

### Task 4: Publish and register

**Files:**
- Modify: `C:/Users/38185/ZCodeProject/mrt-daytour-wireframes/furano/winter/index.html`
- Modify: `C:/Users/38185/ZCodeProject/线路详情页/furano/winter/03_交付/README.md`
- Modify: `C:/Users/38185/knowledge/platform-ops/LIVE.md`

- [ ] Stage only the spec, plan, v57 comparison/assets, and winter index; preserve unrelated v52 files and commit with `furano winter v57: add Hokkaido route collection`.
- [ ] Push `origin main`, wait for Pages, and run desktop/mobile online checks against `v57_bilingual.html` and the winter index.
- [ ] Register actual dimensions, slice counts, commit, evidence, independent-review result, and outstanding user visual review in README, LIVE, and WORKLOG; deliver the online link.
