#!/usr/bin/env python3
"""Stage 21 contract-review and README-delta checks; no agent/integration runs."""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, re, sys
from collections import Counter
from pathlib import Path

P='docs/research-logs/2026-09-10-stage-21-'
INPUT=P+'review-contracts.json'; LOG=P+'cross-project-review.md'; REPORT=P+'verification.json'; SELF=P+'verify.py'
INDEX='docs/research-logs/README.md'; README='docs/research-logs/2026-09-10-stage-20-public-readme.md'
HEAD='2787492a590aff16febcf80852c04453407c6bdf'; TREE='2ab49f0e905e2cb6178443198013dd230bd068df'
NEW_HEADING='Project structure that grows with the work'
PREVIOUS={
 'docs/research-logs/2026-09-10-stage-20-public-readme.md':'47dd06043b7d49987aec41612325a57542d68e0d',
 'docs/research-logs/2026-09-10-stage-20-readme-design.md':'9ec6fa6572dffd307bcf93a5ce78586b1d81b969',
 'docs/research-logs/2026-09-10-stage-20-inputs.json':'c3131be357b140333a4858e8b89d8e420e4975f6',
 'docs/research-logs/2026-09-10-stage-20-verify.py':'8375816f75913c96e46c35e91fc4256d2a2f9ac5',
 'docs/research-logs/2026-09-10-stage-20-verification.json':'795809de514821e4afe223678cdbae88cbd77578',
 INDEX:'0acd75273bfaf4d06f08b3e08b9107f73122b570'}
SCOPE={'commercial','research','legal','narrative','video','video-evaluation','music','audio','uiux','software','consumer','pactwright','progression','packs','licensing'}
CRITICAL_BINDINGS={'R01':'S06','R02':'S07','R03':'S08','R04':'S15','R06':'S12','R07':'S12','R09':'S13','R10':'S17','R12':'S18','R13':'S09','R14':'S10','R15':'S23','R16':'S22','R17':'S21','R18':'S02','R19':'S03','R20':'S02'}

def blob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def digest(text):return hashlib.sha256(text.encode()).hexdigest()
def load(path,name):
 spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

