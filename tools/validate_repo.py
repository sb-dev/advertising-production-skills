#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, re, shutil, tempfile
from pathlib import Path

SKILLS = {
    'advertising-build': ['frame-campaign','ingest-business-brief','define-objective','model-audience','build-message-map','build-claim-proof-map','generate-creative-territories','design-concept','build-creative-brief','adapt-placement','build-media-plan','design-test','prepare-launch-package'],
    'advertising-optimise': ['ingest-results','diagnose-delivery','diagnose-creative','diagnose-audience','diagnose-placement','diagnose-destination','detect-fatigue','propose-next-test','refresh-creative','preserve-learning'],
    'advertising-evaluate': ['audit-claims','audit-proof','audit-format-fit','audit-destination-consistency','audit-test-validity','audit-measurement','audit-policy-context','verify-preservation','diagnose-advertising-failure'],
    'advertising-pack-author': ['author-pack'],
}
SPECS = ['docs/01-advertising-production-skills-system-spec.md','docs/02-advertising-production-skills-workflows-and-artifacts-spec.md','docs/03-advertising-production-skills-repository-and-contracts-spec.md','docs/04-testing-and-benchmark-spec.md','docs/05-advertising-production-customisation-packs-spec.md','docs/06-advertising-production-extension-pack-catalogue.md']
ROOT_REQUIRED = ['README.md','LICENSE','CONTRIBUTING.md','CHANGELOG.md','package.json'] + SPECS
README_HEADINGS = ['Business Building boundary','Truthful and policy-aware advertising','Installation','Quick start','Learn by producing','Project structure grows with the work','Skills','Extension Packs','Execution layer and specialist handoffs','Measurement, optimisation and learning','Benchmarks and evidence','Canonical stress tests','Documentation','Boundaries','Contributing','Licence']
LINK_RE = re.compile(r'(?<!!)\[[^\]]+\]\(([^)]+)\)')
NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')

def parse_frontmatter(text):
    if not text.startswith('---\n') or '\n---\n' not in text[4:]: return {}
    out={}
    for line in text[4:].split('\n---\n',1)[0].splitlines():
        if ':' in line:
            k,v=line.split(':',1); out[k.strip()]=v.strip()
    return out

def link_errors(root,text,source):
    errors=[]
    for target in LINK_RE.findall(text):
        if target.startswith(('http://','https://','#','mailto:')): continue
        target=target.split('#',1)[0]
        if not target: continue
        path=(source.parent/target).resolve()
        try: path.relative_to(root.resolve())
        except ValueError:
            errors.append(f'{source}: link escapes repository: {target}'); continue
        if not path.exists(): errors.append(f'{source}: missing link target: {target}')
    return errors

