# Evaluation Alignment

目标是比较 AI 评分与人工评分，而不是让 AI 自己证明自己。报告 Pearson correlation、MAE、平均有符号偏差、样本数和分组结果；相关性目标 ≥ 0.8 是验收目标，不是默认事实。

输入示例：`{"dimension":"character","ai":8.5,"human":7.0}`。样本必须有独立人工标注和来源审计；合成 pending 数据不能用于声称达到目标。
