# 分析器扩展接口

每个分析器读取章节索引与 memory 快照，输出统一记录：`finding_id, engine, severity, evidence[], impact, recommendation, confidence`。新增分析器不得直接改写原始记忆，只提交变更集。