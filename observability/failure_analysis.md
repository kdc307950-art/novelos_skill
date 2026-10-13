# Failure Analysis

失败分类：`retrieval_error`、`schema_error`、`timeout`、`agent_error`、`aggregation_error`、`memory_write_error`、`evaluation_error`。每条记录 `failure_id, execution_id, stage, cause, impact, recovery, recurrence, owner`。

复盘顺序：复现 → 定位阶段 → 判断是否可重试 → 记录降级结果 → 提出最小修复 → 加入回归案例。