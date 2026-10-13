# Cost Tracker

按任务和 Agent 记录 `input_tokens, output_tokens, total_tokens, duration_ms, agent_count, context_level, estimated_cost`。缺少真实 token 计数时标记 estimated，不伪造精确值。

用成本与质量分联合评估路由：若某 Agent 长期成本高、增量发现低且不影响 P0/P1，可降为按需调用。