# Review Process

1. 数据管理员核查来源、许可、去重、split 和字段完整性。
2. Reviewer A 独立填写答案、证据、标签、分数和 confidence。
3. Reviewer B 在不读取 A 结论的情况下独立复核高价值或高风险案例。
4. 一致案例标记 `reviewed`；分歧案例进入 `annotation/disagreement/`。
5. 仲裁者记录结论、依据和是否修改 rubric；修改 rubric 必须增加回归案例。
6. 只有有 reviewer、reviewed_at、evidence、confidence 和稳定答案的案例，才允许 `verified=true`。

每批报告：原始数、待审数、已审数、verified 数、rejected 数、分歧数、各类别分布和来源许可状态。自动生成样本永远从 pending 开始。
