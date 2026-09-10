"""Validate Stage 18 design and source bindings, never execute an agent or provider.

From a full checkout: python3 docs/research-logs/2026-09-10-stage-18-verify.py --root . --final
A partial recovery checkout may supply --known-paths with verified Git blob metadata.
That proves path/identity bindings only, not a local read of absent source contents.
"""
from __future__ import annotations
import argparse
import ast
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import re
from typing import Any

PREFIX='docs/research-logs/'
NAME='2026-09-10-stage-18-'
DESIGN=PREFIX+NAME+'evaluation-benchmark-regression-design.md'
CATALOGUE=PREFIX+NAME+'fixture-catalogue.json'
SCRIPT=PREFIX+NAME+'verify.py'
DIMENSIONS=['deterministic campaign validation','creative quality','campaign reasoning','business alignment','claim / legal / policy validity','experiment quality','measurement quality','optimisation / fatigue','preservation / repair','Extension Pack behaviour','end-to-end campaign production','installation integrity']
SLUGS=['direct-response-performance-campaign','brand-awareness-campaign','b2b-demand-generation-campaign','consumer-app-acquisition-campaign','product-launch-campaign','retargeting-and-reengagement-campaign','local-service-lead-generation','creator-native-social-campaign']
COMMANDS='frame-campaign ingest-business-brief define-objective model-audience build-message-map build-claim-proof-map generate-creative-territories design-concept build-creative-brief adapt-placement build-media-plan design-test prepare-launch-package ingest-results diagnose-delivery diagnose-creative diagnose-audience diagnose-placement diagnose-destination detect-fatigue propose-next-test refresh-creative preserve-learning audit-claims audit-proof audit-format-fit audit-destination-consistency audit-test-validity audit-measurement audit-policy-context verify-preservation diagnose-advertising-failure author-pack'.split()
PACK_NEG_HASH='696fdb59db848458b5a71975833e5d051e5abd7dd7b188536f2de462dc58aab7'
STRESS_NEG_HASH='13a531f9da1953cd4dd5877ed48731f641a50aa4d94154a7043415e0e7082a28'


def git_blob(b: bytes) -> str:
    return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()


