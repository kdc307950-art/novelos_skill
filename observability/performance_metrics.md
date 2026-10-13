# Performance Metrics

核心指标：任务成功率、P0/P1 发现召回率、证据覆盖率、建议采纳率、平均延迟、P95 延迟、每任务 token、Agent 利用率、降级率和 Memory 写入失败率。

指标必须带时间范围、任务类型和样本数；小样本只作观察，不宣称趋势。质量下降时结合 execution trace、cost tracker 和 failure analysis 定位原因。