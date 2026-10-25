---
name: flashdata
description: Use FlashData for Google search, YouTube data and media downloads in app development, research and personal automation. Reuses API-key access or manages temporary access, human claiming, credential handoff and recurring queries through the standalone CLI. Does not install MCP or manage billing.
---

# FlashData

Use the standalone `flashdata` executable. Coding and personal agents share the
same flow; `--audience coding|personal` is descriptive, not a permission boundary.

## Released tools and discovery

- CLI **v1.1.2** for Linux, macOS and Windows:
  https://github.com/flashdatadev/flashdata-cli/releases/tag/v1.1.2
  Use the archive matching the OS/CPU, verify its SHA-256 against `SHA256SUMS`,
  and use its `flashdata` (`flashdata.exe` on Windows). No Node.js or Python runtime
  is required. Installation: https://flashdata.dev/docs/guides/flashdata-cli/reference.md
- For Go application code, SDK **v1.1.0**, Go 1.25+:
  `go get github.com/flashdatadev/flashdata-go@v1.1.0`.
  https://github.com/flashdatadev/flashdata-go/releases/tag/v1.1.0
  The SDK does not persist credentials, schedule tasks or supply the CLI run journal;
  use it when the application owns those responsibilities.

Read https://flashdata.dev/auth.md. Run `flashdata --version`, then
`flashdata discover --json --non-interactive`. For new registration, require live
onboarding `protocolVersion: 2` and `available: true`; do not assume deployment.
Default trusted origins are https://api.flashdata.dev (management),
https://data.flashdata.dev (data) and https://flashdata.dev (browser).
Override them only for an explicitly configured deployment.

## Agent output

For search, query and completed-result reads used by an agent, request Markdown with
`--accept text/plain --respond-with markdown --json=false`. Use `--accept text/plain` alone for
readable original fields. Keep `--json` and the default API representation when a
program needs structured fields or when reading auth, discovery and run metadata.
For async work, use these content options with `--wait` or `jobs result`;
submission and status reads accept only `--accept`. These response choices do not
change billing or submit another query.

## Reuse and protect access

Reuse a valid configured key or saved owner profile first. `flashdata auth status`
verifies access. An explicit `FLASHDATA_API_KEY` overrides the saved key for that
command; select the intended access before checking a saved connection. Existing
owners can use `flashdata auth login` with hidden terminal input, or have their
secret manager supply stdin to `auth login --api-key-stdin --non-interactive`.
Never request a key in chat or put it in command arguments.

Use one absolute private persistent `--state-dir` and the same `--profile` on every
command; defaults are `~/.flashdata` and `default`. Examples below use `research`.
Replace `/absolute/private/flashdata` with an absolute path on the host OS.

Windows uses DPAPI, macOS Keychain, and Linux a desktop keyring when available.
For a new headless Linux profile, auto storage can fall back to a private plaintext
file (0600; directories 0700). Use `--credential-store os` when OS protection is
required. Existing encrypted profiles never silently downgrade. Inspect
`credentialProtection` in status; never print/read vault contents into conversation.
Do not copy protected state to another OS identity or machine.

For legacy script state, use `flashdata auth migrate --from /absolute/legacy-state/connection.json`
with the intended profile/state directory. Preserve execution history; do not start
another trial to replace or bypass missing, expired, revoked or exhausted access.
Legacy `.cjs` helpers are not required for this skill; use the standalone executable.

## Temporary access and first task

Read the current permission catalog at
https://api.flashdata.dev/v2/agent-connections/capabilities:
`permissions` describes `source`, `product`, `trialEligible`, `ownerAllowed` and
`requiresStorageDestination`. Request only sources the task needs. Owner permission
and trial eligibility differ; `sources list` checks the current key's usable sources.

**Published-client boundary:** CLI v1.1.2 and Go SDK v1.1.0 registration still require
at least one of `google_search`, `youtube_search`, `youtube_metadata`,
`youtube_transcript` or `youtube_captions`. Their typed capabilities do not expose
the permission catalog; read that metadata through HTTP. Mixed requests can include
owner-only sources such as `youtube_download`, which become usable after approval.
For a Download-only task, use the HTTP onboarding protocol from `auth.md` with
protected host storage, or import an owner key with that scope. Do not add an
unneeded trial source just to satisfy client validation. The HTTP flow supports
`nextAction: claim` with empty trial scopes; proceed directly to claiming.

For a new CLI profile without access:

```bash
flashdata init --name "Research assistant" --client codex --audience coding --scopes google_search,youtube_metadata --state-dir /absolute/private/flashdata --profile research --json --non-interactive
flashdata search "battery recycling research" --num 5 --accept text/plain --respond-with markdown --run-id first-research --state-dir /absolute/private/flashdata --profile research --json=false --non-interactive
```

Use the actual host label, e.g. `--client openclaw`, when known; otherwise omit
`--client` to use `flashdata-cli`. Registration saves its proof and exact input
before sending. Recover a lost response with the same state and unchanged input.
On 429, honor `Retry-After`; never change the IP, proof, profile or counters to
obtain another allowance.

The CLI saves the ordinary temporary API key privately. Explain the allowance
using returned `trialCredits` and `trialRequestCounts` (also exposed as
`startingAllowanceCredits` and `startingAllowanceRequestEquivalents`). Discovery
reports the current offer at `trial.requestCounts`. Each per-source count spends
the full shared starting allowance; these are not separate quotas or requests
remaining. Omit numeric request claims if price metadata is unavailable. Normal
Data API queries apply the temporary account's scopes, balance and limits.

## Human claim and credential handoff

```bash
flashdata auth claim --state-dir /absolute/private/flashdata --profile research --json --non-interactive
# After human browser approval:
flashdata auth finish --wait --timeout 10m --state-dir /absolute/private/flashdata --profile research --json --non-interactive
flashdata auth status --state-dir /absolute/private/flashdata --profile research --json --non-interactive
```

Show the claim URL and separate eight-digit confirmation code; never put the code
or API credentials in the URL. Claim links last 15 minutes, capped by trial expiry;
generate one when the user is ready. An existing signed-in account is the owner
shown on consent. For a new-account test, use a private window. New users sign up
and verify email; the signup browser resumes claiming automatically. Code entry
and consent share one page. The human handles signup, verification, legal acceptance,
source selection and explicit shared-balance approval; do not approve for them.

Consent covers purchased credits too, has no separate per-key spending cap, and
does not buy credits. Owners can reduce the original scope request, not add sources.
Approval closes the temporary account and revokes its key; unused temporary credits
do not transfer. Verified-signup credits follow the normal account offer separately;
read `account balance` rather than promising a fixed grant.

`auth finish` saves the owner key, verifies it in a fresh instance of the same
executable, and acknowledges installation. Require installed owner access and
`recurringAllowed: true` before recurring work. An unacknowledged key expires after
24 hours; ACK removes that installation expiry. Resume an interrupted handoff with
the same profile and state, never a replacement trial. Keys never belong in chat.

YouTube Download requires approved owner access and a configured storage destination.
Use the normal asynchronous download workflow and account pricing; trial request
equivalents do not cover downloads. Claiming does not create MCP OAuth or authorize
payment. For host-managed MCP OAuth, follow
https://flashdata.dev/docs/integrations/codex/reference.md or
https://flashdata.dev/docs/integrations/openclaw/reference.md; OAuth tokens are not REST keys.

## Recurring tasks and revocation

The host owns scheduling. Configure only work the user requests. Keep executable,
input-file and state-directory paths, profile, task name, schedule and timezone in
the host configuration; never API keys. Use the same OS identity and persistent state.

```bash
flashdata query --recurring --input /absolute/path/daily-research.json --run-id daily-research:2026-10-24:Asia-Shanghai --state-dir /absolute/private/flashdata --profile research --json --non-interactive
```

That run ID identifies one occurrence. Reuse it on retry; use a new dated slot ID
only for the next intended execution. Each fresh process reloads the owner key and
checks live access. A successful repeated ID returns `cached: true` without another
paid submission. Dispatch intent is persisted first; uncertain or failed work is
not automatically resent. Protection is local to the original journal, not a server
replay guarantee or coordination across hosts. Do not erase history to retry work.

Stop on 401/403 (missing or revoked access), 402 (credits), 429 (rate limit), unknown
outcomes or run-input conflicts. Preserve evidence and follow recovery instructions;
never replenish a trial, buy credits, or invent a fresh ID to repeat uncertain work.
`runs recover` reads known accepted work without submitting replacement work.

Revoke the named connection in https://flashdata.dev/app/settings/connections.
After revocation, `auth status`, cached query replay, `runs show RUN_ID --result`
and new recurring requests fail live access checks. Local history remains, and
direct Data API calls with the revoked key are rejected. `auth logout` only removes
local credentials; it does not revoke remote access. Inspect metadata with
`runs list`; do not bypass the client's revoked-access check by reading result files.
