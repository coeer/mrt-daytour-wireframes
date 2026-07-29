"""Shared static renderer for the Furano/Biei editorial detail pages."""

from __future__ import annotations

from html import escape
from typing import Any


TOKENS = {
    "warm_white": "#F7F5F0",
    "white": "#FFFFFF",
    "lavender": "#7C5DAA",
    "light_lavender": "#E9E0F3",
    "flower_pink": "#D96B87",
    "pond_blue": "#2D7F9D",
    "berry": "#B7445F",
    "ink": "#202329",
    "muted": "#62666D",
}

_PICTURES = {
    "hero-farm-tomita": ((960, 720), (1600, 1200)),
    "furano-people": ((960, 480), (1600, 800)),
    "shikisai": ((960, 640), (1600, 1067)),
    "blue-pond": ((960, 640), (1600, 1067)),
    "shirahige": ((960, 640), (1600, 1067)),
    "lavender-softserve": ((720, 540), (1200, 900)),
}

_DIRECTION_CONTRACT = """<!--
THESIS: A Furano day tour reads like a Korean select-shop travel issue, not a card-heavy booking template.
OWN-WORLD: Warm white editorial fields, disciplined black type, lavender/fuchsia route accents, decisive real photography, and timeline-led geometry.
STORY: See the landscape, understand the travel effort and safeguards, then inspect the full itinerary or continue to booking.
FIRST VIEWPORT: Farm Tomita fills the frame; compact Korean or Chinese copy sits low-left, with itinerary and pickup actions above the next-section reveal.
FORM: Photo-led travel issue; pinned direction overrides the seed assignment; seed 88bbc100.
FINISH: unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, and DESIGN.md
-->"""

