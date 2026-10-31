# Handoff — Learn-Project cleanup & restructure

Date: 2026-10-31
Repo: `Knuxy92/Learn-Project` (PUBLIC on GitHub)
Local: `/home/pavarut/.zcode/workspace/draft-b0806f2f-18cf-4d82-8568-653f7f521a34/Learn-Project`
Branch: `Friends` (not yet pushed at handoff time; user then asked to push)

## Context

Personal JS/TS/backend learning project, ~5 months old, being handed to a Thai friend.
Original repo was dirty: private chat logs, machine-specific paths, personal name in sample data, mixed EN/TH docs, TypeScript + SQLite chapters.

Two commits on `Friends` carry all work — read them instead of re-deriving:

- `3513fc8` — "Clean repo for sharing: remove private logs, translate docs to Thai, fix tests"
- `a68e486` — "Restructure curriculum: JavaScript-only, ending at Express backend"

`git show --stat` on each gives the full file-level picture.

## Final shape

23 chapters, JavaScript only (ESM), ending at an Express backend final project.
Track and per-chapter status live in `CURRICULUM_TRACK.md` and `CHAPTER_STATUS.md` — those are the source of truth, do not restate them here.

Key decisions already made (do not relitigate without the user):

- TypeScript fully removed, including toolchain (`tsconfig.json`, `ts-node`, `typescript`, `typescript-eslint`).
- SQLite chapters removed entirely; persistence is JSON files only.
- `package.json` is `"type": "module"`; all imports need explicit `.js`.
- Sample name is `Student` (replaced the real username everywhere).
- Exercise stubs intentionally fail (`assert.fail`) so the student knows what to solve; `pnpm test` therefore only runs reference tests, not exercise tests.

## Verified state

- `pnpm test` → 12/12 pass
- `pnpm lint` → 0 errors
- Chapter examples Ch1–Ch12 run clean; servers in Ch17–Ch21 start
- `exercises/final-task-api/` is an empty skeleton on purpose (student builds it in Ch23)

## Known open items

1. **Git history still contains the removed private files** (`content.md`, `22/*.jsonl`). They were deleted on the branch but remain reachable in `main`'s history. Backups of those files live in `/tmp/learn-project-backup/` on this machine. Removing them for real requires history rewrite + force push — NOT done, and the user has not approved it.
2. **Repo is public.** User was told it may be worth making private before sharing; no action taken.
3. `main` is 2 commits behind `Friends`; no merge has been performed.

## Suggested skills for the next session

- `codebase-memory` — if further structural work is needed, index the repo rather than grepping.
- `subagent-fanout` — the doc-translation and chapter-conversion passes both used parallel subagents effectively; reuse for any bulk per-file work.
- `write-thai` — all user-facing docs are Thai; use for any new prose.
- `git-checkpoint` — before any further restructuring or history rewrite.
- `zero-trust` — relevant if the user asks to clean history or make the repo private, since both touch data exposure.
