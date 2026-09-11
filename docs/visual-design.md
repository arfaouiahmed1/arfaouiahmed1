# Dither editorial system

Updated 2026-09-10. The approved `assets/header-dither.png` masthead is preserved unchanged. Its condensed lettering, ivory paper, charcoal ink, cobalt traces, and restrained vermilion accents establish the visual identity throughout the profile.

## Artwork and typography

The 22 light/dark replacement PNGs are individually created with the built-in image-generation tool, using the approved masthead as a visual reference. They are original raster compositions, not conversions of the old SVG plates. Each pair shares a subject and type hierarchy, with separate light and dark compositions. The paper grain and stochastic dithering belong to the artwork; no animation, remote font, or widget is required.

Display lettering is deliberately condensed and monumental. Small monospaced labels describe each theme. Exact dates, metrics, project claims, and links stay in Markdown so they remain selectable and readable on small screens.

## Asset inventory

| Pair | Editorial subject | Role |
| :--- | :--- | :--- |
| `header-{light,dark}.png` | Ahmed Arfaoui and a computational knot | Companion mastheads; the original approved masthead remains the README lead |
| `journey-{light,dark}.png` | Fragmented ribbon becoming an open geometric loop | Personal journey section |
| `internships-{light,dark}.png` | Four distinct computational specimens | Four internship disciplines |
| `systems-{light,dark}.png` | Suspended planes, chain, surface, and sieve | Core systems overview |
| `evidence-{light,dark}.png` | Prism and open frames | Measurement and calibration |
| `architecture-owc-{light,dark}.png` | Floating pages and globe | Browser-intelligence project artwork |
| `architecture-huntflow-{light,dark}.png` | Folded chain and document layers | Human-guided workflow project artwork |
| `architecture-pitwall-{light,dark}.png` | Aerodynamic ribbon and particulate field | Forecasting and uncertainty project artwork |
| `architecture-signalrank-{light,dark}.png` | Particles and perforated plates | Retrieval and relevance project artwork |
| `timeline-{light,dark}.png` | Continuous strand becoming an engineered lattice | The common thread across the projects; distinct from the journey artwork |
| `evaluation-{light,dark}.png` | Contrasting specimens inside a common frame | Engineering judgment and technical focus |

There are **22 replacement images**, plus the two retained generated assets `header-dither.png` and `dither-field.png`: **24 PNGs in total**. No SVG files are shipped. The README uses GitHub `<picture>` elements for theme selection.

## Art versus engineering evidence

The project illustrations are conceptual covers. They do not encode architecture topology, dates, or measured data. The README supplies separate Mermaid architecture maps, Markdown experience tables, and sourced calibration charts. This keeps exact relationships and numbers independent of image generation.

Architecture maps are compact views based on the repository audit. SignalRank explicitly branches into lexical and vector retrieval before reciprocal rank fusion. Optional reranking is shown as optional. The maps omit many internal calls and are not exhaustive runtime traces.

The PitWall charts report the same committed champion artifact: 3,931 test laps, 58.4% raw and 78.6% calibrated coverage against a nominal 80% interval, with mean widths 1.20 s and 2.26 s. These are artifact-specific results, not claims about every model implementation in the repository. SignalRank retains its weak-label and single-CV evaluation caveat.

## Provenance and maintenance

`image-generation.json` records the built-in generation prompt for every replacement, the generated source filename, and the published PNG hash. PNGs are resized and palette-optimized for GitHub after generation; their composition is not reconstructed with a vector renderer.

Preserve the approved masthead when revising the set. Recheck `visual-data.json`, `profile-audit.md`, and the linked source repositories before changing technical claims. Keep the 22 replacement filenames stable and maintain both themes.