_CSS = """
:root {
  --warm-white: #F7F5F0;
  --white: #FFFFFF;
  --lavender: #7C5DAA;
  --light-lavender: #E9E0F3;
  --flower-pink: #D96B87;
  --pond-blue: #2D7F9D;
  --berry: #B7445F;
  --ink: #202329;
  --muted: #62666D;
  --line: rgba(32, 35, 41, .18);
  --content: 860px;
  --wide: 1180px;
  --radius: 14px;
}

* { box-sizing: border-box; }

html { color-scheme: light; }

@media (prefers-reduced-motion: no-preference) {
  html { scroll-behavior: smooth; }
  .hero__photo img { animation: hero-arrival 1100ms cubic-bezier(.16, 1, .3, 1) both; }
}

@keyframes hero-arrival {
  from { transform: scale(1.025); filter: saturate(.88); }
  to { transform: scale(1); filter: saturate(1); }
}

body {
  margin: 0;
  overflow-x: hidden;
  background: var(--warm-white);
  color: var(--ink);
  font-family: Pretendard, "Noto Sans KR", "Noto Sans CJK SC", "Source Han Sans SC",
    "Microsoft YaHei", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 16px;
  line-height: 1.7;
  word-break: keep-all;
  overflow-wrap: anywhere;
}

html[lang="zh-CN"] body { word-break: normal; }

img { display: block; width: 100%; height: auto; }

a { color: inherit; }

.skip-link {
  position: fixed;
  z-index: 100;
  top: 10px;
  left: 10px;
  min-height: 44px;
  padding: 10px 16px;
  background: var(--ink);
  color: var(--white);
  transform: translateY(-160%);
}

.skip-link:focus { transform: translateY(0); }

:focus-visible {
  outline: 3px solid var(--flower-pink);
  outline-offset: 3px;
}

.hero {
  position: relative;
  min-height: 96svh;
  display: grid;
  align-items: end;
  isolation: isolate;
  overflow: hidden;
  color: var(--white);
  background: var(--ink);
}

.hero__photo,
.hero__photo picture,
.hero__photo img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.hero__photo { z-index: 0; }

.hero__photo img { object-fit: cover; object-position: center 56%; }

.hero::after {
  content: "";
  position: absolute;
  z-index: 1;
  inset: 0;
  background: linear-gradient(180deg, rgba(15, 13, 20, .03) 20%, rgba(15, 13, 20, .78) 100%);
}

.hero__inner {
  position: relative;
  z-index: 2;
  width: min(100% - 32px, var(--wide));
  margin: 0 auto;
  padding: clamp(88px, 14vh, 150px) 0 clamp(42px, 7vh, 72px);
}

.hero__slogan {
  max-width: 34ch;
  margin: 0 0 14px;
  font-size: clamp(.76rem, 1.6vw, .9rem);
  font-weight: 750;
  letter-spacing: .12em;
}

h1,
h2,
h3,
p { margin-top: 0; }

h1 {
  max-width: 14ch;
  margin-bottom: 16px;
  font-size: clamp(2.5rem, 7vw, 5.6rem);
  line-height: 1.02;
  letter-spacing: -.035em;
  text-wrap: balance;
}

.hero__subtitle {
  max-width: 48ch;
  margin-bottom: 26px;
  font-size: clamp(.95rem, 2vw, 1.15rem);
  line-height: 1.55;
}

.actions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.button {
  min-height: 46px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 11px 18px;
  border: 1px solid transparent;
  border-radius: 999px;
  background: var(--berry);
  color: var(--white);
  font-size: .92rem;
  font-weight: 750;
  line-height: 1.35;
  text-decoration: none;
  transition: background-color 160ms ease-out, color 160ms ease-out;
}

.button:hover { background: #98364E; }

.button--quiet {
  border-color: rgba(255, 255, 255, .72);
  background: rgba(32, 35, 41, .42);
}

.button--quiet:hover { background: var(--white); color: var(--ink); }

.button--ink { background: var(--ink); }
.button--ink:hover { background: #3A3E46; }

.section {
  padding: clamp(76px, 10vw, 130px) 16px;
}

.section__inner {
  width: min(100%, var(--content));
  margin: 0 auto;
}

.section__inner--wide { width: min(100%, var(--wide)); }

.section h2 {
  max-width: 18ch;
  margin-bottom: 18px;
  font-size: clamp(1.75rem, 4.2vw, 2.8rem);
  line-height: 1.12;
  letter-spacing: -.025em;
  text-wrap: balance;
}

.lead {
  max-width: 68ch;
  margin-bottom: 38px;
  color: var(--muted);
}

.benefits {
  position: relative;
  z-index: 2;
  margin-top: -1px;
  background: var(--white);
}

.benefit-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.benefit {
  min-height: 168px;
  padding: 20px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  background: var(--white);
}

.benefit__icon { display: block; margin-bottom: 20px; font-size: 1.45rem; }
.benefit h3 { margin-bottom: 8px; font-size: 1.05rem; line-height: 1.25; }
.benefit p { margin-bottom: 0; color: var(--muted); font-size: .86rem; line-height: 1.55; }

.pain-solution { background: var(--light-lavender); }

.story-split {
  display: grid;
  grid-template-columns: minmax(0, .78fr) minmax(0, 1.4fr);
  gap: clamp(28px, 6vw, 76px);
  align-items: center;
}

.story-split__copy p { max-width: 36ch; margin-bottom: 0; }

.editorial-photo {
  overflow: hidden;
  border-radius: var(--radius);
  background: #DDD8D1;
}

.editorial-photo img { aspect-ratio: 2 / 1; object-fit: cover; }

.pickup { background: var(--warm-white); }

.pickup-grid {
  display: grid;
  grid-template-columns: minmax(0, .78fr) minmax(0, 1.22fr);
  gap: clamp(34px, 7vw, 84px);
  align-items: center;
}

.pickup-time {
  display: inline-block;
  margin-bottom: 22px;
  color: var(--lavender);
  font-size: clamp(1.35rem, 3vw, 2rem);
  font-weight: 850;
}

.plain-list {
  padding: 0;
  margin: 0;
  list-style: none;
}

.plain-list li {
  position: relative;
  padding: 13px 0 13px 23px;
  border-bottom: 1px solid var(--line);
}

.plain-list li::before {
  content: "";
  position: absolute;
  top: 24px;
  left: 1px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--lavender);
}

.route-figure { margin: 0; }

.route-canvas {
  position: relative;
  min-height: 390px;
  padding: 28px;
  overflow: hidden;
  border-radius: var(--radius);
  background: var(--ink);
  color: var(--white);
}

.route-canvas svg {
  position: absolute;
  inset: 34px 28px 56px;
  width: calc(100% - 56px);
  height: calc(100% - 90px);
}

.route-stops {
  position: relative;
  z-index: 1;
  min-height: 304px;
  margin: 0;
  padding: 8px 0;
  list-style: none;
}

.route-stops li {
  position: absolute;
  max-width: 118px;
  font-size: .76rem;
  font-weight: 750;
  line-height: 1.25;
}

.route-stops li:nth-child(1) { left: 0; bottom: 2%; }
.route-stops li:nth-child(2) { left: 17%; top: 40%; }
.route-stops li:nth-child(3) { left: 36%; top: 9%; }
.route-stops li:nth-child(4) { right: 28%; top: 28%; }
.route-stops li:nth-child(5) { right: 6%; top: 4%; }
.route-stops li:nth-child(6) { right: 0; bottom: 6%; }

.route-caption {
  margin-top: 12px;
  color: var(--muted);
  font-size: .76rem;
}

.itinerary {
  padding-bottom: clamp(90px, 14vw, 170px);
  background: var(--white);
}

.timeline {
  position: relative;
  margin-top: 52px;
}

.timeline::before {
  content: "";
  position: absolute;
  top: 12px;
  bottom: 0;
  left: 110px;
  width: 2px;
  background: var(--lavender);
}

.stop {
  position: relative;
  display: grid;
  grid-template-columns: 86px minmax(0, 1fr);
  gap: 54px;
  padding: 0 0 clamp(54px, 9vw, 108px);
}

.stop::before {
  content: "";
  position: absolute;
  z-index: 1;
  top: 7px;
  left: 104px;
  width: 14px;
  height: 14px;
  border: 3px solid var(--white);
  border-radius: 50%;
  background: var(--lavender);
  box-shadow: 0 4px 14px rgba(32, 35, 41, .18);
}

.stop__time {
  padding-top: 2px;
  color: var(--lavender);
  font-size: .8rem;
  font-weight: 850;
  line-height: 1.35;
  text-align: right;
}

.stop__content { min-width: 0; }

.stop__content h3 {
  margin-bottom: 9px;
  font-size: clamp(1.25rem, 3vw, 1.85rem);
  line-height: 1.18;
  letter-spacing: -.018em;
}

.stop__duration { margin-bottom: 14px; color: var(--muted); font-size: .88rem; }
.stop__description { max-width: 62ch; margin-bottom: 22px; }
.stop__note { max-width: 62ch; margin-bottom: 0; color: var(--muted); font-size: .87rem; }

.stop[data-peak="true"] .stop__content {
  padding: clamp(28px, 5vw, 54px);
  border-radius: var(--radius);
  background: var(--light-lavender);
}

.stop[data-peak="true"]::before { background: var(--flower-pink); }

.itinerary-photo {
  width: min(100%, 700px);
  overflow: hidden;
  border-radius: var(--radius);
  background: #E7E2DB;
}

.itinerary-photo img { aspect-ratio: 3 / 2; object-fit: cover; }

.itinerary-photo--detail { width: min(100%, 420px); }
.itinerary-photo--detail img { aspect-ratio: 4 / 3; }

.included-badge {
  display: inline-flex;
  min-height: 32px;
  align-items: center;
  margin: 0 0 16px;
  padding: 4px 11px;
  border-radius: 999px;
  background: var(--flower-pink);
  color: var(--ink);
  font-size: .75rem;
  font-weight: 800;
}

.road-window {
  position: relative;
  width: min(100%, 700px);
  aspect-ratio: 16 / 8;
  overflow: hidden;
  border: 12px solid var(--ink);
  border-radius: 44px 44px 18px 18px;
  background: var(--warm-white);
}

.road-window::after {
  content: "";
  position: absolute;
  inset: 0 50% 0 auto;
  width: 1px;
  background: rgba(32, 35, 41, .28);
}

.road-line {
  position: absolute;
  left: -8%;
  right: -8%;
  bottom: -28%;
  height: 76%;
  border: 4px solid var(--lavender);
  border-bottom: 0;
  border-radius: 50% 50% 0 0;
  transform: perspective(300px) rotateX(58deg);
}

.road-line::before {
  content: "";
  position: absolute;
  left: 50%;
  top: -80%;
  width: 3px;
  height: 240%;
  background: var(--flower-pink);
  transform: translateX(-50%);
}

.road-label {
  position: absolute;
  z-index: 1;
  right: 18px;
  bottom: 14px;
  max-width: 25ch;
  padding: 7px 10px;
  background: var(--white);
  font-size: .7rem;
  font-weight: 750;
  line-height: 1.3;
}

.included { background: var(--ink); color: var(--white); }

.included-grid {
  display: grid;
  grid-template-columns: .8fr .8fr 1.4fr;
  gap: 1px;
  margin-top: 44px;
  background: rgba(255, 255, 255, .23);
}

.included-column {
  padding: clamp(24px, 4vw, 38px);
  background: var(--ink);
}

.included-column h3 { margin-bottom: 18px; font-size: 1.15rem; }

.included-column ul {
  padding-left: 20px;
  margin: 0;
  color: #E8E7E3;
}

.included-column li + li { margin-top: 10px; }

.cancellation { background: var(--warm-white); }

.refund-bands {
  display: grid;
  grid-template-columns: 1fr 1fr;
  margin-top: 42px;
  border: 1px solid var(--line);
  border-radius: var(--radius);
  overflow: hidden;
}

.refund-band { padding: clamp(28px, 5vw, 50px); background: var(--white); }
.refund-band + .refund-band { border-left: 1px solid var(--line); }
.refund-band--positive { background: var(--light-lavender); }
.refund-band h3 { margin-bottom: 10px; font-size: 1.18rem; }
.refund-band p { margin-bottom: 0; }

.refund-notes {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin-top: 14px;
}

.refund-note {
  padding: 24px;
  border-radius: var(--radius);
  background: var(--white);
}

.refund-note strong { display: block; margin-bottom: 7px; }
.refund-note p { margin-bottom: 0; color: var(--muted); }
.local-time-note { margin-top: 18px; color: var(--muted); font-size: .82rem; }

.faq { background: var(--white); }

.faq-list {
  margin-top: 42px;
  border-top: 1px solid var(--ink);
}

.faq-list details { border-bottom: 1px solid var(--line); }

.faq-list summary {
  min-height: 64px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 20px;
  padding: 16px 2px;
  cursor: pointer;
  font-weight: 750;
  list-style: none;
}

.faq-list summary::-webkit-details-marker { display: none; }
.faq-list summary::after { content: "+"; flex: 0 0 auto; color: var(--lavender); font-size: 1.5rem; }
.faq-list details[open] summary::after { content: "−"; }

.faq-answer {
  max-width: 72ch;
  padding: 0 2px 24px;
  color: var(--muted);
}

.faq-answer p { margin-bottom: 0; }

.closing {
  position: relative;
  min-height: 66svh;
  display: grid;
  align-items: end;
  overflow: hidden;
  color: var(--white);
  background: var(--pond-blue);
}

.closing__photo,
.closing__photo picture,
.closing__photo img {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

.closing__photo img { object-fit: cover; object-position: center 58%; }

.closing::after {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(15, 36, 43, .08), rgba(15, 36, 43, .82));
}

.closing__inner {
  position: relative;
  z-index: 1;
  width: min(100% - 32px, var(--content));
  margin: 0 auto;
  padding: 110px 0 50px;
}

.closing__inner h2 { max-width: 15ch; }
.closing__inner > p { max-width: 54ch; }

.guarantees {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 0;
  margin: 28px 0;
  list-style: none;
}

.guarantees li {
  padding: 8px 12px;
  border: 1px solid rgba(255, 255, 255, .54);
  border-radius: 999px;
  font-size: .8rem;
  font-weight: 750;
}

.credits {
  padding: 28px 16px;
  background: var(--ink);
  color: #E8E7E3;
  text-align: center;
}

.credits a {
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  color: inherit;
  font-size: .82rem;
  text-underline-offset: 4px;
}

@media (max-width: 820px) {
  .benefit-grid { grid-template-columns: repeat(2, 1fr); }
  .story-split,
  .pickup-grid { grid-template-columns: 1fr; }
  .story-split__copy p { max-width: 65ch; }
  .included-grid { grid-template-columns: 1fr; }
  .timeline::before { left: 76px; }
  .stop { grid-template-columns: 60px minmax(0, 1fr); gap: 34px; }
  .stop::before { left: 70px; }
}

@media (max-width: 560px) {
  .hero { min-height: 92svh; }
  .hero__photo img { object-position: 58% center; }
  .hero__inner { padding-bottom: 36px; }
  h1 { font-size: clamp(2.4rem, 11vw, 3.4rem); }
  .actions { display: grid; grid-template-columns: 1fr; }
  .button { width: 100%; }
  .section { padding-inline: 16px; }
  .benefit-grid { grid-template-columns: 1fr 1fr; gap: 8px; }
  .benefit { min-height: 152px; padding: 16px; }
  .benefit__icon { margin-bottom: 16px; }
  .route-canvas { min-height: 350px; padding: 22px; }
  .route-stops { min-height: 270px; }
  .route-stops li { max-width: 86px; font-size: .68rem; }
  .timeline::before { left: 56px; }
  .stop { grid-template-columns: 42px minmax(0, 1fr); gap: 30px; }
  .stop::before { left: 50px; }
  .stop__time { font-size: .68rem; overflow-wrap: normal; word-break: normal; }
  .stop[data-peak="true"] .stop__content { padding: 24px 20px; }
  .road-window { border-width: 8px; border-radius: 30px 30px 14px 14px; }
  .refund-bands,
  .refund-notes { grid-template-columns: 1fr; }
  .refund-band + .refund-band { border-top: 1px solid var(--line); border-left: 0; }
  .closing { min-height: 72svh; }
}

@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    scroll-behavior: auto !important;
    animation-duration: .01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: .01ms !important;
  }
}
"""

