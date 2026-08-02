# Task 4 Report: Furano bilingual review page

## Status

Implemented and verified. Commit: `feaf046` (`feat: add responsive Furano bilingual page`).

## Implementation

- Added `render_bilingual(kr, zh)` to the approved shared renderer.
- Added a Korean-left / Chinese-right `language-grid` with a literal 40px desktop gap.
- Added a subtle Korean-column divider; at `max-width: 880px`, the layout becomes one column with Korean first and a bottom divider.
- Kept language columns independent rather than aligning individual sentences.
- Rendered shared photography and route/road illustrations once before the associated bilingual composition.
- Preserved the exact approved section order:
  `top`, `benefits`, `pain-solution`, `pickup`, `itinerary`, `included`,
  `cancellation`, `faq`, `closing`.
- Kept exactly eight native FAQ `<details>` items total, with the first item open. Each FAQ item pairs Korean and Chinese content inside the same native disclosure.
- Added `lang="ko"` and `lang="zh-CN"` ownership to reading columns and bilingual route/FAQ fragments.
- Reused the no-cache document shell, asset version `20260729-v4`, direction contract seed `88bbc100`, visible focus rules, 44px targets, and reduced-motion rules.
- Added the `"bi": "bilingual.html"` build mapping and regenerated all three pages.
- Isolated bilingual-only CSS so `furano/index.html` and `furano/wireframe_kr.html` remain byte-identical to the approved Task 3 outputs.

## TDD evidence

### RED 1

Command:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_render -v
```

Observed expected failure:

```text
ImportError: cannot import name 'render_bilingual' from 'tools.furano_renderer'
FAILED (errors=1)
```

The renderer and build target did not exist.

### GREEN 1

After the minimum bilingual renderer and build mapping were implemented, the focused render suite passed:

```text
Ran 9 tests in 0.149s
OK
```

### RED 2

Self-review added a narrower semantic/responsive regression for translated route labels, shared-media ordering, and removal of the unused single-language timeline rail. The focused test failed on the missing Chinese route-language span:

```text
AssertionError: '<span lang="zh-CN">札幌</span>' not found
FAILED (failures=1)
```

### GREEN 2

After the smallest route/CSS correction:

```text
Ran 1 test in 0.001s
OK

Ran 9 tests in 0.131s
OK
```

## Generated-output and parity evidence

Builder:

```text
Wrote zh: ...\furano\index.html
Wrote kr: ...\furano\wireframe_kr.html
Wrote bi: ...\furano\bilingual.html
```

Approved-phrase scan:

```powershell
rg -n "예정|预计|미성사|不成团|일본어·영어|日语/英语" furano/index.html furano/wireframe_kr.html furano/bilingual.html
```

Result: approved estimated-time, failed-formation refund, and Japanese/English driver phrases were found across the appropriate outputs.

Forbidden-language scan:

```powershell
rg -n "한국어 기사|카카오톡 한국어 상담|司机会韩语|KakaoTalk韩语咨询|spec-bar|设计建议" furano/index.html furano/wireframe_kr.html furano/bilingual.html
```

Result: zero matches.

Single-language parity:

```powershell
git diff --exit-code -- furano\index.html furano\wireframe_kr.html
```

Result: exit 0; both approved single-language outputs are unchanged.

## Final tests

Command:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest discover -s tests -v
```

Result:

```text
Ran 18 tests in 0.142s
OK
```

Coverage includes asset/license contracts, content/redline contracts, bilingual ordering and shared media, exact eight-item FAQ behavior, build outputs, direction seed, semantic language ownership, responsive breakpoint CSS, 44px targets, skip link, focus rules, and reduced motion.

## Files

- Modified `tools/furano_renderer.py`
- Modified `tools/build_furano.py`
- Modified `tests/test_furano_render.py`
- Regenerated `furano/bilingual.html`
- Added this report

No Task 1–3 source, asset, or approved single-language generated output changed. Generated Python cache directories were removed before commit.

## Self-review

