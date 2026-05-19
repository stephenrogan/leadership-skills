#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
try:
    import yaml
except Exception:
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
REQUIRED_SECTIONS = ['Overview','When to Use','Inputs','Workflow','Output Format','Human Decision Boundary','Quality Bar','Failure Modes','References']
FORBIDDEN = [
    'automatically terminate', 'decide compensation', 'send the customer', 'promise the customer',
    'diagnose the employee', 'ignore hr', 'publish automatically'
]
NAME_RE = re.compile(r'^[a-z0-9]+(?:-[a-z0-9]+)*$')

def parse_skill(path):
    text = path.read_text()
    if not text.startswith('---\n'):
        raise AssertionError(f'{path}: missing YAML frontmatter')
    end = text.find('\n---\n', 4)
    if end == -1:
        raise AssertionError(f'{path}: unclosed YAML frontmatter')
    raw = text[4:end]
    body = text[end+5:]
    if yaml:
        fm = yaml.safe_load(raw)
    else:
        fm = {}
        for line in raw.splitlines():
            if ':' in line and not line.startswith(' '):
                k,v=line.split(':',1); fm[k.strip()] = v.strip().strip('"')
    return fm, body, text

def validate():
    errors = []
    skill_dirs = sorted([p for p in SKILLS.iterdir() if p.is_dir()])
    if len(skill_dirs) < 20:
        errors.append(f'Expected at least 20 skills, found {len(skill_dirs)}')
    for d in skill_dirs:
        try:
            skill = d / 'SKILL.md'
            if not skill.exists():
                raise AssertionError(f'{d}: missing SKILL.md')
            fm, body, text = parse_skill(skill)
            name = fm.get('name')
            desc = fm.get('description')
            if name != d.name:
                raise AssertionError(f'{skill}: name must match parent directory ({name} != {d.name})')
            if not name or len(name) > 64 or not NAME_RE.match(name) or '--' in name:
                raise AssertionError(f'{skill}: invalid name {name!r}')
            if not desc or len(desc) > 1024 or len(desc) < 80:
                raise AssertionError(f'{skill}: bad description length')
            if 'Use ' not in desc and 'Use when' not in desc:
                raise AssertionError(f'{skill}: description must include use trigger language')
            for field in ['license','compatibility','metadata']:
                if field not in fm:
                    raise AssertionError(f'{skill}: missing optional-but-required-by-this-repo field {field}')
            if len(body.splitlines()) > 500:
                raise AssertionError(f'{skill}: body exceeds 500 lines')
            for sec in REQUIRED_SECTIONS:
                if f'## {sec}' not in body:
                    raise AssertionError(f'{skill}: missing section {sec}')
            for phrase in FORBIDDEN:
                if phrase in text.lower():
                    raise AssertionError(f'{skill}: forbidden phrase {phrase}')
            if 'Human leader' not in text and 'human leader' not in text and 'manager owns' not in text.lower():
                raise AssertionError(f'{skill}: missing human ownership language')
            if not (d/'references'/'framework.md').exists():
                raise AssertionError(f'{d}: missing references/framework.md')
            if not (d/'assets'/'output-template.md').exists():
                raise AssertionError(f'{d}: missing assets/output-template.md')
            ep = d/'evals'/'evals.json'
            if not ep.exists():
                raise AssertionError(f'{d}: missing evals/evals.json')
            data = json.loads(ep.read_text())
            if data.get('skill_name') != name:
                raise AssertionError(f'{ep}: skill_name mismatch')
            evs = data.get('evals') or []
            if len(evs) < 4:
                raise AssertionError(f'{ep}: expected at least 4 evals')
            for ev in evs:
                for key in ['id','prompt','expected_output','assertions']:
                    if key not in ev:
                        raise AssertionError(f'{ep}: eval missing {key}')
                if len(ev['assertions']) < 4:
                    raise AssertionError(f'{ep}: eval {ev.get("id")} has too few assertions')
            prompts = ' '.join(ev.get('prompt','').lower() for ev in evs)
            if 'boundary test' not in prompts or 'messy input test' not in prompts:
                raise AssertionError(f'{ep}: missing boundary or messy-input eval')
        except Exception as e:
            errors.append(str(e))
    return errors

if __name__ == '__main__':
    errors = validate()
    if errors:
        print('VALIDATION FAILED')
        for e in errors:
            print('-', e)
        sys.exit(1)
    print('VALIDATION PASSED')
    print(f'Skills validated: {len([p for p in SKILLS.iterdir() if p.is_dir()])}')
