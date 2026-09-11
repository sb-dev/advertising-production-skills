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
README_HEADINGS = ['Claims, proof and commercial control','Install','Quick start — Local inspection search unit','Learn by producing','Project structure grows with the campaign','Skills','Extension Packs','Execution','Measurement, optimisation and learning','Testing and benchmarks','Documentation','Boundaries','Contributing','Licence']
LEAK_PATTERNS = [r'\bStage\s+\d+\b',r'feat/bootstrap',r'production scaffold',r'bootstrap progress',r'\bnot-run\b',r'maturity promotion',r'docs/research-logs/']
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

def validate_readme(root,text):
    errors=[]
    for h in README_HEADINGS:
        if f'## {h}' not in text: errors.append(f'README missing section: {h}')
    for pattern in LEAK_PATTERNS:
        if re.search(pattern,text,re.I): errors.append(f'README leaks bootstrap/process state: {pattern}')
    for token in ['SYN-E01-OFFER@1','SYN-E01-PROOF@1','Produce brief.md','Use a request-to-schedule CTA']:
        if token not in text: errors.append(f'README quick start incomplete: missing {token}')
    learn=text.split('## Learn by producing',1)[1].split('## Project structure grows with the campaign',1)[0] if '## Learn by producing' in text else ''
    for level in range(1,6):
        if f'### Level {level} —' not in learn: errors.append(f'README missing Level {level}')
    for i in range(1,16):
        if learn.count(f'E{i:02d} ') != 1: errors.append(f'README progression must contain E{i:02d} exactly once')
    for skill in SKILLS:
        if f'### `{skill}`' not in text: errors.append(f'README missing substantive skill section: {skill}')
    if 'npx skills add sb-dev/advertising-production-skills' not in text: errors.append('README missing canonical install route')
    errors += link_errors(root,text,root/'README.md')
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
    if readme.is_file(): errors += validate_readme(root,readme.read_text())
    ex=root/'examples/README.md'
    if not ex.is_file(): errors.append('missing examples/README.md')
    else:
        t=ex.read_text()
        for i in range(1,16):
            if f'### E{i:02d}.' not in t: errors.append(f'examples index missing E{i:02d}')
        for level in range(1,6):
            if f'## Level {level} —' not in t: errors.append(f'examples index missing Level {level}')
        errors += link_errors(root,t,ex)
    manifest=root/'benchmarks/suites.json'
    if not manifest.is_file(): errors.append('missing benchmarks/suites.json')
    else:
        try:
            data=json.loads(manifest.read_text()); expected={'core_vertical':1,'primary_examples':15,'pack_conditions':48,'canonical_cases':79,'pack_authoring_cases':2,'supplemental_regressions':4,'installation_combinations':8}
            if data.get('designed_case_counts')!=expected: errors.append('benchmark designed case counts changed')
            if data.get('execution_status')!='not-run': errors.append('benchmark manifest overstates execution')
        except Exception as e: errors.append(f'invalid benchmark manifest: {e}')
    for p in ['benchmarks/README.md','tools/validate_repo.py','tests/test_repository.py','.github/workflows/validate.yml','.github/pull_request_template.md','docs/research-logs/2026-09-11-stage-22-production-repository-scaffold.md','docs/research-logs/2026-09-11-stage-23-public-readme-conformance.md']:
        if not (root/p).is_file(): errors.append(f'missing repository surface: {p}')
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
        elif p=='README.md':
            levels='\n'.join(f'### Level {l} — fixture\n'+ '\n'.join(f'- E{i:02d} case' for i in range((l-1)*3+1,l*3+1)) for l in range(1,6))
            skills='\n'.join(f'### `{s}`\nfixture' for s in SKILLS)
            f.write_text('# Advertising Production Skills\n\n'+'\n'.join('## '+h for h in README_HEADINGS[:3])+'\nSYN-E01-OFFER@1\nSYN-E01-PROOF@1\nProduce brief.md\nUse a request-to-schedule CTA\n## Learn by producing\n'+levels+'\n## Project structure grows with the campaign\nfixture\n## Skills\n'+skills+'\n'+'\n'.join('## '+h for h in README_HEADINGS[6:])+'\nnpx skills add sb-dev/advertising-production-skills\n')
        else: f.write_text('# fixture\n')
    for skill,intents in SKILLS.items():
        base=root/'skills'/skill; (base/'commands').mkdir(parents=True,exist_ok=True); (base/'references').mkdir(parents=True,exist_ok=True)
        links='\n'.join(f'- [{i}](commands/{i}.md)' for i in intents)
        (base/'SKILL.md').write_text(f'---\nname: {skill}\ndescription: fixture activation contract\nlicense: MIT\n---\n# {skill}\n{links}\n[core](references/core-contract.md)\n')
        (base/'references/core-contract.md').write_text('# core\n')
        for i in intents: (base/'commands'/f'{i}.md').write_text(f'# {i}\n\n**Owner:** `{skill}`\n\n## Purpose\nx\n## Inputs\nx\n## Outputs\nx\n## Checks\nx\n## Failure routing\nx\n')
    (root/'examples').mkdir(); (root/'examples/README.md').write_text('# Learn by Producing\n'+'\n'.join(f'## Level {l} — fixture\n'+ '\n'.join(f'### E{i:02d}. case' for i in range((l-1)*3+1,l*3+1)) for l in range(1,6))+'\n')
    (root/'benchmarks').mkdir(); (root/'benchmarks/README.md').write_text('# Benchmarks\n'); (root/'benchmarks/suites.json').write_text(json.dumps({'execution_status':'not-run','designed_case_counts':{'core_vertical':1,'primary_examples':15,'pack_conditions':48,'canonical_cases':79,'pack_authoring_cases':2,'supplemental_regressions':4,'installation_combinations':8}}))
    (root/'tools').mkdir(); shutil.copy2(__file__,root/'tools/validate_repo.py')
    (root/'tests').mkdir(); (root/'tests/test_repository.py').write_text('# fixture test\n')
    (root/'.github/workflows').mkdir(parents=True); (root/'.github/workflows/validate.yml').write_text('pnpm/action-setup@v4\nversion: 12.3.4\npnpm validate\npnpm test\n'); (root/'.github/pull_request_template.md').write_text('# PR\n')
    for name in ['2026-09-11-stage-22-production-repository-scaffold.md','2026-09-11-stage-23-public-readme-conformance.md']:
        p=root/'docs/research-logs'/name; p.parent.mkdir(parents=True,exist_ok=True); p.write_text('# evidence\n')

