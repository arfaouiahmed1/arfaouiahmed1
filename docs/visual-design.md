# Visual system and source notes

## Layout

Keep the main page readable as a professional introduction: one open architecture diagram, expandable subsystem diagrams, an evaluation figure, a dated project chronology and concise technical focus. The original geometric AA header anchors the identity.

Palette: warm paper / graphite with burnt orange as the only chromatic accent. Light and dark SVGs use matching typography and geometry. Diagram flow markers animate over five seconds; they illustrate data/request direction and are not live telemetry. `prefers-reduced-motion: reduce` disables movement. Static rendering retains every node, arrow and caption.

## Architecture sources

| Asset | Scope | Evidence |
| --- | --- | --- |
| architecture-owc | Simplified console, API, SQL, agent and browser subsystem relationships | Open-Web-Catcher: docs/wiki/Architecture.md; src/agents/orchestrator.py; tools/playwright/ |
| architecture-huntflow | Source ingestion and evidence-fed supervised workflows | huntflow: docs/ARCHITECTURE.md; src/lib/vault/search.ts; src/lib/agents/checkpointer.ts; scrapling-agent/rate_limiter.py |
| architecture-pitwall | Data/features, modeling, held-out calibration, forecast/simulation and serving | PitWall-ML: src/pitwall/models/pace/hybrid_model.py; src/pitwall/evaluation/calibration.py; src/pitwall/simulation/engine.py; README.md |
| architecture-signalrank | Lexical/vector branching, RRF, optional cross-encoder and ranked output | signalrank: backend/app/retrieval/bm25.py; hybrid.py; backend/app/rerank/cross_encoder.py |

These are subsystem diagrams, not exhaustive runtime traces. Return messages, authentication and most persistence writes are omitted for readability. The PitWall diagram represents model pipeline capabilities; its newer hybrid model does not inherit the older champion artifact's metrics.

## Chart contract

- Question: How does interval calibration change empirical coverage and mean interval width in the committed PitWall champion run?
- Takeaway: coverage moves from 58.4% toward the nominal 80% target, reaching 78.6%; the intervals widen from 1.20 s to 2.26 s.
- Family: comparison / benchmark. Two horizontal-bar panels, one for coverage (%), one for interval width (seconds). Both axes start at zero; a dashed reference marks 80% coverage.
- Grain: raw versus calibrated outputs of a single recorded run, 3,931 test laps. These are the two complete conditions in the source, not a time series; no extra observations are invented.
- Source: PitWall-ML/artifacts/champion/metrics.json, reviewed 2026-09-10. Corresponding splits are in artifacts/champion/splits.json. Raw fields are saved in visual-data.json. No training was rerun.
- Renderer: Matplotlib SVG export, font glyphs converted to paths for consistent GitHub rendering. Direct labels and fixed row order supplement neutral/orange fill.
- Surface: GitHub README image with theme-specific variants and a descriptive alt string carrying all values. Source artifact and calibration code are linked beside the figure.

## Timeline contract

The six timestamps are GitHub REST repository `created_at` values, captured 2026-09-10 and stored in visual-data.json. Dates are UTC. They describe repository creation, not first work, launch, public release, completion, employment or graduation. Equal row spacing shows chronological order rather than elapsed duration.

## Rebuild

Run `python scripts/build_visuals.py` from the repository after installing Matplotlib. This regenerates the eight architecture SVGs, two evaluation SVGs and two timeline SVGs. Headers remain separately editable SVGs. Review updated source facts before changing visual-data.json.

## Verification

Parsed every SVG as XML and checked README image references and expandable-section balance. Inspected exported light/dark visual previews for labels, arrows and chart scales. Metrics were compared with repository artifacts and dates with repository metadata. No project test suite or training pipeline was rerun for this presentation change.
