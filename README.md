# Recursive Curriculum Composer

**T21-063** · `recursive-curriculum-composer`

A local deterministic curriculum prototype that composes short learning prompts, scores learner responses for plateau/context-mismatch signals, and selects the next pedagogy path from recorded evidence.

## Implemented

- Locale-aware curriculum composition with shipped `en-US` and `es-US` seed content.
- Per-learner response scoring.
- Plateau detection from zero matches or consistently short responses.
- Context-mismatch detection using deterministic locale/topic keyword checks.
- Pedagogy evolution between `scaffold-local` and `stretch`.
- SQLite state storage.
- SHA-256 hash-linked records with chain verification.
- Local HTTP proof API and browser proof surface.
- No paid API dependency.

## Proof path

The proof executes the full local sequence:

1. Compose curriculum content.
2. Score learner answers.
3. Detect plateau or mismatch.
4. Evolve the pedagogy.
5. Verify the stored record hash chain.

```bash
./boot063.sh verify
```

## Run

```bash
./boot063.sh doctor
./boot063.sh verify
./boot063.sh up
```

Default endpoint:

```text
http://127.0.0.1:8765
```

Routes:

```text
GET  /health
GET  /healthz
POST /proof
```

Use `PORT` to change the bind port and `TITAN_DB` to change the SQLite path.

## Repository layout

```text
apps/web/               browser proof surface
services/api/engine.py  curriculum, scoring, evolution logic
services/api/common.py  SQLite + SHA-256 record chain
services/api/server.py  local HTTP server
tests/test_proof.py     end-to-end proof
data/                   local state
boot063.sh              doctor / verify / up launcher
```

## Current boundary

This is a deterministic working prototype, not a general-purpose curriculum model. The shipped locale seed set is currently `en-US` and `es-US`, and mismatch detection is rule-based.

## Ownership

Owner: Julius Cameron Hill / Titan Universal AI LLC  
Watermark: `":"`
