# QuietAlert TODO

- [ ] **Overview:** Show computed total alerts versus the computed naive fixed-30% comparator, reduction, pages/week, average persistence delay, healthy campaigns, 20-row heatmap, routing donut, latest feed, trust proxy, and the note “first 14 days = warmup”.
- [ ] **Alert Inbox:** Show typed alerts with severity, ID, campaign name, channel chip, vertical tag, LP badge, signature, window, persistence, money at risk, route, and plain-English reason; include route/channel/vertical filters.
- [ ] **Incident Command:** Show Open → Acknowledged → Investigating → Resolved lifecycle in a Kanban board with MTTD, MTTR, affected campaigns, and feedback actions.
- [ ] **Campaign Explorer:** Show all 20 real campaign names with channel, vertical, landing-page group, health state, sparkline, and wide/tight volatility badges.
- [ ] **Shared Causes:** Collapse symptoms by landing-page group, channel, or vertical into merged root causes with affected campaign chips and one diagnostic action.
- [ ] **Money Impact:** Show money at risk, wasted spend, lost revenue estimate, channel bars, revenue waterfall, and estimated money saved by earlier QuietAlert detection.
- [ ] **Fatigue Battle:** Compare naive fixed-30% and QuietAlert trust using label-free routed-alert-load proxies, explicitly avoid incident-recall or mute-day claims without labels, and provide a replay scrubber plus play action.
- [ ] **What-If Lab:** Let judges select a campaign, failure type, date, severity, or preset and safely inject a copy-of-data scenario with caught/delay/signature/naive comparison output.
- [ ] **Alert Policies:** Show routing rules, alert budget, quiet hours, persistence controls, and a live last-30-days routing preview.
- [ ] **Notification Preview:** Show Slack, digest, and push-style alert messages plus a weekly report action.
- [ ] **Data Health:** Show schema detection, continuity, value checks, campaign quality scores, and correction log.
- [ ] **Evaluation:** Explain label-free operation when no labels file exists; show alerts per campaign-month, stability score, live operator-review precision from 3 prefilled reviews, alerts/week, and operator review mode.
- [ ] **Sensitivity Lab:** Provide z_band, k_min, z_hi controls, an alert-budget value, recall-versus-attention curve, SRE ceiling, and z_band × k_min sweep.
- [ ] **Explain-Why Assistant:** Provide Cmd/Ctrl+K access, deterministic “why fired / why not fired” answers with band, z-score, and baseline citations.
- [ ] **Upload Data:** Provide a CSV dropzone, accepted schema chips, bundled dataset status, and Load → Baselines → Consensus → Fingerprint → Route stepper.
- [ ] **Settings:** Provide currency, timezone, theme, threshold defaults, data source, webhook sample payload, and audit log.
- [ ] **Offline safety:** Serve from bundled `public/data/*.json` and `daily_campaign_metrics.csv` when Flask/backend routes are unavailable; keep `/api/*` shapes available through `app.py`.
- [ ] **Judge delivery:** Include README setup commands, `scripts/export_for_ui.py`, and `docs/DEMO.md` with a 90-second flow.
