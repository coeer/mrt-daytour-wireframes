---
name: Furano & Biei Day Tour
description: A photo-led Korean travel issue for a Sapporo-based Furano and Biei day tour.
colors:
  warm-white: "#F7F5F0"
  white: "#FFFFFF"
  ink: "#202329"
  muted: "#62666D"
  line: "rgba(32, 35, 41, .18)"
  lavender: "#7C5DAA"
  light-lavender: "#E9E0F3"
  flower-pink: "#D96B87"
  berry: "#B7445F"
  pond-blue: "#2D7F9D"
typography:
  display:
    fontFamily: "Pretendard, Noto Sans KR, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: "clamp(2.5rem, 7vw, 5.6rem)"
    fontWeight: 700
    lineHeight: 1.02
    letterSpacing: "-.035em"
  headline:
    fontFamily: "Pretendard, Noto Sans KR, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: "clamp(1.75rem, 4.2vw, 2.8rem)"
    lineHeight: 1.12
    letterSpacing: "-.025em"
  body:
    fontFamily: "Pretendard, Noto Sans KR, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: "16px"
    lineHeight: 1.7
  label:
    fontFamily: "Pretendard, Noto Sans KR, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, system-ui, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: ".8rem"
    fontWeight: 850
    lineHeight: 1.35
rounded:
  editorial: "14px"
  pill: "999px"
spacing:
  page-gutter: "16px"
  card: "20px"
  section: "clamp(76px, 10vw, 130px)"
components:
  button-primary:
    backgroundColor: "{colors.berry}"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "11px 18px"
    height: "46px"
  button-quiet:
    backgroundColor: "rgba(32, 35, 41, .42)"
    textColor: "{colors.white}"
    rounded: "{rounded.pill}"
    padding: "11px 18px"
    height: "46px"
  card-editorial:
    backgroundColor: "{colors.white}"
    rounded: "{rounded.editorial}"
    padding: "20px"
---

# Design System: Furano & Biei Day Tour

## Overview

**Creative North Star: "The Summer Route Issue"**

This is a Korean select-shop travel issue built around real destination photography, not a card-heavy booking template. Warm-white editorial fields and disciplined near-black type give the facts room to breathe; lavender, fuchsia, and pond blue work as geographic signals drawn from the day itself.

The reading experience moves from a full-bleed landscape to the travel effort and safeguards, then into a time-led itinerary. It is direct and mobile-minded: substantial vertical intervals, concise copy measures, evident route geometry, and a small set of decisive actions. Evidence, timing, and conditions stay legible without turning the page into a dashboard.

**Key Characteristics:**

- Real photography carries the emotional peak and closes the journey.
- Lavender route geometry and fuchsia peak markers make the day scannable.
- Flat editorial surfaces use borders and tonal fields before shadow.
- Korean and Chinese text share one compact CJK-first sans-serif voice.

## Colors

The palette is a warm-paper editorial base punctuated by the colors of Furano and Biei, with ink retaining authority over all long-form information.

### Primary

- **Booking Berry:** used for the affirmative hero and closing actions; reserve it for the decision path rather than broad decoration.
- **Route Lavender:** used for route lines, time labels, icons, and ordinary itinerary markers.

### Secondary

- **Flower Pink:** marks the itinerary's peak moment, small status badges, and keyboard focus.
- **Blue Pond:** appears as a destination accent and the closing photo field.

### Tertiary

- **Lavender Field:** a pale tonal field for the travel-friction section, selected itinerary stop, and positive refund condition.

### Neutral

- **Warm Paper:** the default editorial page field.
- **White Surface:** separates benefits, itinerary, cards, and text panels from the paper field.
- **Editorial Ink:** carries all primary text, dark route panels, and structural rules.
- **Quiet Ink:** carries supporting copy and captions.
- **Soft Ink Line:** separates adjacent facts without introducing a heavy card grid.

### Named Rules

**The Route-Color Rule.** Lavender is the default navigational signal; flower pink is reserved for a true peak or state, never a second general-purpose CTA color.

**The Paper-First Rule.** Use warm paper or white as the dominant field. Strong color belongs to photography, route diagrams, and compact emphasis.

## Typography

**Display Font:** Pretendard, with Noto Sans KR, Noto Sans CJK SC, Source Han Sans SC, Microsoft YaHei, system-ui, -apple-system, BlinkMacSystemFont, and sans-serif fallbacks.

**Body Font:** The same CJK-first sans-serif stack.

**Character:** Strong, tightly tracked display text sits over a highly readable CJK body rhythm. The system uses weight and scale rather than a separate display face, keeping Korean and Chinese outputs aligned.

### Hierarchy