def validate(root):
    root=root.resolve(); errors=[]
    for p in ROOT_REQUIRED:
        if not (root/p).is_file(): errors.append(f'missing required file: {p}')
    lic=(root/'LICENSE').read_text(errors='replace') if (root/'LICENSE').is_file() else ''
    if not lic.startswith('MIT License\n'): errors.append('LICENSE is not MIT')
    try:
        pkg=json.loads((root/'package.json').read_text()); scripts=pkg.get('scripts',{})
        if pkg.get('license')!='MIT': errors.append('package.json licence is not MIT')
        if scripts.get('validate')!='python3 tools/validate_repo.py': errors.append('pnpm validate is not bound to repository validator')
        if scripts.get('test')!="python3 -m unittest discover -s tests -p 'test_*.py'": errors.append('pnpm test is not bound to repository tests')
        if not str(pkg.get('packageManager','')).startswith('pnpm@'): errors.append('packageManager is not pinned')
    except Exception as e: errors.append(f'invalid package.json: {e}')
    skill_root=root/'skills'; actual={p.name for p in skill_root.iterdir() if p.is_dir()} if skill_root.is_dir() else set()
    if actual != set(SKILLS): errors.append(f'skill set mismatch: {sorted(actual)}')
    for skill,intents in SKILLS.items():
        base=skill_root/skill; sk=base/'SKILL.md'; ref=base/'references/core-contract.md'; cmd=base/'commands'
        for p in [sk,ref]:
            if not p.is_file(): errors.append(f'missing skill file: {p.relative_to(root)}')
        if sk.is_file():
            text=sk.read_text(); meta=parse_frontmatter(text)
            if meta.get('name')!=skill: errors.append(f'{skill}: frontmatter name mismatch')
            if not NAME_RE.fullmatch(meta.get('name','')): errors.append(f'{skill}: invalid name')
            if not meta.get('description') or len(meta['description'])>1024: errors.append(f'{skill}: invalid description')
            if meta.get('license')!='MIT': errors.append(f'{skill}: licence mismatch')
            errors += link_errors(root,text,sk)
        files=sorted(p.stem for p in cmd.glob('*.md')) if cmd.is_dir() else []
        if files != sorted(intents): errors.append(f'{skill}: command set mismatch: {files}')
        for intent in intents:
            p=cmd/f'{intent}.md'
            if p.is_file():
                t=p.read_text()
                for token in [f'# {intent}',f'**Owner:** `{skill}`','## Purpose','## Inputs','## Outputs','## Checks','## Failure routing']:
                    if token not in t: errors.append(f'{p.relative_to(root)} missing {token}')
        if ref.is_file(): errors += link_errors(root,ref.read_text(),ref)
    if sum(map(len,SKILLS.values())) != 33: errors.append('internal expected intent count is not 33')
    if [len(SKILLS[k]) for k in SKILLS] != [13,10,9,1]: errors.append('internal owner distribution is wrong')
    readme=root/'README.md'
    if readme.is_file():
        t=readme.read_text()
        for h in README_HEADINGS:
            if f'## {h}' not in t: errors.append(f'README missing section: {h}')
        if 'Current status: production scaffold' not in t: errors.append('README does not state scaffold status')
        if 'clean external installation and host-compatibility evidence are Stage 25 requirements' not in t: errors.append('README overstates installation evidence')
        if 'five levels × three primary examples = fifteen' not in t: errors.append('README does not state exact 5x3 progression')
        errors += link_errors(root,t,readme)
    ex=root/'examples/README.md'
    if not ex.is_file(): errors.append('missing examples/README.md')
    else:
        t=ex.read_text(); ids=re.findall(r'^\| (E\d{2}) \| (L\d) \|',t,re.M); expected=[f'E{i:02d}' for i in range(1,16)]
        if [x[0] for x in ids] != expected: errors.append(f'example IDs mismatch: {ids}')
        levels={f'L{i}':0 for i in range(1,6)}
        for _,level in ids: levels[level]=levels.get(level,0)+1
        if any(v!=3 for v in levels.values()): errors.append(f'example level distribution mismatch: {levels}')
        if 'execution_status: not-run' not in t: errors.append('examples index must preserve not-run status')
        errors += link_errors(root,t,ex)
    manifest=root/'benchmarks/suites.json'
    if not manifest.is_file(): errors.append('missing benchmarks/suites.json')
    else:
        try:
            data=json.loads(manifest.read_text()); expected={'core_vertical':1,'primary_examples':15,'pack_conditions':48,'canonical_cases':79,'pack_authoring_cases':2,'supplemental_regressions':4,'installation_combinations':8}
            if data.get('designed_case_counts')!=expected: errors.append('benchmark designed case counts changed')
            if data.get('execution_status')!='not-run': errors.append('benchmark manifest overstates execution')
        except Exception as e: errors.append(f'invalid benchmark manifest: {e}')
    for p in ['benchmarks/README.md','tools/validate_repo.py','tests/test_repository.py','.github/workflows/validate.yml','.github/pull_request_template.md','docs/research-logs/2026-09-11-stage-22-production-repository-scaffold.md']:
        if not (root/p).is_file(): errors.append(f'missing scaffold surface: {p}')
    if (root/'extension-packs').exists() and not any((root/'extension-packs').iterdir()): errors.append('empty extension-packs directory is cosmetic')
    if (root/'integrations').exists() and not any((root/'integrations').iterdir()): errors.append('empty integrations directory is cosmetic')
    workflow=root/'.github/workflows/validate.yml'
    if workflow.is_file():
        w=workflow.read_text()
        for token in ['pnpm validate','pnpm test','pnpm/action-setup@v4','version: 12.3.4']:
            if token not in w: errors.append(f'CI missing: {token}')
    return errors

