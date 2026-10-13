# Executor

Executor 接收 Runtime 计划并按依赖执行 Agent。计划至少包含 `task_id、task_type、agents、context_level、constraints、timeout_policy`。

Agent 可串行（前一个输出是后一个输入）或并行（互不依赖）；任一 Agent 失败由 Error Handler 处理，成功结果仍可进入 Aggregation，不因单点失败使整任务崩溃。