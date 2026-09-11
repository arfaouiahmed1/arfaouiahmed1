# Profile editorial audit

Reviewed 2026-09-10; earlier-project audit expanded 2026-09-11. Scope: the account's public repositories, the supplied résumé, and the public portfolio source. The README is an editorial portfolio, not a production-readiness certification. Claims are limited to code, committed artifacts, and supplied experience evidence.

## Positioning decision

The profile presents Ahmed Arfaoui as an **AI/ML Engineer** building agentic systems, retrieval/ranking pipelines, predictive ML, and the backend surfaces that make those systems inspectable. Education is part of the journey, but the page leads with systems and engineering practice rather than student identity.

## Selection and pin-order recommendation

| Order | Repository | Decision |
| :--- | :--- | :--- |
| 1 | [Open-Web-Catcher](https://github.com/arfaouiahmed1/Open-Web-Catcher) | Lead: browser-agent orchestration, bounded specialist roles, evidence capture, and operator tooling. |
| 2 | [huntflow](https://github.com/arfaouiahmed1/huntflow) | Feature: local-first product with source ingestion, provenance, retrieval, durable workflows, and human review. |
| 3 | [PitWall-ML](https://github.com/arfaouiahmed1/PitWall-ML) | Feature: predictive ML, uncertainty calibration, serving, simulation, and monitoring. |
| 4 | [signalrank](https://github.com/arfaouiahmed1/signalrank) | Feature: focused information-retrieval workbench with explicit ablations and relevance metrics. |
| 5 | [Data-Farmers-FarmWise-4DS3](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3) | Dedicated agricultural data science case study: YOLOv8 segmentation, disease experiments, tabular modeling, Gemma/FAISS RAG, and two repository-linked videos. |
| 6 | [pursivo](https://github.com/arfaouiahmed1/pursivo) | Supporting native Android engineering with Room persistence, evidence storage, and optional AI adapters; label alpha. |
| — | RepForge | Omit from feature set: the ML engine still contains TODO inference and simulated calibration. |
| 7 | [NewBot-AI](https://github.com/arfaouiahmed1/NewBot-AI) | Include as NEWSBOT AI: earlier NLP work documented in the portfolio, plus a public React/TypeScript prototype with a real Gemini streaming/search-grounding integration. Distinguish sample dashboard data from model outputs. |
| — | Stage | Omit: placeholder repository material. |
| — | ahmed-arfaoui-portfolio | Include as interface engineering and visual storytelling: responsive case studies, journey, photography, and an inspected motion implementation with reduced-motion support. |

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

- **FarmWise:** expanded beyond the initial deployment-only review. Inspected the weed-detection notebook (YOLOv8l-seg training/fine-tuning, dataset checks, prediction comparisons, ONNX export); the smaller disease notebook (ResNet experiments); the Gemma treatment notebook (Sentence Transformers, FAISS, retrieved disease/treatment records, RAG-versus-LLM cosine-similarity experiment); and Random Forest crop / CatBoost yield scripts. The root README and user's clarification support YOLOv8 plant-disease work. Mistral is supplied in the user's project description; the inspected committed RAG notebook specifically uses Gemma. No real-time FPS, accuracy, mAP, crop-yield improvement, or RAG-document-count claims are added without aligned evaluation evidence. Deployment fallbacks remain relevant to reliability claims.
- **NEWSBOT AI:** corrected the initial omission. `App.tsx`, `constants.ts`, `pages/Dashboard.tsx`, `pages/DeepDive.tsx`, and `components/GlobalAssistant.tsx` establish the public implementation: React/TypeScript views and sample datasets, plus Gemini chat creation, streamed responses, Google Search tooling, and grounding-source rendering. The portfolio's `app/content.ts` describes FAISS, FLAN-T5, Mistral, LoRA, LIME/SHAP, sentiment/bias analysis, and forecasting. These broader capabilities are attributed to the portfolio case study, not claimed to be implemented in the public UI repository.
- **Personal portfolio:** inspected `package.json`, `app/projects/page.tsx`, `app/content.ts`, and `app/components/MotionSystem.tsx`. Next.js/React/TypeScript, case-study pages, photography assets, scroll-driven CSS progress, IntersectionObserver reveals, and reduced-motion/progressive-enhancement paths are present. No three.js, GSAP, or Framer Motion claim is made.
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

## Additional evidence for the earlier projects

- FarmWise root README links both the [product video](https://youtu.be/Dbv44AOnYsQ) and [technical demo](https://youtu.be/bAqBds2t3mg). YouTube content could not be fetched during this review; no viewing claim or timing/performance measurement is based on those videos.
- User's 2026-09-11 clarification identifies FarmWise as data science work and supplies a FarmValley-branded description of YOLOv8 weed/crop segmentation and Mistral/Gemma RAG. The profile keeps the repository's FarmWise name and includes the supplied capabilities with the implementation distinction above.
- [Weed training notebook](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3/blob/main/Notebooks/Weed%20Detection/weed-detection.ipynb)
- [Gemma RAG notebook](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3/blob/main/Notebooks/Treatment%20Recommendation/gemma.ipynb)
- [Crop and yield model scripts](https://github.com/arfaouiahmed1/Data-Farmers-FarmWise-4DS3/tree/main/Models/ml_models)
- [NewsBot assistant](https://github.com/arfaouiahmed1/NewBot-AI/blob/main/components/GlobalAssistant.tsx)
- [Portfolio case-study content](https://github.com/arfaouiahmed1/ahmed-arfaoui-portfolio/blob/main/app/content.ts)
- [Portfolio motion system](https://github.com/arfaouiahmed1/ahmed-arfaoui-portfolio/blob/main/app/components/MotionSystem.tsx)
