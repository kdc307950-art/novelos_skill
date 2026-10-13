# NovelOS Benchmark Suite v1.0

目标配额为 3000 条 pending/verified 案例：Continuity 1000、Character 700、Structure 500、Literary 400、Commercial 300、Failure 100。当前生成器产生合成 pending 案例；verified 数量、许可和人工标签单独报告。

```bash
python -m benchmark_suite.generate_suite --out benchmark_suite/pending
python -m benchmark_suite.validate_suite benchmark_suite/pending
```
