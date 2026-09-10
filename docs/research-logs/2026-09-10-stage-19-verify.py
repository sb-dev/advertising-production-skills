#!/usr/bin/env python3
"""Check Stage 19 specification contracts. Does not install or execute Agent Skills.

Run from a full checkout, or pass --partial for the explicitly incomplete recovery
workspace. Partial mode uses a hash-verified remote path map for unmounted old files;
it never claims their bodies were parsed. All six NEW specification bodies are read.
"""
from __future__ import annotations
import argparse
from collections import Counter
from copy import deepcopy
from hashlib import sha1, sha256
import json
from pathlib import Path, PurePosixPath
import re
import sys

PREFIX = 'docs/research-logs/2026-09-10-stage-19-'
SPEC_NAMES = [
 '01-advertising-production-skills-system-spec.md',
 '02-advertising-production-skills-workflows-and-artifacts-spec.md',
 '03-advertising-production-skills-repository-and-contracts-spec.md',
 '04-testing-and-benchmark-spec.md',
 '05-advertising-production-customisation-packs-spec.md',
 '06-advertising-production-extension-pack-catalogue.md',
]
SPECS = ['docs/'+n for n in SPEC_NAMES]
SOURCE = PREFIX+'source-contracts.json'
LOG = PREFIX+'six-canonical-specifications.md'
REPORT = PREFIX+'verification.json'
SELF = PREFIX+'verify.py'
INDEX = 'docs/research-logs/README.md'
COMMANDS = '''frame-campaign ingest-business-brief define-objective model-audience build-message-map build-claim-proof-map generate-creative-territories design-concept build-creative-brief adapt-placement build-media-plan design-test prepare-launch-package ingest-results diagnose-delivery diagnose-creative diagnose-audience diagnose-placement diagnose-destination detect-fatigue propose-next-test refresh-creative preserve-learning audit-claims audit-proof audit-format-fit audit-destination-consistency audit-test-validity audit-measurement audit-policy-context verify-preservation diagnose-advertising-failure author-pack'''.split()
RESOURCE_NAMES = set('system-boundaries brief-and-evidence strategy production media destination measurement optimisation policy-and-actions invocation evaluation-contract pack-contract pack-authoring'.split())
FIELD_LABELS = {'thesis':'Thesis','activation':'Activation and exclusions','inputs':'Required inputs','grammar':'Behavioural grammar','build':'Build effect','optimise':'Optimise effect','evaluate':'Evaluate effect','outputs':'Added outputs','repair':'Smallest repair','prohibited':'Prohibited defaults','differential':'Required differential question'}


def git_blob(data: bytes) -> str:
 return sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()


def git_tree(files: dict) -> str:
 root = {}
 for path, record in files.items():
  parts = PurePosixPath(path).parts
  if not parts or path.startswith('/') or '..' in parts:
   raise ValueError('Unsafe tree path: '+path)
  node = root
  for part in parts[:-1]:
   node = node.setdefault(part,{})
  node[parts[-1]] = (record['mode'],record['sha'])
 def encode(node):
  content = b''
  for name, value in sorted(node.items(),key=lambda kv:kv[0]+('/' if isinstance(kv[1],dict) else '')):
   mode, digest = ('40000',encode(value)) if isinstance(value,dict) else value
   content += mode.encode()+b' '+name.encode()+b'\0'+bytes.fromhex(digest)
  return sha1(b'tree '+str(len(content)).encode()+b'\0'+content).hexdigest()
 return encode(root)


def section(text: str, heading: str, level: int=3) -> str:
 start = re.search(r'^'+re.escape(heading)+r'\s*$',text,re.M)
 if not start:
  return ''
 tail=text[start.end():]
 end=re.search(r'^#{1,'+str(level)+r'} ',tail,re.M)
 return tail[:end.start()] if end else tail


def prompt(text: str, heading: str) -> str | None:
 body=section(text,heading)
 matches=re.findall(r'```text\n(.*?)\n```',body,re.S)
 return matches[0] if len(matches)==1 else None


def strip_fences(text: str) -> str:
 return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.S|re.M)


