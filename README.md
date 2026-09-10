<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/header-dark.svg">
  <img src="assets/header-light.svg" alt="Ahmed Arfaoui — AI/ML Engineer. Agents, retrieval, predictive systems." width="100%">
</picture>

# Ahmed Arfaoui · AI/ML Engineer

I build systems that turn messy inputs into useful decisions: browser agents that collect evidence, search pipelines that rank relevant results, and ML models that serve predictions with uncertainty.

My work spans **Python and TypeScript**, from data collection and model evaluation to APIs, orchestration, and the interfaces people use to inspect the results.

**[Portfolio](https://ahmed-arfaoui-portfolio.vercel.app)** · **[LinkedIn](https://www.linkedin.com/in/ahmedarfaoui99/)** · **[Email](mailto:ahmedarfaoui2000@gmail.com)**

[Selected systems](#01--selected-systems) · [Evaluation](#02--evaluation-in-practice) · [Project timeline](#04--project-timeline) · [Technical focus](#05--technical-focus)

## 01 / Selected systems

### [Open Web Catcher](https://github.com/arfaouiahmed1/Open-Web-Catcher)
**Multi-agent browser automation for streaming-piracy investigation.**

Coordinates classification, landing-page, hosting-page, and embedded-player specialists to navigate dynamic sites and collect stream URLs, screenshots, and provider context.

- **Orchestration:** LangGraph handoffs, role-scoped tools, execution budgets, and cancellation.
- **Evidence:** Playwright MCP tools capture browser state and media candidates; an operator console exposes runs, tool calls, and cost/token telemetry.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-owc-dark.svg">
  <img src="assets/architecture-owc-light.svg" alt="Open Web Catcher architecture: console to FastAPI, SQL storage, LangGraph specialists, Playwright MCP tools and isolated Chromium pages." width="100%">
</picture>

<details>
<summary><strong>Inspect the agent responsibilities</strong></summary>

| Role | Responsibility |
| :--- | :--- |
| Classification | Identify the page type and route the task. |
| Landing | Extract event listings and candidate player links. |
| Hosting | Interact with source controls and player overlays. |
| Embedded | Inspect the player and collect media evidence. |

Tool calls, screenshots, stream candidates and provider context remain inspectable in run records.

</details>

`Python` `LangGraph` `Playwright / MCP` `FastAPI` `PostgreSQL` `Next.js`

[Architecture](https://github.com/arfaouiahmed1/Open-Web-Catcher/blob/main/docs/wiki/Architecture.md) · [Orchestrator code](https://github.com/arfaouiahmed1/Open-Web-Catcher/blob/main/src/agents/orchestrator.py) · [Console screenshots](https://github.com/arfaouiahmed1/Open-Web-Catcher#-commercial-features)

### [HuntFlow](https://github.com/arfaouiahmed1/huntflow)
**A local-first AI workspace for the full job-application workflow.**

Connects job discovery, candidate evidence, document drafting, and application tracking in a single-user application.

- **Data pipeline:** ATS connectors, per-host rate limiting, circuit breakers, and bucketed deduplication that preserves source provenance.
- **Agent workflows:** LangGraph orchestration with SQLite checkpoints and human approval gates; a document vault combines BM25 and vector retrieval through reciprocal rank fusion.

<details>
<summary><strong>Architecture / ingestion, evidence and human review</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-huntflow-dark.svg">
  <img src="assets/architecture-huntflow-light.svg" alt="HuntFlow: ATS sources feed the crawler and SQLite; job records and retrieved evidence feed LangGraph workflows and human review." width="100%">
</picture>

Job ingestion preserves provenance. The evidence vault retrieves context through BM25 and vector rank fusion. LangGraph checkpoints support interrupt/resume workflows.

</details>

`TypeScript` `Next.js` `LangGraph` `SQLite` `Python / FastAPI` `Docker`

[Architecture](https://github.com/arfaouiahmed1/huntflow/blob/master/docs/ARCHITECTURE.md) · [Retrieval code](https://github.com/arfaouiahmed1/huntflow/blob/master/src/lib/vault/search.ts) · [Run locally](https://github.com/arfaouiahmed1/huntflow#quickstart)

### [PitWall ML](https://github.com/arfaouiahmed1/PitWall-ML)
**Lap-time forecasting and race-strategy simulation.**

Combines race-data ingestion, pace models, uncertainty calibration, and a strategy simulator with an API and race dashboard.

- **Modeling:** LightGBM pace models, a physics-plus-residual model, session-based evaluation splits, conformal calibration, and leakage tests.
- **Operations:** FastAPI serving, WebSocket updates, and drift monitoring.
- **Recorded evaluation:** **1.27 s MAE across 3,931 test laps**, with **78.6% calibrated coverage** for a nominal 80% interval. Reported for the committed champion run; evaluation artifacts and session splits are linked below.

<details>
<summary><strong>Architecture / training, calibration and serving</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-pitwall-dark.svg">
  <img src="assets/architecture-pitwall-light.svg" alt="PitWall: race data to features and session splits, pace models, held-out calibration, forecasts and simulation, then API and dashboard." width="100%">
</picture>

The physics-plus-residual model is a separate implementation from the committed champion run reported here. Calibration is fitted on validation predictions; test sessions remain separate.

</details>

`Python` `Polars` `LightGBM` `FastAPI` `Next.js` `Prometheus`

[Dashboard demo](https://arfaouiahmed1.github.io/PitWall-ML/) · [Evaluation artifact](https://github.com/arfaouiahmed1/PitWall-ML/blob/main/artifacts/champion/metrics.json) · [Data splits](https://github.com/arfaouiahmed1/PitWall-ML/blob/main/artifacts/champion/splits.json)

### [SignalRank](https://github.com/arfaouiahmed1/signalrank)
**A retrieval and ranking workbench for matching CVs to jobs.**

Separates candidate retrieval, rank fusion, and optional cross-encoder reranking so each stage can be compared.

- **Retrieval:** BM25, PostgreSQL full-text search, and pgvector search paths; reciprocal rank fusion combines candidate lists.
- **Evaluation:** precision, recall, MRR, and nDCG with ablations. The committed **500-job** evaluation compares retrieval baselines using weak relevance labels, with cross-encoder evaluation kept separate.

<details>
<summary><strong>Architecture / retrieve, fuse and rerank</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-signalrank-dark.svg">
  <img src="assets/architecture-signalrank-light.svg" alt="SignalRank: a CV branches into lexical and vector retrieval; reciprocal rank fusion merges candidates, an optional cross-encoder reranks them, and relevance metrics evaluate results." width="100%">
</picture>

BM25 and PostgreSQL full-text ranking are distinct lexical paths. If the cross-encoder cannot load, results retain fused ordering. The committed retrieval evaluation uses weak labels and excludes the cross-encoder.

</details>

`Python` `FastAPI` `PostgreSQL / pgvector` `Sentence Transformers` `React`

[Interactive demo](https://arfaouiahmed1.github.io/signalrank/) · [Ranking code](https://github.com/arfaouiahmed1/signalrank/blob/main/backend/app/retrieval/hybrid.py) · [Evaluation artifact](https://github.com/arfaouiahmed1/signalrank/blob/main/artifacts/metrics.json)

## 02 / Evaluation in practice

**Uncertainty should be measured alongside prediction error.** In PitWall's committed champion run, calibration brings coverage closer to the 80% target, at the cost of wider intervals.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/evaluation-dark.svg">
  <img src="assets/evaluation-light.svg" alt="PitWall committed champion evaluation on 3,931 test laps: raw coverage 58.4%, calibrated coverage 78.6%, target 80%; mean interval width increases from 1.20 to 2.26 seconds." width="100%">
</picture>

[Inspect the recorded metrics](https://github.com/arfaouiahmed1/PitWall-ML/blob/main/artifacts/champion/metrics.json) · [Inspect the calibration code](https://github.com/arfaouiahmed1/PitWall-ML/blob/main/src/pitwall/evaluation/calibration.py)

## 03 / Beyond the core

| Project | Engineering focus | Explore |
| :--- | :--- | :--- |
| **[FarmWise](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3)** | Collaborative agricultural application connecting crop prediction and YOLO image-model endpoints to a Django REST / Next.js interface. | [Video demo](https://youtu.be/bAqBds2t3mg) |
| **[Pursivo](https://github.com/arfaouiahmed1/pursivo)** | Android application tracker with Room persistence, an evidence vault, and optional provider-backed AI drafting. Kotlin / Compose; alpha foundation. | [Architecture](https://github.com/arfaouiahmed1/pursivo/blob/main/docs/architecture.md) |

## 04 / Project timeline

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.svg">
  <img src="assets/timeline-light.svg" alt="Repository creation chronology: FarmWise January 21 2025; Open Web Catcher April 5 2026; Pursivo August 4, HuntFlow August 18, SignalRank August 20, and PitWall ML August 21 2026. Dates describe repository creation, not completion." width="100%">
</picture>

<details>
<summary><strong>Timeline sources and exact dates</strong></summary>

Dates are GitHub repository creation timestamps, shown in UTC. This is a code-portfolio chronology; spacing does not represent elapsed time.

| Created | Repository |
| :--- | :--- |
| 2025-01-21 | [Data-Farmers-FarmWise-4DS3](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3) |
| 2026-04-05 | [Open-Web-Catcher](https://github.com/arfaouiahmed1/Open-Web-Catcher) |
| 2026-08-04 | [pursivo](https://github.com/arfaouiahmed1/pursivo) |
| 2026-08-18 | [huntflow](https://github.com/arfaouiahmed1/huntflow) |
| 2026-08-20 | [signalrank](https://github.com/arfaouiahmed1/signalrank) |
| 2026-08-21 | [PitWall-ML](https://github.com/arfaouiahmed1/PitWall-ML) |

</details>

## 05 / Technical focus

| Area | What I work on |
| :--- | :--- |
| **Agent systems** | LangGraph state machines, browser tools, structured handoffs, checkpoints, human approval |
| **Retrieval & ranking** | BM25, vector search, rank fusion, cross-encoders, relevance evaluation |
| **Predictive ML** | Feature engineering, boosted trees, temporal/session splits, calibration, error analysis |
| **System delivery** | FastAPI, SQL persistence, Docker, TypeScript interfaces, execution traces and monitoring |

I care about the whole path: where the data came from, what the model actually measured, how failures are handled, and whether someone can inspect the result.

---

**Interested in AI/ML engineering work involving agents, retrieval, or predictive systems?**  
[Let's talk](mailto:ahmedarfaoui2000@gmail.com) · [Explore my portfolio](https://ahmed-arfaoui-portfolio.vercel.app)
