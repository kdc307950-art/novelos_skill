# Execution Policy

1. Agent 必须遵守 [agents/interface.md](../agents/interface.md)。
2. 先读当前状态和相关记忆，再调用专家；禁止无路由的全量分析。
3. Agent 之间不直接修改对方结果；Orchestrator 负责合并、去重和冲突标注。
4. 任何 memory 更新先写 history，再更新当前值；冲突值并列保存，等待作者确认。
5. P0 连续性问题和高置信度事实冲突优先进入决策层；低置信度推断不得阻断流程。
6. 上下文不足时发出 context request，不用臆测填充。