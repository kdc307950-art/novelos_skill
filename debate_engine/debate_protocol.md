# Debate Protocol

Debate Engine 只处理需要多专业权衡的决策，不替代普通单 Agent 分析。流程固定为三轮：

1. **Independent Judgment**：每个被选 Agent 独立提交 position、claim、证据、风险和置信度，不读取其他 Agent 立场。
2. **Challenge and Response**：Agent 只质疑可验证的假设、证据缺口和目标权重，回应必须引用对方 argument_id；禁止人身化或重复表态。
3. **Consensus**：Consensus Builder 按任务目标权重、专业权重和证据强度合并，输出保留分歧、首选方案、备选方案和需要作者确认的条件。

每轮保存结构化记录，禁止把私人思维链作为日志；只保留结论、证据、反驳点和决策依据。