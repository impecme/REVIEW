---
name: notebooklm-sync-workspace
description: >-
  Sync files in a local workspace directory to a specified NotebookLM notebook.
  Compares local filenames with the notebook's existing sources and uploads
  only the missing files, preventing duplicates.
---

# NotebookLM Workspace Sync

## Overview
This skill allows the agent to synchronize a workspace directory with a NotebookLM notebook, uploading only new files (like `.md` and `.png`) that are not already present in the notebook.

## Dependencies
None. Uses the `notebooklm-mcp-cli` tools CLI client under the hood.

## Quick Start
To sync the current directory to notebook `32e9041a-ca86-4b21-96c4-147319601794` via proxy:
```powershell
uv run python C:\Users\27412\.gemini\config\plugins\antigravity-lazy-pack\skills\03-upload-notebooklm\scripts\sync_notebook.py sync --notebook-id 32e9041a-ca86-4b21-96c4-147319601794 --dir d:\projectbuilding\AI_skills --proxy http://127.0.0.1:7897
```

## Utility Scripts
The skill provides the `sync_notebook.py` command-line utility.

### Subcommand: `sync`
```
usage: sync_notebook.py sync [-h] --notebook-id NOTEBOOK_ID --dir DIR [--proxy PROXY] [--exts EXTS]
```
Arguments:
* `--notebook-id`: (Required) The ID of the NotebookLM notebook.
* `--dir`: (Required) Absolute path to the directory containing files to sync.
* `--proxy`: (Optional) Network proxy URL (e.g. `http://127.0.0.1:7897`).
* `--exts`: (Optional) Comma-separated list of file extensions/globs (default: `*.md,*.png`).

## Common Mistakes
* **Authentication status**: Ensure the CLI has active credentials. Run `nlm login` if authorization errors occur.
* **Network Proxies**: Make sure the `--proxy` argument is passed if the network connection to Google services is restricted.
