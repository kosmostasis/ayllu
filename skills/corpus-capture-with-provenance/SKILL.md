# Skill: corpus-capture-with-provenance

Download Venezuela corpus (Plan País + MCM) and record provenance (URL, capture time, sha256, classification).

## Inputs

- URL list (embedded in script or config)
- Target dir: default `venezuela/corpus` (plan-pais/mesas, mcm)

## Outputs

- `venezuela/corpus/plan-pais/mesas/*.pdf`
- `venezuela/corpus/mcm/*.pdf`, `venezuela/corpus/mcm/*.html`
- `venezuela/corpus/plan-pais/provenance.yml`
- `venezuela/corpus/mcm/provenance.yml`
- `venezuela/corpus/plan-pais/INDEX.md`, `venezuela/corpus/mcm/INDEX.md` (pre-existing; hashes can be filled from provenance)

## Steps

1. Run download script from repo root: `./scripts/download_corpus.sh [OUT_DIR]`.
2. Script creates plan-pais/mesas and mcm; downloads each URL; computes sha256; writes provenance.yml with capture_time and file/sha256.
3. Commit provenance.yml and INDEX; do not commit PDF/HTML (gitignored).

## Commands

```bash
./scripts/download_corpus.sh
# or
./scripts/download_corpus.sh /path/to/out
```

## Quality checklist

- [ ] Every downloaded file has an entry in provenance.yml with sha256 and capture_time.
- [ ] Classification (Plan País vs MCM) is correct in INDEX and provenance.
- [ ] No binaries committed; only provenance and INDEX in git.

## Failure modes

- URL 404 or network error: script fails at curl; fix URL or retry.
- Capture time: script uses UTC; ensure date command supports -u.
- Re-run: provenance is overwritten with new capture time and hashes; that is intended.