_BILINGUAL_CSS = """
.bilingual .section__inner { width: min(100%, var(--wide)); }
.bilingual .closing__inner { width: min(100% - 32px, var(--wide)); }
.bilingual h1 { font-size: clamp(2.2rem, 4vw, 4.1rem); }
.bilingual .timeline::before { display: none; }
.bilingual .included-grid { grid-template-columns: 1fr; }

.language-grid {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 40px;
}

.language-column { min-width: 0; }

.language-column--kr {
  border-right: 1px solid var(--line);
}

.language-label {
  display: inline-flex;
  min-height: 44px;
  align-items: center;
  margin-bottom: 18px;
  color: #31536B;
  font-size: .78rem;
  font-weight: 800;
}

.hero .language-label,
.closing .language-label { color: var(--white); }
.language-column--zh .language-label { color: #7A4D2D; }
.hero .language-column--zh .language-label,
.closing .language-column--zh .language-label { color: var(--white); }

.bilingual-media {
  width: min(100%, var(--wide));
  margin: 0 auto clamp(34px, 6vw, 68px);
}

.bilingual-media .editorial-photo img { aspect-ratio: 16 / 7; }

.bilingual .benefit-grid { grid-template-columns: repeat(2, 1fr); }
.bilingual .benefit { min-height: 152px; }
.bilingual .pickup-copy .lead { margin-bottom: 24px; }
.bilingual .route-figure { margin-bottom: clamp(34px, 6vw, 68px); }

.bilingual-stop {
  padding: 0 0 clamp(54px, 9vw, 108px);
}

.bilingual-stop[data-peak="true"] {
  padding: clamp(28px, 5vw, 54px);
  margin-bottom: clamp(54px, 9vw, 108px);
  border-radius: var(--radius);
  background: var(--light-lavender);
}

.bilingual-stop__media { margin-bottom: 28px; }
.bilingual-stop__media .itinerary-photo { width: 100%; }
.bilingual-stop__media .itinerary-photo--detail { width: min(100%, 520px); }

.bilingual-stop .stop__time {
  display: block;
  padding: 0;
  margin-bottom: 8px;
  text-align: left;
}

.bilingual-faq summary,
.bilingual-faq .faq-answer {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 40px;
}

.bilingual-faq summary { position: relative; padding-right: 34px; }
.bilingual-faq summary::after { position: absolute; right: 2px; }
.bilingual-faq .faq-answer { max-width: none; }
.bilingual-faq .faq-answer p { min-width: 0; }
.bilingual-faq .faq-answer p:first-child {
  border-right: 1px solid var(--line);
}

@media (max-width: 880px) {
  .language-grid,
  .bilingual-faq summary,
  .bilingual-faq .faq-answer { grid-template-columns: 1fr; }

  .language-column--kr {
    padding: 0 0 32px;
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }

  .language-column--zh { padding-top: 32px; }
  .bilingual-faq summary,
  .bilingual-faq .faq-answer { gap: 12px; }
  .bilingual-faq .faq-answer p:first-child {
    padding: 0 0 18px;
    border-right: 0;
    border-bottom: 1px solid var(--line);
  }
}
"""


