# 人工标注协议

1. 核查来源、数据许可、文本完整性和原始拆分。
2. 标注事实证据位置，允许“信息不足”，不把作者偏好当作唯一答案。
3. 对修复方案评估因果收益、作者意图与修改成本；不要强行复制原文答案。
4. 文学/商业质量分必须有 rubric 与理由。无真实留存数据时只做相对风险判断。
5. 两名审阅者独立审阅高争议案例；分歧进入仲裁，保留各自意见。
6. 将 human_label 模板保存为独立 annotation_id 文件。数据行引用它，记录 reviewer/reviewed_at 后才可标 reviewed/verified。

自动清洗通过、LLM 自评或高 confidence 均不能替代人工验证。数据规模同时报告原始、待审、已审、验证和各 split 数量。

## V3.6 标注流程

标注者先核查来源/许可，再独立回答任务，填写 evidence、labels、reasoning_summary 和 confidence。标注完成后交给第二名审阅者复核；分歧写入 `annotation/disagreement/`，仲裁前保持 pending。只有 `verified=true`、有 annotation_id/reviewer/reviewed_at 且 `status=verified` 的案例可以导出为黄金测试集。
