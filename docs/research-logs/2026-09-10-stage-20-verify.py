#!/usr/bin/env python3
"""Stage 20 document checks only. No installer, host, advertising or paid operation runs."""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, posixpath, re, subprocess, sys
from pathlib import Path

P='docs/research-logs/2026-09-10-stage-20-'
COPY=P+'public-readme.md'; INPUT=P+'inputs.json'; LOG=P+'readme-design.md'; REPORT=P+'verification.json'; INDEX='docs/research-logs/README.md'
HEADS=['What the design covers','Business Building boundary','Truthful and policy-aware advertising','Installation','Quick start','Learn by Producing','Skills','Extension Packs','Execution layer and specialist handoffs','Measurement, optimisation and learning','Benchmarks and evidence','Canonical stress tests','Documentation','Boundaries','Contributing and support','Licence and third-party rights']
SKILLS=['advertising-build','advertising-optimise','advertising-evaluate','advertising-pack-author']

def blob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def digest(text):return hashlib.sha256(text.encode()).hexdigest()
def clean(text):return re.sub(r'^```[^\n]*\n.*?^```\s*$', '', text, flags=re.S|re.M)
def anchor(s):return re.sub(r'[^\w\- ]','',s.lower()).replace(' ','-')
def targets(text):return re.findall(r'\[[^\]]+\]\(([^)]+)\)',clean(text))
def resolve(path,target):
 if re.match(r'^[a-z]+:',target):return None
 file,sep,frag=target.partition('#')
 name=posixpath.normpath(posixpath.join(posixpath.dirname(path),file)) if file else path
 return name,frag

def rebase(text):
 def change(m):
  target=m[2]
  if target.startswith('#') or re.match(r'^[a-z]+:',target):return m[0]
  name,frag=resolve(COPY,target)
  return m[1]+name+('#'+frag if frag else '')+')'
 # Current copy contains no Markdown link syntax inside its two fenced prompts.
 return re.sub(r'(\[[^\]]+\]\()([^)]+)\)',change,text)