def validate(config,files,old_config,old_checks,identities):
 checks=[]
 def add(k,ok,detail=''):checks.append(dict(check=k,result='PASS' if ok else 'FAIL',detail=detail))
 text=files[README]
 # Explicit Stage 21 addition, not a mutation of the historical Stage 20 checker.
 heads=list(old_checks.HEADS)
 heads.insert(heads.index('Skills'),NEW_HEADING)
 original=old_checks.HEADS
 old_checks.HEADS=heads
 try:checks.extend(old_checks.check_copy(text,old_config,files))
 finally:old_checks.HEADS=original
 expected=dict(old_config['baseline_files'])
 expected.update({p:dict(mode='100644',sha=h) for p,h in PREVIOUS.items()})
 add('Current predecessor identity and all fifty file entries match',config['accepted_commit']==HEAD and config['accepted_tree']==TREE and config['baseline_files']==expected and len(expected)==50)
 add('Predecessor Git tree independently reconstructs',identities.git_tree(expected)==TREE)
 before=text; valid=True
 for change in reversed(config['readme_changes']):
  compound=change['insert']+change['anchor']
  valid=valid and bool(change['insert']) and before.count(compound)==1
  before=before.replace(compound,change['anchor'],1)
 add('Exactly two additive corrections reconstruct the accepted README',len(config['readme_changes'])==2 and valid and blob(before.encode())==PREVIOUS[README] and config['readme_before_blob']==PREVIOUS[README])
 structure=old_checks.clean(text).split('## '+NEW_HEADING+'\n',1)[-1].split('## Skills',1)[0]
 add('New structure guidance preserves requested-versus-produced scope',len(structure)>650 and 'requested output layout, not evidence' in structure and 'Several logical records can share one file' in structure and 'exact approved business' in structure)
 add('Specialist preflight and Audio migration constraints explicit',all(x in text for x in ['actual prerequisites and approval, locking and retry rules','cannot become that specialist\'s human approval','does not by itself replace the existing Music implementation']))
 add('Original quick-start source projection is unchanged',digest(old_config['quick_start_prompt'])==old_config['quick_start_sha256'])
 sources=config['sources']; source_ids=[s['id'] for s in sources]
 add('Twenty-three source identities and actual access limits recorded',source_ids==[f'S{i:02d}' for i in range(1,24)] and all(re.fullmatch('[0-9a-f]{40}',s['blob']) and all(s[k] for k in ['repository','path','scope','finding','limit','ref']) for s in sources))
 add('Source locators retain actual read refs rather than blob-as-commit URLs',all(s['url']==f"https://github.com/{s['repository']}/blob/{s['ref']}/{s['path']}" for s in sources) and all(s['ref']=='2b30c6736edea698e8a11f855bb47b9b399d90fd' for s in sources[:5]) and all(s['ref']=='main' for s in sources[5:]))
 add('Current data and registry sources remain correctly scoped',sources[4]['blob']=='df66c5cbee11d424df35696f845c4d1d1dd28b9c' and 'proposed' in sources[4]['finding'] and sources[-1]['blob']=='1b62f09eac0186f6bc40ad06675b67e7d6fa9b2c' and 'not tested' in sources[-1]['limit'])
 cases=config['cases']; by_id={r['id']:r for r in cases}
 add('All twenty distinct counterexamples and responsibility areas represented',[r['id'] for r in cases]==[f'R{i:02d}' for i in range(1,21)] and set(r['area'] for r in cases)==SCOPE)
 add('Every manual review records mutation finding repair and preservation',all(all(len(r[k])>35 for k in ['lower_trust_change','finding','smallest_repair','preserved']) and r['advertising_contract'] and r['result']=='PASS' for r in cases))
 add('All source-to-contract review references resolve',all(set(r['sources'])<=set(source_ids) for r in cases) and all(k in by_id and source in by_id[k]['sources'] for k,source in CRITICAL_BINDINGS.items()))
 add('Manual reviews cannot masquerade as runtime cases',all(r['method']=='manual source-to-contract counterexample review' and r['runtime_execution']=='not-run' for r in cases) and config['runtime_executions']=='not-run' and config['external_writes']=='none')
 candidates=config['extraction_candidates']
 add('Five abstraction dispositions preserve multiple sources and differences',[r['id'] for r in candidates]==[f'X{i:02d}' for i in range(1,6)] and all(len(r['sources'])>=2 and set(r['sources'])<=set(source_ids) and len(r['difference'])>60 and len(r['next_evidence'])>60 for r in candidates))
 add('No candidate is promoted to an extracted runtime',[r['decision'] for r in candidates]==['Retain as candidate; no extraction','Retain semantic pattern only; no common quality score','Retain as candidate; no shared repair engine','Retain packaging-check candidate, not a new installer','Reject extraction'])
 log=files[LOG]
 responsibilities=re.findall(r'^\| (\d+) [^|]+ \|',log,re.M)
 add('Fourteen central responsibilities individually reviewed',responsibilities==[str(i) for i in range(1,15)])
 add('Six-document ownership and exact inherited obligations retained',all(x in log for x in ['01 system/boundaries','02 workflows/artefacts','03 repository/skills','04 independent benchmark','05 pack semantics','06 actual selected catalogue','33 intents','48 pack conditions','79 canonical cases','eight installation combinations']))
 add('Actual review finding and additive repair are documented',all(f'| F{i:02d} ' in log for i in range(1,7)) and 'Only two additive insertions' in log and 'The root README and all six specs remain unchanged.' in log)
 add('Conformance retains stage-specific scope and no invented runtime',all(f'| A{i:02d} ' in log for i in range(1,10)) and '**not installed-agent executions**' in log and 'No unresolved Advertising-owned contract conflict remains' in log)
 known=set(expected)|set(files)|set(config.get('_actual_local_paths',[]))
 errors=identities.links_errors({README:text,LOG:log,INDEX:files[INDEX]},known)
 add('All current documentation paths and source references resolve',not errors,'; '.join(errors))
 errors=identities.syntax_errors({README:text,LOG:log,INDEX:files[INDEX]})
 add('New document fences and table structures valid',not errors,'; '.join(errors))
 index=files[INDEX]
 add('All Stage 0-19 progress is byte-preserved',digest(index.split('| 20:')[0])==config['progress_prefix_sha256'])
 add('Progress records actual Stage 20 and only adds this stage',HEAD in index and '| 21: Cross-project review |' in index and '| 22–27 | NOT STARTED |' in index)
 return checks

