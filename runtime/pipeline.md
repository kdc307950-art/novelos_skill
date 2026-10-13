# Pipeline

标准管线：

`INPUT → PREPROCESS → ANALYSIS → DEBATE(optional) → AGGREGATION → DECISION → EVALUATION → MEMORY_UPDATE → OUTPUT`

每阶段写入事件：`task_id、stage、started_at、ended_at、status、artifacts、errors`。阶段输出只允许被下一阶段消费，避免 Agent 越权改状态。
