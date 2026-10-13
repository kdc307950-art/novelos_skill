# Orchestrator Router

Router 根据任务分类、范围、小说状态和已有结论选择最小 Agent 集合。先读取 `memory/novel_state.json` 与最近变更，再决定是否需要补充上下文。

当任务涉及角色生死、主题取舍、商业与文学目标冲突、重大结构重构或用户明确要求多方意见时，路由到 `debate_engine/`；普通事实提取和单维诊断不启动 Debate。

| 任务 | 必选 Agent | 可选 Agent |
|---|---|---|
| 单章诊断 | structure、continuity、reader | character、scene |
| 整卷深度编辑 | structure、character、scene、continuity、reader | commercial、style、world |
| 连载维护 | continuity、scene、reader_memory | character、commercial |
| 人物心理 | character | continuity、reader |
| 市场定位 | commercial、reader | structure |
| 文风审查 | style | reader |

Router 输出 `selected_agents`、`skipped_agents`、`reasons`、`context_level` 和 `estimated_cost`。同一证据已被近期任务处理时复用结论，不重复调用。
