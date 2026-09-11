"""Render honest, reproducible GitHub metadata as local PNG cards."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import random
import re
from urllib.request import Request, urlopen
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OWNER = 'arfaouiahmed1'

def fetch_repositories():
    headers = {'Accept': 'application/vnd.github+json', 'User-Agent': 'profile-stats', 'X-GitHub-Api-Version': '2022-11-28'}
    if os.getenv('GH_TOKEN'):
        headers['Authorization'] = 'Bearer ' + os.environ['GH_TOKEN']
    repos = []
    page = 1
    while True:
        req = Request(f'https://api.github.com/users/{OWNER}/repos?type=owner&per_page=100&page={page}', headers=headers)
        with urlopen(req, timeout=30) as response:
            batch = json.load(response)
        if not isinstance(batch, list):
            raise ValueError('Unexpected GitHub response; preserving previous stats')
        for r in batch:
            if not r['private'] and not r['fork']:
                repos.append({'name': r['name'], 'url': r['html_url'], 'private': False, 'fork': False,
                              'stars': r['stargazers_count'], 'forks': r['forks_count'], 'language': r['language']})
        if len(batch) < 100:
            break
        page += 1
    return {'owner': OWNER, 'observed_on': datetime.now(timezone.utc).date().isoformat(), 'repos': sorted(repos, key=lambda r: r['name'].lower())}

def summarize(data):
    repos = [r for r in data['repos'] if not r['private'] and not r['fork']]
    langs = Counter(r['language'] for r in repos if r['language'])
    return repos, sorted(langs.items(), key=lambda x: (-x[1], x[0])), sum(r['stars'] for r in repos)

def font(size, bold=False, mono=False):
    name = 'DejaVuSansMono.ttf' if mono else ('DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf')
    for location in [f'/usr/share/fonts/truetype/dejavu/{name}', name]:
        try:
            return ImageFont.truetype(location, size)
        except OSError:
            pass
    return ImageFont.load_default(size=size)

def display_font(size):
    return ImageFont.truetype('/usr/share/fonts/opentype/urw-base35/NimbusSansNarrow-Bold.otf', size)

def render(data, theme):
    repos, langs, stars = summarize(data)
    light = theme == 'light'
    paper, ink, muted, rule = ('#f2efe6', '#20201f', '#62625c', '#c8c5bb') if light else ('#20201f', '#f2efe6', '#b8b6ac', '#494943')
    accent = '#2458d3' if light else '#8aa7ff'
    top = langs[:5]
    if len(langs)>5:
        top.append(('Other',sum(n for _,n in langs[5:])))
    h = 474 + max(1,len(top))*68
    im = Image.new('RGB', (1400,h), paper)
    d = ImageDraw.Draw(im)
    # Small print registration marks frame the data without decorating the marks.
    for x,y in [(25,25),(1375,25),(25,h-25),(1375,h-25)]:
        d.line((x-8,y,x+8,y),fill=muted,width=1)
        d.line((x,y-8,x,y+8),fill=muted,width=1)
    d.text((56,31),'GITHUB / OPEN SOURCE INDEX',font=font(21,mono=True),fill=muted)
    d.text((1010,31),data['observed_on']+' / UTC',font=font(21,mono=True),fill=muted)
    d.line((56,75,1344,75),fill=ink,width=2)
    for i,(value,label) in enumerate([(len(repos),'PUBLIC REPOSITORIES'),(stars,'STARS RECEIVED'),(len(langs),'PRIMARY LANGUAGES')]):
        x=56+i*444
        d.text((x,99),str(value).zfill(2),font=display_font(174),fill=ink,stroke_width=2)
        d.text((x+4,275),label,font=font(21,mono=True),fill=muted)
        if i<2:d.line((x+410,108,x+410,304),fill=rule,width=1)
    d.line((56,329,1344,329),fill=ink,width=2)
    d.text((56,345),'LANGUAGE / REPOSITORIES',font=display_font(34),fill=ink)
    d.text((1030,353),'SHARE OF REPOS',font=font(20,mono=True),fill=muted)
    classified=sum(n for _,n in langs)
    for i,(name,count) in enumerate(top):
        y=407+i*68
        d.text((56,y+2),str(i+1).zfill(2),font=font(20,mono=True),fill=accent)
        d.text((110,y),name,font=font(25,True),fill=ink)
        d.text((535,y+2),f'{count:02d} / {classified:02d}',font=font(23,mono=True),fill=muted)
        d.rectangle((725,y+3,1195,y+28),fill=rule)
        width=470*count/max(classified,1)
        if width:d.rectangle((725,y+3,725+round(width)-1,y+28),fill=accent if i==0 else ink)
        d.text((1230,y+1),f'{count/max(classified,1):.0%}',font=font(23,mono=True),fill=ink)
        d.line((56,y+49,1344,y+49),fill=rule,width=1)
    unknown=len(repos)-classified
    d.text((56,h-42),f'PRIMARY LANGUAGE PER REPO / {unknown} UNCLASSIFIED / FORKS EXCLUDED',font=font(18,mono=True),fill=muted)
    im.save(ROOT/f'assets/github-stats-{theme}.png',optimize=True)

def update_readme(data):
    repos,langs,stars=summarize(data)
    summary=f"{len(repos)} public repositories, {stars} stars received; primary languages: " + ', '.join(f'{name}: {n} repos' for name,n in langs)
    body=f'''<img src="assets/github-cover.png" alt="Code in Public — dithered open frames with a cobalt orbit." width="100%">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github-stats-dark.png">
  <img src="assets/github-stats-light.png" alt="{summary}." width="100%">
</picture>

<sub>Public owned repositories · primary-language counts · updated {data['observed_on']} · [Data](docs/github-stats.json)</sub>'''
    path=ROOT/'README.md'
    old=path.read_text()
    updated,n=re.subn(r'<!-- github-stats:start -->.*?<!-- github-stats:end -->',lambda _: '<!-- github-stats:start -->\n'+body+'\n<!-- github-stats:end -->',old,flags=re.S)
    if n!=1:raise ValueError('Expected exactly one stats block')
    path.write_text(updated)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--snapshot',type=Path);args=ap.parse_args()
    data=json.loads(args.snapshot.read_text()) if args.snapshot else fetch_repositories()
    if not data['repos']:
        raise ValueError('Refusing to replace stats with an empty response')
    for theme in ['light','dark']:
        render(data,theme)
    update_readme(data)
    (ROOT/'docs/github-stats.json').write_text(json.dumps(data,indent=2)+'\n')
    print(f"Updated {len(data['repos'])} public repository records")

if __name__=='__main__':
    main()
