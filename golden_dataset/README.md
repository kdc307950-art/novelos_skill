# Golden Dataset

`pending/` 保存自动生成或外部导入后等待人工审阅的案例；`verified/` 只接受有 reviewer、时间、证据和标签理由的案例；`rejected/` 保存被拒绝或版权/质量审查不通过的案例。目录状态是数据生命周期，不代表模型质量。

V3.6 首批目标为 1000 条合成基准：连续性 200、人物 200、结构 200、文学 150、商业 150、失败 100。所有自动生成样本为 `synthetic/pending`，需要人工复核后才能进入 verified。

当前队列可用：`python -m dataset_factory.exporter.generate_synthetic --out golden_dataset/pending`。重复运行会覆盖同名 pending 文件；验证前请先保留 Git 变更记录。
