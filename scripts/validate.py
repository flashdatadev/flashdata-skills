"""Validate portable skill files without executing examples or using the network."""
import ast
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'


def main():
    skills = sorted(SKILLS.glob('*/SKILL.md'))
    if not skills:
        raise ValueError('No skills found')
    examples = 0
    for skill in skills:
        content = skill.read_text(encoding='utf-8')
        frontmatter = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', content, re.S)
        if not frontmatter:
            raise ValueError(f'Missing frontmatter: {skill}')
        for field in ('name', 'description'):
            match = re.search(rf'^{field}:\s*(\S[^\n]*)$', frontmatter[1], re.M)
            if not match:
                raise ValueError(f'Missing {field}: {skill}')
            if field == 'name' and match[1].strip().strip('"\'') != skill.parent.name:
                raise ValueError(f'Skill name differs from directory: {skill}')
        for path in skill.parent.rglob('*'):
            if path.is_symlink():
                raise ValueError(f'Symlinks are not portable: {path}')
            if not path.is_file() or path.suffix != '.md':
                continue
            text = path.read_text(encoding='utf-8')
            for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', text):
                url = urlsplit(target.strip('<>'))
                if url.scheme or url.netloc or not url.path:
                    continue
                resolved = (path.parent / unquote(url.path)).resolve()
                if not resolved.is_relative_to(skill.parent.resolve()) or not resolved.is_file():
                    raise ValueError(f'Missing or non-portable reference: {path} -> {target}')
            for code in re.findall(r'^```python\s*\n(.*?)^```', text, re.M | re.S):
                ast.parse(code, filename=str(path))
                examples += 1
    print(f'Validated {len(skills)} skills and {examples} Python examples; no API calls made.')


if __name__ == '__main__':
    main()
