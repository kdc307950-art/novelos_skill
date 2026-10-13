# Prompt Evolution

提示版本采用 `agent_vN`，每次变更记录目标、差异、适用任务、基准结果、回归结果和回滚条件。新版本只有在 Golden Dataset 不下降且目标指标改善后才可设为默认。