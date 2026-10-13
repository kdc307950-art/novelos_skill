# 工作流

## 增量循环

`任务分类 → Orchestrator 路由 → Context Manager 装载 → 解析场景 → Agent 执行 → Decision Engine → History 记录 → Memory 更新 → Snapshot → 报告`。

每个变更集包含 `change_id, entity_id, operation(add|update|conflict|revert), old_value, new_value, source, time, confidence, status`，写入 `memory/history/memory_change_log.json`。冲突值并列保留，待作者确认后再标记 canonical。

Context Manager 使用三级上下文：Level 1 当前章节、Level 2 当前卷相关摘要、Level 3 历史检索。每次任务记录实际加载层级和引用，避免重复加载全文。

## 任务模式

单章模式强调局部节奏和新增事实；整本模式强调弧线、伏笔回收和长期风险；改稿模式只处理指定优先级；审稿模式输出决策摘要而非正文。
