# Runtime Core

Runtime 是 NovelOS 的唯一执行边界：接收任务、生成计划、调度 Agent、管理状态、收集结果、触发 Evaluation，并在验证后更新 Memory。

Agent 不得直接修改 canonical memory。所有结果必须符合 `agents/interface.md`，先进入候选变更，再由 Runtime 校验、Decision Engine 决策、History 记录后写入。