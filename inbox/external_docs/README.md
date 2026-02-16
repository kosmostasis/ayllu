# inbox/external_docs/

**Purpose:** Landing zone for documents imported from outside the repo (Desktop, Email, shared drives, etc.).

**Rule:** No absolute paths in code, scripts, docs, or patches. External docs must be imported here first, then referenced by repo-relative path.

## Import

Run from repo root:

```bash
./scripts/import_external_docs.sh
```

Or copy manually into this folder. Update `scripts/import_external_docs.sh` to add new source paths.

## Structure

- `inbox/external_docs/<original_filename>` — imported files
- Reference as `inbox/external_docs/<filename>` from anywhere in the repo