def main(root):
 config=json.loads((root/INPUT).read_text())
 old_input='docs/research-logs/2026-09-10-stage-20-inputs.json'
 old_config=json.loads((root/old_input).read_text())
 old=load(root/'docs/research-logs/2026-09-10-stage-20-verify.py','stage20_frozen')
 identities=load(root/'docs/research-logs/2026-09-10-stage-19-verify.py','stage19_identity')
 files={str(p.relative_to(root)):p.read_text() for p in (root/'docs').rglob('*.md')}
 config['_actual_local_paths']=[str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()]
 checks=validate(config,files,old_config,old,identities)
 def add(k,ok,detail=''):checks.append(dict(check=k,result='PASS' if ok else 'FAIL',detail=detail))
 absent=[];drift=[]
 for path,entry in config['baseline_files'].items():
  if path in (README,INDEX):continue
  p=root/path
  if not p.is_file():absent.append(path)
  elif blob(p.read_bytes())!=entry['sha']:drift.append(path)
 add('Every available accepted file outside the two owned changes is unchanged',not drift,', '.join(drift))
 add('All six actual specification bodies and original root are preserved',all((root/p).is_file() and blob((root/p).read_bytes())==m['sha'] for p,m in config['baseline_files'].items() if p=='README.md' or re.match(r'docs/0[1-6]-',p)))
 add('Frozen prior checker and source projection retain exact identities',all(blob((root/p).read_bytes())==PREVIOUS[p] for p in [old_input,'docs/research-logs/2026-09-10-stage-20-verify.py']))
 # Mutation execution tests these document/inventory checks, not agent judgement.
 mutations=[
 ('omit new required structure',lambda c,f:f.__setitem__(README,f[README].replace('## '+NEW_HEADING,'## Missing structure',1)),'All required public sections'),
 ('change original quick-start price',lambda c,f:f.__setitem__(README,f[README].replace('GBP 25 total, one-off.','GBP 9 total, one-off.',1)),'Complete E01'),
 ('silently rewrite another sentence',lambda c,f:f.__setitem__(README,f[README].replace('Evidence-led advertising,','Autonomous advertising,',1)),'Exactly two additive'),
 ('remove a source identity',lambda c,f:c['sources'].pop(),'Twenty-three source'),
 ('invent an immutable source commit',lambda c,f:c['sources'][5].__setitem__('ref',c['sources'][5]['blob']),'Source locators'),
 ('remove adverse review',lambda c,f:c['cases'].pop(),'All twenty distinct'),
 ('omit smallest repair',lambda c,f:c['cases'][0].__setitem__('smallest_repair',''),'Every manual review'),
 ('fabricate installed execution',lambda c,f:c['cases'][0].__setitem__('runtime_execution','passed'),'Manual reviews'),
 ('wrong consumer source binding',lambda c,f:c['cases'][14].__setitem__('sources',['S06']),'All source-to-contract'),
 ('premature shared extraction',lambda c,f:c['extraction_candidates'][0].__setitem__('decision','Implemented shared runtime'),'No candidate'),
 ('drop source-specific differences',lambda c,f:c['extraction_candidates'][1].__setitem__('difference','same'),'Five abstraction'),
 ('break review link',lambda c,f:f.__setitem__(README,f[README].replace('(2026-09-10-stage-21-cross-project-review.md)','(missing-review.md)')),'All local README'),
 ('claim neighbouring repository write',lambda c,f:c.__setitem__('external_writes','registry updated'),'Manual reviews'),
 ('alter accepted progress',lambda c,f:f.__setitem__(INDEX,f[INDEX].replace('Stage 1 log','Deleted prior evidence',1)),'All Stage 0-19'),
 ]
 for name,change,rule in mutations:
  c=copy.deepcopy(config);f=copy.deepcopy(files);change(c,f)
  result=validate(c,f,old_config,old,identities)
  add('Negative mutation rejected: '+name,any(r['result']=='FAIL' and r['check'].startswith(rule) for r in result))
 paths=[README,LOG,INPUT,SELF,INDEX]
 report=dict(stage=21,scope='Document/inventory/integrity checks and separately identified manual contract review; no installed integrations',result='PASS' if all(r['result']=='PASS' for r in checks) else 'FAIL',count=len(checks),negative_mutations=len(mutations),manual_counterexamples=20,manual_review_is_not_runtime=True,checks=checks,source_records=23,extraction_candidates=5,runtime_executions='not-run',external_writes='none',publication='requires subsequent actual remote verification',metadata_only_prior_paths=absent,input_blobs={p:blob((root/p).read_bytes()) for p in paths})
 (root/REPORT).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(dict(result=report['result'],count=len(checks),mutations=len(mutations),failures=[r for r in checks if r['result']=='FAIL']),ensure_ascii=False,indent=2))
 return report['result']=='PASS'

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--root',type=Path,default=Path('.'));a=p.parse_args()
 try:sys.exit(0 if main(a.root.resolve()) else 1)
 except (OSError,ValueError,KeyError,AssertionError) as e:print(str(e),file=sys.stderr);sys.exit(2)
