# Changelog

## v3.6.5

- 新增 Dataset Maturity：人物/结构/文学评分 rubric 与双审阅流程。
- 新增 AI/人工评分对齐、Pearson/MAE、偏差分析和 A/B 对比骨架。
- 新增 pending/verified/rejected 数据进度统计。

## v3.6.0

- 新增 Dataset Factory：采集、清洗、分类、验证和导出模块。
- 新增 1000 条 synthetic/pending Golden Dataset 队列，按六类配额组织。
- 新增 Human Annotation Pipeline、分歧队列和 verified 导出门槛。
- 新增模型相关性、A/B 对比、评估报告和 Agent Improvement Loop。

## v3.5.1

- Published the Literary Benchmark Dataset foundation and source review workflow.
- Refreshed the GitHub showcase page and release download entry.

## v2.2

- 新增统一 Agent Interface、Orchestrator 路由和执行策略。
- 新增 Memory History 与 Snapshot 规范。
- 升级人物 Schema，支持 Want/Need/Lie/Wound/Defense/Transformation。
- 升级 Scene Schema，支持场景功能和情绪曲线。
- 新增 Decision Engine 优先级、修改策略和风险评估。
- 新增竞品分析、Context Manager、README 和回归测试案例。

## v2.3

- 新增 Runtime Core：Executor、Pipeline、State Manager、Error Handler、Scheduler。
- 新增 Memory Retrieval、相关度评分、Context Builder 和记忆衰减策略。
- 新增 Evaluation Core、质量评分、Benchmark、Regression 和 Human Feedback 规范。
- 新增连续性、人物、伏笔 Benchmark 与最小 fixtures/expected 案例。

## v2.4

- 新增 Observability Layer：execution trace、agent trace、cost tracker、failure analysis、performance metrics。
- 新增统一 `observability/execution_record.json` Schema。
- Runtime、Evaluation、Memory 和报告入口接入执行轨迹与成本/性能记录。
- 新增 Literary Intelligence：审美、主题、象征、散文、叙事声音和文学评分。
- 新增 Golden Dataset 四类集合与合成校准案例。
- 新增 Learning Loop：反馈记忆、偏好学习、Agent 优化和 Prompt Evolution。

## v2.5

- 新增 Multi-Agent Debate Engine：独立判断、互相质疑、冲突加权和共识构建。
- Debate 仅在重大取舍、专业意见冲突或用户明确要求时启动。
- 新增 Author Intelligence Model：偏好、风格、禁忌、修正记忆与演化追踪。
- 新增 Literary Knowledge Graph：节点、关系、模式与检索规范。
- 新增 Human Calibration Layer：专家标注、分数对齐和权重调整。
- 升级 Decision Intelligence：方案生成、取舍分析、后果预测和最终选择。

## v3.0

- Literary Graph 2.0：实体、模式、关系、文学机制和检索。
- Golden Dataset：masterpiece、good、average、failed、ai_generated、human_written。
- Creative Simulation Engine：分支生成、结果预测、只读模拟和后果检查。
- Author Model 2.0：taste、belief、rejection patterns、creative identity。
- Evaluation 2.0、Human Feedback 和五类 V3 Benchmark。

## v3.5

- 新增可执行 Runtime：Executor、Pipeline、Task State、JSONL trace、Memory Manager。
- 拆分 Memory Schema 与 Runtime Storage，增加 proposal → validate → commit → snapshot 边界。
- 新增 Evaluation Runner、统一评分、Literary Engine heuristics 和 `python test.py` smoke suite。
- 新增 MVP Knowledge Base 与 baseline/NovelOS A/B comparison contract。
- 新增 NovelOS Literary Benchmark Dataset：六类目录、统一 case schema、6 条合成种子、来源清单、人工标注协议和去重/分割/验证工具。
- 新增受控 GitHub 采集工具：查询、仓库评分、固定提交下载、格式提取和质量清洗；默认不下载故事正文。

## v2.1

- 引入 Orchestrator、小说状态层、人物心理、Scene Engine、读者记忆和市场承诺模型。
