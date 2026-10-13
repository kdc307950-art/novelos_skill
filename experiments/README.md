# Experiment Engine

实验记录固定数据、模型、NovelOS 版本、指标、成本和人评状态。当前 `tasks.jsonl` 提供 20 个计划任务；它们未运行时保持 `planned/pending`，不生成虚假结果。

```bash
python experiments/create_plan.py
python -m experiments.runner experiments/experiment.example.json --out experiments/results/EXP_001.json
```