def target_path(source: str, target: str) -> str | None:
 if target.startswith('/') or '\\' in target:
  return '!unsafe!'
 if re.match(r'^(https?://|mailto:)',target):
  return None
 target=target.split('#',1)[0]
 if not target:
  return source
 parts=list(PurePosixPath(source).parent.parts)
 for part in target.split('/'):
  if part in ('','.'):
   continue
  if part=='..':
   if not parts:
    return '!unsafe!'
   parts.pop()
  else:
   parts.append(part)
 return '/'.join(parts)


def links_errors(files: dict[str,str], known: set[str]) -> list[str]:
 errors=[]
 for path,text in files.items():
  clean=strip_fences(text)
  defs=dict(re.findall(r'^\[([^\]]+)\]:\s+(\S+)',clean,re.M))
  targets=re.findall(r'\[[^\]]+\]\(([^)]+)\)',clean)+list(defs.values())
  for label in re.findall(r'\[[^\]]+\]\[([^\]]+)\]',clean):
   if label not in defs:errors.append(f'{path}: undefined reference {label}')
  for label in re.findall(r'(?<!\])\[(S\d+)\](?![:(])',clean):
   if label not in defs:errors.append(f'{path}: undefined source {label}')
  for target in targets:
   resolved=target_path(path,target)
   if resolved is not None and resolved not in known:
    errors.append(f'{path}: missing/unsafe target {target}')
   if '#' in target and resolved in files:
    frag=target.split('#',1)[1]
    heads=re.findall(r'^#{1,6}\s+(.+)$',strip_fences(files[resolved]),re.M)
    anchors={re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in heads}
    if frag and frag not in anchors:errors.append(f'{path}: unresolved fragment {target}')
 return errors


def syntax_errors(files: dict[str,str]) -> list[str]:
 errors=[]
 for path,text in files.items():
  if len(re.findall(r'^```',text,re.M))%2:errors.append(f'{path}: unbalanced fences')
  clean=strip_fences(text); widths=[]
  for line in clean.splitlines()+['']:
   if line.startswith('|'):
    widths.append(len(re.split(r'(?<!\\)\|',line))-2)
   elif widths:
    if len(set(widths))!=1:errors.append(f'{path}: table widths {widths}')
    widths=[]
 return errors


