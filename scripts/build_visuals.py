"""Rebuild profile SVG diagrams and evaluation plots: python scripts/build_visuals.py.

Requires matplotlib. Metrics are the reviewed repository snapshots in docs/visual-data.json.
Diagrams show simplified subsystem relationships, not exhaustive runtime call graphs.
"""
from pathlib import Path
import json
from html import escape
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'docs/visual-data.json').read_text())
ASSETS = ROOT / 'assets'
PALETTES = {
 'light': dict(bg='#f1f0e9', fg='#202426', muted='#5e6567', line='#c5c8c3', accent='#b74520', box='#fafaf6'),
 'dark': dict(bg='#16191c', fg='#f1f0e9', muted='#adb3b5', line='#454d50', accent='#ff926b', box='#1d2327'),
}

def svg_start(title, subtitle, p, height=430):
 return [f'<svg xmlns="http://www.w3.org/2000/svg" width="900" height="{height}" viewBox="0 0 900 {height}" role="img" aria-labelledby="title desc">',
 f'<title id="title">{escape(title)}</title><desc id="desc">{escape(subtitle)}</desc>',
 f'<rect width="900" height="{height}" fill="{p["bg"]}"/>',
 f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10" fill="{p["muted"]}"/></marker></defs>',
 '<style>.signal{stroke-dasharray:5 14;animation:flow 5s linear infinite}@keyframes flow{to{stroke-dashoffset:-76}}@media(prefers-reduced-motion:reduce){.signal{animation:none}}</style>',
 f'<text x="32" y="43" fill="{p["fg"]}" font-family="DejaVu Sans,Arial,sans-serif" font-size="24" font-weight="bold">{escape(title)}</text>',
 f'<text x="32" y="71" fill="{p["muted"]}" font-family="DejaVu Sans,Arial,sans-serif" font-size="15">{escape(subtitle)}</text>']

def box(parts, p, x, y, title, subtitle, focus=False):
 parts += [f'<rect x="{x}" y="{y}" width="230" height="88" fill="{p["box"]}" stroke="{p["accent"] if focus else p["line"]}" stroke-width="1.5"/>',
 f'<text x="{x+16}" y="{y+35}" fill="{p["fg"]}" font-family="DejaVu Sans,Arial,sans-serif" font-size="20" font-weight="bold">{escape(title)}</text>',
 f'<text x="{x+16}" y="{y+63}" fill="{p["muted"]}" font-family="DejaVu Sans,Arial,sans-serif" font-size="14">{escape(subtitle)}</text>']

def edge(parts,p,path,animated=False,dashed=False):
 parts.append(f'<path d="{path}" fill="none" stroke="{p["muted"]}" stroke-width="1.5" marker-end="url(#arrow)"'+(' stroke-dasharray="5 5"' if dashed else '')+'/>')
 if animated:
  parts.append(f'<path class="signal" d="{path}" fill="none" stroke="{p["accent"]}" stroke-width="2.5"/>')

