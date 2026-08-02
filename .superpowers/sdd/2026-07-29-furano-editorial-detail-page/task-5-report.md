# Task 5 local QA

## Status

Local-only correctness and mechanical QA completed. No external canonical copy, remote push/merge, live-site request, browser screenshot review, finish review, or design-system documentation was performed in this bounded pass.

## Remote verifier

Created `tests/verify_furano_remote.py` with `urllib.request`. It checks the three `?v=4` page URLs for HTTP 200, all four required markers, and all four banned markers; it also checks the five large `-1600.webp` assets for HTTP 200 and `Content-Type: image/webp`.

The verifier was intentionally **not executed**. Its `verify_` filename also keeps it outside the default `unittest discover` pattern (`test*.py`), so the local suite did not contact the live site.

## Commands and exact results

### Fresh build

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools/build_furano.py
```

Result: exit 0. Wrote `furano/index.html`, `furano/wireframe_kr.html`, and `furano/bilingual.html`.

### Full local unittest suite

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest discover -s tests -v
```

Result: exit 0; `Ran 20 tests in 0.136s`; `OK`.

The verifier source was also parsed with Python's `compile(..., "exec")` without invoking `main`; result: `Remote verifier syntax: OK (not executed)`.

### Impeccable detector (single permitted run)

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe' 'C:\Users\38185\.codex\skills\impeccable\scripts\detect.mjs' --json furano/index.html furano/wireframe_kr.html furano/bilingual.html
```

Result: exit 0. Exact JSON output:

```json
[]
```

No findings required contextual confirmation or a TDD fix. The detector was not rerun.

### Source-level audit

A combined read-only PowerShell audit checked the three generated pages, `tools/build_furano.py`, and `tools/furano_renderer.py` for required markers, redlines, direction contracts, content definitions, responsive-width hazards, generated sync, and linked local image existence.

Exact result lines:

```text
PAGE furano/index.html required_missing=0 redlines_present=0 local_image_refs=12 missing_images=0 direction_first=True seed_present=True
PAGE furano/wireframe_kr.html required_missing=0 redlines_present=0 local_image_refs=12 missing_images=0 direction_first=True seed_present=True
PAGE furano/bilingual.html required_missing=0 redlines_present=0 local_image_refs=12 missing_images=0 direction_first=True seed_present=True
DIRECTION_CONTRACT pages=3 unique=1 finish_present=True
CONTENT_SOURCE definitions=2
tools\build_furano.py:72:KR = {
tools\build_furano.py:119:ZH = {
SOURCE_REDLINES present=0
OVERFLOW_AUDIT fixed_width_gt_390=0 positive_fixed_min_width=0 responsive_880=True min_width_zero=True
GENERATED_SYNC changed_after_build=0
```

The six audited redlines were `spec-bar`, `设计建议`, `한국어 기사`, `司机会韩语`, `카카오톡 한국어 상담`, and `KakaoTalk韩语咨询`. The sole canonical language definitions are `KR` and `ZH` in `tools/build_furano.py`; the three outputs remained byte-stable after the fresh build.

## Files

- Added `tests/verify_furano_remote.py`.
- Rebuilt and verified `furano/index.html`, `furano/wireframe_kr.html`, and `furano/bilingual.html`; the fresh build introduced no generated diff.
- Appended this local-QA report.
- No renderer or content fix was needed.

## Concerns and deferred work

- Desktop/mobile screenshots, interaction checks, reduced-motion browser QA, and the finish reviewer are owned by the controller and remain pending.
- `DESIGN.md` and any sidecar were deliberately not created.
- The canonical `C:\Users\38185\ZCodeProject` copy, Git operations against remotes, publication, and live GitHub Pages verification were deliberately not performed.

## Final post-commit verification

- Re-ran the full local suite after commit: exit 0; `Ran 20 tests in 0.163s`; `OK`.
- Removed 2 regenerated `__pycache__` directories; 0 remained.
- Verified this report exists.
- `git status --short --branch` printed only `## codex/furano-editorial-v4...origin/codex/furano-editorial-v4 [ahead 3]`, proving no tracked or untracked worktree changes.
- Commit: `35ce2418255a31a9d81b639f8b4dc54ac9745739 test: verify Furano editorial detail pages`.

## Fix Round 1 evidence

### Browser finding received

At `390x844`, controller evidence measured the bilingual hero at `1076.0px` with `#benefits` at `1075px`; the Chinese title and actions extended below the first viewport. Both single-language heroes measured `776.5px` with `#benefits` at `775.5px` and passed.

### Root cause

The bilingual hero stacked two complete language columns while inheriting the single-page phone rules: a 40px language-grid row gap, 32px padding on each side of the language separator, two vertically stacked 46px actions per language, and the full label/type spacing. Those additive blocks made the hero's intrinsic content height exceed its otherwise-correct `92svh` mobile minimum.

### TDD and implementation

- RED: added two focused renderer contracts; both failed because there were no bilingual hero separator overrides and no bilingual phone action-row override.
- GREEN: the focused command passed 2/2 tests after the minimal CSS change (`Ran 2 tests in 0.002s`; `OK`).
- At `<=880px`, only the bilingual hero removes the inherited grid gap and uses 16px on each side of the Korean/Chinese separator; Korean remains above Chinese.
- At `<=560px`, only bilingual hero padding, labels, slogan, title, subtitle, and actions are compacted. Each language retains both visible actions in a two-column row, and buttons retain `min-height: 44px`.
- Desktop rules, single-language rules, hero image, copy, language order, and CTA markup were not changed.

### Regeneration and verification

```powershell
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' tools/build_furano.py
git diff --exit-code 35ce241 -- furano/index.html furano/wireframe_kr.html
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest tests.test_furano_render.RenderContractTests.test_bilingual_mobile_hero_compacts_only_its_language_separator tests.test_furano_render.RenderContractTests.test_bilingual_phone_hero_keeps_both_actions_in_compact_rows -v
& 'C:\Users\38185\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe' -m unittest discover -s tests -v
```

Exact results:

- Fresh build wrote all three pages.
- Chinese and Korean single-page HTML remained byte-identical to commit `35ce241`.
- Focused renderer contracts: 2/2 passed in `0.002s`.
- Full suite: 22/22 passed in `0.160s`.
- Changed-file audit found exactly `tools/furano_renderer.py`, `tests/test_furano_render.py`, and `furano/bilingual.html`; no unexpected file changed.
- Redline audit found 0 prohibited markers. Bilingual required version/itinerary/FAQ/seed markers, both hero languages, all four hero actions, and the 44px button floor remained present.
- `git diff --check` passed.
- The Impeccable detector was deliberately not rerun; its one permitted Task 5 run remains the previously recorded `[]`.

### Remaining controller check

The controller must recapture the bilingual page at `390x844` and confirm the rendered hero is at most `820px`, `#benefits` peeks above the fold, all four actions remain readable/usable, and no overflow or copy clipping was introduced.

### Fix Round 1 commit

- Commit: `21b78bb1cf881944e4487b081230607aa93aa6a1 fix: compact Furano bilingual mobile hero`.
- Post-commit `git status --short --branch` printed only `## codex/furano-editorial-v4...origin/codex/furano-editorial-v4 [ahead 4]`; the worktree is clean.
- Post-commit single-language byte-identity check passed again; 0 cache directories remained.

## Finish Review Fix

### Material finding

The Impeccable finish reviewer identified one fidelity/type issue: decorative platform emoji were carrying visual identity in hero subtitles, benefit icons, bilingual language flags, and non-itinerary labels instead of the committed lavender/fuchsia/pond-blue editorial system.

### TDD evidence

- RED: four focused generated-output contracts all failed against `21b78bb`: renderer-authored devices absent, subtitle unstructured/unescaped, itinerary color emoji unwrapped, and the FAQ title still carrying `💡`.
- GREEN after the single correction batch: 4/4 focused tests passed (`Ran 4 tests in 0.005s`; `OK`).
- Full suite after regeneration: 26/26 passed (`Ran 26 tests in 0.169s`; `OK`).

### Implementation

- Replaced bilingual flag glyphs with visible `KR`/`CN` typographic codes. Their parent language sections retain `lang="ko"` / `lang="zh-CN"`, and each label retains its full accessible name through `aria-label`.
- Replaced trusted raw subtitle HTML with an exact two-line tuple in the sole content source and a renderer helper that escapes each line. A renderer-authored three-dot lavender/flower-pink/pond-blue motif replaces `💜🌈💙`.
- Replaced all four rendered benefit emoji with one restrained inline line-icon family; the ticket uses a self-authored route-weight ticket geometry.
- Removed decorative emoji from non-itinerary pickup, service, FAQ-title, FAQ-closing, header, and legacy pain display fields without removing any product fact.
- Kept authoritative itinerary descriptions unchanged in the content model. Rendered `💜`, `🌈`, and `💧` are wrapped in `.copy-emoji` with low visual salience.
- Preserved the existing bilingual mobile compact-hero CSS, four 44px mobile hero actions, page structure, and one-source generation.

### Correctness and audits

- Fresh build regenerated `furano/index.html`, `furano/wireframe_kr.html`, and `furano/bilingual.html`.
- Exact changed-file set: the three generated pages, `tools/build_furano.py`, `tools/furano_renderer.py`, and `tests/test_furano_render.py`; 0 unexpected files.
- All three pages had 0 forbidden platform glyphs outside the itinerary section.
- Wrapped color-emoji counts were `1/1/1` on each single page and `2/2/2` on the bilingual page for `💜/🌈/💧`.
- Hero dot motif counts were 1 per single page and 2 on bilingual; ticket line-icon counts matched the same pattern.
- Locked FAQ arrays remained 8 questions/answers per language with unchanged SHA-256 digests: Korean `695302d0c97aecf11c71e198146914d9e41103a43b874bf3694d498b6cddb5d2`; Chinese `42f2716a4131be3401c3d6ec94ec022960da5331efa35035422be6d57e87a97a`.
- Product-redline audit found 0 violations; trusted raw subtitle interpolation count was 0; `git diff --check` passed.
- The Impeccable detector was not rerun.

### Remaining visual confirmation

The controller should include the regenerated pages in the final recapture/reviewer verdict, including confirmation that the bilingual hero remains at most 820px at `390x844` and the dot motif/line icons render crisply.

### Finish Review Fix commit

- Commit: `5db2c9c60601d2226af545ede78f4c35f67d6322 fix: refine Furano editorial iconography`.
- Post-commit `git status --short --branch` printed only `## codex/furano-editorial-v4...origin/codex/furano-editorial-v4 [ahead 5]`; the worktree is clean.
- Post-commit cache count: 0.

## Final Impeccable Correction

- Root cause: the existing `.copy-emoji` helper recognized only `💜/🌈/💧` descriptions; itinerary name and note fields bypassed it, leaving `🚗/🍽️/⏰` and other locked itinerary glyphs at full salience. The FAQ section-title `💡` was already absent after the prior correction.
- TDD RED: the expanded semantic contract failed on unwrapped itinerary glyphs while the FAQ-title/Q&A preservation contract passed.
- Minimal fix: the renderer now applies the existing low-salience treatment to all eight authoritative itinerary glyphs (`🚗/💜/🎢/🌈/🍽️/📸/💧/⏰`) across time, name, duration, description, and note output. `tools/build_furano.py` remained byte-identical to `5db2c9c`.
- Verification: focused tests passed 2/2 in `0.003s`; full suite passed 26/26 in `0.160s`.
- Render audit: Chinese and Korean pages each contain 8 wrapped itinerary glyphs; bilingual contains 16. All three have 0 full-salience itinerary glyphs remaining and no FAQ-title `💡`.
- Locked FAQ digests remain Korean `695302d0c97aecf11c71e198146914d9e41103a43b874bf3694d498b6cddb5d2` and Chinese `42f2716a4131be3401c3d6ec94ec022960da5331efa35035422be6d57e87a97a`, with 8 Q/A pairs each.
- Exact changed set before commit: three generated HTML pages, `tools/furano_renderer.py`, and `tests/test_furano_render.py`; 0 unexpected files. Production redlines: 0. `git diff --check`: pass. Detector: not rerun.
- Commit: `8b553b9bc3ea9be5a0fa49a9ff56f2316253433d fix: subdue Furano itinerary emoji`.
- Post-commit status printed only `## codex/furano-editorial-v4...origin/codex/furano-editorial-v4 [ahead 6]`; worktree clean, cache count 0, authoritative content model unchanged.

## Controller browser QA and final visual confirmation

The three generated pages were served locally and tested in the Codex in-app browser at `1280x900` and `390x844`.

### Responsive measurements

- Chinese single page: hero `864px` desktop / `776.5px` mobile; the benefits section begins at `863px` / `775.5px`, so it peeks above both initial folds.
- Korean single page: hero `864px` desktop / `776.5px` mobile; the benefits section begins at `863px` / `775.5px`, so it peeks above both initial folds.
- Bilingual page after Fix Round 1: hero `864px` desktop / `776.5px` mobile; the benefits section begins at `863px` / `775.5px`, so the previous 1076px mobile failure is resolved.
- Bilingual desktop columns compute to `570px 570px` with an exact `40px` gap. At mobile they compute to one `343.2px` column, with Korean visually above Chinese.
- All six viewport combinations reported no horizontal overflow. Every visible action/summary measured at least `44px` high. All pages contain eight native `details` elements with one initially open.
- At mobile, all four bilingual hero actions remain visible, each `44px` high and about `167.6px` wide. Korean and Chinese hero titles render at `31.232px` without clipping.

### Media, runtime, and accessibility evidence

- After traversing the bilingual page, all seven rendered images reported `complete=true` and a positive natural width; the responsive 960/720px derivatives were selected at mobile.
- Browser console warnings/errors: none.
- Every FAQ `summary` has native `tabIndex=0`, and pointer activation toggled the second disclosure. The browser automation surface did not synthesize Enter/Space toggles reliably, so keyboard behavior is additionally grounded in the unmodified native `details`/`summary` implementation and the semantic render tests.
- The reduced-motion media rule is present in the live stylesheet; the full suite verifies it. This browser surface does not expose media-feature emulation.

### Accepted screenshots for finish review

- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\korean-desktop-top.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\korean-mobile-top.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\chinese-desktop-top.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\chinese-mobile-top.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\bilingual-desktop-top-fixed.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\bilingual-mobile-top-fixed.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\korean-desktop-itinerary.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\korean-mobile-itinerary.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\bilingual-desktop-itinerary.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\bilingual-mobile-itinerary.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\chinese-desktop-faq.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\chinese-mobile-faq.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\bilingual-desktop-faq.png`
- `C:\Users\38185\Documents\Codex\2026-07-29\chrome-plugin-chrome-openai-bundled-file\work\qa-screenshots\bilingual-mobile-faq.png`

Full-page screenshots from this browser backend were rejected as evidence because its long-page capture path tiled or blanked viewports; the bounded viewport screenshots above are the authoritative visual artifacts.

## Final verdict and design-system documentation

- Final finish review verdict: pass with no regressions after corrections `5db2c9c` and `8b553b9`.
- `DESIGN.md` and `.impeccable/design.json` were generated and validated against the renderer tokens, layout constants, component patterns, and canonical document structure.
- The local Task 5 evidence is complete; remote verification remains pending explicit publication authorization.

## Final whole-branch review corrections

- TDD RED: the six focused contracts failed on missing itinerary keys/digests, key-driven media mapping, bilingual photo names, hidden full language names, and hero preload. After correcting two assertions to report failures rather than missing-key errors, the focused run failed 6/6 for the expected missing behavior.
- TDD GREEN: the same focused run passed 6/6 after the minimal renderer and content changes. The final full local suite passed 36/36 in `0.183s`.
- All eight Korean and Chinese itinerary records now carry the exact `ITINERARY_KEYS` sequence. Media, badge, note, and peak rendering dispatch by key rather than position; a reorder contract proves the mapping remains attached to the intended stop.
- Authoritative itinerary SHA-256 baselines are Korean `58a84d0897f5a713c6805250a98fdab8f3145f807fb02950e629f8a0f1414455` and Chinese `c623354ee406268b3625e7880b38e414eb20076973fe96f0fc250da925ece65a`. FAQ digests remain unchanged at Korean `695302d0c97aecf11c71e198146914d9e41103a43b874bf3694d498b6cddb5d2` and Chinese `42f2716a4131be3401c3d6ec94ec022960da5331efa35035422be6d57e87a97a`.
- The bilingual output contains seven shared-photo `role="img"` wrappers, seven empty image alts, and fourteen unique referenced Korean/Chinese hidden-label IDs. Visible `KR`/`CN` codes remain while full language names are present as hidden owned text.
- Each of all three modes has exactly one responsive versioned hero preload, one eager high-priority hero image, lazy nonhero images, exact canonical section order, and one itinerary peak. The explicit height-only source-dimension regression is covered.
- Fresh regeneration wrote all three pages; a second temporary build was byte-identical 3/3. `DESIGN.md` and the sidecar now document the bilingual `<=560px` 92svh/two-column 44px-action exception.
- The remote verifier now bans `카카오톡 한국어 상담` and `KakaoTalk韩语咨询`; syntax was validated but the verifier was not executed. The Impeccable detector was not rerun. Publication verification remains pending explicit authorization.

## Final hero preload candidate correction

- TDD RED: the exact preload/hero-candidate contract failed because the eager hero image exposed no width-descriptor `srcset` or `sizes`, while the preload used `960w, 1600w` with `100vw`.
- TDD GREEN: the focused contract passed after both the preload and hero image began consuming one shared, versioned candidate string. The hero remains inside `picture` with no conflicting `source`; eager loading, `fetchpriority="high"`, dimensions, CSS, and single/bilingual alt semantics are unchanged.
- Fresh regeneration wrote all three pages. The full suite passed 36/36 in `0.179s`, a second temporary build was byte-identical 3/3, and `git diff --check` passed.
- The detector and remote verifier were not run; nothing was pushed or copied to the canonical project.