- **Display** (700, `clamp(2.5rem, 7vw, 5.6rem)`, 1.02): hero destination promise; constrained to a compact measure.
- **Headline** (700, `clamp(1.75rem, 4.2vw, 2.8rem)`, 1.12): section-level narrative turns.
- **Title** (700, `clamp(1.25rem, 3vw, 1.85rem)`, 1.18): itinerary-stop names.
- **Body** (400, 16px, 1.7): long-form travel and policy information; primary descriptions stay within 62–68ch.
- **Label** (850, `.8rem`, 1.35): times, route labels, guarantees, and compact operational signals.

### Named Rules

**The Compact Promise Rule.** Keep hero and section headings short enough to retain a deliberate, low-left editorial block; do not expand them into marketing paragraphs.

## Layout

Desktop content is held to an 860px reading column, with hero and selected overview grids extending to 1180px. Sections use `clamp(76px, 10vw, 130px)` vertical padding and a 16px outer gutter. The hero occupies 96svh, drops copy to the lower edge, and places actions immediately below the subtitle.

Four benefit tiles establish conditions at desktop width; split editorial and pickup areas use asymmetric two-column grids. The itinerary is the signature layout: an 86px time rail, 54px gap, lavender vertical rule, and 14px circular markers. At 820px, story grids stack, benefit tiles become two columns, and the timeline rail tightens. At 560px, actions become full-width, the rail becomes 42px with a 30px gap, and cards retain a dense two-column benefit rhythm.

**The Timeline-First Rule.** When describing a day, show movement and time as a continuous reading spine instead of scattering stops into unrelated cards.

## Elevation & Depth

This is flat by default. White surfaces, pale lavender fields, fine soft-ink rules, and full-bleed photography create separation; the only recurring shadow is a restrained halo on timeline markers. Hero and closing photos gain depth from dark vertical gradients rather than floating containers.

### Shadow Vocabulary

- **Route Marker Halo** (`box-shadow: 0 4px 14px rgba(32, 35, 41, .18)`): anchors a timeline stop over the white itinerary field.

### Named Rules

**The No-Floating-Card Rule.** Do not add ambient shadows to ordinary cards or information panels; use a border, tonal field, or photo crop first.

## Shapes

Editorial images, benefit panels, refund bands, and peak-stop fields share gently softened 14px corners. Action buttons and small guarantee or inclusion labels are fully pill-shaped. The route-window illustration is the intentional exception: a thick ink frame with exaggerated 44px upper corners and smaller 18px lower corners evokes a car windscreen.

## Components

### Buttons

Compact and weighty pills keep the next action close to the hero copy.

- **Shape:** fully rounded (`999px`) with a 46px minimum height.
- **Primary:** Booking Berry background, white text, and `11px 18px` padding.
- **Hover / Focus:** primary darkens; keyboard focus receives a 3px Flower Pink outline with a 3px offset.
- **Quiet / Ink:** the quiet hero action uses a translucent ink field with a white border, then inverts on hover; ink is used for actions on light closing contexts.

### Cards / Containers

- **Corner Style:** gently curved (`14px`) where a panel needs containment.
- **Background:** white is the ordinary information surface; Lavender Field marks a selected moment or favorable policy.
- **Shadow Strategy:** flat by default; only timeline markers use the Route Marker Halo.
- **Border:** one soft-ink rule on ordinary benefit and refund surfaces.
- **Internal Padding:** `20px` for benefits; responsive editorial callouts grow with their section.

### Navigation

The primary navigation is a two-action hero group rather than a persistent top bar. It wraps horizontally on larger screens and becomes a one-column, full-width stack on small screens. A fixed skip link appears only on keyboard focus.

### Timeline Stops

Time, position, and editorial content align on one lavender rail. Standard stops receive a lavender marker; the featured stop changes its marker to Flower Pink and places its copy in a Lavender Field panel. The mobile rail remains visible and compresses rather than disappearing.

### Route Canvas

A dark ink panel holds a simplified SVG route with named stops as positioned labels. It is an explanatory day-order diagram, not a precise map, and it should remain a compact visual break between pickup details and the full itinerary.

### FAQ Disclosure

FAQ items use semantic disclosure rows with no card background: an ink top rule, soft-ink dividers, a 64px minimum summary row, lavender plus/minus indicator, and muted answer copy. This keeps operational detail calm and linear.

## Do's and Don'ts

### Do:

- **Do** let licensed, real destination photography carry large emotional moments, especially the hero and closing field.
- **Do** preserve the 860px reading measure, 1180px wide measure, and `clamp(76px, 10vw, 130px)` section rhythm when extending the issue.
- **Do** use lavender for ordinary route/time signals and Flower Pink only for a highlight, state, or visible focus treatment.
- **Do** keep travel conditions in direct, scan-friendly groups before the detailed itinerary.

### Don't:

- **Don't** replace the timeline with a grid of generic destination cards.
- **Don't** add ratings, prices, availability, urgency, certificates, or vehicle imagery without verified product evidence.
- **Don't** use decorative shadows to make standard content panels float.
- **Don't** let Korean or Chinese text clip; retain the compact CJK stack, flexible grids, and mobile full-width actions.
