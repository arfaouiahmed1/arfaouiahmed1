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

## Navigation and GitHub metadata — 2026-09-11

Eight individually generated PNG link banners extend the masthead typography to portfolio, LinkedIn, résumé, email, source code, live demos, video, and photography. See `link-generation.json` for source-image hashes and provenance. Primary calls to action use these reusable banners, with descriptive alternative text; supporting evidence links remain selectable text.

Eight technology tiles use the official Devicon glyphs, rendered as PNGs on the same ivory field. Sources: `https://github.com/devicons/devicon/tree/master/icons/{python,typescript,pytorch,scikitlearn,postgresql,fastapi,docker,nextjs}`. Devicon is MIT licensed; its license is retained in `devicon-LICENSE.txt`. Brand colors help recognition while the tile framing follows the profile palette.

Two deterministic light/dark stats PNGs report public owned repository totals, stars received, and primary-language repository counts. They are drawn from the GitHub REST snapshot in `github-stats.json`, never image-generated. The weekly GitHub Actions workflow refreshes the snapshot, both cards, and accessible README table. Language proportions exclude unclassified repositories from the denominator and do not claim proficiency or coding time. Accountwide totals include all public owned repositories, whether or not featured on the profile.

The complete inventory is now 42 PNGs: the original 24 editorial assets, eight link banners, eight technology tiles, and two stats cards. The approved name masthead remains unchanged. No SVG assets or animations are shipped.

### Stats editorial polish

The GitHub section now opens with an individually generated `github-cover.png` illustration: monumental CODE IN PUBLIC lettering, interlocking dither frames, cobalt orbit, and vermilion marker. Generation used the approved name masthead as its reference. The numerical panel uses Nimbus Sans Narrow Bold display numerals, monospaced annotations, registration marks, and a restrained cobalt/charcoal bar chart. Each bar reports the same denominator and a zero-to-100% track. The workflow installs `fonts-urw-base35` to preserve this typography on refresh. Both numerical themes remain deterministic and accessible through the accompanying table. Total PNG inventory: 43.

### Complete stack icon rows

The toolkit now covers 34 named technologies across five grouped rows and seven project-specific rows. All 12 new assets are static PNGs in `assets/stacks/`, with readable labels and descriptive alt text. Devicon provides official glyphs under the retained MIT license. Technologies without a supplied Devicon glyph use original typographic identifiers rather than invented official logos. See `stack-icons.json` for the inventory. Node.js is verified against HuntFlow's Node 22 engine requirement. Project text retains methodological concepts such as BM25, vector retrieval, and streaming separately from tool identities. Total PNG inventory: 55.
