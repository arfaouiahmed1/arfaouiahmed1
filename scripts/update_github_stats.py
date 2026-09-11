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

def render(data, theme):
    repos, langs, stars = summarize(data)
    light = theme == 'light'
    paper, ink, muted, rule = ('#f2efe6', '#20201f', '#60615e', '#cecac0') if light else ('#20201f', '#f2efe6', '#b5b4ad', '#454641')
    colors = ['#2055ca', '#ec5a36', '#52786d', '#8a79a3', '#a5824b', '#687c99']
    extra_rows = max(0, (min(len(langs), 6) + 1)//2 - 3)
    h = 670 + extra_rows*50
    im = Image.new('RGB', (1400, h), paper)
    d = ImageDraw.Draw(im)
    # Decorative ink pattern, separated from the measured marks.
    rng = random.Random(27)
    for _ in range(1200):
        x, y = rng.randrange(1110, 1350), rng.randrange(32, 108)
        if rng.random() < (x-1110)/300:
            d.rectangle((x,y,x+1,y+1), fill=muted)
    d.text((52,35), 'PUBLIC CODE / GITHUB', font=font(55, True), fill=ink)
    d.line((52,115,1348,115), fill=rule, width=2)
    for x, value, label in [(52,len(repos),'PUBLIC REPOSITORIES'),(500,stars,'STARS RECEIVED'),(948,len(langs),'PRIMARY LANGUAGES')]:
        d.text((x,140),str(value).zfill(2),font=font(88,True),fill=ink)
        d.text((x,247),label,font=font(21,mono=True),fill=muted)
    d.line((52,302,1348,302),fill=rule,width=2)
    d.text((52,325),'REPOSITORY LANGUAGE MIX',font=font(27,True),fill=ink)
    classified=sum(n for _,n in langs)
    top=langs[:5]
    if len(langs)>5:
        top.append(('Other',sum(n for _,n in langs[5:])))
    x=52
    for i,(name,count) in enumerate(top):
        w=1296*count/max(classified,1)
        d.rectangle((round(x),383,round(x+w)-3,410),fill=colors[i])
        x+=w
        lx=52+(i%2)*665
        ly=438+(i//2)*49
        d.rectangle((lx,ly+7,lx+14,ly+21),fill=colors[i])
        text=f'{name}  {count} / {classified}  ({count/max(classified,1):.1%})'
        d.text((lx+29,ly),text,font=font(23),fill=ink)
    d.line((52,h-94,1348,h-94),fill=rule,width=2)
    unknown=len(repos)-classified
    d.text((52,h-75),f'PRIMARY LANGUAGE PER REPO / {unknown} UNCLASSIFIED / FORKS EXCLUDED',font=font(18,mono=True),fill=muted)
    d.text((52,h-44),f"GITHUB REST METADATA / UPDATED {data['observed_on']} UTC",font=font(18,mono=True),fill=muted)
    im.save(ROOT/f'assets/github-stats-{theme}.png',optimize=True)

def update_readme(data):
    repos,langs,stars=summarize(data)
    body='''<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/github-stats-dark.png">
  <img src="assets/github-stats-light.png" alt="GitHub public repository totals and primary-language distribution; exact figures follow." width="100%">
</picture>

<details>
<summary>Stats, scope, and source</summary>

'''
    body+=f"Updated **{data['observed_on']} UTC** · **{len(repos)} public repositories** · **{stars} stars received** · **{len(langs)} primary languages**.\n\n"
    body+='| Primary language | Repositories |\n| :--- | ---: |\n'
    for name,n in langs:
        body+=f'| {name} | {n} |\n'
    body+=f"| Not classified | {len(repos)-sum(n for _,n in langs)} |\n\n"
    body+='Language proportions count repositories with a GitHub-assigned primary language. They do not measure coding time, language bytes, or proficiency. Public owned repositories are included across the account; forks and private repositories are excluded.\n\n[Source snapshot](docs/github-stats.json) · [Refresh workflow](.github/workflows/github-stats.yml)\n\n</details>'
    path=ROOT/'README.md'
    old=path.read_text()
    updated,n=re.subn(r'<!-- github-stats:start -->.*?<!-- github-stats:end -->',lambda _: '<!-- github-stats:start -->\n'+body+'\n<!-- github-stats:end -->',old,flags=re.S)
    if n!=1:
        raise ValueError('Expected exactly one stats block')
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