def write_fixture(root):
    for p in ROOT_REQUIRED:
        f=root/p; f.parent.mkdir(parents=True,exist_ok=True)
        if p=='LICENSE': f.write_text('MIT License\nfixture\n')
        elif p=='package.json': f.write_text(json.dumps({'license':'MIT','packageManager':'pnpm@12.3.4','scripts':{'validate':'python3 tools/validate_repo.py','test':"python3 -m unittest discover -s tests -p 'test_*.py'"}}))
        elif p=='README.md': f.write_text('# Advertising Production Skills\n\n**Current status: production scaffold.** clean external installation and host-compatibility evidence are Stage 25 requirements. five levels × three primary examples = fifteen\n\n'+'\n'.join('## '+h for h in README_HEADINGS)+'\n')
        else: f.write_text('# fixture\n')
    for skill,intents in SKILLS.items():
        base=root/'skills'/skill; (base/'commands').mkdir(parents=True,exist_ok=True); (base/'references').mkdir(parents=True,exist_ok=True)
        links='\n'.join(f'- [{i}](commands/{i}.md)' for i in intents)
        (base/'SKILL.md').write_text(f'---\nname: {skill}\ndescription: fixture activation contract\nlicense: MIT\n---\n# {skill}\n{links}\n[core](references/core-contract.md)\n')
        (base/'references/core-contract.md').write_text('# core\n')
        for i in intents: (base/'commands'/f'{i}.md').write_text(f'# {i}\n\n**Owner:** `{skill}`\n\n## Purpose\nx\n## Inputs\nx\n## Outputs\nx\n## Checks\nx\n## Failure routing\nx\n')
    (root/'examples').mkdir(); rows='\n'.join(f'| E{i:02d} | L{((i-1)//3)+1} | case |' for i in range(1,16)); (root/'examples/README.md').write_text('# Examples\n\nexecution_status: not-run\n\n| ID | Level | Name |\n|---|---|---|\n'+rows+'\n')
    (root/'benchmarks').mkdir(); (root/'benchmarks/README.md').write_text('# Benchmarks\n'); (root/'benchmarks/suites.json').write_text(json.dumps({'execution_status':'not-run','designed_case_counts':{'core_vertical':1,'primary_examples':15,'pack_conditions':48,'canonical_cases':79,'pack_authoring_cases':2,'supplemental_regressions':4,'installation_combinations':8}}))
    (root/'tools').mkdir(); shutil.copy2(__file__,root/'tools/validate_repo.py')
    (root/'tests').mkdir(); (root/'tests/test_repository.py').write_text('# fixture test\n')
    (root/'.github/workflows').mkdir(parents=True); (root/'.github/workflows/validate.yml').write_text('pnpm/action-setup@v4\nversion: 12.3.4\npnpm validate\npnpm test\n'); (root/'.github/pull_request_template.md').write_text('# PR\n')
    p=root/'docs/research-logs/2026-09-11-stage-22-production-repository-scaffold.md'; p.parent.mkdir(parents=True,exist_ok=True); p.write_text('# Stage 22\n')

def self_test():
    failures=[]
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); write_fixture(root)
        errs=validate(root)
        if errs: failures.append('valid fixture failed: '+repr(errs))
        cases=[('missing skill',lambda r: shutil.rmtree(r/'skills/advertising-evaluate')),('wrong metadata',lambda r:(r/'skills/advertising-build/SKILL.md').write_text((r/'skills/advertising-build/SKILL.md').read_text().replace('name: advertising-build','name: wrong'))),('missing command',lambda r:(r/'skills/advertising-build/commands/design-test.md').unlink()),('broken link',lambda r:(r/'skills/advertising-build/SKILL.md').write_text((r/'skills/advertising-build/SKILL.md').read_text()+'\n[bad](missing.md)\n')),('example distribution',lambda r:(r/'examples/README.md').write_text((r/'examples/README.md').read_text().replace('| E03 | L1 |','| E03 | L2 |'))),('false benchmark execution',lambda r:(r/'benchmarks/suites.json').write_text((r/'benchmarks/suites.json').read_text().replace('"not-run"','"passed"')))]
        for name,mutate in cases:
            with tempfile.TemporaryDirectory() as td2:
                r=Path(td2); shutil.copytree(root,r,dirs_exist_ok=True); mutate(r)
                if not validate(r): failures.append('mutation not detected: '+name)
    return failures

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=Path('.')); ap.add_argument('--self-test',action='store_true'); args=ap.parse_args()
    if args.self_test:
        failures=self_test(); print(json.dumps({'result':'PASS' if not failures else 'FAIL','negative_mutations':6,'failures':failures},indent=2)); raise SystemExit(bool(failures))
    errors=validate(args.root); print(json.dumps({'result':'PASS' if not errors else 'FAIL','error_count':len(errors),'errors':errors},indent=2)); raise SystemExit(bool(errors))
if __name__=='__main__': main()