def self_test():
    failures=[]
    with tempfile.TemporaryDirectory() as td:
        root=Path(td); write_fixture(root)
        errs=validate(root)
        if errs: failures.append('valid fixture failed: '+repr(errs))
        cases=[
            ('missing skill',lambda r: shutil.rmtree(r/'skills/advertising-evaluate')),
            ('wrong metadata',lambda r:(r/'skills/advertising-build/SKILL.md').write_text((r/'skills/advertising-build/SKILL.md').read_text().replace('name: advertising-build','name: wrong'))),
            ('missing command',lambda r:(r/'skills/advertising-build/commands/design-test.md').unlink()),
            ('broken link',lambda r:(r/'skills/advertising-build/SKILL.md').write_text((r/'skills/advertising-build/SKILL.md').read_text()+'\n[bad](missing.md)\n')),
            ('bootstrap leakage',lambda r:(r/'README.md').write_text((r/'README.md').read_text()+'\nStage 24 will prove this.\n')),
            ('missing quick-start fact',lambda r:(r/'README.md').write_text((r/'README.md').read_text().replace('SYN-E01-OFFER@1','missing-offer'))),
            ('wrong progression',lambda r:(r/'README.md').write_text((r/'README.md').read_text().replace('E03 case','E04 case',1))),
            ('missing skill section',lambda r:(r/'README.md').write_text((r/'README.md').read_text().replace('### `advertising-evaluate`','### missing-evaluate',1))),
            ('false benchmark execution',lambda r:(r/'benchmarks/suites.json').write_text((r/'benchmarks/suites.json').read_text().replace('"not-run"','"passed"'))),
        ]
        for name,mutate in cases:
            with tempfile.TemporaryDirectory() as td2:
                r=Path(td2); shutil.copytree(root,r,dirs_exist_ok=True); mutate(r)
                if not validate(r): failures.append('mutation not detected: '+name)
    return failures

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',type=Path,default=Path('.')); ap.add_argument('--self-test',action='store_true'); args=ap.parse_args()
    if args.self_test:
        failures=self_test(); print(json.dumps({'result':'PASS' if not failures else 'FAIL','negative_mutations':9,'failures':failures},indent=2)); raise SystemExit(bool(failures))
    errors=validate(args.root); print(json.dumps({'result':'PASS' if not errors else 'FAIL','error_count':len(errors),'errors':errors},indent=2)); raise SystemExit(bool(errors))
if __name__=='__main__': main()