def _text(value: object) -> str:
    return escape(str(value), quote=True)


def picture(
    key: str,
    alt: str,
    *,
    hero: bool = False,
    small_fallback: bool = False,
) -> str:
    """Return a responsive licensed-photo picture with explicit dimensions."""
    from tools.build_furano import ASSET_VERSION

    if key not in _PICTURES:
        raise KeyError(f"Unknown Furano picture: {key}")
    small, large = _PICTURES[key]
    fallback = small if small_fallback else large
    loading = 'loading="eager" fetchpriority="high"' if hero else 'loading="lazy"'
    return (
        "<picture>"
        f'<source media="(max-width: 720px)" '
        f'srcset="img/{key}-{small[0]}.webp?v={ASSET_VERSION}">'
        f'<source srcset="img/{key}-{large[0]}.webp?v={ASSET_VERSION}">'
        f'<img src="img/{key}-{fallback[0]}.webp?v={ASSET_VERSION}" '
        f'width="{fallback[0]}" height="{fallback[1]}" alt="{_text(alt)}" '
        f'{loading} decoding="async">'
        "</picture>"
    )


def document(
    title: str,
    lang: str,
    body: str,
    *,
    extra_css: str = "",
) -> str:
    """Wrap page content in the shared cache-safe semantic document shell."""
    html = f"""<!doctype html>
<html lang="{_text(lang)}">
<head>
  <meta charset="utf-8">
  <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
  <meta http-equiv="Pragma" content="no-cache">
  <meta http-equiv="Expires" content="0">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#202329">
  <title>{_text(title)}</title>
  <style>{_CSS}{extra_css}</style>
</head>
<body>{_DIRECTION_CONTRACT}
{body}
</body>
</html>
"""
    return "\n".join(line.rstrip() for line in html.splitlines()) + "\n"