def check_copy(text,config,files):
 checks=[]
 def check(k,ok,detail=''):checks.append({'check':k,'result':'PASS' if ok else 'FAIL','detail':detail})
 heads=re.findall(r'^## (.+)$',clean(text),re.M)
 check('All required public sections and positioning',heads==HEADS and text.startswith('# Advertising Production Skills\n\nEvidence-led advertising'))
 check('Current design-only status is explicit','**Current availability: design and research only.**' in text and 'produced learning examples and clean-consumer installation results have not yet been verified' in text and 'These are currently designed exercises' in text)
 pattern=r'^\| \[(E\d\d): ([^\]]+)\]\(([^)]+)\) \| (.+) \|$'
 entries=re.findall(pattern,text,re.M)
 check('Exactly fifteen ordered primary examples',[e[0] for e in entries]==[f'E{i:02d}' for i in range(1,16)])
 level_sections=re.findall(r'^### (L[1-5]): [^\n]+\n(.*?)(?=^### L|^Required media)',text,re.S|re.M)
 check('Exactly three primary examples in each of five levels',len(level_sections)==5 and all(re.findall(r'^\| \[(E\d\d):',b,re.M)==[e['id'] for e in config['examples'] if e['level']==lv] for lv,b in level_sections))
 expected=[('docs/research-logs/2026-09-10-stage-16-example-designs-and-prompts.md',e['anchor']) for e in config['examples']]
 check('Each example opens its inspected exact source heading',[resolve(COPY,e[2]) for e in entries]==expected)
 quick_section=text.split('## Quick start\n',1)[-1].split('## Learn by Producing\n',1)[0]
 prompts=re.findall(r'^```text\n(.*?)\n```',quick_section,re.M|re.S)
 check('Complete E01 quick start matches inspected original',len(prompts)==1 and prompts[0]==config['quick_start_prompt'] and digest(prompts[0])==config['quick_start_sha256'])
 check('Quick start states actual named skill and pack prerequisites','two named skills and their compatible selected pack to be implemented, installed and verified first' in text and 'not a sixteenth primary example' in text)
 check('Exactly four intended skills',re.findall(r'^\| `(advertising-[^`]+)` \|',text,re.M)==SKILLS)
 found=re.findall(r'^\| \[P\d\d: `([^`]+)`\]',text,re.M)
 check('Exactly eight selected pack grammars',found==config['packs'])
 check('Pack comparison is required rather than claimed complete','six conditions per pack, forty-eight across the catalogue' in text and 'no material difference' in text and 'Core remains useful without one.' in text)
 check('Actual media and inspection cannot be replaced by plans','execution must create and inspect that file; plans alone are incomplete' in text and 'A prompt, script or storyboard is not a substitute for requested final media.' in text)
 check('Commercial and legal ownership retained','Business Building or the consuming project\'s business owner decides' in text and 'Legal conclusions belong to the appropriate Legal owner' in text and 'A pack grants no new rights, data access or spending authority.' in text)
 check('Distinct outcomes and scoped repair retained',all(x in text for x in ['attribution is not incrementality','revenue is not contribution','Missing or immature data is not zero','smallest responsible layer','A recommendation to pause is not an actual pause']))
 check('All three source-aware stress subjects and corrected FDE retained',all(x in text for x in ['| Kakeibo |','| One-person FDE consultancy |','| Production Skills ecosystem |','authoritative FDE-17@2 correction','outstanding C2/B0 commitments','delivered C1']))
 check('No invented licence or contributor infrastructure','A project licence has not yet been published in this revision.' in text and 'not this repository\'s licence' in text and 'At this revision, contributions concern the documented design.' in text)
 check('No universal score or false runtime evidence','There is no universal advertising quality score.' in text and 'not a count of completed tests' in text and 'No optional integration is claimed to have been tested' in text)
 check('Ordinary use remains independent of Pactwright','ordinary use must remain standalone' in text and 'without Pactwright or an advertising account as a prerequisite' in text)
 blocks=re.findall(r'^```bash\n(.*?)\n```',text,re.M|re.S)
 syntax=True
 for b in blocks:
  result=subprocess.run(['bash','-n'],input=b,text=True,capture_output=True)
  syntax=syntax and result.returncode==0
 check('Installer examples parse as shell without execution',len(blocks)==1 and syntax)
 check('Installer source/version/host guards and selected scope',len(blocks)==1 and all(x in blocks[0] for x in ['${SKILLS_CLI_VERSION:?','${REVISION:?','${AGENT:?','--list','--skill advertising-build --skill advertising-evaluate','--agent "$AGENT" --copy']) and '--global' not in blocks[0] and '--all' not in blocks[0])
 check('Installation readiness limitation is adjacent and explicit','**No supported installation is claimed for this design-only revision.**' in text and 'not a claim that it has run here' in text)
 check('Balanced Markdown fences',len(re.findall(r'^```',text,re.M))%2==0)
 widths=[];bad=False
 for line in clean(text).splitlines()+['']:
  if line.startswith('|'):widths.append(line.count('|'))
  elif widths:bad=bad or len(set(widths))!=1; widths=[]
 check('Markdown tables have consistent columns',not bad)
 current=dict(files);current[COPY]=text
 known=set(config['baseline_files'])|set(current)
 errors=[]
 for t in targets(text):
  item=resolve(COPY,t)
  if item is None:continue
  path,frag=item
  if path.startswith('../') or path not in known:errors.append('Missing/unsafe '+t);continue
  if frag:
   if path==config['examples_source']['path']:anchors={anchor(h) for h in config['examples_source']['headings']}
   elif path in current:anchors={anchor(h) for h in re.findall(r'^#{1,6} (.+)$',clean(current[path]),re.M)}
   else:errors.append('Uninspected anchor '+t);continue
   if frag not in anchors:errors.append('Missing anchor '+t)
 check('All local README targets and anchors resolve',not errors,'; '.join(errors))
 rootcopy=rebase(text)
 check('Root adoption changes only local link locations',[(('README.md',r[1]) if r and r[0]==COPY else r) for t in targets(text) for r in [resolve(COPY,t)]]==[resolve('README.md',t) for t in targets(rootcopy)] and re.findall(r'^```text\n(.*?)\n```',rootcopy.split('## Quick start\n',1)[-1].split('## Learn by Producing\n',1)[0],re.M|re.S)==prompts)
 check('Rebasing preserves all prose and fenced content',re.sub(r'(\[[^\]]+\]\()([^)]+)\)',r'\1TARGET)',text)==re.sub(r'(\[[^\]]+\]\()([^)]+)\)',r'\1TARGET)',rootcopy))
 check('Design remains well below GitHub README truncation limit',len(text.encode())<500*1024)
 return checks

