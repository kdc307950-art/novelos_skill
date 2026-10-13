# Execution Trace

记录一次完整 Runtime 执行的可复现摘要，不记录私人思维链。每次运行生成 `execution_id`，关联任务、模式、选用 Agent、阶段状态、最终评分、Memory 变更和错误。

必填字段：`execution_id, task, start_time, end_time, status, agents[], stages[], final_score, memory_changes, evaluation_ref`。时间统一使用 ISO 8601；Agent 状态必须为 queued/running/success/failed/skipped。