def text_hash(value: Any) -> str:
    return hashlib.sha256(json.dumps(value,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def composed_ids(m: dict[str,Any]) -> dict[str,list[str]]:
    return {
        'primary':[r['id'] for r in m['primary_examples']],
        'packs':[f"PK-{p['id']}-{condition}-{case}" for p in m['pack_designs'] for condition in ('core','pack') for case in ('base','N1','N2')],
        'stress':[f"ST-{p['id']}-P" for p in m['stress_pairs']]+[f"ST-{p['id']}-N{i+1:02}" for p in m['stress_pairs'] for i in range(len(p['negative_changes']))]+[r['id'] for r in m['cross_cases']],
        'author':[r['id'] for r in m['author_cases']],
        'regression':[f"{r['id']}-N{i+1:02}" for r in m['supplemental_regressions'] for i in range(len(r['negative_changes']))],
        'vertical':[m['core_vertical']['id']],
        'installation':[f'I-{s}-{i+1}' for s in m['installation']['skills'] for i in range(len(m['installation']['routes']))]
    }


def validate_catalogue(m: dict[str,Any]) -> list[str]:
    checks=[]
    def check(condition: bool, name: str) -> None:
        require(condition,name); checks.append(name)
    check(m['schema']=='stage18-design-1' and m['stage']==18,'Correct stage/design schema')
    check(m['execution_state']=='not-run' and 'results' not in m,'No fabricated runtime results')
    check(m['accepted_parent']=='2b77a9eb9af9b30c873424efc2708729634be9cd','Verified Stage 17 predecessor')
    check(list(m['dimensions'])==[f'D{i:02}' for i in range(1,13)] and list(m['dimensions'].values())==DIMENSIONS,'All twelve original independent dimensions')
    check(set(m['sources'])=={'bootstrap','commands','packs','examples','stress','stress_acceptance'} and all(re.fullmatch('[a-f0-9]{40}',v['blob']) for v in m['sources'].values()),'Complete pinned source identities')
    check(m['sources']['bootstrap']['blob']=='f72a6f167595d6f178550fb1e02c4885d875b6b2' and m['sources']['stress_acceptance']['blob']=='795ce06386f2265a6390460d0b1263bbb21bf99f','Original authority and corrected FDE authority retained')
    examples=m['primary_examples']
    check([r['id'] for r in examples]==[f'E{i:02}' for i in range(1,16)],'Exactly fifteen ordered primary examples')
    check(Counter(r['level'] for r in examples)=={f'L{i}':3 for i in range(1,6)},'Exactly three examples at each original level')
    check(all(r['source']=='examples' and r['selector']==f"## {r['id']}." and all(isinstance(r[k],str) and r[k].strip() for k in ('required_output','oracle','negative_review')) for r in examples),'Complete primary prompt/output/oracle bindings')
    required_media={'E02':['SVG','PNG','1080'],'E03':['20-second','48-kHz','WAV','listening'],'E05':['15-second','1080x1920','MP4'],'E06':['SVG','PNG','300x250'],'E07':['CTV','MP4','WAV'],'E08':['Sponsored','350','PNG'],'E09':['carousel','PNG','MP4'],'E12':['before.html','after.html','parent-ad.txt'],'E13':['PNG','MP4'],'E14':['Sponsored','SVG/PNG'],'E15':['20-second','MP4','PNG']}
    by_id={r['id']:r for r in examples}
    check(all(all(s in by_id[e]['required_output'] for s in tokens) for e,tokens in required_media.items()),'Required actual modalities and output profiles retained')
    check(by_id['E12']['pack'] is None and by_id['E09']['pack']=='P04' and by_id['E15']['pack']=='P02','Core-only and non-composed pack selections preserved')
    check(all(r['dimensions'] and set(r['dimensions'])<=set(m['dimensions']) for r in examples),'Primary dimension mappings resolve')
    packs=m['pack_designs']
    check([p['id'] for p in packs]==[f'P{i:02}' for i in range(1,9)] and [p['slug'] for p in packs]==SLUGS,'All eight selected pack identities')
    check(all(len(p['observables'])==3 and len(set(p['observables']))==3 and all(v.strip() for v in p['observables']) for p in packs),'Twenty-four distinct pack observables')
    check(all(p['source']=='packs' and p['core_selector']==f"### {p['id']} core-only comparator" and p['pack_selector']==f"### {p['id']} pack showcase" for p in packs),'Exact matched source-prompt selectors')
    check(all(len(p['negative_changes'])==2 for p in packs) and text_hash([p['negative_changes'] for p in packs])==PACK_NEG_HASH,'All sixteen inspected negative texts unchanged')
    selectors=m['stress_prompt_selectors']
    check(set(selectors)=={'K','F','E'} and selectors['F']=={'source':'stress_acceptance','selector':'## Complete replacement FDE prompt'} and selectors['K']['source']==selectors['E']['source']=='stress','Exactly three active stress prompts, corrected FDE only')
    pairs=m['stress_pairs']
    check([p['id'] for p in pairs]==[f'{g}{i:02}' for g,n in (('K',7),('F',6),('E',6)) for i in range(1,n+1)],'All nineteen original-obligation pairs')
    check(all(p['subject']==p['id'][0] and p['positive_oracle'].strip() and p['repair'].strip() for p in pairs),'Positive expectations and smallest-repair contracts for every pair')
    check(sum(len(p['negative_changes']) for p in pairs)==54 and text_hash([p['negative_changes'] for p in pairs])==STRESS_NEG_HASH,'All fifty-four independently stated adverse alternatives retained')
    check([r['id'] for r in m['cross_cases']]==[f'X{i:02}' for i in range(1,7)] and all(r['input'].strip() and r['oracle'].strip() for r in m['cross_cases']),'Six complete cross-contract case definitions')
    check([r['id'] for r in m['author_cases']]==['A01','A02'] and all('advertising-pack-author' in r['prompt'] and r['oracle'].strip() for r in m['author_cases']),'Two actual-owning-skill authoring case contracts')
    v=m['core_vertical']
    check(v['id']=='V01' and all(t in v['prompt'] for t in ('SYNTHETIC','thirteen-area','three distinct cheap','two complete search bundles','nine-field','advertising-evaluate','advertising-optimise','before/after','U1','U2','U3','U4')),'Complete first vertical and offline test-preflight contract')
    check([r['id'] for r in m['supplemental_regressions']]==['G01','G02','G03'] and [len(r['negative_changes']) for r in m['supplemental_regressions']]==[1,2,1],'Clock, backlog and stale-policy defects retain four mutation trials')
    commands=m['command_coverage']
    check([c['name'] for c in commands]==COMMANDS and [c['id'] for c in commands]==[f'C{i:02}' for i in range(1,34)],'All thirty-three original/accepted command contracts mapped')
    check(Counter(c['owner'] for c in commands)=={'advertising-build':13,'advertising-optimise':10,'advertising-evaluate':9,'advertising-pack-author':1},'Exact four-skill ownership distribution')
    check(all(c['evidence_case'] in set(by_id)|{'A01','A02'} for c in commands),'Every command maps to an actual designed evidence case')
    install=m['installation']
    check(install['skills']==['advertising-build','advertising-optimise','advertising-evaluate','advertising-pack-author'] and len(install['routes'])==2 and len(install['checks'])==6,'Four independent skills and both installation routes')
    check('not a new owner approval' in m['negative_wrapper'] and 'preserving unaffected work' in m['negative_wrapper'],'Lower-trust wrapper retains authority and preservation')
    ids=composed_ids(m)
    check({k:len(v) for k,v in ids.items()}=={'primary':15,'packs':48,'stress':79,'author':2,'regression':4,'vertical':1,'installation':8} and all(len(v)==len(set(v)) for v in ids.values()),'Exact expanded suite counts with unique case IDs')
    return checks


def first_prompt(text: str, selector: str) -> str:
    # Select a heading, then the first complete fence before the next heading of that rank.
    lines=text.splitlines(); matches=[i for i,l in enumerate(lines) if l.startswith(selector)]
    require(len(matches)==1,f'Ambiguous/missing source selector: {selector}')
    rank=len(lines[matches[0]])-len(lines[matches[0]].lstrip('#'))
    selected=[]
    for line in lines[matches[0]+1:]:
        if re.match(r'^#{1,'+str(rank)+r'} ',line): break
        selected.append(line)
    blocks=re.findall(r'```(?:text)?\n(.*?)\n```','\n'.join(selected),re.S)
    require(len(blocks)==1,f'Expected one complete prompt at {selector}')
    return blocks[0]


def run(root: Path, known: dict[str,str], final: bool) -> dict[str,Any]:
    root=root.resolve(); m=json.loads((root/CATALOGUE).read_text()); doc=(root/DESIGN).read_text()
    checks=validate_catalogue(m); loaded={}; metadata_only=[]
    for name,source in m['sources'].items():
        relative=PREFIX+source['path']; p=(root/relative).resolve()
        require(p.is_relative_to(root),'Source escaped root')
        if p.is_file():
            require(git_blob(p.read_bytes())==source['blob'],f'Source changed: {relative}')
            loaded[name]=p.read_text()
        else:
            require(known.get(relative)==source['blob'],f'Unavailable source binding: {relative}')
            metadata_only.append(relative)
    checks.append('All source identities verified against local bytes or explicit verified remote metadata')
    if 'examples' in loaded:
        for r in m['primary_examples']: first_prompt(loaded['examples'],r['selector'])
        checks.append('Fifteen actual source prompt blocks extracted')
    if 'packs' in loaded:
        for p in m['pack_designs']:
            a=first_prompt(loaded['packs'],p['core_selector']);b=first_prompt(loaded['packs'],p['pack_selector'])
            require(a.split('\n',1)[1]==b.split('\n',1)[1],f'Unmatched prompt facts: {p["id"]}')
        checks.append('Eight actual source prompt pairs match after activation line')
    for s in m['stress_prompt_selectors'].values():
        if s['source'] in loaded: first_prompt(loaded[s['source']],s['selector'])
    checks.append('Available stress source prompts extracted; absent bodies explicitly metadata-only')
    require(all(f'### D{i:02}.' in doc for i in range(1,13)),'Missing dimension contract')
    require(all(f'| A{i:02} ' in doc for i in range(1,10)),'Missing conformance requirement')
    require(all(s in doc for s in ('19 positive','54 adverse','79 cases','48 runs','FDE-17@2','not private hidden reasoning','No numerical judge reliability','No claim of human-calibrated','G01','G02')),'Missing substantive evidence boundary')
    require('R01' in doc and 'R02' in doc and 'R03' in doc,'Missing research source')
    checks.append('All dimension, conformance, provenance and execution-boundary sections present')
    for rel in (DESIGN,PREFIX+'README.md'):
        text=(root/rel).read_text(); require(text.count('```')%2==0,f'Unbalanced fences: {rel}')
        definitions=dict(re.findall(r'^\[([^\]]+)\]:\s*(\S+)',text,re.M))
        named=re.findall(r'\[[^\]\n]+\]\[([^\]]+)\]',text)
        require(all(n in definitions for n in named),f'Unresolved named reference: {rel}')
        urls=list(definitions.values())+re.findall(r'\]\(([^)\s]+)\)',text)
        for url in urls:
            if re.match(r'^https?://',url): continue
            target=((root/rel).parent/url.split('#')[0]).resolve()
            require(target.is_relative_to(root),'Link escaped root')
            target_rel=str(target.relative_to(root))
            require(target.is_file() or target_rel in known,f'Missing local target: {url}')
        widths=[]
        for line in text.splitlines()+['']:
            if line.startswith('|'): widths.append(len(re.split(r'(?<!\\)\|',line)))
            elif widths:
                require(len(set(widths))==1,f'Inconsistent table columns: {rel}');widths=[]
    ast.parse((root/SCRIPT).read_text())
    checks.append('Markdown fences, table widths, named/local paths and verifier syntax pass')
    if final:
        require('Stage acceptance: PASS' in doc and 'DRAFT_' not in doc,'Incomplete final acceptance')
        require('All mandatory Stage 18' in doc,'Missing substantive exit')
        checks.append('Final acceptance and exit have no draft markers')
    mutations=[
        ('missing example',lambda x:x['primary_examples'].pop()),
        ('wrong level',lambda x:x['primary_examples'][0].update(level='L5')),
        ('missing actual WAV',lambda x:x['primary_examples'][2].update(required_output='script only')),
        ('changed pack negative',lambda x:x['pack_designs'][0]['negative_changes'].__setitem__(0,'Approved new monthly price.')),
        ('missing stress alternative',lambda x:x['stress_pairs'][0]['negative_changes'].pop()),
        ('old FDE prompt',lambda x:x['stress_prompt_selectors']['F'].update(source='stress')),
        ('missing command',lambda x:x['command_coverage'].pop()),
        ('invented runtime pass',lambda x:x.update(execution_state='passed')),
        ('missing dimension',lambda x:x['dimensions'].pop('D05')),
        ('missing remote install route',lambda x:x['installation']['routes'].pop()),
        ('duplicate cross case',lambda x:x['cross_cases'][1].update(id='X01')),
        ('missing first vertical',lambda x:x['core_vertical'].update(prompt='A plan only.'))
    ]
    for name,fn in mutations:
        corrupt=copy.deepcopy(m);fn(corrupt)
        try: validate_catalogue(corrupt)
        except (ValueError,KeyError): checks.append('Negative mutation rejected: '+name)
        else: raise ValueError('Checker accepted mutation: '+name)
    return {'scope':'Stage 18 design/inventory checks only','runtime_execution_state':'not-run','checks':[{'check':c,'result':'PASS'} for c in checks],'count':len(checks),'negative_mutations':len(mutations),'suite_counts':{k:len(v) for k,v in composed_ids(m).items()},'metadata_only_source_paths':metadata_only,'input_blobs':{rel:git_blob((root/rel).read_bytes()) for rel in (DESIGN,CATALOGUE,SCRIPT,PREFIX+'README.md')}}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    parser.add_argument('--known-paths',type=Path)
    parser.add_argument('--final',action='store_true')
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    try:
        report=run(args.root,json.loads(args.known_paths.read_text()) if args.known_paths else {},args.final)
        rendered=json.dumps(report,ensure_ascii=False,indent=2)+'\n'
        if args.output: args.output.write_text(rendered)
        print(rendered)
    except (OSError,ValueError,KeyError,TypeError) as error:
        parser.exit(1,f'Design verification failed: {error}\n')
