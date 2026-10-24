# Contributing

Keep each skill self-contained under `skills/<name>/`. Its SKILL.md frontmatter
must provide a matching `name` and a clear `description`. Put supporting material
inside that skill's `references/` directory and use relative links.

Run `python3 scripts/validate.py` with Python 3.10+ before submitting changes.
Review examples against the documented API and preserve source citations, budget
handling and credential boundaries. Tests must not submit paid API queries.

Update both README languages when changing installation or the skill catalog.
Shared skills also have compatibility copies in flashdatadev/flashdata-mcp for
existing client plugins; update those copies in a corresponding change and run
that repository's plugin synchronization check. Do not assume that publishing
source updates npm packages or marketplace listings.
