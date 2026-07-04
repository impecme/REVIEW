---
name: notebooklm-visual-organize
description: >-
  Generates and saves visual summaries (mind maps, slide decks, infographics)
  for materials uploaded inside a Google NotebookLM notebook.
---

# NotebookLM Visual Organizer

## Overview
This skill allows the agent to visually organize and summarize uploaded sources in a Google NotebookLM notebook by creating:
1. **Mind Maps**: Structured visual trees linking concepts, layout configurations, and AOT compilation pipelines.
2. **Slide Decks**: Presentation slides covering specific focus areas (e.g., Triton vs. TileLang transition).
3. **Infographics**: Visually formatted briefing boards describing optimization constraints.

## Dependencies
Uses the `notebooklm-mcp-cli` tools CLI client under the hood.

## Quick Start
To generate and save a mind map in notebook `32e9041a-ca86-4b21-96c4-147319601794`:
```powershell
uv run python C:\Users\27412\.gemini\config\plugins\antigravity-lazy-pack\skills\06-visual-organize-notebooklm\scripts\visual_organize.py mindmap --notebook-id 32e9041a-ca86-4b21-96c4-147319601794 --title "TileLang 算子开发知识图谱" --proxy http://127.0.0.1:7897
```

## Utility Scripts
The skill provides the `visual_organize.py` command-line utility.

### Subcommand: `mindmap`
```
usage: visual_organize.py mindmap [-h] --notebook-id NOTEBOOK_ID [--title TITLE] [--proxy PROXY]
```

### Subcommand: `slides`
```
usage: visual_organize.py slides [-h] --notebook-id NOTEBOOK_ID [--title TITLE] [--prompt PROMPT] [--proxy PROXY]
```

### Subcommand: `infographic`
```
usage: visual_organize.py infographic [-h] --notebook-id NOTEBOOK_ID [--title TITLE] [--prompt PROMPT] [--proxy PROXY]
```

## Common Mistakes
* **Authentication status**: Ensure the CLI session is valid. Run `python -m notebooklm_tools.cli.main login` if a `ClientAuthenticationError` occurs.
* **Empty Notebook**: A `ValueError` is raised if no sources are found in the notebook. Ensure files have been uploaded prior to calling these visual features.
