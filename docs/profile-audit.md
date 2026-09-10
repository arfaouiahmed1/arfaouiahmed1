# Profile editorial audit

Reviewed 2026-09-10. Scope: the account's 11 public repositories, including this profile. Selection follows implemented systems and relevance to AI/ML engineering; it is not a production-readiness certification. Read repository trees and READMEs, then representative implementation and evaluation files for the featured systems. No training run or application deployment was reproduced.

## Selection and recommended pin order

| Order | Repository | Decision |
| --- | --- | --- |
| 1 | Open-Web-Catcher | Lead: strongest browser-agent system, bounded orchestration, evidence capture and operator tooling. |
| 2 | huntflow | Feature: integrated AI product, source ingestion, retrieval, durable orchestration and human review. |
| 3 | PitWall-ML | Feature: predictive ML, uncertainty, serving and monitoring; use the committed champion artifact's scoped results. |
| 4 | signalrank | Feature: focused information-retrieval project with inspectable fusion, reranking and evaluation. |
| 5 | Data-Farmers-FarmWise-4DS3 | Supporting: collaborative applied ML/computer-vision application with a repository-linked video demo. |
| 6 | pursivo | Supporting: native Android engineering and explicit AI provider integration; label alpha. |
| — | RepForge | Omit from featured work: useful Android breadth, but the ML engine still delegates to rules and simulates calibration. |
| — | ahmed-arfaoui-portfolio | Use as the portfolio destination rather than another featured project. |
| — | NewBot-AI | Omit: thin documentation and less compelling AI/ML evidence than the selected work. |
| — | Stage | Omit: directory structure is largely placeholder README material. |
| — | arfaouiahmed1 | Replaced starter profile with this redesign. |

Pins are recommendations; this change edits repository files, not account pin settings.

## Claim checks

### Open Web Catcher
- Read `src/agents/orchestrator.py`: LangGraph, typed handoff context, specialist roles, workflow budget/cancellation errors, evidence checklists.
- Checked Playwright runtime/tool paths and `src/storage/database.py`; current runtime is Playwright, not the earlier Puppeteer implementation.
- Linked existing architecture guide and console screenshots.
- Omitted site-success counts, provider-count marketing, universal reliability claims and unverified throughput.

### HuntFlow
- Read `src/agents/multiAgentAppGraph.ts`, `src/lib/agents/checkpointer.ts`, `src/lib/vault/search.ts`, `src/lib/dedup.ts`, and `scrapling-agent/rate_limiter.py`.
- Verified StateGraph orchestration, SQLite checkpoint implementation, BM25/vector RRF retrieval, company-bucket deduplication and per-host circuit breaking.
- Describe as a single-user, local-first application, not hosted SaaS.
- Omitted 100,000-candidate performance and benchmark pass-rate claims without reproducing or locating corresponding run evidence.

### PitWall ML
- Read `src/pitwall/models/pace/hybrid_model.py`, `src/pitwall/evaluation/calibration.py`, `src/pitwall/simulation/engine.py`, `src/pitwall/monitoring/drift.py`, `pipelines/benchmark_challengers.py`, and champion artifacts.
- Committed `artifacts/champion/metrics.json`: MAE 1.271354942 s, n=3931, calibrated coverage 0.7855507504. Rounded in profile to 1.27 s and 78.6%.
- `artifacts/champion/splits.json` records 2024/2025 training, Spanish GP 2025 validation, São Paulo and United States GP 2025 test sessions.
- Champion metrics set `quantile_enabled: false`. The profile does not attribute this run's metrics to the newer quantile/hybrid model.
- README's 0.302 s newer hybrid and cross-circuit benchmark tables lack matching committed machine-readable benchmark results in the inspected tree; omitted.
- Demo URL is repository-sourced. A static dashboard/demo is not proof of a running model backend.

