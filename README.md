<p align="center">
  <img src="assets/header-dither.png" alt="Ahmed Arfaoui — AI / ML Engineer. Agent systems, retrieval, predictive ML." width="100%">
</p>

<p align="center">
  <strong>AI / ML ENGINEER</strong> &nbsp;·&nbsp; AGENT SYSTEMS &nbsp;·&nbsp; RETRIEVAL &nbsp;·&nbsp; PREDICTIVE ML
</p>

I build the parts of AI products that have to survive contact with the real world: browser agents that leave evidence, retrieval systems that can be evaluated, and predictive services that expose uncertainty instead of hiding it.

My earlier work spans **agricultural computer vision, tabular modeling, and NLP**. Today, I bring that foundation into agents, retrieval, and predictive services.

My work moves across **Python and TypeScript**, from data ingestion and model evaluation to LangGraph orchestration, FastAPI services, SQL persistence, monitoring, and the interfaces people use to inspect a run.

<p>
  <a href="https://ahmed-arfaoui-portfolio.vercel.app"><img src="assets/links/portfolio.png" alt="Portfolio" width="190"></a>
  <a href="https://www.linkedin.com/in/ahmedarfaoui99/"><img src="assets/links/linkedin.png" alt="Linkedin" width="190"></a>
  <a href="resume/Ahmed-Arfaoui-AI-ML-Engineer-Resume.pdf"><img src="assets/links/resume.png" alt="Download résumé" width="190"></a>
  <a href="mailto:ahmedarfaoui2000@gmail.com"><img src="assets/links/email.png" alt="Email" width="190"></a>
</p>