def _route_figure(
    ui: dict[str, Any],
    secondary_ui: dict[str, Any] | None = None,
) -> str:
    if secondary_ui is None:
        stops = "".join(f"<li>{_text(stop)}</li>" for stop in ui["route_stops"])
        label = _text(ui["route_label"])
        caption = _text(ui["route_disclaimer"])
    else:
        stops = "".join(
            f'<li><span lang="ko">{_text(primary)}</span> / '
            f'<span lang="zh-CN">{_text(secondary)}</span></li>'
            for primary, secondary in zip(
                ui["route_stops"],
                secondary_ui["route_stops"],
                strict=True,
            )
        )
        label = _text(f'{ui["route_label"]} / {secondary_ui["route_label"]}')
        caption = (
            f'<span lang="ko">{_text(ui["route_disclaimer"])}</span> / '
            f'<span lang="zh-CN">{_text(secondary_ui["route_disclaimer"])}</span>'
        )
    return f"""
<figure class="route-figure" role="img" aria-label="{label}">
  <div class="route-canvas">
    <svg viewBox="0 0 620 320" aria-hidden="true" focusable="false">
      <path d="M24 282 C95 262 91 193 154 178 S224 52 298 68 S377 154 431 121 S511 25 565 51 S573 239 607 274"
        fill="none" stroke="#E9E0F3" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M24 282 C95 262 91 193 154 178 S224 52 298 68 S377 154 431 121 S511 25 565 51 S573 239 607 274"
        fill="none" stroke="#D96B87" stroke-width="2" stroke-dasharray="3 11" stroke-linecap="round"/>
      <g fill="#FFFFFF" stroke="#7C5DAA" stroke-width="5">
        <circle cx="24" cy="282" r="8"/><circle cx="154" cy="178" r="8"/>
        <circle cx="298" cy="68" r="8"/><circle cx="431" cy="121" r="8"/>
        <circle cx="565" cy="51" r="8"/><circle cx="607" cy="274" r="8"/>
      </g>
    </svg>
    <ol class="route-stops">{stops}</ol>
  </div>
  <figcaption class="route-caption">{caption}</figcaption>
</figure>"""


def _road_window(ui: dict[str, Any]) -> str:
    return f"""
<div class="road-window" role="img" aria-label="{_text(ui['road_label'])}">
  <span class="road-line" aria-hidden="true"></span>
  <span class="road-label">{_text(ui['road_note'])}</span>
</div>"""


def _itinerary(content: dict[str, Any], ui: dict[str, Any]) -> str:
    items = content["itinerary"]
    blocks: list[str] = []
    for index, item in enumerate(items):
        peak = ' data-peak="true"' if item.get("peak") else ""
        description = item.get("desc", "")
        duration = item.get("dur", "")
        note = item.get("note", "")
        media = ""
        extra = ""

        if index == 1:
            extra = f'<p class="stop__note">{_text(ui["tomita_note"])}</p>'
        elif index == 2:
            media = _road_window(ui)
        elif index == 3:
            media = (
                f'<span class="included-badge">{_text(ui["included_badge"])}</span>'
                f'<div class="itinerary-photo">{picture("shikisai", ui["shikisai_alt"])}</div>'
            )
        elif index == 4:
            media = (
                f'<div class="itinerary-photo itinerary-photo--detail">'
                f'{picture("lavender-softserve", ui["softserve_alt"])}</div>'
            )
            extra = f'<p class="stop__note">{_text(ui["lunch_note"])}</p>'
        elif index == 5:
            media = f'<div class="itinerary-photo">{picture("blue-pond", ui["blue_pond_alt"])}</div>'
        elif index == 6:
            media = f'<div class="itinerary-photo">{picture("shirahige", ui["shirahige_alt"])}</div>'

        blocks.append(
            f"""<article class="stop"{peak}>
  <time class="stop__time">{_text(item["time"])}</time>
  <div class="stop__content">
    <h3>{_text(item["name"])}</h3>
    {f'<p class="stop__duration">{_text(duration)}</p>' if duration else ''}
    {f'<p class="stop__description">{_text(description)}</p>' if description else ''}
    {extra}
    {media}
    {f'<p class="stop__note">{_text(note)}</p>' if note else ''}
  </div>
</article>"""
        )
    return "\n".join(blocks)


def _list(items: tuple[str, ...] | list[str]) -> str:
    return "".join(f"<li>{_text(item)}</li>" for item in items)


