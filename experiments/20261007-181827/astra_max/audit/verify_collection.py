from pathlib import Path
import os, json, hashlib, re, datetime
from urllib.parse import unquote

out = Path(__file__).resolve().parent.parent
assert out == Path('/home/fainic/data/human-agent-collaboration-rules-worktrees/20261007-181827/astra_max')
assert Path.cwd().resolve() == out
inventory = json.loads((out / 'audit/workspace-inventory.json').read_text())
selection = json.loads((out / 'audit/selection.json').read_text())
coverage = json.loads((out / 'audit/review-coverage.json').read_text())
errors = []
source_counts = {}
source_changes = []
source_mtime_changes = []
for repo in inventory['repositories']:
    root = Path(repo['source_root'])
    assert root in (Path('/home/fainic/data/research-process'), Path('/home/fainic/data/multiarm-problem-gen'))
    expected = {row['path']: row for row in repo['files']}
    actual = {}
    for current, dirs, files in os.walk(root, followlinks=False):
        dirs[:] = [d for d in dirs if d != '.git' and not (Path(current) / d).is_symlink()]
        for name in files:
            if name == '.git':
                continue
            p = Path(current) / name
            rel = p.relative_to(root).as_posix()
            if p.is_symlink():
                errors.append('Unexpected symlink: ' + str(p))
                continue
            data = p.read_bytes()
            actual[rel] = hashlib.sha256(data).hexdigest()
            old = expected.get(rel)
            if old is None or actual[rel] != old['sha256']:
                source_changes.append(str(p))
            if old and p.stat().st_mtime_ns != old['mtime_ns']:
                source_mtime_changes.append(str(p))
    for rel in set(expected) - set(actual):
        source_changes.append(str(root / rel) + ' [missing]')
    source_counts[repo['name']] = len(actual)
if source_changes:
    errors.append('Source files changed or missing since inventory')
copies = []
sections_checked = 0
for entry in selection['entries']:
    source = Path(entry['source'])
    copy = out / entry['copy']
    assert out in copy.resolve().parents
    a = source.read_bytes()
    b = copy.read_bytes()
    digest = hashlib.sha256(b).hexdigest()
    equal = a == b and digest == entry['sha256'] and len(b) == entry['size']
    independent = not copy.is_symlink() and (copy.stat().st_dev, copy.stat().st_ino) != (source.stat().st_dev, source.stat().st_ino)
    if not equal or not independent:
        errors.append('Copy mismatch or shared inode: ' + entry['copy'])
    content = b.decode('utf-8').splitlines()
    for section in entry['key_sections']:
        sections_checked += 1
        start, end = section['start'], section['end']
        if not (1 <= start <= end <= len(content)) or content[start - 1] != section['first_line']:
            errors.append('Section reference mismatch: ' + entry['copy'] + ' / ' + section['title'])
    copies.append({'path': entry['copy'], 'source': str(source), 'bytes': len(b), 'sha256': digest, 'byte_equal': equal, 'independent_regular_file': independent})
listed = {entry['copy'] for entry in selection['entries']}
actual_copies = {p.relative_to(out).as_posix() for p in (out / 'sources').rglob('*') if p.is_file()}
if listed != actual_copies:
    errors.append('Copy manifest does not match actual sources tree')
index = (out / 'INDEX.md').read_text()
links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', index)
link_rows = []
for target in links:
    value = unquote(target.split('#', 1)[0])
    p = (out / value).resolve()
    # This report is created immediately below; all other targets must already exist.
    exists = p.is_file() or p == out / 'audit/verification.json'
    inside = out in p.parents
    if not exists or not inside:
        errors.append('Invalid INDEX link: ' + target)
    link_rows.append({'target': target, 'exists': exists, 'inside_worktree': inside})
index_copies = {row['target'] for row in link_rows if row['target'].startswith('sources/')}
if index_copies != listed:
    errors.append('INDEX does not reference exactly the collected files')
covered = {(repo['name'], row['path']) for repo in coverage['repositories'] for row in repo['files']}
expected_coverage = {(repo['name'], row['path']) for repo in inventory['repositories'] for row in repo['files']}
if covered != expected_coverage:
    errors.append('Coverage inventory mismatch')
report = {
    'checked_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'result': 'PASS' if not errors else 'FAIL',
    'source_inventory_at_utc': inventory['captured_at_utc'],
    'source_current_files_checked': source_counts,
    'source_content_unchanged_since_inventory': not source_changes,
    'source_content_changes': source_changes,
    'source_mtime_changes': source_mtime_changes,
    'copied_files': len(copies),
    'copied_bytes': sum(row['bytes'] for row in copies),
    'all_copies_byte_equal_to_sources': all(row['byte_equal'] for row in copies),
    'all_copies_independent_regular_files': all(row['independent_regular_file'] for row in copies),
    'key_section_references_checked': sections_checked,
    'index_links_checked': len(link_rows),
    'unique_index_links_checked': len({row['target'] for row in link_rows}),
    'index_source_links_match_collected_files': index_copies == listed,
    'review_coverage_matches_inventory': covered == expected_coverage,
    'execution_scope_note': coverage['execution_scope_note'],
    'historical_tests_reexecuted': False,
    'historical_authorization_or_isolation_independently_proved': False,
    'source_embedded_links_rewritten': False,
    'source_embedded_link_closure_guaranteed': False,
    'errors': errors,
    'copies': copies,
    'index_links': link_rows
}
(out / 'audit/verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
assert (out / 'audit/verification.json').is_file()
print(json.dumps({k: v for k, v in report.items() if k not in ['copies', 'index_links']}, ensure_ascii=False, indent=2))
raise SystemExit(1 if errors else 0)
