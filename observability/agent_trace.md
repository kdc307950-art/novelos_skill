# Agent Trace

记录结构化操作轨迹：输入引用、检查维度、输出 finding ID、证据数量、耗时、状态和失败原因。不得保存或要求模型暴露私人思维链；只记录可审计的输入/输出摘要。

示例字段：`agent, task_id, input_refs[], checked[], finding_ids[], duration_ms, status, error_code`。