def render_single(content: dict[str, object], lang: str) -> str:
    """Render one Korean or Simplified Chinese editorial page."""
    ui = content["editorial"]
    assert isinstance(ui, dict)
    highlights = content["hl"]
    assert isinstance(highlights, list)
    benefit_indexes = (0, 1, 2, 5)
    benefits = "".join(
        f"""<article class="benefit">
  <span class="benefit__icon" aria-hidden="true">{_text(highlights[index][0])}</span>
  <h3>{_text(ui["benefit_titles"][position])}</h3>
  <p>{_text(highlights[index][1])}</p>
</article>"""
        for position, index in enumerate(benefit_indexes)
    )

    pickup_items = content["pickup"]
    assert isinstance(pickup_items, list)
    faq_items = content["faq"]
    assert isinstance(faq_items, list)
    faq = "".join(
        f"""<details{' open' if index == 0 else ''}>
  <summary>{_text(question)}</summary>
  <div class="faq-answer"><p>{_text(answer)}</p></div>
</details>"""
        for index, (question, answer) in enumerate(faq_items)
    )

    guarantees = "".join(f"<li>{_text(item)}</li>" for item in ui["guarantees"])
    body = f"""
<a class="skip-link" href="#main-content">{_text(ui["skip"])}</a>
<header class="hero" id="top">
  <div class="hero__photo">{picture("hero-farm-tomita", ui["hero_alt"], hero=True)}</div>
  <div class="hero__inner">
    <p class="hero__slogan">{_text(content["slogan"])}</p>
    <h1>{_text(content["h1"])}</h1>
    <p class="hero__subtitle">{str(content["subtitle"])}</p>
    <nav class="actions" aria-label="{_text(ui["page_title"])}">
      <a class="button" href="#itinerary">{_text(ui["primary_cta"])}</a>
      <a class="button button--quiet" href="#pickup">{_text(ui["secondary_cta"])}</a>
    </nav>
  </div>
</header>

<main id="main-content">
  <section class="section benefits" id="benefits">
    <div class="section__inner section__inner--wide">
      <h2>{_text(ui["benefits_title"])}</h2>
      <p class="lead">{_text(ui["benefits_intro"])}</p>
      <div class="benefit-grid">{benefits}</div>
    </div>
  </section>

  <section class="section pain-solution" id="pain-solution">
    <div class="section__inner section__inner--wide story-split">
      <div class="story-split__copy">
        <h2>{_text(ui["pain_title"])}</h2>
        <p>{_text(ui["pain_body"])}</p>
      </div>
      <div class="editorial-photo">{picture("furano-people", ui["people_alt"])}</div>
    </div>
  </section>

  <section class="section pickup" id="pickup">
    <div class="section__inner section__inner--wide pickup-grid">
      <div>
        <h2>{_text(ui["pickup_title"])}</h2>
        <strong class="pickup-time">{_text(content["pickup_time"])}</strong>
        <p class="lead">{_text(ui["pickup_intro"])}</p>
        <ul class="plain-list">{_list(pickup_items)}</ul>
      </div>
      {_route_figure(ui)}
    </div>
  </section>

  <section class="section itinerary" id="itinerary">
    <div class="section__inner">
      <h2>{_text(ui["itinerary_title"])}</h2>
      <p class="lead">{_text(ui["itinerary_intro"])}</p>
      <div class="timeline">{_itinerary(content, ui)}</div>
    </div>
  </section>

  <section class="section included" id="included">
    <div class="section__inner section__inner--wide">
      <h2>{_text(ui["included_title"])}</h2>
      <div class="included-grid">
        <section class="included-column">
          <h3>{_text(ui["included_heading"])}</h3>
          <ul>{_list(ui["included_items"])}</ul>
        </section>
        <section class="included-column">
          <h3>{_text(ui["not_included_heading"])}</h3>
          <ul>{_list(ui["not_included_items"])}</ul>
        </section>
        <section class="included-column">
          <h3>{_text(ui["service_heading"])}</h3>
          <ul>{_list(ui["service_items"])}</ul>
        </section>
      </div>
    </div>
  </section>

  <section class="section cancellation" id="cancellation">
    <div class="section__inner">
      <h2>{_text(ui["cancellation_title"])}</h2>
      <div class="refund-bands">
        <article class="refund-band refund-band--positive">
          <h3>{_text(ui["refund_early_title"])}</h3>
          <p>{_text(ui["refund_early_body"])}</p>
        </article>
        <article class="refund-band">
          <h3>{_text(ui["refund_late_title"])}</h3>
          <p>{_text(ui["refund_late_body"])}</p>
        </article>
      </div>
      <div class="refund-notes">
        <article class="refund-note">
          <strong>{_text(ui["formation_title"])}</strong>
          <p>{_text(ui["formation_body"])}</p>
        </article>
        <article class="refund-note">
          <strong>{_text(ui["weather_title"])}</strong>
          <p>{_text(ui["weather_body"])}</p>
        </article>
      </div>
      <p class="local-time-note">{_text(ui["local_time_note"])}</p>
    </div>
  </section>

  <section class="section faq" id="faq">
    <div class="section__inner">
      <h2>{_text(content["faq_title"])}</h2>
      <div class="faq-list">{faq}</div>
    </div>
  </section>

  <section class="closing" id="closing">
    <div class="closing__photo">{picture("blue-pond", ui["blue_pond_alt"])}</div>
    <div class="closing__inner">
      <h2>{_text(ui["closing_title"])}</h2>
      <p>{_text(ui["closing_body"])}</p>
      <ul class="guarantees">{guarantees}</ul>
      <nav class="actions" aria-label="{_text(ui["closing_title"])}">
        <a class="button" href="#itinerary">{_text(ui["closing_itinerary"])}</a>
        <a class="button button--quiet" href="#top">{_text(ui["back_to_top"])}</a>
      </nav>
    </div>
  </section>
</main>

<footer class="credits">
  <a href="img/SOURCES.md">{_text(ui["sources"])}</a>
</footer>"""
    return document(str(ui["page_title"]), lang, body)


def _language_grid(kr_html: str, zh_html: str) -> str:
    return f"""<div class="language-grid">
  <section class="language-column language-column--kr" lang="ko">{kr_html}</section>
  <section class="language-column language-column--zh" lang="zh-CN">{zh_html}</section>
</div>"""


def _language_label(content: dict[str, Any]) -> str:
    return f'<span class="language-label">{_text(content["header"])}</span>'


def _bilingual_benefits(content: dict[str, Any]) -> str:
    ui = content["editorial"]
    highlights = content["hl"]
    benefit_indexes = (0, 1, 2, 5)
    benefits = "".join(
        f"""<article class="benefit">
  <span class="benefit__icon" aria-hidden="true">{_text(highlights[index][0])}</span>
  <h3>{_text(ui["benefit_titles"][position])}</h3>
  <p>{_text(highlights[index][1])}</p>
</article>"""
        for position, index in enumerate(benefit_indexes)
    )
    return f"""
{_language_label(content)}
<h2>{_text(ui["benefits_title"])}</h2>
<p class="lead">{_text(ui["benefits_intro"])}</p>
<div class="benefit-grid">{benefits}</div>"""


def _bilingual_route_figure(
    kr_ui: dict[str, Any],
    zh_ui: dict[str, Any],
) -> str:
    return _route_figure(kr_ui, zh_ui)