def validate_contents(files: dict[str,str], c: dict, final: bool=False):
 checks=[]
 def check(label, ok, detail=''):
  checks.append({'check':label,'result':'PASS' if ok else 'FAIL','detail':detail})
 exists=set(files)&set(SPECS)
 check('Six exact canonical specification paths',exists==set(SPECS))
 if exists!=set(SPECS):return checks
 texts=[files[p] for p in SPECS]; s1,s2,s3,s4,s5,s6=texts
 check('Six complete versioned canonical document bodies',all(t.startswith('# Advertising Production Skills:') and 'Version: 1.0' in t and len(t)>10000 and re.search(r'\*Advertising Production Skills: .* v1\.0 · 10 September 2026\*\s*$',t) for t in texts))
 check('Six-specification ownership matrix and cross-links',all(n in s1 for n in SPEC_NAMES) and all('Ownership' in t or 'Purpose and authority' in t for t in texts))
 check('Four skills and distinct external ownership',all(x in s1 and x in s3 for x in c['expected_skills']) and all(x in s1 for x in ['Business Building','Deep Research','Legal Skills','Optional Pactwright','account administration; asset rendering; campaign upload; bidding/spend; ad serving; data collection; conversion tracking; attribution computation; hosting']))
 for prefix,count in c['model_counts'].items():
  found=re.findall(r'^\| '+re.escape(prefix)+r'(\d\d) \|',s2,re.M)
  check(f'Complete {prefix} model: {count} distinct records',found==[f'{i:02d}' for i in range(1,count+1)])
 check('Evidence chain and independent knowledge/approval states',all(x in s2 for x in ['business/customer evidence\n→ message hypothesis\n→ claim\n→ substantiation / proof\n→ creative expression\n→ placement adaptation','`observed`, `supplied`, `derived`, `hypothesis`, `unknown`, `conflicted`, `not-applicable`','`pending`, `approved-for-scope`, `rejected`, `expired`, `superseded`']))
 check('Authority, actual fidelity and unknown effects preserved',all(x in s2 for x in ['A prompt is not an image; a script is not audio; a storyboard is not a movie.','I + L + A <= relevant authorised ceiling','Unknown potentially billable/mutating outcomes are reconciled using their original identity before reissuing.']) and 'A tool\'s missing catalogue entry does not establish permission loss.' in s1)
 check('Five independent lifecycle facets retained',all(f'| {x} |' in s2 for x in ['Delivery','Performance assessment','Evidence validity','Fatigue finding','Succession']))
 check('All external and Legal handoff fields retained',all(f'| Q{i:02d} ' in s2 for i in range(1,9)) and all(f'| U{i:02d} ' in s2 for i in range(1,8)) and all(f'| H{i} ' in s2 for i in range(1,9)) and all(f'J{i} ' in s2 for i in range(1,7)))
 command_blocks=re.findall(r'<!-- command:([a-z0-9-]+) -->\n(.*?)<!-- /command:\1 -->',s3,re.S)
 check('All 33 command blocks in accepted order',[n for n,b in command_blocks]==COMMANDS)
 owners=[]; complete=True
 for n,b in command_blocks:
  m=re.search(r'^Owner: (\S+)',b,re.M)
  owners.append(m[1] if m else '')
  complete=complete and all(x in b for x in ['**Inputs.**','**Operation and outputs.**','**Checks and failure.**']) and len(b)>500
 check('All 33 command contracts have substantive input/output/failure text',complete and len(command_blocks)==33)
 check('Exact skill ownership distribution 13/10/9/1',dict(Counter(owners))==c['command_owner_counts'])
 table=re.findall(r'^\| (C\d\d) \| `([^`]+)` \| `([^`]+)` \|',s3,re.M)
 check('Registry and command owner definitions agree',len(table)==33 and [x[1] for x in table]==COMMANDS and [x[2] for x in table]==owners)
 resources={}; resource_pairs=[]
 for text in texts:
  resource_pairs+=re.findall(r'<!-- resource:([a-z0-9-]+) -->\n(.*?)<!-- /resource:\1 -->',text,re.S)
 resources=dict(resource_pairs)
 check('Thirteen unique complete shared resource blocks',set(resources)==RESOURCE_NAMES and len(resource_pairs)==13 and all(len(b)>500 for b in resources.values()))
 check('Every command resource resolves without sibling skill dependency',all((m:=re.search(r'^Resources: (.+)$',b,re.M)) is not None and set(x.strip() for x in m[1].split(','))<=RESOURCE_NAMES for n,b in command_blocks))
 installed={f'consumer/skill/references/{name}.md':body for name,body in resources.items()}
 check('Extracted resource links are self-contained',not links_errors(installed,set(installed)), '; '.join(links_errors(installed,set(installed))))
 check('Installed operation and helper implementation are not falsely claimed',all(x in s3 for x in ['not a claim that the files or integrations shown below already exist','eight route/skill combinations','No hosted inference, ad account','A helper cannot manufacture an agent execution']))
 dims=re.findall(r'^### (D\d\d)\.',s4,re.M)
 check('Twelve independent evaluation dimension contracts',dims==[f'D{i:02d}' for i in range(1,13)] and all(len(section(s4,h))>450 for h in re.findall(r'^### D\d\d\..+$',s4,re.M)))
 examples=re.findall(r'^\| (E\d\d) \| (L\d) ',s4,re.M)
 check('Fifteen primary examples with exact 5-by-3 progression',[e for e,l in examples]==[f'E{i:02d}' for i in range(1,16)] and Counter(l for e,l in examples)=={f'L{i}':3 for i in range(1,6)})
 check('Actual output modalities and semantic boundaries retained',all(x in s4 for x in ['actual 1080×1080 PNG','actual 15-second 1080×1920 30-fps MP4s','Actual 20-second 48-kHz mono WAV','before.html/after.html','decoded [3,15) body identical','false/true/true/true/false']))
 check('Exact inherited suite obligations and frozen source retained',all(x in s4 for x in ['48 conditions','79 cases: 19 positive + 54 adverse + 6 cross-contract','A01 complete revision dossier; A02','G01, G02\'s two mutations, G03: four trials','eight combinations','ea4789ce26599b47c2153f970701aef2d7456877','`execution_state: not-run`']))
 check('Corrected FDE prompt, clock, backlog and cohort distinction retained',all(x in s4 for x in ['FDE-17@2','45-day lead-entry maturity','C1 is already delivered','C2/B0 consume sixteen hours','40/9/2/1','do not append the historical contradictory F prompt']))
 check('Owning-skill phases and fair comparison retained',all(x in s4 for x in ['actual active owning skill','C04\'s E10 mapping needs actual build-owned','Do not feed one condition\'s output to the other','build-only'] ) and 'no material difference' in s4)
 check('Twelve pack fields and ten full authoring steps',re.findall(r'^\| (PK\d\d) \|',s5,re.M)==[f'PK{i:02d}' for i in range(1,13)] and re.findall(r'^\| (AP\d\d) ',s5,re.M)==[f'AP{i:02d}' for i in range(1,11)])
 precedence='verified legal / standards / platform constraints\n+ explicit business / campaign requirements\n→ approved offer / audience / brand decisions\n→ selected Advertising Extension Pack\n→ core Advertising defaults'
 check('Identical original precedence in contract and catalogue',precedence in s5 and precedence in s6)
 pack_heads=re.findall(r'^### (P\d\d)\. (\S+)$',s6,re.M)
 check('All eight original pack IDs and slugs exactly once',pack_heads==[(p['id'],p['slug']) for p in c['packs']])
 fields_ok=obs_ok=neg_ok=prompts_ok=matched=True
 for p in c['packs']:
  b=section(s6,f"### {p['id']}. {p['slug']}")
  for field,label in FIELD_LABELS.items():
   m=re.search(r'\*\*'+re.escape(label)+r'\.\*\* (.*?)(?=\n\n)',b,re.S)
   fields_ok=fields_ok and bool(m) and sha256(m[1].encode()).hexdigest()==p['fields_sha256'][field]
  for i,o in enumerate(p['observables'],1):obs_ok=obs_ok and f"- {p['id']}-B{i}: {o}" in b
  for i,(challenge,expected) in enumerate(p['negatives'],1):neg_ok=neg_ok and f"| {p['id']}-N{i} | {challenge} | {expected} |" in b
  cp=prompt(s6,f"### {p['id']} core-only comparator"); pp=prompt(s6,f"### {p['id']} pack showcase")
  prompts_ok=prompts_ok and cp is not None and pp is not None
  if cp is not None and pp is not None:
   prompts_ok=prompts_ok and sha256(cp.encode()).hexdigest()==p['core_prompt_sha256'] and sha256(pp.encode()).hexdigest()==p['pack_prompt_sha256'] and len(cp)>1500 and 'synthetic and limited to this exercise' in cp
   matched=matched and cp.split('\n',1)[1]==pp.split('\n',1)[1]
  else:matched=False
 check('All 88 pack-specific contract fields retain inspected source meaning/text',fields_ok)
 check('All 24 exact pack observables retained',obs_ok and len(re.findall(r'^- P\d\d-B[123]:',s6,re.M))==24)
 check('All 16 exact negative inputs and expected repairs retained',neg_ok and len(re.findall(r'^\| P\d\d-N[12] \|',s6,re.M))==16)
 check('All 16 complete copyable prompts match captured source text',prompts_ok and len(re.findall(r'^### P\d\d (?:core-only comparator|pack showcase)$',s6,re.M))==16)
 check('All eight comparator pairs differ only in activation',matched)
 check('Catalogue maturity and 48-condition obligations are truthful',s6.count('Status: design complete; runtime not run.')==8 and '**48 actual condition executions**' in s6 and 'not completed runs or statistical reliability' in s6 and 'No runtime grammar, installed compatibility, completed showcase' in s6)
 known=set(c['baseline']['files'])|set(files)|set(c.get('_local_paths',[]))
 errs=syntax_errors(files); check('All Markdown fences and table columns valid',not errs,'; '.join(errs))
 errs=links_errors(files,known);check('All local file and named-reference targets resolve',not errs,'; '.join(errs))
 if INDEX in files:
  check('All Stage 0-17 progress content is byte-preserved',sha256(files[INDEX].split('| 18:')[0].encode()).hexdigest()==c['progress_prefix_sha256'])
  check('Progress identifies verified Stage 18 and leaves later stages unstarted',c['baseline']['commit'] in files[INDEX] and '| 20–27 | NOT STARTED |' in files[INDEX] and 'publication gate remains separate' in files[INDEX])
 if final:
  check('Substantive conformance and honest publication gate recorded',LOG in files and 'Design and document verification: PASS' in files[LOG] and 'Publication: not yet verified' in files[LOG] and '| A11 ' in files[LOG])
 return checks


