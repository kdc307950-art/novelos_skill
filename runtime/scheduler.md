# Scheduler

Scheduler 根据 Router 计划、Agent 依赖、上下文成本和优先级安排执行。默认先运行连续性与结构基础检查，再运行人物/商业/读者等派生分析；同一证据在同一任务内只计算一次。

调度记录 `selected、skipped、reason、estimated_cost、actual_cost`，为后续 Evaluation 提供运行质量证据。