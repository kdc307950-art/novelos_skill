# NovelOS 中文说明书

NovelOS 是面向百万字长篇小说的 AI 编辑与创作工作台。它维护人物、世界观、时间线、伏笔和写作状态，使用多 Agent 分析、辩论、评测和记忆提交帮助作者长期管理作品。

默认使用 **Editor Mode**：分析、规划、审稿和提出修改方案。作者明确授权后才进入 **Creator Mode**：生成场景、章节初稿、扩写或重写。生成内容经过自审、修订和作者确认后，才可进入 Canonical Memory。

## 快速开始

```bash
git clone https://github.com/kdc307950-art/novelos_skill.git
cd novelos_skill
python test.py
```

期望输出：

```text
5 benchmarks
Passed: 5
Failed: 0
```

最新压缩包：[NovelOS v3.10.1](https://github.com/kdc307950-art/novelos_skill/releases/latest)

## GUI Alpha

```bash
python interfaces/gui/server.py
```

打开 <http://127.0.0.1:8765>。GUI 提供项目状态、章节编辑、编辑面板和 Memory 概览。

## MCP Alpha

```bash
python -m interfaces.mcp.server
```

客户端配置示例：

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

MCP 提供 10 个 Tools、5 个 Resources 和 5 个 Prompts。`update_memory` 必须先返回 proposal；`generate_scene` 和 `rewrite_scene` 还需要 `mode="creator"` 与 `confirm=true`。

## 核心流程

```text
任务分类 → Runtime → Orchestrator → Memory Retrieval
→ Agent 分析/创作 → Debate → Decision → Evaluation
→ Self Review → Proposal → Author Confirmation → Memory Commit
```

## 数据与验证

- 3000 条 Benchmark Suite pending 配额
- 1000 条 Golden Dataset pending 队列
- 来源、许可、split、置信度和人工审阅状态
- A/B 对比、盲评、统计、消融和失败分析

当前自动生成数据不会被标记为人工验证结果。详见 [数据集说明](../dataset/literary_benchmark/README.md)、[贡献指南](../CONTRIBUTING.md) 和 [安全说明](../SECURITY.md)。

## 目录导航

| 目录 | 作用 |
| --- | --- |
| `runtime/` | 执行、状态、日志和 Memory Commit |
| `memory/` | Canon、人物、场景、写作状态和快照 |
| `creator_engine/` | 场景计划、写作、风格、自审和修订 |
| `interfaces/gui/` | 作者工作台 |
| `interfaces/mcp/` | AI 客户端接入 |
| `evaluation/`、`benchmark_suite/` | 质量评测与基准 |

项目许可为 MIT；第三方数据遵循各自许可和署名要求。
