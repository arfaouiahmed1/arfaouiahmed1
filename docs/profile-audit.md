# Profile editorial audit

Reviewed 2026-09-10. Scope: the account's public repositories, the supplied résumé, and the public portfolio source. The README is an editorial portfolio, not a production-readiness certification. Claims are limited to code, committed artifacts, and supplied experience evidence.

## Positioning decision

The profile presents Ahmed Arfaoui as an **AI/ML Engineer** building agentic systems, retrieval/ranking pipelines, predictive ML, and the backend surfaces that make those systems inspectable. Education is part of the journey, but the page leads with systems and engineering practice rather than student identity.

## Selection and pin-order recommendation

| Order | Repository | Decision |
| :--- | :--- | :--- |
| 1 | [Open-Web-Catcher](https://github.com/arfaouiahmed1/Open-Web-Catcher) | Lead: browser-agent orchestration, bounded specialist roles, evidence capture, and operator tooling. |
| 2 | [huntflow](https://github.com/arfaouiahmed1/huntflow) | Feature: local-first product with source ingestion, provenance, retrieval, durable workflows, and human review. |
| 3 | [PitWall-ML](https://github.com/arfaouiahmed1/PitWall-ML) | Feature: predictive ML, uncertainty calibration, serving, simulation, and monitoring. |
| 4 | [signalrank](https://github.com/arfaouiahmed1/signalrank) | Feature: focused information-retrieval workbench with explicit ablations and relevance metrics. |
| 5 | [Data-Farmers-FarmWise-4DS3](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3) | Supporting collaborative applied ML / computer vision application with a repository-linked demo. |
| 6 | [pursivo](https://github.com/arfaouiahmed1/pursivo) | Supporting native Android engineering with Room persistence, evidence storage, and optional AI adapters; label alpha. |
| — | RepForge | Omit from feature set: the ML engine still contains TODO inference and simulated calibration. |
| — | NewBot-AI | Omit: public shell is thinner than the selected work and does not provide comparable evidence. |
| — | Stage | Omit: placeholder repository material. |
| — | ahmed-arfaoui-portfolio | Link as the portfolio destination rather than duplicate its claims as a project. |

Pins are recommendations for the GitHub account; this repository change does not alter account pin settings.

## Journey and internship evidence

The résumé and portfolio journey source support these exact chapters:

- **IPEIB, 2019–2022:** Mathematics and Physics preparatory cycle; described as difficult, followed by a change of route.
- **ESPRIT, 2022–2026:** Engineering degree in Software Engineering, Data Science & AI specialization, Mention Excellent.
- **CMR Tunisie, Jul–Aug 2024:** BI & Data Science internship; multi-source sales analytics and ARIMA/SARIMA/SARIMAX/Prophet comparisons.
- **ESPRIT, Jun–Aug 2025:** Data Science internship; FastAPI/data infrastructure, Gemini RAG personalized quizzes, six clustering approaches, +15% silhouette score, sub-200 ms inference.
- **VERMEG, Aug–Sep 2025:** Data Science internship; 50+ XML security configurations converted to Java, 90% conversion accuracy, approximately 95% manual-refactoring reduction.
- **Soft Stars, Dec 2025–Jun 2026:** AI & Agentic Systems Engineering graduation internship; Open Web Catcher evaluation with 126 runs, 97.6% tool-call success, and $0.152 average persisted-run cost.

The README labels these as résumé/project-evaluation outcomes and does not generalize them into claims about every project.

## Claim checks

### Open Web Catcher

- Read the architecture guide, orchestrator, browser tool/runtime, storage, and operator-console paths.
- Verified LangGraph role-scoped specialists, typed handoff context, budgets/cancellation, Playwright MCP, isolated browser context, FastAPI, PostgreSQL, and Next.js.
- Omitted site-success counts, provider-count marketing, throughput claims, and universal reliability claims.

### HuntFlow

- Read `docs/ARCHITECTURE.md`, multi-agent graph, SQLite checkpointer, vault search, deduplication, and rate-limiter code.
- Verified LangGraph state orchestration, interrupt/resume checkpoints, BM25/vector reciprocal-rank fusion, provenance-preserving company buckets, per-host rate limits, and circuit breakers.
- Omitted 100,000-candidate performance and benchmark pass-rate claims without reproducible evidence.

### PitWall ML

- Read pace models, calibration, simulation, drift monitoring, benchmark pipeline, and champion artifacts.
- The committed champion artifact reports MAE **1.271354942 s** over **3,931** test laps, raw coverage **58.4%**, calibrated coverage **78.6%**, raw mean width **1.20 s**, and calibrated width **2.2575 s**.
- `quantile_enabled` is `false` in that artifact. The profile does not attribute those numbers to the newer hybrid/quantile implementation.
- Omitted newer README benchmark numbers where no matching machine-readable artifact was found.

### SignalRank

- Read BM25, PostgreSQL full-text, pgvector, RRF, cross-encoder fallback, API, evaluation code, and `artifacts/metrics.json`.
- The committed evaluation covers **500 jobs/qrels**, weak relevance labels, one CV, and no cross-encoder result.
- Omitted latency placeholders, universal lift claims, and estimated reranker gains.

### Supporting work

- **FarmWise:** crop prediction and YOLO endpoints exist behind Django REST / Next.js; no accuracy or production-reliability claim is made because model-loading fallback paths exist.
- **Pursivo:** Kotlin / Compose, Room, evidence vault, and provider-backed grounding adapters are implemented; grounding prompts are not presented as a guarantee against fabrication.
- **RepForge:** on-device ML and calibration remain incomplete/simulated; omitted from the main narrative.

## Design and maintenance

- Warm paper / graphite / cobalt / vermilion dither-print system with condensed display type and mono machine labels.
- Raster-first local PNG plates, no remote font/script/widget dependency, and a generated raster masthead based on the supplied dither references.
- Light/dark variants, descriptive alt text, and real Markdown claims; no visible animation is required.
- Keep every metric tied to a source artifact or dated experience evidence. Re-run the audit when the source repositories or résumé change.

## Sources reviewed

- [Open-Web-Catcher](https://github.com/arfaouiahmed1/Open-Web-Catcher)
- [huntflow](https://github.com/arfaouiahmed1/huntflow)
- [PitWall-ML](https://github.com/arfaouiahmed1/PitWall-ML)
- [signalrank](https://github.com/arfaouiahmed1/signalrank)
- [Data-Farmers-FarmWise-4DS3](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3)
- [pursivo](https://github.com/arfaouiahmed1/pursivo)
- [ahmed-arfaoui-portfolio](https://github.com/arfaouiahmed1/ahmed-arfaoui-portfolio)
- Supplied résumé PDF, renamed in the profile repository as `resume/Ahmed-Arfaoui-AI-ML-Engineer-Resume.pdf`.