def _bilingual_stop_copy(
    item: dict[str, Any],
    ui: dict[str, Any],
    index: int,
) -> str:
    duration = item.get("dur", "")
    description = item.get("desc", "")
    note = item.get("note", "")
    extra = ""
    badge = ""
    if index == 1:
        extra = f'<p class="stop__note">{_text(ui["tomita_note"])}</p>'
    elif index == 3:
        badge = f'<span class="included-badge">{_text(ui["included_badge"])}</span>'
    elif index == 4:
        extra = f'<p class="stop__note">{_text(ui["lunch_note"])}</p>'
    return f"""
<time class="stop__time">{_text(item["time"])}</time>
<h3>{_text(item["name"])}</h3>
{badge}
{f'<p class="stop__duration">{_text(duration)}</p>' if duration else ''}
{f'<p class="stop__description">{_text(description)}</p>' if description else ''}
{extra}
{f'<p class="stop__note">{_text(note)}</p>' if note else ''}"""


def _bilingual_itinerary(
    kr: dict[str, Any],
    zh: dict[str, Any],
) -> str:
    kr_ui = kr["editorial"]
    zh_ui = zh["editorial"]
    blocks: list[str] = []
    for index, (kr_item, zh_item) in enumerate(
        zip(kr["itinerary"], zh["itinerary"], strict=True)
    ):
        media = ""
        if index == 2:
            shared_road_ui = {
                "road_label": f'{kr_ui["road_label"]} / {zh_ui["road_label"]}',
                "road_note": f'{kr_ui["road_note"]} / {zh_ui["road_note"]}',
            }
            media = _road_window(shared_road_ui)
        elif index == 3:
            media = (
                '<div class="itinerary-photo">'
                f'{picture("shikisai", kr_ui["shikisai_alt"], small_fallback=True)}</div>'
            )
        elif index == 4:
            media = (
                '<div class="itinerary-photo itinerary-photo--detail">'
                f'{picture("lavender-softserve", kr_ui["softserve_alt"], small_fallback=True)}</div>'
            )
        elif index == 5:
            media = (
                '<div class="itinerary-photo">'
                f'{picture("blue-pond", kr_ui["blue_pond_alt"], small_fallback=True)}</div>'
            )
        elif index == 6:
            media = (
                '<div class="itinerary-photo">'
                f'{picture("shirahige", kr_ui["shirahige_alt"], small_fallback=True)}</div>'
            )

        media_html = (
            f'<div class="bilingual-stop__media">{media}</div>' if media else ""
        )
        peak = ' data-peak="true"' if kr_item.get("peak") else ""
        blocks.append(
            f"""<article class="bilingual-stop"{peak}>
  {media_html}
  {_language_grid(
      _bilingual_stop_copy(kr_item, kr_ui, index),
      _bilingual_stop_copy(zh_item, zh_ui, index),
  )}
</article>"""
        )
    return "\n".join(blocks)


def _bilingual_included(content: dict[str, Any]) -> str:
    ui = content["editorial"]
    return f"""
{_language_label(content)}
<h2>{_text(ui["included_title"])}</h2>
<div class="included-grid">
  <section class="included-column">
    <h3>{_text(ui["included_heading"])}</h3>
    <ul>{_list(ui["included_items"])}</ul>
  </section>
  <section class="included-column">
    <h3>{_text(ui["not_included_heading"])}</h3>
    <ul>{_list(ui["not_included_items"])}</ul>
  </section>
  <section class="included-column">
    <h3>{_text(ui["service_heading"])}</h3>
    <ul>{_list(ui["service_items"])}</ul>
  </section>
</div>"""


def _bilingual_cancellation(content: dict[str, Any]) -> str:
    ui = content["editorial"]
    return f"""
{_language_label(content)}
<h2>{_text(ui["cancellation_title"])}</h2>
<div class="refund-bands">
  <article class="refund-band refund-band--positive">
    <h3>{_text(ui["refund_early_title"])}</h3>
    <p>{_text(ui["refund_early_body"])}</p>
  </article>
  <article class="refund-band">
    <h3>{_text(ui["refund_late_title"])}</h3>
    <p>{_text(ui["refund_late_body"])}</p>
  </article>
</div>
<div class="refund-notes">
  <article class="refund-note">
    <strong>{_text(ui["formation_title"])}</strong>
    <p>{_text(ui["formation_body"])}</p>
  </article>
  <article class="refund-note">
    <strong>{_text(ui["weather_title"])}</strong>
    <p>{_text(ui["weather_body"])}</p>
  </article>
</div>
<p class="local-time-note">{_text(ui["local_time_note"])}</p>"""


def _bilingual_faq(kr: dict[str, Any], zh: dict[str, Any]) -> str:
    items = []
    for index, ((kr_question, kr_answer), (zh_question, zh_answer)) in enumerate(
        zip(kr["faq"], zh["faq"], strict=True)
    ):
        items.append(
            f"""<details{' open' if index == 0 else ''}>
  <summary>
    <span lang="ko">{_text(kr_question)}</span>
    <span lang="zh-CN">{_text(zh_question)}</span>
  </summary>
  <div class="faq-answer">
    <p lang="ko">{_text(kr_answer)}</p>
    <p lang="zh-CN">{_text(zh_answer)}</p>
  </div>
</details>"""
        )
    return "".join(items)


def _bilingual_closing(content: dict[str, Any]) -> str:
    ui = content["editorial"]
    guarantees = "".join(f"<li>{_text(item)}</li>" for item in ui["guarantees"])
    return f"""
{_language_label(content)}
<h2>{_text(ui["closing_title"])}</h2>
<p>{_text(ui["closing_body"])}</p>
<ul class="guarantees">{guarantees}</ul>
<nav class="actions" aria-label="{_text(ui["closing_title"])}">
  <a class="button" href="#itinerary">{_text(ui["closing_itinerary"])}</a>
  <a class="button button--quiet" href="#top">{_text(ui["back_to_top"])}</a>
</nav>"""