### SignalRank
- Read retrieval BM25, RRF and cross-encoder modules, API module, `backend/app/evaluation/compare.py`, and `artifacts/metrics.json`.
- True BM25 uses `rank_bm25`; the PostgreSQL path uses `ts_rank`, not exact BM25. Profile distinguishes these paths.
- Cross-encoder code falls back to fused ordering if the model is unavailable.
- Artifact has 500 jobs/qrels, weak relevance labels, a single CV and no cross-encoder result. Hybrid nDCG@10 is about 0.259, below the recorded embedding baseline of about 0.276.
- Evaluation code contains hard-coded latency placeholders. No latency, universal ranking lift, or estimated CE gain appears in the profile.

### Supporting work
- FarmWise: read `Deployment/backend/api/ml_utils.py` and `Deployment/backend/api/views.py`; crop model loading and YOLO endpoints exist. Some prediction failures return fixed fallback values, so no accuracy or production reliability claim is made. Authorship is described as collaborative.
- Pursivo: inspected module tree and `GroundedEngines.kt`; structured analysis/drafting provider calls and grounding prompts are implemented. Grounding prompts are not presented as a guarantee against fabrication.
- RepForge: `ProgressionEngine.kt` contains TODO LiteRT inference and simulated calibration. Do not advertise shipped on-device ML.

## Sources and snapshots

- [Open-Web-Catcher](https://github.com/arfaouiahmed1/Open-Web-Catcher) — inspected default-branch snapshot `c3ebdae681363a1a36503bb173dbbea9db377372`.
- [huntflow](https://github.com/arfaouiahmed1/huntflow) — inspected default-branch snapshot `7daa4d9a3aa5d86b36471bf7f316d44b7ca9375d`.
- [signalrank](https://github.com/arfaouiahmed1/signalrank) — inspected default-branch snapshot `e7ee20308b8685fc5c5b4272f9da03ceca53c296`.
- [PitWall-ML](https://github.com/arfaouiahmed1/PitWall-ML) — inspected default-branch snapshot `71a0f10678d657996db351b624dc00b9c8e2e359`.
- [Data-Farmers-FarmWise-4DS3](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3) — inspected default-branch snapshot `d4f16b7affbe323d88c5bf4599ca510f5e6ce0f7`.
- [Stage](https://github.com/arfaouiahmed1/Stage) — inspected default-branch snapshot `879e04fcf510cf31392b500163768ed5b88ba19c`.
- [NewBot-AI](https://github.com/arfaouiahmed1/NewBot-AI) — inspected default-branch snapshot `2a7564201924407febbba6f05a80b92d2211cc60`.
- [ahmed-arfaoui-portfolio](https://github.com/arfaouiahmed1/ahmed-arfaoui-portfolio) — inspected default-branch snapshot `058b891c6879248c2118bcdb774c879afba645be`.
- [pursivo](https://github.com/arfaouiahmed1/pursivo) — inspected default-branch snapshot `7168e3dbf60ddea038c2195a907652e60aefc313`.
- [RepForge](https://github.com/arfaouiahmed1/RepForge) — inspected default-branch snapshot `6e29bf592413dcedef0ee752303c3e91bb525632`.
- [arfaouiahmed1](https://github.com/arfaouiahmed1/arfaouiahmed1) — inspected default-branch snapshot `81eaef07d0e0fb31ca040a754a4d348599b20504`.

Public demo, portfolio, LinkedIn and email links came from repository READMEs. Direct web availability checks were blocked by the browsing environment; they were not certified live. No fabricated demo URL was added.

## Design and maintenance

- Graphite / warm paper with burnt-orange accent; architectural rules and a custom geometric AA monogram.
- Local, self-contained SVG headers for GitHub light/dark preferences. No remote font, script, animation or widget dependencies.
- Real Markdown headings, text and links carry all substantive content; the banner is supplementary and has descriptive alternative text.
- Sequential project sections preserve readability on narrow screens. Tables are limited to supporting projects and skill mapping.
- Keep evaluation claims tied to artifact versions. Recheck this audit when the source repositories change.
