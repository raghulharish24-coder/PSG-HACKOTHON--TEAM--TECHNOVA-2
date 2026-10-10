# QuietAlert — Round 2 UI/UX Implementation Plan

## Product scope
Extend the existing QuietAlert ops command center into the full Round 2 judge-facing product for PS-04. Preserve the dark, indigo, evidence-first visual language while making all 16 requested modules reachable from the collapsible sidebar and usable with bundled fallback data when Flask is offline.

## Design direction
QuietAlert keeps its evidence-first ops command center, but the supplied Seamless Web3 Banking direction becomes the visual shell: near-black #020202 canvas, 33px rounded artboards, split gradient panes, glass top-bar pills, Figtree uppercase display type, Instrument Sans body copy, restrained white/gray semantic surfaces, a monochrome motion texture, and a floating silver metric card. Severity remains semantic inside the operational tables and charts; the hero is intentionally monochrome so the product feels premium rather than decorative. The Overview now carries the Web3-style split-pane presentation, while all 16 modules inherit the rounded artboard and typography system.

## Full module map
1. Overview: pitch KPIs, heatmap, routing, feed, trust.
2. Alert Inbox: typed alert table, filters, reasons, feedback.
3. Incident Command: lifecycle Kanban, MTTD/MTTR, acknowledge/investigate/resolve actions.
4. Campaign Explorer: 20 real campaigns, volatility, sparklines, naive overlay.
5. Shared Causes: LP/channel/vertical symptom merging.
6. Money Impact: at-risk KPIs, channel bars, waterfall, saved-by-catching card.
7. Fatigue Battle: naive mute versus QuietAlert replay.
8. What-If Lab: copy-only scenario injection and result evidence.
9. Alert Policies: routing rules, budgets, quiet hours, persistence, preview.
10. Notification Preview: Slack, daily digest, mobile push tabs, weekly report.
11. Data Health: schema, continuity, values, scores, corrections.
12. Evaluation: label-free proxies, stability, operator review.
13. Sensitivity Lab: threshold controls, curve, sweep.
14. Explain-Why Assistant: Cmd/Ctrl+K, deterministic evidence citations, why-not-fired.
15. Upload Data: dropzone, schema chips, pipeline stepper.
16. Settings: currency/timezone/theme/thresholds, webhook sample, audit log.

## Implementation
The existing dependency-light HTML/CSS/JavaScript app remains the preview and static publishing surface. The sidebar is expanded with all module IDs, each module receives its own `view-*` section, and `script.js` adds the interactions that matter in a live judge session: Judge Mode, Cmd/Ctrl+K focus, incident lifecycle buttons, what-if injection, policy saving, notification tabs, assistant questions, and settings/webhook actions. `app.py` now exposes the full requested endpoint shape with safe demo responses. The bundled JSON/CSV contract remains the offline source of truth.

## Delivery and validation
`npm run dev` serves the UI on port 3000 and `python app.py` serves the optional endpoint wrapper on port 5000. `public/manus-routes.json` remains synchronized for the single-page route. Validation covers all 16 nav/view IDs, JavaScript syntax, bundled dataset shape, preview responses, API endpoints, and mobile/desktop screenshots.