- Confirmed the first body child remains the direction contract comment containing seed `88bbc100`.
- Confirmed Korean appears before Chinese in every shared `language-grid`.
- Confirmed the route illustration precedes its bilingual columns and uses semantic language spans.
- Confirmed there are seven `<picture>` elements for seven section-level photo placements, without duplicating the shared hero media.
- Confirmed the bilingual itinerary does not inherit the single-language timeline rail.
- Confirmed FAQ uses eight disclosures total, not eight per language.
- Confirmed bilingual-only CSS does not alter the approved single-language artifacts.
- Confirmed `git diff --check` is clean and the final worktree contains only Task 4 implementation files.

## Concerns

The in-app/browser-control runtime reported no available browser, so screenshot-based inspection at 390×844 and 1280px could not be completed in this environment. Responsive behavior is covered by the generated CSS and render-contract assertions, but a later visual smoke check at those two viewports remains advisable.

## Fix Round 1 recovery (2026-08-02)

Recovered the interrupted reviewer-fix work without discarding its partial edits. The finished renderer now gives every one of the 17 bilingual language grids exactly one immediately preceding node marked `data-shared-media`. Existing hero, editorial, route, road, itinerary, and closing media remain shared; the previously empty placements use only compact factual geometry strips. Farm Tomita remains the sole full-viewport hero and the itinerary's designated peak.

Mixed-language semantics were also corrected: both skip-link text fragments own explicit `lang` values, and the shared route and road illustrations now use unique `aria-labelledby` references to Korean and Chinese labels instead of mixed-language `aria-label` strings.

### RED 1 — reviewer contract against `feaf046`

Command (the committed renderer was loaded from Git and rendered with the current approved content):

```powershell
git show feaf046:tools/furano_renderer.py | & 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -c "import sys; from tools.build_furano import KR, ZH; ns = {}; source = sys.stdin.read().lstrip(chr(65279)); exec(compile(source, 'feaf046:tools/furano_renderer.py', 'exec'), ns); html = ns['render_bilingual'](KR, ZH); actual = html.count('data-shared-media'); assert actual == 17, f'expected 17 shared-media nodes, got {actual}'"
```

Observed expected failure:

```text
AssertionError: expected 17 shared-media nodes, got 0
```

### GREEN 1 — shared-media structure and language ownership

Command:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_render -v
```

Result:

```text
Ran 11 tests in 0.140s
OK
```

The added DOM contract walks all 17 grids and all eight itinerary stops, proving one direct shared-media predecessor per grid. The accessibility contract proves skip-link language ownership, removal of mixed `aria-label` values, two language-owned labels per shared route/road illustration, and uniqueness of every referenced ID.

### RED 2 — regenerated single-language parity

The first recovery regeneration exposed one blank line added by the new optional route labels. A focused regression was added and run:

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_render.RenderContractTests.test_single_pages_have_required_sections_and_no_wireframe_meta -v
```

Observed expected failure:

```text
Regex matched: '<figure class="route-figure" ...>\n\n'
FAILED (failures=1)
```

### GREEN 2 — parity-preserving optional labels

After making the bilingual label prefix conditional, the focused regression passed and all pages were regenerated:

```text
Ran 1 test in 0.001s
OK
Wrote zh: furano\index.html
Wrote kr: furano\wireframe_kr.html
Wrote bi: furano\bilingual.html
```

Single-language byte parity was then checked directly against the Task 4 commit:

```powershell
git diff --exit-code feaf046 -- furano/index.html furano/wireframe_kr.html
```

Result: exit 0; both single-language pages are byte-stable relative to `feaf046`.

### Final recovery verification

Focused render/content suites:

```text
Ran 16 tests in 0.135s
OK
```

Full suite:

```text
Ran 20 tests in 0.160s
OK
```

The approved-phrase scan found the estimated-time, failed-formation refund, and Japanese/English driver phrases in the appropriate generated pages. The forbidden-language/redline scan returned exit 1 with zero matches, as expected. `git diff --check` was clean, and generated Python cache directories were removed before commit.
