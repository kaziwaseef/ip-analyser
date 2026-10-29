from pathlib import Path
import hashlib
import json
import re

base = Path(__file__).resolve().parents[3]
run = base / 'markets/us/runs/2026-10-21-01'
result_path = run / 'outputs/verification.json'
if not result_path.exists():
    result_path.write_text('{}\n')
issues = []
sources = json.loads((base / 'evidence/sources.json').read_text())
ids = [entry['id'] for entry in sources]
if len(ids) != len(set(ids)):
    issues.append('duplicate source IDs')
source_files_checked = 0
for source_id in ['S-233', 'S-234']:
    entry = next(entry for entry in sources if entry['id'] == source_id)
    for record in entry['files']:
        data = (base / record['path']).read_bytes()
        source_files_checked += 1
        if len(data) != record['bytes'] or hashlib.sha256(data).hexdigest() != record['sha256']:
            issues.append(source_id + ' hash/size mismatch')
hashes = json.loads((run / 'inputs/hashes.json').read_text())
workspace = base.parents[1]
for record in hashes:
    target = run / record['snapshot'] if record.get('snapshot') else workspace / record['source']
    data = target.read_bytes()
    if len(data) != record['bytes'] or hashlib.sha256(data).hexdigest() != record['sha256']:
        issues.append('input hash mismatch: ' + str(target))
documents = list(run.glob('*.md')) + list((run / 'outputs').glob('*.md'))
documents += list((base / 'supplier-requests/2026-10-21-02').glob('*.md'))
documents += [base / name for name in ['AGENTS.md', 'overview.md', 'product.md', 'features.md', 'intake.md', 'rights.md', 'tool-register.md', 'decision-log.md']]
links_checked = 0
for document in documents:
    for target in re.findall(r'\]\(([^)]+)\)', document.read_text()):
        target = target.strip('<>').split('#', 1)[0]
        if not target or '://' in target:
            continue
        links_checked += 1
        if not (document.parent / target).resolve().exists():
            issues.append('missing link: ' + str(document) + ' -> ' + target)
overview = (base / 'overview.md').read_text()
recent = overview.split('## Recent changes', 1)[1].split('## Old change summary', 1)[0]
recent_count = len(re.findall(r'^### ', recent, re.M))
if recent_count != 10:
    issues.append('changelog count: ' + str(recent_count))
capture = json.loads((base / 'evidence/raw/US11289248B2-identity-check-2026-10-21.json').read_text())
identity = json.loads(capture['result']['result'])
if 'magnetocaloric' not in identity['title'].lower() or 'LaFe' not in identity['claims']:
    issues.append('unexpected patent identity capture')
message = (base / 'supplier-requests/2026-10-21-02/message.md').read_text().split('---\n', 1)[1]
result = {
    'date': '2026-10-21',
    'source_entries': len(sources),
    'new_source_files_checked': source_files_checked,
    'input_and_reused_hashes_checked': len(hashes),
    'local_links_checked': links_checked,
    'overview_recent_changes': recent_count,
    'supplier_message_words': len(message.split()),
    'US11289248_identity_checked': identity['title'],
    'issues': issues,
}
result_path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n')
print(json.dumps(result, indent=2, ensure_ascii=False))
raise SystemExit(bool(issues))