def main(root,final):
 config=json.loads((root/INPUT).read_text())
 files={str(p.relative_to(root)):p.read_text() for p in (root/'docs').rglob('*.md')}
 text=files[COPY];checks=check_copy(text,config,files)
 def add(k,ok,detail=''):checks.append({'check':k,'result':'PASS' if ok else 'FAIL','detail':detail})
 helper=root/'docs/research-logs/2026-09-10-stage-19-verify.py'
 spec=importlib.util.spec_from_file_location('stage19_identity',helper);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 add('Predecessor complete tree reconstructs verified Stage 19',mod.git_tree(config['baseline_files'])==config['accepted_tree'])
 drift=[];metadata=[]
 for path,entry in config['baseline_files'].items():
  if path==INDEX:continue
  p=root/path
  if not p.is_file():metadata.append(path)
  elif blob(p.read_bytes())!=entry['sha']:drift.append(path)
 add('All locally present preceding files remain byte-identical',not drift,', '.join(drift))
 add('Actual root README is preserved',blob((root/'README.md').read_bytes())==config['baseline_files']['README.md']['sha'])
 index=(root/INDEX).read_text()
 add('Stage 0-18 progress is byte-preserved',digest(index.split('| 19:')[0])==config['progress_prefix_sha256'])
 add('Progress records actual Stage 19 and leaves Stage 21 onward unstarted',config['accepted_commit'] in index and '| 21–27 | NOT STARTED |' in index and '| 20: Public README design |' in index)
 topic_text=files[LOG].split('## Topic-to-copy conformance\n',1)[-1].split('## Publication design',1)[0]
 topics=re.findall(r'^\| ([^|]+) \|',topic_text,re.M)[1:]
 add('Conformance covers all seventeen source topics',[x.strip().lower().replace('×','x') for x in topics]==[x.lower() for x in config['topics']])
 known=set(config['baseline_files'])|{str(p.relative_to(root)) for p in root.rglob('*') if p.is_file()}
 link_errors=mod.links_errors({LOG:files[LOG],INDEX:index},known)
 add('Research records and progress resolve all local links',not link_errors,'; '.join(link_errors))
 if final:add('Substantive design acceptance recorded', 'Design acceptance: PASS' in files[LOG])
 mutations=[
 ('missing primary example',lambda t:re.sub(r'^\| \[E15:.*\n','',t,flags=re.M),'Exactly fifteen'),
 ('wrong level distribution',lambda t:t.replace('### L2: Coherent creative test','### L1: Coherent creative test'),'Exactly three'),
 ('wrong prompt price',lambda t:t.replace('GBP 25 total, one-off.','GBP 10 total, one-off.',1),'Complete E01'),
 ('missing quick-start prerequisites',lambda t:t.replace('two named skills and their compatible selected pack to be implemented, installed and verified first','no installed resources'),'Quick start states'),
 ('missing skill',lambda t:t.replace('| `advertising-pack-author` |','| `advertising-universal` |'),'Exactly four'),
 ('wrong pack',lambda t:t.replace('[P08: `creator-native-social-campaign`]','[P08: `universal-ad-pack`]'),'Exactly eight'),
 ('unsupported current maturity',lambda t:t.replace('**Current availability: design and research only.**','**Current availability: mature and benchmarked.**'),'Current design-only'),
 ('unverified install claimed ready',lambda t:t.replace('**No supported installation is claimed for this design-only revision.**','**All hosts are supported now.**'),'Installation readiness'),
 ('broken source anchor',lambda t:t.replace('#e01-local-inspection-search-unit','#missing-example'),'All local README'),
 ('missing specification target',lambda t:t.replace('(../01-advertising-production-skills-system-spec.md)','(../missing-spec.md)',1),'All local README'),
 ('invented licence',lambda t:t.replace('A project licence has not yet been published in this revision.','This repository is MIT licensed.'),'No invented licence'),
 ('dropped actual media requirement',lambda t:t.replace('execution must create and inspect that file; plans alone are incomplete','plans are sufficient'),'Actual media'),
 ]
 for label,mutation,rule in mutations:
  result=check_copy(mutation(text),config,files)
  add('Mutation rejected: '+label,any(x['result']=='FAIL' and x['check'].startswith(rule) for x in result))
 paths=[COPY,INPUT,LOG,INDEX,P+'verify.py']
 report={'stage':20,'scope':'README design, source projection, Markdown/reference and shell-syntax checks only','result':'PASS' if all(c['result']=='PASS' for c in checks) else 'FAIL','checks':checks,'count':len(checks),'negative_mutations':len(mutations),'runtime_tests':'not-run','installer_execution':'not-run; bash -n syntax checks only','publication':'requires subsequent actual remote readback','metadata_only_prior_paths':metadata,'input_blobs':{p:blob((root/p).read_bytes()) for p in paths}}
 (root/REPORT).write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
 (root.parent/'stage20-root-readme-preview.md').write_text(rebase(text))
 print(json.dumps({'result':report['result'],'checks':len(checks),'mutations':len(mutations),'failures':[c for c in checks if c['result']=='FAIL']},ensure_ascii=False,indent=2))
 return report['result']=='PASS'

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=Path('.'));parser.add_argument('--final',action='store_true');args=parser.parse_args()
 try:sys.exit(0 if main(args.root.resolve(),args.final) else 1)
 except (OSError,ValueError,KeyError) as error:print(str(error),file=sys.stderr);sys.exit(2)
