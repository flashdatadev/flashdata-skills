# FlashData Skills

[简体中文](README.zh-CN.md) · [FlashData CLI](https://github.com/flashdatadev/flashdata-cli) · [API docs](https://flashdata.dev/docs)

Give your AI agent Google Search and YouTube data: web results, video metadata, transcripts and bulk exports.

## Install

Install the CLI with [uv](https://docs.astral.sh/uv/), then set up your agent:

```sh
uv tool install flashdata-cli
flashdata setup
```

Choose Codex, Claude Code or Cursor and confirm the project directory. Setup installs 16 CLI skills and configures access without a paid query. MCP is optional.

**Try before signing up.** Eligible new users can start with temporary access and limited Credits for Google Search and YouTube metadata. Setup reuses existing credentials; if you have a key, run `flashdata auth login` first. See [account setup](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/onboarding.md) for trial limits and signing up later.

[Other CLI installers](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/installation.md) include pip, uv pip, Homebrew, APT, RPM and standalone downloads.

## Use

Ask your agent for the result you need:

- “Search for recent battery recycling research and include source links.”
- “Find three YouTube videos about this topic and summarize their available transcripts with timestamps.”
- “Export metadata for the video IDs in this file to JSONL.”
- “Deliver MP3 audio for these videos to my configured bucket.”

Skills use plain text for individual query content; ask for Markdown or structured JSON when needed. Bulk exports stay **JSONL**. Downloads require owner access and your cloud storage destination; exported rows contain delivery receipts. See the [bulk guide](skills/flashdata/references/bulk.md).

Data queries use Credits. Tell your agent your budget, or check the allowance with `flashdata account balance`.

## Available skills

| Skill | Purpose |
| --- | --- |
| [flashdata](skills/flashdata/SKILL.md) | CLI setup, queries and bulk workflows |
| [google-search](skills/google-search/SKILL.md) | Google web search |
| [google-news](skills/google-news/SKILL.md) | News results and coverage |
| [google-image-search](skills/google-image-search/SKILL.md) | Image discovery |
| [google-shopping](skills/google-shopping/SKILL.md) | Products and merchant offers |
| [google-video-search](skills/google-video-search/SKILL.md) | Video discovery across websites |
| [google-places](skills/google-places/SKILL.md) | Local businesses and places |
| [youtube-search](skills/youtube-search/SKILL.md) | YouTube video search |
| [youtube-extended-search](skills/youtube-extended-search/SKILL.md) | Larger YouTube search result sets |
| [youtube-metadata](skills/youtube-metadata/SKILL.md) | Video details, statistics and chapters |
| [youtube-transcript](skills/youtube-transcript/SKILL.md) | Available transcripts and timestamps |
| [youtube-captions](skills/youtube-captions/SKILL.md) | Uploader captions |
| [youtube-channel](skills/youtube-channel/SKILL.md) | Channel profiles and uploads |
| [youtube-autocomplete](skills/youtube-autocomplete/SKILL.md) | Search suggestions |
| [youtube-license-check](skills/youtube-license-check/SKILL.md) | License-label classification |
| [youtube-download](skills/youtube-download/SKILL.md) | Media delivery to customer storage |
| [flashdata-mcp](skills/flashdata-mcp/SKILL.md) | Optional web and video research through MCP |

## Setup options

Install for a specific agent across your projects:

```sh
flashdata setup --agent codex --global --non-interactive
```

Use `--skill google-search` to select one skill. `--skip-auth` installs skills offline without creating access or changing credentials; queries still need configured access. See [agent setup](https://github.com/flashdatadev/flashdata-cli/blob/main/docs/agent-setup.md) for project directories and other agents.

For MCP, use the optional [flashdata-mcp skill and connection guide](skills/flashdata-mcp/references/connection.md). It is not part of the default 16-skill installation.

For manual installation, copy a skill's entire directory, including its references, assets and scripts. Install the CLI separately.

## Upgrade

```sh
uv tool upgrade flashdata-cli
flashdata setup
```

Setup refreshes unmodified skills and preserves local edits. If you used another installer, upgrade the CLI with that installer before rerunning setup.

[Contributing and tests](CONTRIBUTING.md) · [Report an issue](https://github.com/flashdatadev/flashdata-skills/issues) · [Security](SECURITY.md) · [MIT license](LICENSE)
