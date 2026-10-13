# Conflict Resolution

冲突不靠简单多数票解决。最终判断由以下因素加权：

`decision_weight = task_goal_weight × agent_expertise_weight × evidence_strength`

任务目标权重来自用户请求；专业权重由 Agent 对该问题的职责决定；证据强度依据证据数量、直接性、一致性和置信度评分。若证据不足或权重接近，输出分歧和条件式建议，不伪造共识。

商业化优化可提高商业 Agent 权重；文学提升可提高文学 Agent 权重；人物生死必须提高人物弧光和连续性约束的权重。