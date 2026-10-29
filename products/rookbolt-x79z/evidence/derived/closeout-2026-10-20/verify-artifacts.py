from pathlib import Path
import hashlib,json,re,sys
P=Path(__file__).resolve().parents[3];run=P/'markets/us/runs/2026-10-20-06';issues=[];sources=json.load(open(P/'evidence/sources.json'));ids=[s['id'] for s in sources]
if len(ids)!=len(set(ids)):issues.append('Duplicate source IDs')
rights=json.load(open(P/'rights-map.json'))
if len(rights.values())!=len(set(rights.values())):issues.append('Duplicate right IDs')
checked=0
for s in sources:
 for f in s.get('files',[]):
  p=P/f['path'];checked+=1
  if not p.is_file():issues.append(s['id']+' missing '+str(p));continue
  b=p.read_bytes()
  if f.get('bytes')!=len(b) or f.get('sha256')!=hashlib.sha256(b).hexdigest():issues.append(s['id']+' hash/size mismatch '+f['path'])
links=0
for f in list(run.glob('*.md'))+list((run/'outputs').glob('*.md'))+[P/'overview.md']:
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text()):
  target=target.strip('<>')
  if re.match(r'\w+://|#|mailto:',target):continue
  target=target.split('#')[0]
  if not target:continue
  links+=1
  if not (f.parent/target).exists():issues.append('Broken link '+str(f.relative_to(P))+' -> '+target)
# Initial frozen inputs must not have drifted.
initial=json.load(open(run/'inputs/hashes.json'));hashes=initial if isinstance(initial,dict) else {}
for rel,value in hashes.items():
 expected=value.get('sha256') if isinstance(value,dict) else value
 f=run/rel
 if not f.exists():issues.append('Frozen input missing '+rel)
 elif expected!=hashlib.sha256(f.read_bytes()).hexdigest():issues.append('Frozen initial input changed '+rel)
final_hashes=json.load(open(run/'inputs/closeout-hashes.json'))
for rel,value in final_hashes.items():
 if hashlib.sha256((run/rel).read_bytes()).hexdigest()!=value:issues.append('Final frozen input changed '+rel)
rows=json.load(open(P/'evidence/derived/closeout-2026-10-20/tm-triage-all.json'));serials=[r['serial'] for r in rows]
if len(rows)!=100 or len(set(serials))!=100:issues.append('Trademark summary count/uniqueness')
stat=json.load(open(P/'evidence/derived/closeout-2026-10-20/official-status-matrix.json'))
if len(stat)!=26:issues.append('Retained utility matrix count')
# Verify title/application/patent identity for new official case sources.
case_count=0;utility_count=0;design_count=0;fee_count=0
for s in sources:
 if int(s['id'][2:])<108:continue
 key=s.get('closeout_key','');doc=s.get('document','')
 if key.endswith('-official'):
  case_count+=1;design_count+=doc.startswith('USD');utility_count+=not doc.startswith('USD')
  fs=[P/f['path'] for f in s['files'] if f['path'].endswith('application-data.json')]
  for f in fs:
   t=json.load(open(f))['text'];docnum=re.sub(r'\D','',doc[:-2]);pub=re.sub(r'[^0-9]','',t)
   if docnum not in pub:issues.append('Official case identity '+doc+' '+f.name)
 if key.endswith('-fees'):
  fee_count+=1
  text=json.load(open(P/s['files'][0]['path']))['text'];pat=re.sub(r'\D','',doc[:-2])
  if 'PATENT #\n'+pat+'\n' not in text:issues.append('Fee patent identity '+doc)
recent=(P/'overview.md').read_text().split('## Recent changes',1)[1].split('## Old change summary',1)[0];recent_count=len(re.findall(r'^### ',recent,re.M))
if recent_count>10:issues.append('Too many overview changelog changes')
comparison=json.load(open(P/'evidence/derived/closeout-2026-10-20/R012-official-mirror-comparison.json'))
if comparison['official_claim_count']!=85 or comparison['different_claim_numbers']:issues.append('R012 official claims mismatch')
# Only template-placeholder phrases, not honest state labels, are prohibited in completed outputs.
for f in run.glob('*.md'):
 for phrase in ['Run ID: not assigned','State product revision, variants','Lead with material issues','Record reviewer or model, context separation','not checked']:
  if phrase in f.read_text():issues.append('Unfilled template '+f.name+' '+phrase)
result=dict(source_entries=len(sources),source_file_entries_checked=checked,local_links_checked=links,initial_hashes_checked=len(hashes),final_input_hashes_checked=len(final_hashes),trademark_summaries=len(rows),unique_trademark_serials=len(set(serials)),retained_utility_documents=len(stat),official_utility_case_sources=utility_count,official_design_case_sources=design_count,valid_fee_sources=fee_count,overview_recent_changes=recent_count,official_R012_claims=85,issues=issues)
(run/'outputs/artifact-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));sys.exit(bool(issues))