def diagram(kind,theme,p):
 specs={
 'owc':('01 / OPEN WEB CATCHER','Service architecture · animated lines illustrate requests, not live activity.',[
 ('Operator console','Next.js · run inspection'),('Backend','FastAPI · run control'),('Run storage','SQL · traces & evidence'),
 ('Specialist agents','LangGraph · bounded roles'),('Browser tools','Playwright · MCP'),('Target pages','Chromium · isolated context')]),
 'huntflow':('02 / HUNTFLOW','Two connected paths: source ingestion and supervised AI work.',[
 ('Job sources','ATS feeds & public boards'),('Crawler sidecar','Rate limits · circuit breaker'),('Local records','SQLite · provenance'),
 ('Evidence vault','BM25 + vectors · RRF'),('Agent workflows','LangGraph · checkpoints'),('Human review','Inspect · approve / revise')]),
 'pitwall':('03 / PITWALL ML','Training and serving · calibration uses held-out validation predictions.',[
 ('Race data','Timing · telemetry'),('Features & splits','Polars · session boundaries'),('Pace models','LightGBM · residual model'),
 ('Dashboard & API','FastAPI · WebSockets'),('Forecasts & strategy','Intervals · Monte Carlo'),('Calibration','Held-out validation set')]),
 'signalrank':('04 / SIGNALRANK','Candidate generation branches, then fusion and optional reranking.',[
 ('CV / query','Candidate profile text'),('Lexical retrieval','BM25 / PostgreSQL FTS'),('Vector retrieval','Embeddings · pgvector'),
 ('Ranked results','P@K · MRR · nDCG'),('Cross-encoder','Optional · fallback to RRF'),('Rank fusion','Reciprocal rank fusion')]),
 }
 title,sub,nodes=specs[kind]; a=svg_start(title,sub,p)
 if kind=='owc':
  routes=[('M262 156H335',True),('M565 156H638',False),('M450 200V222H147V248',False),('M262 292H335',True),('M565 292H638',True)]
  footer='Console → API → orchestration → browser execution; run artifacts persist in SQL.'
 elif kind=='huntflow':
  routes=[('M262 156H335',True),('M565 156H638',False),('M753 200V224H450V248',False),('M262 292H335',True),('M565 292H638',False)]
  footer='Job context + retrieved evidence feed workflows; SQLite also stores checkpoints.'
 elif kind=='pitwall':
  routes=[('M262 156H335',False),('M565 156H638',True),('M753 200V248',False),('M638 292H565',True),('M335 292H262',False)]
  footer='Drift monitoring checks feature distributions; calibration measures interval coverage.'
 else:
  routes=[('M262 156H335',True),('M147 112V94H753V112',True),('M450 200V222H715V248',False),('M753 200V248',False),('M638 292H565',True),('M335 292H262',False)]
  footer='The cross-encoder is optional: unavailable models fall back to fused rank order.'
 for path,animated in routes: edge(a,p,path,animated)
 for i,(name,desc) in enumerate(nodes):box(a,p,32+(i%3)*303,112+(i//3)*136,name,desc,focus=i in [1,4])
 a.append(f'<path d="M32 373H868" stroke="{p["line"]}"/><text x="32" y="403" fill="{p["muted"]}" font-family="DejaVu Sans,Arial,sans-serif" font-size="14">{escape(footer)}</text></svg>')
 (ASSETS/f'architecture-{kind}-{theme}.svg').write_text('\n'.join(a))

def timeline(theme,p):
 a=svg_start('PROJECT CHRONOLOGY','Repository creation dates · milestones in the public code portfolio, not completion dates.',p,650)
 names={'Data-Farmers-FarmWise-4DS3':('FarmWise','Applied ML & computer vision'),'Open-Web-Catcher':('Open Web Catcher','Browser agents & evidence collection'),'pursivo':('Pursivo','Native Android & optional AI'),'huntflow':('HuntFlow','Local-first AI application workflows'),'signalrank':('SignalRank','Retrieval & relevance evaluation'),'PitWall-ML':('PitWall ML','Forecasting & uncertainty calibration')}
 a.append(f'<path d="M233 119V559" stroke="{p["line"]}" stroke-width="2"/>')
 for i,item in enumerate(DATA['timeline']):
  y=123+i*87; name,desc=names[item['repo']]
  a += [f'<circle cx="233" cy="{y}" r="5" fill="{p["accent"]}"/>',f'<text x="32" y="{y+6}" fill="{p["muted"]}" font-family="DejaVu Sans Mono,monospace" font-size="19">{item["created_at"][:10]}</text>',f'<text x="266" y="{y+5}" fill="{p["fg"]}" font-family="DejaVu Sans,Arial,sans-serif" font-size="24" font-weight="bold">{name}</text>',f'<text x="266" y="{y+32}" fill="{p["muted"]}" font-family="DejaVu Sans,Arial,sans-serif" font-size="17">{escape(desc)}</text>']
 a.append(f'<text x="32" y="622" fill="{p["muted"]}" font-family="DejaVu Sans Mono,monospace" font-size="13">SOURCE / GitHub repository metadata · observed 2026-09-10 · spacing is ordinal</text></svg>')
 (ASSETS/f'timeline-{theme}.svg').write_text('\n'.join(a))

def evaluation(theme,p):
 # Contract: compare raw/calibrated coverage and width for one committed run.
 # Two conditions are the full artifact; no temporal trend is inferred.
 # Bars start at zero; direct values + target line distinguish the series.
 m=DATA['pitwall']
 plt.rcParams.update({'font.family':'DejaVu Sans','svg.fonttype':'path','font.size':12})
 fig,axes=plt.subplots(1,2,figsize=(12,4.8),gridspec_kw={'wspace':.5})
 fig.patch.set_facecolor(p['bg'])
 fig.subplots_adjust(left=.16,right=.93,bottom=.26,top=.65)
 fig.text(.035,.91,'PITWALL / CALIBRATION TRADE-OFF',fontsize=21,weight='bold',color=p['fg'])
 fig.text(.035,.83,'Committed champion run · 3,931 test laps · nominal interval coverage: 80%',fontsize=12,color=p['muted'])
 for ax,values,title,limit,fmt in [(axes[0],[100*m['coverage_80'],100*m['coverage_80_calibrated']],'Coverage (%)',100,'{:.1f}%'),(axes[1],[m['mean_width'],m['mean_width_calibrated']],'Mean interval width (s)',3,'{:.2f} s')]:
  ax.set_facecolor(p['bg']); ax.barh([1,0],values,height=.4,color=[p['line'],p['accent']])
  ax.set_yticks([1,0],['Raw','Calibrated']); ax.set_xlim(0,limit); ax.set_ylim(-.6,1.7)
  ax.set_title(title,loc='left',color=p['fg'],fontsize=14,pad=12)
  ax.tick_params(colors=p['muted'],length=0,pad=8); ax.grid(axis='x',color=p['line'],alpha=.45,linewidth=.6); ax.set_axisbelow(True)
  for s in ['top','left','right']:ax.spines[s].set_visible(False)
  ax.spines['bottom'].set_color(p['line'])
  for y,v in zip([1,0],values):ax.text(v+limit*.025,y,fmt.format(v),va='center',color=p['fg'],fontsize=12,weight='bold')
 axes[0].axvline(80,color=p['fg'],linestyle='--',linewidth=1)
 axes[0].text(80,1.45,'80% target',ha='center',fontsize=10,color=p['fg'])
 fig.text(.035,.105,'Coverage rises from 58.4% to 78.6%; mean interval width increases from 1.20 s to 2.26 s.',fontsize=12,color=p['fg'])
 fig.text(.035,.045,'SOURCE / PitWall-ML · artifacts/champion/metrics.json · snapshot 2026-09-10',fontsize=10,color=p['muted'])
 fig.savefig(ASSETS/f'evaluation-{theme}.svg',facecolor=p['bg'],metadata={'Date':None,'Title':'PitWall calibration: coverage and interval width'})
 plt.close(fig)

for theme,p in PALETTES.items():
 for kind in ['owc','huntflow','pitwall','signalrank']:diagram(kind,theme,p)
 timeline(theme,p);evaluation(theme,p)
print('Generated 12 SVG assets.')
