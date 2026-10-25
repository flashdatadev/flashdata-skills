# Changelog

## Unreleased — CLI agent setup

- Make all 15 task skills use the CLI with plain-text output by default.
- Move optional MCP/Python examples into references and simplify setup documentation.


## 2026-10-25

- Separate the standalone CLI skill (`flashdata`) from MCP research (`flashdata-mcp`).
- Prefer Markdown for agents while retaining structured JSON for programs.
- Ship complete, self-contained Python examples that read every result chunk without repeating queries.
- Validate examples on Windows and Linux, including Unicode, expired chunks and unknown submission outcomes.

## 2026-10-24 — Initial official repository

- Published one research skill and 15 Google/YouTube task skills with their references.
- Added English and Chinese installation guides and an offline validation workflow.
- Updated the connection guide to the official FlashData MCP repository.
