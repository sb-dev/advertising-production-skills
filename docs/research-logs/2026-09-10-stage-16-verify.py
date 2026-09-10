"""Verify Stage 16 design structure/data, not installed skills or campaign performance.

Run from a complete checkout at the Stage 16 completion commit:
  python3 docs/research-logs/2026-09-10-stage-16-verify.py --root . --final
For a partial local working copy, --known-paths may supply a verified remote
Git-tree JSON with a `files` path-to-blob mapping. This establishes path existence
only; it never claims that unmounted source contents were inspected locally.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import posixpath
import re
from fractions import Fraction
from pathlib import Path

PREFIX = 'docs/research-logs/'
DESIGN = PREFIX + '2026-09-10-stage-16-example-designs-and-prompts.md'
LOG = PREFIX + '2026-09-10-stage-16-progressive-example-levels.md'
SCRIPT = PREFIX + '2026-09-10-stage-16-verify.py'
REPORT = PREFIX + '2026-09-10-stage-16-verification.json'
INDEX = PREFIX + 'README.md'
EXPECTED_COVERAGE = [
    'B2B', 'B2C', 'Brand', 'Performance', 'Search', 'Social', 'Video', 'Audio',
    'Display', 'Creative strategy', 'Claims/proof', 'Adaptation', 'Media planning',
    'Audiences', 'Testing', 'Measurement', 'Fatigue', 'Optimisation',
    'Destination handoff', 'Legal/policy constraints', 'Cross-domain asset production', 'Repair',
]

def git_blob(data: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def validate(texts: dict[str, str], known: set[str], final: bool) -> list[dict[str, str]]:
    results = []
    def check(name: str, condition: bool) -> None:
        results.append({'check': name, 'result': 'PASS' if condition else 'FAIL'})
    design, log, index = texts[DESIGN], texts[LOG], texts[INDEX]
    blocks = re.findall(r'^## (E\d{2})\. ([^\n]+)\n(.*?)(?=^## |\Z)', design, re.M | re.S)
    check('Exactly fifteen ordered unique primary records', [x[0] for x in blocks] == [f'E{i:02}' for i in range(1,16)])
    by_id = {b[0]: b[2] for b in blocks}
    levels = [re.search(r'^Level: (L[1-5]) ', b[2], re.M) for b in blocks]
    check('Exactly three at each level in the specified progression', all(levels) and [m[1] for m in levels] == [f'L{1+(i//3)}' for i in range(15)])
    prompts = {i: re.findall(r'```text\n(.*?)\n```', body, re.S) for i, body in by_id.items()}
    check('One complete text prompt per primary example', len(prompts)==15 and all(len(p)==1 for p in prompts.values()) and len(re.findall(r'^```text$', design, re.M))==15)
    p = {i: x[0] for i,x in prompts.items() if len(x)==1}
    check('Every design has learning, acceptance and adverse-review contracts', len(blocks)==15 and all('Learning problem:' in b[2] and 'Acceptance oracle:' in b[2] and 'Adversarial review:' in b[2] for b in blocks))
    check('Every prompt includes its own synthetic facts and local output scope', len(p)==15 and all('SYNTHETIC teaching exercise' in t and f'SYN-{i}-' in t and f'production/advertising/{i}' in t for i,t in p.items()))
    check('Every prompt binds actual artefacts and evaluation without implicit paid action', len(p)==15 and all('.md' in t and 'evaluat' in t.lower() and 'paid generation' in t.lower() and 'authorised' in t for t in p.values()))
    check('All skill activations match level responsibilities', len(p)==15 and all('advertising-evaluate' in t and ('advertising-build' in t if int(i[1:])<=9 else 'advertising-optimise' in t) for i,t in p.items()))
    check('No prompt depends on copying facts from another example', all(not re.search(r'(same (facts|brief|inputs) as|copy (E\d\d|the previous)|as in E\d\d)',t,re.I) for t in p.values()))
    check('All three canonical L5 cases are retained and synthetic', all(i in p and name in p[i] and 'fixture' in p[i] for i,name in [('E13','Kakeibo'),('E14','Forward Deployment Engineer'),('E15','Production Skills ecosystem')]))
    check('Actual media is required at the declared fidelity', all(i in p and kind in p[i].lower() and 'actual' in p[i].lower() for i,kind in [('E02','png'),('E03','wav'),('E05','mp4'),('E07','ctv.mp4'),('E08','display.png'),('E09','mp4'),('E13','mp4'),('E14','png'),('E15','mp4')]))
    check('E04 has a controlled always-visible changed headline', 'always shows headline 1' in p.get('E04','') and 'four assemblies per arm' in p.get('E04','') and 'All remaining exact strings' in p.get('E04',''))
    check('E05 bounds opening and fixes the shared body', '[0,3)' in p.get('E05','') and '[3,15)' in p.get('E05','') and 'must be identical' in p.get('E05',''))
    check('App retained-use windows have exact boundaries and anchors', all('[168,192)' in p.get(i,'') for i in ['E09','E13']) and 'after first save' in p.get('E09','') and 'after first payment' in p.get('E13',''))
    rows10 = re.findall(r'^(Q\d{2}): (\d+) rows; (.+)$', p.get('E10',''), re.M)
    check('E10 derives 24 raw, six distinct, four qualified outcomes', len(rows10)==6 and len({r[0] for r in rows10})==6 and sum(int(r[1]) for r in rows10)==24 and sum('completed qualified registration' in r[2] for r in rows10)==4)
    check('E10 retains the strict fourteen-day boundary', 'strictly less than 14 elapsed days' in p.get('E10','') and 'Exactly 14 days is excluded' in p.get('E10',''))
    rows11 = re.findall(r'^(Baseline|Current) (High|Low): (\d+) impressions, (\d+) clicks, (\d+) qualified outcomes, GBP (\d+) spend\.', p.get('E11',''), re.M)
    d11 = {(period,context): tuple(map(int,(imp,click,q,cost))) for period,context,imp,click,q,cost in rows11}
    valid11 = set(d11)=={(a,b) for a in ['Baseline','Current'] for b in ['High','Low']}
    if valid11:
        rates = {k: Fraction(v[1],v[0]) for k,v in d11.items()}
        aggregate = {period: Fraction(sum(v[1] for k,v in d11.items() if k[0]==period),sum(v[0] for k,v in d11.items() if k[0]==period)) for period in ['Baseline','Current']}
        standard = {period: (rates[(period,'High')]+rates[(period,'Low')])/2 for period in ['Baseline','Current']}
        cost = {period: Fraction(sum(v[3] for k,v in d11.items() if k[0]==period),sum(v[2] for k,v in d11.items() if k[0]==period)) for period in ['Baseline','Current']}
        valid11 = aggregate=={'Baseline':Fraction(3,50),'Current':Fraction(7,250)} and rates[('Baseline','High')]==rates[('Current','High')]==Fraction(1,10) and rates[('Baseline','Low')]==rates[('Current','Low')]==Fraction(1,50) and set(standard.values())=={Fraction(3,50)} and cost=={'Baseline':Fraction(3),'Current':Fraction(55,13)}
    check('E11 actual prompt data reproduce aggregate, context, standardised and cost oracles', valid11)
    check('E12 is core-only and supplies the inclusive mathematical refund rule', 'No pack is activated' in p.get('E12','') and 'Pack: none; core-only' in by_id.get('E12','') and '0 <= hours <= 720' in p.get('E12','') and [0<=h<=720 for h in [-1,0,719,720,721]]==[False,True,True,True,False])
    rows13 = re.findall(r'([AB]): (\d+) platform-credited conversions, (\d+) distinct paid subscriptions, (\d+) retained users, (\d+) first-charge refunds',p.get('E13',''))
    d13={arm:tuple(map(int,(credits,paid,retained,refunds))) for arm,credits,paid,retained,refunds in rows13}
    valid13=set(d13)=={'A','B'} and '200 assigned eligible people and GBP 120 media spend' in p.get('E13','') and 'GBP 4 per retained' in p.get('E13','')
    if valid13:
        valid13=Fraction(120,d13['A'][2])==Fraction(60,11) and Fraction(120,d13['B'][2])==Fraction(24,5) and [d13[a][2]*4-120 for a in ['A','B']]==[-32,-20] and Fraction(d13['B'][2]-d13['A'][2],200)==Fraction(3,200)
    check('E13 prompt data preserve negative first-cycle contribution and limited effect',valid13)
    check('E14 preserves quote-only pricing, capacity and descriptive evidence', all(s in p.get('E14','') for s in ['No fixed project price is supplied','two fit calls per week','one paid implementation engagement per month','2 qualified teams','4 qualified teams','descriptive fixture data, not a causal experiment']))
    check('E15 retains two price paths, units and unknown net value', all(s in p.get('E15','') for s in ['not required for the software licence','operational ratios, not person-conversion probabilities','Refund status and fulfilment cost','No cross-path']) or all(s in p.get('E15','') for s in ['not required for the software licence','operational ratios, not person-conversion probabilities','Refund status and fulfilment cost','no cross-path']))
    candidates=re.findall(r'^\| (D\d{2}) \|[^\n]+',log,re.M)
    selected=re.findall(r'^\| D\d{2} \|[^\n]+\| SELECT (E\d{2}):',log,re.M)
    check('Candidate pool contains 25 alternatives and exactly fifteen unique selections', candidates==[f'D{i:02}' for i in range(1,26)] and selected==[f'E{i:02}' for i in range(1,16)])
    coverage_section=log.split('### Literal coverage matrix',1)[-1].split('## 5.',1)[0]
    coverage=re.findall(r'^\| ([^|]+?) \|[^\n]+',coverage_section,re.M)
    check('All twenty-two original coverage dimensions have mapped rows', all(c in [x.strip() for x in coverage] for c in EXPECTED_COVERAGE))
    check('Inherited nine formats remain explicit and associated with primary examples', all(s in coverage_section for s in ['static E02','search E01/E04','social video E05','CTV E07','display E06','carousel E09/E13','vertical E05/E09/E13','native/sponsored E08/E14','audio E03/E07']))
    check('Every example has a recorded substantive inspection', all(re.search(r'^\| '+i+r' \|',log,re.M) for i in by_id) and len(by_id)==15)
    check('Stage progression preserves future work as unstarted', '| 16: Five progressive example levels | PASS |' in index and '| 17–27 | NOT STARTED |' in index and 'b277f68d928cd673da6025d492cb8f32d83cd91a' in index)
    check('Design does not claim performed installed or media execution', 'none is claimed' in log and 'No example execution or installed capability is claimed' in design and 'not executions of an installed skill' in log)
    markup_ok=True
    links_ok=True
    for path,text in texts.items():
        if not path.endswith('.md'): continue
        markup_ok &= len(re.findall(r'^```',text,re.M))%2==0
        stripped=re.sub(r'^```.*?^```\s*$', '', text, flags=re.M|re.S)
        width=None
        for line in stripped.splitlines():
            if line.startswith('|'):
                n=len(re.split(r'(?<!\\)\|',line))-2
                if width is None: width=n
                markup_ok &= n==width
            else: width=None
        defs=dict(re.findall(r'^\[([^\]]+)\]:\s*(\S+)',stripped,re.M))
        labels=re.findall(r'\[[^\]]+\]\[([^\]]+)\]',stripped)
        links_ok &= all(label in defs for label in labels)
        targets=re.findall(r'\[[^\]]+\]\(([^)]+)\)',stripped)+list(defs.values())
        for target in targets:
            if re.match(r'https?://|mailto:|#',target): continue
            target=target.split('#',1)[0]
            joined=posixpath.normpath(posixpath.join(posixpath.dirname(path),target))
            links_ok &= joined in known
    check('Markdown fences and table widths are balanced',bool(markup_ok))
    check('Every named and local documentation reference resolves',bool(links_ok))
    if final:
        check('Final acceptance and substantive exit are present', 'Stage acceptance: PASS' in log and 'PENDING' not in log and 'REVIEW |' not in log and 'All mandatory Stage 16' in log)
        check('Every mandatory conformance row passes',len(re.findall(r'^\| A\d{2} [^\n]+\| PASS \|$',log,re.M))==10)
    return results

def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path('.'))
    parser.add_argument('--known-paths',type=Path)
    parser.add_argument('--final',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        texts={p:(args.root/p).read_text(encoding='utf-8') for p in [DESIGN,LOG,INDEX]}
        known={str(p.relative_to(args.root)) for p in args.root.rglob('*') if p.is_file()}
        if args.known_paths:
            known.update(json.loads(args.known_paths.read_text())['files'])
        checks=validate(texts,known,args.final)
        mutations=[
            ('missing primary example',DESIGN,lambda s: re.sub(r'^## E15\..*?(?=^## Catalogue)', '', s, flags=re.M|re.S)),
            ('wrong level distribution',DESIGN,lambda s: s.replace('Level: L5 — full advertising-production thesis.','Level: L4 — diagnose and repair campaign performance.',1)),
            ('missing prompt synthetic label',DESIGN,lambda s: s.replace('This is a SYNTHETIC teaching exercise.','This is a teaching exercise.',1)),
            ('uncontrolled search assembly',DESIGN,lambda s: s.replace('always shows headline 1','sometimes shows headline 1')),
            ('incorrect duplicate count',DESIGN,lambda s: s.replace('Q06: 6 rows;','Q06: 7 rows;')),
            ('changed within-context rate',DESIGN,lambda s: s.replace('Current High: 200 impressions, 20 clicks','Current High: 200 impressions, 21 clicks')),
            ('inconsistent core-only selection',DESIGN,lambda s: s.replace('Pack: none; core-only.','Pack: direct-response-performance-campaign.')),
            ('duplicate selected candidate',LOG,lambda s: s.replace('SELECT E15:','SELECT E14:')),
            ('broken local source link',LOG,lambda s: s.replace('[Examples]: 2026-09-10-stage-16-example-designs-and-prompts.md','[Examples]: missing-file.md')),
        ]
        for name,path,mutate in mutations:
            changed=dict(texts); changed[path]=mutate(texts[path])
            rejected=changed[path]!=texts[path] and any(c['result']=='FAIL' for c in validate(changed,known,args.final))
            checks.append({'check':'Negative mutation rejected: '+name,'result':'PASS' if rejected else 'FAIL'})
        report={'scope':'Stage 16 design/document/data verification only; no installed-skill or campaign execution', 'mode':'final' if args.final else 'review','result':'PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL','check_count':len(checks),'checks':checks,'primary_examples':15,'levels':{'L1':3,'L2':3,'L3':3,'L4':3,'L5':3},'complete_prompts':15,'candidate_pool':25,'coverage_dimensions':22,'negative_mutations':9,'input_blobs':{p:git_blob((args.root/p).read_bytes()) for p in [DESIGN,LOG,INDEX,SCRIPT]}}
        output=args.output or args.root/REPORT
        output.parent.mkdir(parents=True,exist_ok=True)
        output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
        print(json.dumps({'result':report['result'],'check_count':len(checks),'failures':[c['check'] for c in checks if c['result']=='FAIL'],'report':str(output)},indent=2))
        return 0 if report['result']=='PASS' else 1
    except (OSError,ValueError,KeyError) as exc:
        print(f'Verification could not complete: {exc}')
        return 2

if __name__=='__main__':
    raise SystemExit(main())
