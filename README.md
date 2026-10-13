<div align="center">

<img src="assets/novelos-mark.png" alt="NovelOS" width="164" />

# NovelOS

**面向百万字长篇小说的 AI 编辑与创作工作台。**

管理世界观、人物、时间线、伏笔、章节创作和审稿流程。默认编辑，授权创作。

NovelOS is an AI-native workspace for planning, writing, reviewing, and maintaining long-form fiction.

[![Version](https://img.shields.io/badge/version-3.10.1-6366f1.svg)](CHANGELOG.md)
[![Release](https://img.shields.io/github/v/release/kdc307950-art/novelos_skill?label=download)](https://github.com/kdc307950-art/novelos_skill/releases/latest)
[![License](https://img.shields.io/badge/license-MIT-22c55e.svg)](LICENSE)
[![Benchmarks](https://img.shields.io/badge/benchmarks-3000%20pending-f59e0b.svg)](benchmark_suite/README.md)

<a href="https://github.com/kdc307950-art/novelos_skill/releases/latest">Download</a> · <a href="#gui-alpha">GUI Alpha</a> · <a href="#mcp-alpha">MCP Alpha</a> · <a href="CONTRIBUTING.md">Contribute</a>

</div>

## Why NovelOS

Long fiction needs state across chapters. NovelOS routes each request to the smallest useful set of editors, retrieves evidence from project memory, debates high impact choices, evaluates the result, and keeps proposed changes behind a commit boundary.

| Capability | What you get |
| --- | --- |
| Editorial analysis | Structure, scenes, characters, continuity, literary quality, reader and commercial review |
| Long memory | Canon, character state, timeline, foreshadowing, writing state and snapshots |
| Decision support | Multi-agent debate, options, tradeoffs, consequence prediction and revision plans |
| Creator Mode | Authorized scene drafting, chapter drafting, rewriting, self-review and style adaptation |
| Evidence | Golden datasets, benchmark suite, blind-review contracts, metrics and ablation plans |
| Integrations | GUI workspace and MCP tools, resources and prompts backed by the same Core |

## Architecture

```mermaid
flowchart LR
  U[Author or AI client] --> I[GUI / MCP]
  I --> R[Runtime Kernel]
  R --> O[Orchestrator]
  O --> M[Memory Retrieval]
  M --> A[Editorial or Creator Agents]
  A --> D[Debate and Decision]
  D --> E[Evaluation and Evidence]
  E --> C[Proposal / Confirmation / Commit]
  C --> S[Reports and Snapshots]
```

## Quick start

Clone the repository and run the dependency free checks:

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

The latest source archive is available from the [v3.10.1 release](https://github.com/kdc307950-art/novelos_skill/releases/latest).

## GUI Alpha

The GUI is a local workspace with a project dashboard, chapter editor, editor panel and Memory overview. It needs only the Python standard library.

```bash
python interfaces/gui/server.py
```

Open [http://127.0.0.1:8765](http://127.0.0.1:8765). You can paste a chapter into the editor, click **分析章节**, and see the shared Core API response. The interface starts in Editor Mode; creator actions require explicit authorization and review.

The GUI entrypoint is [interfaces/gui/server.py](interfaces/gui/server.py), with its static workspace in [interfaces/gui/static](interfaces/gui/static).

## MCP Alpha

The MCP adapter uses JSON-RPC over stdin/stdout and exposes the same Core through 10 tools, 5 resources and 5 prompts.

Start it locally:

```bash
python -m interfaces.mcp.server
```

For an MCP client configuration, point the command at the repository environment:

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

Available surfaces:

| Surface | Examples |
| --- | --- |
| Tools | `analyze_chapter`, `check_continuity`, `get_character`, `get_timeline`, `search_knowledge`, `evaluate_scene`, `generate_scene`, `rewrite_scene`, `update_memory`, `get_project_status` |
| Resources | `novelos://project/current`, `novelos://character/all`, `novelos://timeline/current`, `novelos://world/rules`, `novelos://writing/state` |
| Prompts | `novelos-review-chapter`, `novelos-plan-next-chapter`, `novelos-character-analysis`, `novelos-write-scene`, `novelos-revise-scene` |

Read tools and resources are available immediately. `update_memory` returns a proposal until `confirm=true`; `generate_scene` and `rewrite_scene` also require `mode="creator"`. This keeps GUI and MCP writes behind the same confirmation gate.

## Data and validation

NovelOS includes a 3,000-case pending Benchmark Suite, a 1,000-case Golden Dataset queue, provenance-aware ingestion tools, human annotation rubrics, blind-evaluation contracts, statistics, ablation and failure analysis.

```bash
python -m benchmark_suite.validate_suite benchmark_suite/pending
python -m dataset_factory.validator.progress golden_dataset/pending
python -m unittest discover -s tests/unit -p "test_dataset*.py"
```

Current queues are synthetic and pending human review. The repository reports framework validation separately from intelligence validation; it does not claim model superiority without fixed baselines and blind human scores.

## Repository map

| Directory | Purpose |
| --- | --- |
| `runtime/` | Executor, pipeline, state, logs and Memory Commit |
| `agents/`, `orchestrator/` | Agent contracts, routing and modes |
| `editor_engine/`, `creator_engine/` | Editor Mode and authorized Creator Mode |
| `memory/`, `memory_engine/` | Canon, runtime storage, retrieval and snapshots |
| `literary_engine/`, `literary_graph/` | Literary analysis and reusable mechanisms |
| `debate_engine/`, `decision_engine/` | Debate, options, tradeoffs and final selection |
| `evaluation/`, `evaluation_engine/` | Scoring, runners and evaluation reports |
| `benchmark_suite/`, `experiments/`, `comparison/` | Scientific validation and A/B experiments |
| `human_eval/`, `annotation/`, `evidence/` | Human review and evidence records |
| `interfaces/gui/`, `interfaces/mcp/` | Human and AI ecosystem entrypoints |

## Runtime modes

Editor Mode is the default for diagnosis, planning, review and revision decisions. Creator Mode is entered only when the author explicitly requests drafting, expansion or rewriting. Creator drafts pass through context loading, scene planning, generation, self-review, revision and author confirmation before Memory Commit.

## Contributing

Start with [CONTRIBUTING.md](CONTRIBUTING.md). New agents must follow [agents/interface.md](agents/interface.md); new data must include provenance, license, split, labels and review status. See [SECURITY.md](SECURITY.md) before sharing unpublished text or author feedback.

## Project documents

[Skill entry point](SKILL.md) · [Changelog](CHANGELOG.md) · [V3.6 dataset](dataset/literary_benchmark/README.md) · [V3.9 validation](benchmark_suite/README.md) · [Creator Mode](creator_engine/quality_checker/self_review.md) · [MCP Alpha](interfaces/mcp/README.md)

## License

MIT. See [LICENSE](LICENSE). Third-party datasets keep their own licenses and attribution requirements.