[My journey](#00--my-journey) · [Internships](#01--internships) · [Core systems](#02--core-systems) · [Evidence](#03--evidence-over-decoration) · [Earlier projects](#04--earlier-data-science--creative-engineering) · [Technical focus](#06--technical-focus) · [GitHub stats](#07--github-stats)

## 00 / My journey

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/journey-dark.png">
  <img src="assets/journey-light.png" alt="My Journey — dithered ribbon transforming from fragments into an open geometric loop." width="100%">
</picture>

My route into engineering was not a straight line. I started with the **Mathematics and Physics preparatory cycle at IPEIB (2019–2022)**. It was a difficult period, and I changed direction rather than letting the first route define the outcome.

At **ESPRIT (2022–2026)** I completed an engineering degree in Software Engineering, specialized in Data Science & AI, and graduated with **Mention Excellent**. Internships during that period turned that direction into a practice: reporting and forecasting, then applied ML services, then GenAI-assisted modernization, and finally multi-agent browser intelligence.

| Period | Chapter | What it added |
| :--- | :--- | :--- |
| **2019–2022** | IPEIB · preparatory cycle | Mathematics, physics, resilience, and a deliberate change of route |
| **2022–2026** | ESPRIT · software engineering | Data Science & AI specialization, systems engineering, Mention Excellent |
| **2024–2026** | Four internships | Forecasting → APIs and clustering → GenAI modernization → agentic systems |
| **2026 →** | AI / ML engineering | Building inspectable systems that connect models to decisions |

## 01 / Internships

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/internships-dark.png">
  <img src="assets/internships-light.png" alt="In Practice — four sculptural forms representing forecasting, ML services, GenAI, and agents." width="100%">
</picture>

These placements are the connective tissue between my education and the systems in the repositories below. The results are reported from my résumé and project evaluations; they are kept scoped to the work where they were measured.

### Soft Stars · AI & Agentic Systems Engineering Intern
**December 2025 – June 2026 · Graduation internship**

Built **[Open Web Catcher](https://github.com/arfaouiahmed1/Open-Web-Catcher)**, a multi-agent web-intelligence system for navigating dynamic pages and collecting inspectable evidence.

- Evolved an n8n / Puppeteer prototype into a LangChain / LangGraph / MCP / FastAPI / Next.js architecture.
- Recorded **126 end-to-end runs**, **97.6% tool-call success**, and **$0.152 average persisted-run cost** in the project evaluation.
- Connected PostgreSQL persistence and Azure Service Bus around resumable, observable runs.

### VERMEG · Data Science Intern
**August 2025 – September 2025**

Worked on AI-assisted legacy-code modernization: converting **50+ XML security configurations into Java** with Spring Boot and Spring AI.

- Reached **90% conversion accuracy** in the evaluated set.
- Reduced manual refactoring effort by approximately **95%** for the targeted workflow.
- The engineering constraint was not just generation; it was preserving structure and making the output reviewable.

### ESPRIT · Data Science Intern
**June 2025 – August 2025**

Built the backend and data layer for an ML learning platform, including **FastAPI services**, data models, database infrastructure, and Gemini-backed RAG for personalized quiz generation.

- Evaluated **six clustering approaches** rather than selecting an algorithm by default.
- Improved the measured silhouette score by **15%** and kept inference under **200 ms** in the reported evaluation.

### CMR Tunisie · BI & Data Science Intern
**July 2024 – August 2024**

Worked with multi-source sales data across ingestion, cleaning, transformation, and analytics. Compared **ARIMA, SARIMA, SARIMAX, and Prophet** models for time-series forecasting, building the analytical foundation that later shaped my interest in production ML evaluation.

## 02 / Core systems

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/systems-dark.png">
  <img src="assets/systems-light.png" alt="Core Systems — dithered computational sculptures for agents, workflows, forecasts, and ranking." width="100%">
</picture>

<p align="center">
  <img src="assets/dither-field.png" alt="Dither field of connected computational forms: a halftone signal, orbital path, vermilion marker, and faceted system geometry." width="100%">
</p>
<p align="center"><sub>FIELD NOTE / INPUT → EVIDENCE → DECISION → TRACE</sub></p>

### [Open Web Catcher](https://github.com/arfaouiahmed1/Open-Web-Catcher)

<p>
  <a href="https://github.com/arfaouiahmed1/Open-Web-Catcher"><img src="assets/links/source.png" alt="Open Web Catcher source code" width="190"></a>
</p>
**Browser agents that collect evidence from difficult web surfaces.**

The system coordinates role-scoped specialists for classification, landing pages, hosting pages, and embedded players. A LangGraph orchestrator controls handoffs and budgets; Playwright MCP operates an isolated browser context; FastAPI and PostgreSQL persist the run; a Next.js console makes tool calls and evidence inspectable.

<details>
<summary><strong>Architecture map</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-owc-dark.png">
  <img src="assets/architecture-owc-light.png" alt="Open Web Catcher — floating page forms and a wireframe globe, illustrating browser intelligence." width="100%">
</picture>

```mermaid
flowchart TD
  UI[Next.js console] <--> API[FastAPI]
  API --> G[LangGraph orchestrator]
  G <--> S[Role-scoped specialists]
  S --> MCP[Playwright MCP]
  MCP --> B[Isolated browser context]
  B --> E[Collected evidence]
  E --> G
  API <--> DB[(PostgreSQL run records)]
```

[Architecture notes](https://github.com/arfaouiahmed1/Open-Web-Catcher/blob/main/docs/wiki/Architecture.md) · [Orchestrator](https://github.com/arfaouiahmed1/Open-Web-Catcher/blob/main/src/agents/orchestrator.py)
</details>

<p><img src="assets/stacks/owc.png" alt="Python, LangGraph, Playwright, FastAPI, PostgreSQL, Next.js" width="600"></p>

`Python` `LangGraph` `Playwright MCP` `FastAPI` `PostgreSQL` `Next.js`

### [HuntFlow](https://github.com/arfaouiahmed1/huntflow)

<p>
  <a href="https://github.com/arfaouiahmed1/huntflow"><img src="assets/links/source.png" alt="HuntFlow source code" width="190"></a>
</p>
**A local-first application workflow with retrieval and human gates.**

HuntFlow connects job discovery, candidate evidence, document drafting, and application tracking. ATS connectors use per-host rate limits and circuit breakers; bucketed deduplication preserves provenance; LangGraph workflows checkpoint in SQLite; the evidence vault combines BM25 and vector retrieval with reciprocal rank fusion before a human review step.

<details>
<summary><strong>Architecture map</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-huntflow-dark.png">
  <img src="assets/architecture-huntflow-light.png" alt="HuntFlow — interlocking folded bands and document forms, illustrating human-guided workflows." width="100%">
</picture>

```mermaid
flowchart TD
  ATS[ATS and job sources] --> ING[Rate limits and circuit breakers]
  ING --> D[Deduplication with provenance]
  D --> G[LangGraph workflow]
  V[BM25 and vector evidence vault] --> G
  G <--> C[(SQLite checkpoints)]
  G --> H[Human review]
  H --> R[Resume workflow]
  R --> G
```

[Architecture](https://github.com/arfaouiahmed1/huntflow/blob/master/docs/ARCHITECTURE.md) · [Vault retrieval](https://github.com/arfaouiahmed1/huntflow/blob/master/src/lib/vault/search.ts)
</details>

<p><img src="assets/stacks/huntflow.png" alt="TypeScript, Node.js, Next.js, LangGraph, SQLite" width="500"></p>

`TypeScript` `Next.js` `LangGraph` `SQLite` `BM25` `Vector retrieval`

### [PitWall ML](https://github.com/arfaouiahmed1/PitWall-ML)

<p>
  <a href="https://github.com/arfaouiahmed1/PitWall-ML"><img src="assets/links/source.png" alt="PitWall ML source code" width="190"></a>
  <a href="https://arfaouiahmed1.github.io/PitWall-ML/"><img src="assets/links/demo.png" alt="PitWall ML live demo" width="190"></a>
</p>
**Lap-time forecasting with calibrated uncertainty and a strategy simulator.**

The project combines race-data ingestion, Polars feature pipelines, LightGBM pace models, a physics-plus-residual path, temporal/session splits, conformal calibration, FastAPI/WebSocket serving, and Prometheus/Grafana drift monitoring.

<details>
<summary><strong>Architecture map</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-pitwall-dark.png">
  <img src="assets/architecture-pitwall-light.png" alt="PitWall ML — an aerodynamic ribbon and particulate field, illustrating forecasts and uncertainty." width="100%">
</picture>

```mermaid
flowchart TD
  DATA[Race data] --> F[Polars features]
  F --> SPLIT[Temporal and session splits]
  SPLIT --> M[Pace model training]
  SPLIT --> CAL[Held-out calibration data]
  M --> P[Forecasts]
  CAL --> C[Conformal calibration]
  P --> C
  C --> SIM[Strategy simulation]
  C --> API[FastAPI and WebSockets]
  SIM --> API
  API --> MON[Monitoring and dashboard]
```

[Champion metrics](https://github.com/arfaouiahmed1/PitWall-ML/blob/main/artifacts/champion/metrics.json) · [Session splits](https://github.com/arfaouiahmed1/PitWall-ML/blob/main/artifacts/champion/splits.json) · [Dashboard](https://arfaouiahmed1.github.io/PitWall-ML/)
</details>

<p><img src="assets/stacks/pitwall.png" alt="Python, Polars, FastAPI, Prometheus, Grafana" width="500"></p>

`Python` `Polars` `LightGBM` `FastAPI` `WebSockets` `Prometheus`

### [SignalRank](https://github.com/arfaouiahmed1/signalrank)

<p>
  <a href="https://github.com/arfaouiahmed1/signalrank"><img src="assets/links/source.png" alt="SignalRank source code" width="190"></a>
  <a href="https://arfaouiahmed1.github.io/signalrank/"><img src="assets/links/demo.png" alt="SignalRank live demo" width="190"></a>
</p>
**A retrieval and ranking workbench for matching CVs to jobs.**

SignalRank keeps the search stages explicit: BM25 and PostgreSQL full-text retrieval sit beside pgvector search; reciprocal rank fusion combines candidate lists; an optional cross-encoder can rerank them; precision, recall, MRR, and nDCG make the trade-offs measurable.

<details>
<summary><strong>Architecture map</strong></summary>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/architecture-signalrank-dark.png">
  <img src="assets/architecture-signalrank-light.png" alt="SignalRank — particles and layered sieves, illustrating retrieval and relevance." width="100%">
</picture>

```mermaid
flowchart TD
  Q[CV query] --> L[BM25 and PostgreSQL full-text]
  Q --> V[pgvector retrieval]
  L --> RRF[Reciprocal rank fusion]
  V --> RRF
  RRF --> CE{Cross-encoder enabled?}
  CE -->|Yes| R[Rerank candidates]
  CE -->|No| F[Fused ranking]
  R --> E[Relevance evaluation]
  F --> E
```

[Retrieval code](https://github.com/arfaouiahmed1/signalrank/blob/main/backend/app/retrieval/hybrid.py) · [Evaluation artifact](https://github.com/arfaouiahmed1/signalrank/blob/main/artifacts/metrics.json) · [Demo](https://arfaouiahmed1.github.io/signalrank/)
</details>

<p><img src="assets/stacks/signalrank.png" alt="Python, FastAPI, PostgreSQL, React" width="400"></p>

`Python` `FastAPI` `PostgreSQL` `pgvector` `Sentence Transformers` `React`

## 03 / Evidence over decoration

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/evidence-dark.png">
  <img src="assets/evidence-light.png" alt="Evidence — a dithered prism and open frames, an editorial illustration of measurement and calibration." width="100%">
</picture>

These are the results supported by the committed artifacts and scoped project evaluations:

| Evidence | Recorded result | Scope |
| :--- | :--- | :--- |
| **PitWall ML** | **1.27 s MAE** across **3,931 test laps** | Committed champion metrics artifact |
| **PitWall ML** | **58.4% raw → 78.6% calibrated coverage** | Nominal 80% interval; calibration widens mean interval from **1.20 s → 2.26 s** |
| **SignalRank** | **500 jobs / qrels** with P@K, recall, MRR, and nDCG comparisons | Weak relevance labels; one committed evaluation artifact |
| **Open Web Catcher** | **126 runs · 97.6% tool-call success · $0.152 average persisted-run cost** | Internship/project evaluation reported in résumé |

Calibration is a product decision as much as a modeling step: coverage moves toward the target, but the interval gets wider. Retrieval metrics are treated as an experiment, not a universal claim; the SignalRank artifact explicitly uses weak labels and keeps cross-encoder results separate.

<details>
<summary><strong>PitWall calibration: coverage and interval width</strong></summary>

```mermaid
xychart-beta
  title "Test coverage: nominal target 80%"
  x-axis [Raw, Calibrated]
  y-axis "Coverage (%)" 0 --> 100
  bar [58.4, 78.6]
```

```mermaid
xychart-beta
  title "The cost of higher coverage"
  x-axis [Raw, Calibrated]
  y-axis "Mean interval width (seconds)" 0 --> 3
  bar [1.20, 2.26]
```

Same committed champion artifact; **3,931 test laps**. Higher coverage comes with wider intervals. [Source metrics](https://github.com/arfaouiahmed1/PitWall-ML/blob/main/artifacts/champion/metrics.json).

</details>

## 04 / Earlier data science & creative engineering

### [FarmWise](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3) · Agricultural data science
**Computer vision, predictive models, and retrieval-assisted farming support in one collaborative project.**

FarmWise brings several data science problems into the same agricultural platform: identifying plant disease, separating weeds and crops in images, analyzing field imagery, recommending crops, predicting yield, and retrieving treatment guidance. The web experience connects **Next.js / TypeScript** with **Django REST**.

- **Computer vision:** YOLOv8-based plant-disease detection and weed/crop segmentation, alongside ResNet disease-classification experiments and satellite-imagery work. The weed notebook trains **YOLOv8l-seg** and compares initial and fine-tuned predictions.
- **Dataset engineering:** checks for corrupted images, image/label mismatches, empty annotations, segmentation geometry, and class imbalance; augmentation, prediction inspection, and ONNX export steps are part of the notebook workflow.
- **Predictive modeling:** a scikit-learn **Random Forest** crop-classification pipeline and **CatBoost** yield-regression work, with a Random Forest fallback in the training script. Soil, weather, crop, and farming inputs connect the models to practical decisions.
- **Farming support with RAG:** Mistral and Gemma work for agricultural assistance. The committed **Gemma** experiment embeds disease/treatment records with Sentence Transformers, retrieves them through **FAISS**, and compares retrieval-assisted answers with LLM-only answers.

The breadth here is the engineering story: preparing data, training different model families, inspecting predictions, and bringing the results into a shared application. The RAG notebook's similarity comparison is an experiment, not a measure of treatment correctness.

<p>
  <a href="https://youtu.be/Dbv44AOnYsQ"><img src="assets/links/video.png" alt="FarmWise product video" width="190"></a>
  <a href="https://youtu.be/bAqBds2t3mg"><img src="assets/links/video.png" alt="FarmWise technical demo" width="190"></a>
  <a href="https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3"><img src="assets/links/source.png" alt="FarmWise source code" width="190"></a>
</p>

<sub>Videos: product overview · technical demo</sub>

[Training notebooks](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3/tree/main/Notebooks) · [Predictive-model code](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3/tree/main/Models/ml_models)

<p><img src="assets/stacks/farmwise.png" alt="Python, YOLOv8, PyTorch, scikit-learn, CatBoost, Gemma, Django REST" width="700"></p>

`Python` `YOLOv8` `PyTorch` `scikit-learn` `CatBoost` `Gemma` `FAISS` `Next.js` `Django`

### [NEWSBOT AI](https://github.com/arfaouiahmed1/NewBot-AI) · News analysis & NLP
**An earlier exploration of retrieval, language models, and explainable news analysis.**

My [portfolio case study](https://ahmed-arfaoui-portfolio.vercel.app/projects) documents semantic search with **FAISS / Sentence Transformers**, **FLAN-T5 and Mistral**, LoRA fine-tuning, sentiment and bias analysis, forecasting, and explanations with **LIME / SHAP**.

The public repository contains the **React / TypeScript** application: a news dashboard, article deep dives, alternative-perspective views, trends, and scenario displays. Its assistant integrates **Gemini**, streams responses, enables **Google Search grounding**, and renders the returned source links. The dashboard articles and forecast scenarios use sample data; the broader training and explainability work is documented in the portfolio rather than shipped in this repository.

<p>
  <a href="https://github.com/arfaouiahmed1/NewBot-AI"><img src="assets/links/source.png" alt="NewsBot source code" width="190"></a>
  <a href="https://ahmed-arfaoui-portfolio.vercel.app/projects"><img src="assets/links/portfolio.png" alt="NewsBot case study" width="190"></a>
</p>

[Assistant implementation](https://github.com/arfaouiahmed1/NewBot-AI/blob/main/components/GlobalAssistant.tsx)

<p><img src="assets/stacks/newsbot.png" alt="React, TypeScript, Gemini API" width="300"></p>

`React` `TypeScript` `Gemini API` `Streaming responses` `Search grounding`

### [Personal portfolio](https://ahmed-arfaoui-portfolio.vercel.app) · Interface engineering & visual storytelling

<p><img src="assets/stacks/portfolio.png" alt="Next.js, React, TypeScript, Node.js" width="400"></p>
**A place for the projects, the route into engineering, and the photography alongside it.**

Built with **Next.js, React, and TypeScript**, the portfolio combines project case studies, internship experience, a personal journey, and a photography gallery. Custom responsive layouts and a scroll-driven motion system give the site its visual character; reduced-motion support and progressive enhancement keep the content accessible when motion is disabled or unavailable.

<p>
  <a href="https://ahmed-arfaoui-portfolio.vercel.app"><img src="assets/links/portfolio.png" alt="Portfolio" width="190"></a>
  <a href="https://ahmed-arfaoui-portfolio.vercel.app/photography"><img src="assets/links/photography.png" alt="Photography" width="190"></a>
  <a href="https://github.com/arfaouiahmed1/ahmed-arfaoui-portfolio"><img src="assets/links/source.png" alt="Source" width="190"></a>
</p>

## 05 / How the systems fit together

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/timeline-dark.png">
  <img src="assets/timeline-light.png" alt="The Throughline — a continuous strand resolving from raw particles into an engineered lattice." width="100%">
</picture>

The recurring loop is simple to state and difficult to fake:

**Messy input becomes structured evidence. Models and agents turn that evidence into decisions; evaluation and inspectable delivery make the result useful.**

That loop appears in different forms across the portfolio:

- **Open Web Catcher:** pages become browser evidence, then agent decisions and operator traces.
- **HuntFlow:** job sources become provenance-preserving records, then retrieved context and reviewable drafts.
- **SignalRank:** a CV becomes lexical/vector candidates, then a fused ranking with relevance metrics.
- **PitWall ML:** timing data becomes temporally split features, then calibrated forecasts and simulation outputs.
- **FarmWise:** field images and agricultural records become vision predictions, crop/yield estimates, and retrieved farming guidance.
- **NEWSBOT AI:** news context becomes assistant responses with inspectable grounding sources.

## 06 / Technical focus

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/evaluation-dark.png">
  <img src="assets/evaluation-light.png" alt="Engineering Judgment — contrasting dithered specimens within a common frame, illustrating comparison and inspection." width="100%">
</picture>

**Languages & runtimes**

<p><img src="assets/stacks/languages.png" alt="Python, JavaScript, TypeScript, Node.js, Java, Jupyter" width="600"></p>

**Machine learning & data**

<p><img src="assets/stacks/machine-learning.png" alt="PyTorch, scikit-learn, YOLOv8, CatBoost, Polars, Gemma, Mistral" width="700"></p>

LightGBM

**Agents, retrieval & browser automation**

<p><img src="assets/stacks/agents-retrieval.png" alt="LangGraph, LangChain, Playwright, Gemini API" width="400"></p>

FAISS · Sentence Transformers

**APIs & persistence**

<p><img src="assets/stacks/backend.png" alt="FastAPI, Django REST, PostgreSQL, SQLite, Spring Boot" width="500"></p>

pgvector

**Interfaces, infrastructure & delivery**

<p><img src="assets/stacks/delivery.png" alt="Next.js, React, Docker, Azure, Prometheus, Grafana, Git, GitHub Actions" width="800"></p>

| Area | What I actually build |
| :--- | :--- |
| **Agent systems** | LangGraph state machines, bounded handoffs, role-scoped tools, browser automation, checkpoints, cancellation, human approval |
| **Retrieval & ranking** | BM25, PostgreSQL full-text search, pgvector, reciprocal rank fusion, optional cross-encoders, ablations, relevance metrics |
| **Computer vision & applied data science** | YOLOv8 segmentation, disease-classification experiments, image/annotation validation, augmentation, crop classification, yield regression |
| **NLP & AI interfaces** | Retrieval-assisted question answering, streamed model responses, search grounding, source presentation, news-analysis interfaces |
| **Predictive ML** | Polars feature engineering, LightGBM, physics-plus-residual models, temporal/session splits, conformal calibration, error analysis |
| **Backend & delivery** | FastAPI, PostgreSQL / SQLite, Docker, WebSockets, Azure Service Bus, Prometheus/Grafana, Next.js / React interfaces |
| **Engineering quality** | Evidence records, reproducible artifacts, leakage tests, rate limits, circuit breakers, fallbacks, cost and token telemetry |

## 07 / GitHub stats

<!-- github-stats:start -->
<img src="assets/github-cover.png" alt="Code in Public — dithered open frames with a cobalt orbit." width="100%">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github-stats-dark.png">
  <img src="assets/github-stats-light.png" alt="9 public repositories, 4 stars received; primary languages: Jupyter Notebook: 2 repos, Kotlin: 2 repos, Python: 2 repos, TypeScript: 2 repos, CSS: 1 repos." width="100%">
</picture>

<sub>Public owned repositories · primary-language counts · updated 2026-09-21 · [Data](docs/github-stats.json)</sub>
<!-- github-stats:end -->

## 08 / Current direction

I am looking for AI/ML engineering work where the interesting problems are at the boundary: agents that need guardrails, retrieval that needs honest evaluation, and models that have to become dependable services.

<p>
  <a href="https://ahmed-arfaoui-portfolio.vercel.app"><img src="assets/links/portfolio.png" alt="Portfolio" width="190"></a>
  <a href="https://www.linkedin.com/in/ahmedarfaoui99/"><img src="assets/links/linkedin.png" alt="Linkedin" width="190"></a>
  <a href="resume/Ahmed-Arfaoui-AI-ML-Engineer-Resume.pdf"><img src="assets/links/resume.png" alt="Download résumé" width="190"></a>
  <a href="mailto:ahmedarfaoui2000@gmail.com"><img src="assets/links/email.png" alt="Email" width="190"></a>
</p>

<sub>Visual system: raster dither-print geometry, restrained cobalt / vermilion accents, condensed display type, and a shared editorial grid. All project claims above are grounded in the linked repositories, committed artifacts, résumé, or portfolio source.</sub>