def run(root: Path, partial: bool, final: bool):
 c=json.loads((root/SOURCE).read_text())
 c['_local_paths']=[str(p.relative_to(root)) for p in (root/'docs').rglob('*') if p.is_file()]
 files={p:(root/p).read_text() for p in SPECS+[LOG,INDEX] if (root/p).is_file()}
 checks=validate_contents(files,c,final)
 def add(label,ok,detail=''):checks.append({'check':label,'result':'PASS' if ok else 'FAIL','detail':detail})
 add('Captured 35-file baseline reconstructs exact remote Git tree',len(c['baseline']['files'])==35 and git_tree(c['baseline']['files'])==c['baseline']['tree'])
 add('Five recovered specification files match uploaded Git blobs',all((root/p).exists() and git_blob((root/p).read_bytes())==h for p,h in c['recovered_spec_blobs'].items()))
 absent=[]; changed=[]
 for p,m in c['baseline']['files'].items():
  if p==INDEX:continue
  if not (root/p).is_file():absent.append(p)
  elif git_blob((root/p).read_bytes())!=m['sha']:changed.append(p)
 add('Available accepted baseline bodies remain unchanged',not changed,', '.join(changed))
 add('Source-body access is complete or explicitly partial',partial or not absent,f'{len(absent)} old bodies use verified remote metadata' if partial else ', '.join(absent))
 old=root/c['pack_source']['source_path']
 if old.is_file():
  src=old.read_text(); ok=git_blob(old.read_bytes())==c['pack_source']['source_blob']
  for p in c['packs']:
   for condition,key in [('core-only comparator','core_prompt_sha256'),('pack showcase','pack_prompt_sha256')]:
    block=prompt(src,f"### {p['id']} {condition}")
    ok=ok and block is not None and sha256(block.encode()).hexdigest()==p[key]
  add('Full original source independently confirms all sixteen prompt captures',ok)
 else:
  add('Unavailable full source is not falsely claimed parsed',partial and c['pack_source']['method'].startswith('manual transcription'), 'Exact source/prompt comparison used connector content; optional whole-file re-extraction did not run')
 add('No premature production scaffold introduced',not any((root/p).exists() for p in ['skills','examples','extension-packs','benchmarks','tests','tools','integrations','.github','package.json']))
 # Each mutation is checked by the relevant content rule, not by whole-document hashes.
 mutations=[
 ('remove sixth spec',SPECS[5],lambda t:None,'Six exact canonical specification paths'),
 ('remove brief area',SPECS[1],lambda t:re.sub(r'^\| BR\.C13 .*\n','',t,flags=re.M),'Complete BR.C model'),
 ('change command owner',SPECS[2],lambda t:t.replace('Owner: advertising-pack-author','Owner: advertising-build',1),'Exact skill ownership distribution'),
 ('remove command output contract',SPECS[2],lambda t:t.replace('**Operation and outputs.**','**Omitted output.**',1),'All 33 command contracts'),
 ('break resource endpoint',SPECS[1],lambda t:t.replace('<!-- /resource:media -->','<!-- /resource:missing -->'),'Thirteen unique'),
 ('reference unavailable resource',SPECS[2],lambda t:t.replace('Resources: brief-and-evidence','Resources: nonexistent-model',1),'Every command resource'),
 ('leak repository dependency into installed resource',SPECS[0],lambda t:t.replace('<!-- resource:system-boundaries -->','<!-- resource:system-boundaries -->\n[Private source](../../research-only.md)'),'Extracted resource links'),
 ('drop dimension',SPECS[3],lambda t:t.replace('### D12. Installation integrity','### Removed. Installation integrity'),'Twelve independent'),
 ('change example level',SPECS[3],lambda t:t.replace('| E01 | L1','| E01 | L2'),'Fifteen primary'),
 ('replace audio output',SPECS[3],lambda t:t.replace('Actual 20-second 48-kHz mono WAV','Planned audio script'),'Actual output modalities'),
 ('use obsolete FDE prompt',SPECS[3],lambda t:t.replace('FDE-17@2','FDE-17@1'),'Corrected FDE prompt'),
 ('reverse precedence',SPECS[4],lambda t:t.replace('→ selected Advertising Extension Pack\n→ core Advertising defaults','→ core Advertising defaults\n→ selected Advertising Extension Pack'),'Identical original precedence'),
 ('remove pack contract field',SPECS[5],lambda t:t.replace('**Evaluate effect.**','**Omitted effect.**',1),'All 88 pack-specific'),
 ('drop pack observable',SPECS[5],lambda t:re.sub(r'^- P01-B1:.*\n','',t,flags=re.M),'All 24 exact'),
 ('alter negative instruction',SPECS[5],lambda t:t.replace('Change the price to a monthly GBP 40 subscription because it should improve lifetime value.','Approve all price changes.',1),'All 16 exact negative'),
 ('alter one comparator fact',SPECS[5],lambda t:t.replace('offers a two-hour online workshop and workbook to UK adults for GBP 40 total','offers a two-hour online workshop and workbook to UK adults for GBP 45 total',1),'All eight comparator'),
 ('truncate copyable prompt',SPECS[5],lambda t:t.replace('Fixture SYN-DR-15@1 offers','See the earlier fixture. SYN-DR-15@1 offers',1),'All 16 complete'),
 ('invent mature catalogue',SPECS[5],lambda t:t.replace('Status: design complete; runtime not run.','Status: mature; all runtime tests passed.',1),'Catalogue maturity'),
 ('break documentation link',SPECS[0],lambda t:t.replace('(02-advertising-production-skills-workflows-and-artifacts-spec.md)','(missing-spec.md)',1),'All local file'),
 ('remove table column',SPECS[5],lambda t:t.replace('| ID | Selected grammar | Distinct decision problem | Current evidence |','| ID | Selected grammar | Current evidence |'),'All Markdown'),
 ('rewrite accepted progress',INDEX,lambda t:t.replace('Stage 1 log','Changed earlier work',1),'All Stage 0-17'),
 ]
 for name,path,transform,expected_check in mutations:
  altered=deepcopy(files); result=transform(altered[path])
  if result is None:del altered[path]
  else:altered[path]=result
  findings=validate_contents(altered,c,final)
  add('Negative mutation rejected: '+name,any(x['result']=='FAIL' and x['check'].startswith(expected_check) for x in findings),expected_check)
 missing_report_contract=deepcopy(c)
 missing_report_contract['_local_paths']=[p for p in c['_local_paths'] if p!=REPORT]
 report_path_findings=validate_contents(files,missing_report_contract,final)
 add('Negative mutation rejected: missing actual non-Markdown report path',any(x['result']=='FAIL' and x['check']=='All local file and named-reference targets resolve' for x in report_path_findings))
 failures=[x for x in checks if x['result']=='FAIL']
 all_inputs=SPECS+[SOURCE,LOG,INDEX,SELF]
 report={'scope':'Stage 19 specification content, integrity and mutation checks only; no installed Agent Skills, generated media, live campaigns or installation tests',
 'result':'FAIL' if failures else 'PASS','publication':'NOT_VERIFIED','runtime_execution_state':'not-run',
 'accepted_head':c['baseline']['commit'],'accepted_tree':c['baseline']['tree'],
 'count':len(checks),'negative_mutations':len(mutations)+1,'checks':checks,
 'specifications':6,'commands':33,'resources':13,'packs':8,'complete_pack_prompts':16,'pack_observables':24,'pack_negative_inputs':16,
 'retained_suite_obligations':c['suite_counts'],'metadata_only_old_source_paths':absent,
 'input_blobs':{p:git_blob((root/p).read_bytes()) for p in all_inputs if (root/p).is_file()}}
 out=root/REPORT;out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 # Verify saved report and every reported byte identity; no report self-hash recursion.
 saved=json.loads(out.read_text())
 assert saved['count']==len(saved['checks'])
 assert all(git_blob((root/p).read_bytes())==h for p,h in saved['input_blobs'].items())
 print(json.dumps({'result':report['result'],'checks':len(checks),'mutations':len(mutations)+1,'failures':failures,'report':str(out)},ensure_ascii=False,indent=2))
 return bool(failures)

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--root',type=Path,default=Path.cwd())
 parser.add_argument('--partial',action='store_true',help='Explicitly permit old source bodies known only through the verified remote tree')
 parser.add_argument('--final',action='store_true',help='Require final substantive conformance log')
 args=parser.parse_args()
 try:sys.exit(1 if run(args.root.resolve(),args.partial,args.final) else 0)
 except (OSError,ValueError,KeyError,AssertionError) as exc:
  print('Verification could not complete: '+str(exc),file=sys.stderr);sys.exit(2)
