# NovelOS v2.2

NovelOS 是面向百万字长篇小说的编辑 Agent Framework。它通过 Orchestrator 选择专家，维护人物/时间线/伏笔/关系/世界记忆，运行结构、场景、连续性、商业、读者和文风分析，再由 Decision Engine 输出“改、暂缓、不改”的可执行决策。

## 运行原则

- 先调度再分析，按任务选择最小专家集合。
- 所有结论回指证据；事实、推断、建议分离。
- 记忆变更保留来源、置信度和历史，不静默覆盖冲突。
- 输出诊断、局部示例和改稿计划，不批量生成正文。

## 目录

- `orchestrator/`：任务分类、路由、执行策略、分层上下文。
- `agents/`：统一 Agent Interface 与总编辑调度规范。
- `memory/`：人物、时间线、伏笔、关系、世界和小说状态 Schema。
- `engines/`、`*_engine/`：结构、人物、场景、连续性、商业、读者和文风模块。
- `decision_engine/`：优先级、修改策略和风险评估。
- `tests/`：连续性、人物、场景、商业和回归测试案例。

## 标准工作流

`Task Classifier → Runtime Kernel → Orchestrator → Context/Memory Retrieval → Agents → Decision Engine → Evaluation → Observability → Memory Update → Snapshot → Report`

Runtime、Evaluation、Memory Intelligence、Observability、Literary Intelligence、Learning、Debate、Author Model、Literary Graph、Calibration、Decision Intelligence 和 Creative Simulation 的规范分别见对应目录。V3 数据集位于 `dataset/`，固定案例位于 `benchmark/`、`evaluation/dataset/` 与 `tests/`。

详细入口见 [SKILL.md](SKILL.md)。
