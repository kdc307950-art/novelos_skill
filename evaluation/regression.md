# Regression Evaluation

每次引擎、提示版本或 Schema 变更后运行 `tests/regression/` 与 `evaluation/dataset/`：比较关键发现是否保留、评分是否异常下降、记忆字段是否丢失、Agent 输出协议是否完整。失败时阻止版本标记为稳定，并把新失败加入 `failure_cases/`。
