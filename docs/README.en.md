# NovelOS English Guide

NovelOS is an AI workspace for planning, writing, reviewing, and maintaining million-word fiction. It keeps characters, world rules, timelines, foreshadowing, and writing state in evidence-backed memory, then routes work through editorial agents, debate, evaluation, and audited memory commits.

**Editor Mode** is the default: analysis, planning, review, and revision decisions. **Creator Mode** is explicitly authorized by the author for scene drafting, chapter drafting, expansion, or rewriting. Drafts pass self-review and revision before an author-confirmed Memory Commit.

## Quick start

```bash
git clone https://github.com/kdc307950-art/novelos_skill.git
cd novelos_skill
python test.py
```

Expected output:

```text
5 benchmarks
Passed: 5
Failed: 0
```

Latest archive: [NovelOS v3.10.1](https://github.com/kdc307950-art/novelos_skill/releases/latest)

## GUI Alpha

```bash
python interfaces/gui/server.py
```

Open <http://127.0.0.1:8765>. The GUI provides project status, chapter editing, an editor panel, and a Memory overview.

## MCP Alpha

```bash
python -m interfaces.mcp.server
```

Client configuration:

```json
{
  "mcpServers": {
    "novelos": {
      "command": "python",
      "args": ["-m", "interfaces.mcp.server"],
      "cwd": "/absolute/path/to/novelos_skill"
    }
  }
}
```

The adapter exposes 10 tools, 5 resources, and 5 prompts. `update_memory` returns a proposal until confirmed. `generate_scene` and `rewrite_scene` additionally require `mode="creator"` and `confirm=true`.

## Core workflow

```text
Task classification → Runtime → Orchestrator → Memory Retrieval
→ Editorial or Creator Agents → Debate → Decision → Evaluation
→ Self Review → Proposal → Author Confirmation → Memory Commit
```

## Data and validation

- 3,000 pending Benchmark Suite quota
- 1,000 pending Golden Dataset queue
- Provenance, licenses, splits, confidence, and human review status
- A/B comparison, blind review, statistics, ablation, and failure analysis

Synthetic pending data is never presented as human-verified evidence. See the [dataset guide](../dataset/literary_benchmark/README.md), [contribution guide](../CONTRIBUTING.md), and [security guide](../SECURITY.md).

## Repository map

| Directory | Purpose |
| --- | --- |
| `runtime/` | Execution, state, logs, and Memory Commit |
| `memory/` | Canon, character, scene, writing state, and snapshots |
| `creator_engine/` | Scene planning, writing, style, self-review, and revision |
| `interfaces/gui/` | Author workspace |
| `interfaces/mcp/` | AI client integration |
| `evaluation/`, `benchmark_suite/` | Quality evaluation and benchmarks |

The project is MIT licensed. Third-party datasets keep their own licenses and attribution requirements.