def render_bilingual(
    kr: dict[str, object],
    zh: dict[str, object],
) -> str:
    """Render the Korean-left, Simplified-Chinese-right review page."""
    kr_ui = kr["editorial"]
    zh_ui = zh["editorial"]
    assert isinstance(kr_ui, dict)
    assert isinstance(zh_ui, dict)
    kr_pickup = kr["pickup"]
    zh_pickup = zh["pickup"]
    assert isinstance(kr_pickup, list)
    assert isinstance(zh_pickup, list)

    hero = _language_grid(
        f"""
{_language_label(kr)}
<p class="hero__slogan">{_text(kr["slogan"])}</p>
<h1>{_text(kr["h1"])}</h1>
<p class="hero__subtitle">{str(kr["subtitle"])}</p>
<nav class="actions" aria-label="{_text(kr_ui["page_title"])}">
  <a class="button" href="#itinerary">{_text(kr_ui["primary_cta"])}</a>
  <a class="button button--quiet" href="#pickup">{_text(kr_ui["secondary_cta"])}</a>
</nav>""",
        f"""
{_language_label(zh)}
<p class="hero__slogan">{_text(zh["slogan"])}</p>
<h1>{_text(zh["h1"])}</h1>
<p class="hero__subtitle">{str(zh["subtitle"])}</p>
<nav class="actions" aria-label="{_text(zh_ui["page_title"])}">
  <a class="button" href="#itinerary">{_text(zh_ui["primary_cta"])}</a>
  <a class="button button--quiet" href="#pickup">{_text(zh_ui["secondary_cta"])}</a>
</nav>""",
    )

    pickup = _language_grid(
        f"""
{_language_label(kr)}
<h2>{_text(kr_ui["pickup_title"])}</h2>
<strong class="pickup-time">{_text(kr["pickup_time"])}</strong>
<p class="lead">{_text(kr_ui["pickup_intro"])}</p>
<ul class="plain-list">{_list(kr_pickup)}</ul>""",
        f"""
{_language_label(zh)}
<h2>{_text(zh_ui["pickup_title"])}</h2>
<strong class="pickup-time">{_text(zh["pickup_time"])}</strong>
<p class="lead">{_text(zh_ui["pickup_intro"])}</p>
<ul class="plain-list">{_list(zh_pickup)}</ul>""",
    )

    itinerary_heading = _language_grid(
        f"""
{_language_label(kr)}
<h2>{_text(kr_ui["itinerary_title"])}</h2>
<p class="lead">{_text(kr_ui["itinerary_intro"])}</p>""",
        f"""
{_language_label(zh)}
<h2>{_text(zh_ui["itinerary_title"])}</h2>
<p class="lead">{_text(zh_ui["itinerary_intro"])}</p>""",
    )

    faq_heading = _language_grid(
        f"{_language_label(kr)}<h2>{_text(kr['faq_title'])}</h2>",
        f"{_language_label(zh)}<h2>{_text(zh['faq_title'])}</h2>",
    )

    body = f"""
<a class="skip-link" href="#main-content">{_text(kr_ui["skip"])} / {_text(zh_ui["skip"])}</a>
<div class="bilingual">
<header class="hero" id="top">
  <div class="hero__photo">{picture("hero-farm-tomita", kr_ui["hero_alt"], hero=True, small_fallback=True)}</div>
  <div class="hero__inner">{hero}</div>
</header>

<main id="main-content">
  <section class="section benefits" id="benefits">
    <div class="section__inner">{_language_grid(
        _bilingual_benefits(kr),
        _bilingual_benefits(zh),
    )}</div>
  </section>

  <section class="section pain-solution" id="pain-solution">
    <div class="section__inner">
      <div class="bilingual-media">
        <div class="editorial-photo">{picture("furano-people", kr_ui["people_alt"], small_fallback=True)}</div>
      </div>
      {_language_grid(
          f'{_language_label(kr)}<h2>{_text(kr_ui["pain_title"])}</h2><p>{_text(kr_ui["pain_body"])}</p>',
          f'{_language_label(zh)}<h2>{_text(zh_ui["pain_title"])}</h2><p>{_text(zh_ui["pain_body"])}</p>',
      )}
    </div>
  </section>

  <section class="section pickup" id="pickup">
    <div class="section__inner pickup-copy">
      {_bilingual_route_figure(kr_ui, zh_ui)}
      {pickup}
    </div>
  </section>

  <section class="section itinerary" id="itinerary">
    <div class="section__inner">
      {itinerary_heading}
      <div class="timeline">{_bilingual_itinerary(kr, zh)}</div>
    </div>
  </section>

  <section class="section included" id="included">
    <div class="section__inner">{_language_grid(
        _bilingual_included(kr),
        _bilingual_included(zh),
    )}</div>
  </section>

  <section class="section cancellation" id="cancellation">
    <div class="section__inner">{_language_grid(
        _bilingual_cancellation(kr),
        _bilingual_cancellation(zh),
    )}</div>
  </section>

  <section class="section faq" id="faq">
    <div class="section__inner">
      {faq_heading}
      <div class="faq-list bilingual-faq">{_bilingual_faq(kr, zh)}</div>
    </div>
  </section>

  <section class="closing" id="closing">
    <div class="closing__photo">{picture("blue-pond", kr_ui["blue_pond_alt"], small_fallback=True)}</div>
    <div class="closing__inner">{_language_grid(
        _bilingual_closing(kr),
        _bilingual_closing(zh),
    )}</div>
  </section>
</main>

<footer class="credits">
  <a href="img/SOURCES.md">
    <span lang="ko">{_text(kr_ui["sources"])}</span>&nbsp;/&nbsp;
    <span lang="zh-CN">{_text(zh_ui["sources"])}</span>
  </a>
</footer>
</div>"""
    title = f'{kr_ui["page_title"]} / {zh_ui["page_title"]}'
    return document(title, "ko", body, extra_css=_BILINGUAL_CSS)


__all__ = ["TOKENS", "document", "picture", "render_bilingual", "render_single"]
