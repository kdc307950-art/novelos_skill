# NovelOS Literary Benchmark Dataset

目标是可追溯的小说判断数据：既有冲突，也有合理反转；既有失败，也有成功和不确定例子。现阶段为基础设施与 6 条原创合成种子，尚未达到 1000 条或人工验证规模。

| 类别 | Month 1 计划 |
| --- | ---: |
| [01_Continuity](01_Continuity/cases.jsonl) | 300 |
| [02_Character](02_Character/cases.jsonl) | 200 |
| [03_Structure](03_Structure/cases.jsonl) | 200 |
| [04_Literary](04_Literary/cases.jsonl) | 100 |
| [05_Commercial](05_Commercial/cases.jsonl) | 100 |
| [06_Failure](06_Failure/cases.jsonl) | 100 |

以上计划合计 1100；首阶段最低目标 1000。第二阶段最低目标 10000；原分类规模合计 12000，作为扩展配额，不当成已完成数量。

## 数据工作流

```bash
python -m crawler.github_search --out dataset/literary_benchmark/sources/search-results.json
python -m crawler.repo_analyzer dataset/literary_benchmark/sources/search-results.json --out dataset/literary_benchmark/sources/ranked.json
python -m crawler.downloader reviewed-manifest.json --out data_work/raw/source-name
python -m crawler.build_dataset data_work/raw/source-name/data.csv --mapping field-map.json --manifest reviewed-manifest.json --category 02_Character --out data_work/review/character.jsonl
python -m crawler.validate_dataset dataset/literary_benchmark
python -m unittest discover -s tests/unit -p 'test_dataset*.py'
```

搜索和排名只形成候选。Dataset Quality 需人工填写 0–1；未审查的数据许可得分为 0。星数/分叉用对数归一化，活动用时间衰减，权重为 20/15/20/30/15。

下载清单见 [模板](sources/manifest.example.json)。Downloader 只下载明确路径，固定完整提交 SHA；不执行第三方代码，不递归下载故事链接。标准 JSON/JSONL、CSV、TXT、平坦 XML 可提取；复杂格式需独立适配器。默认 200 字符下限可为短推理题显式下调；短题不因篇幅短就默认无价值。

去重基于规范化内容+问题+答案，避免删除同一书的不同问题。分割依据原文 document/book ID，避免一本书跨 train/test 泄漏；跨来源近重复需要二次人工审查。语言完整性检查仅是初筛。

## 格式与审阅

统一结构见 [case.schema.json](case.schema.json)。保留原始答案和来源；缺少人类质量分时 labels 留空，禁止将自动预测伪装为专家分数。每条 verified=true 必须有 annotation_id、reviewer 和审阅时间；合成样本也需要复核。

类别专用信息放在 details：连续性 before/after/conflict，人物 history/decision/reasoning，结构 role/turning_point，文学 theme/symbolism/mechanism，商业 hook/reader_expectation，失败 problem/why_bad/fix。

事实类评价报告正确/错误/不确定及证据位置；审美和商业评价采用人工 rubric 或成对偏好，商业风险不得声称实际留存率。模型输出必须单独保存，不能与参考答案合并。当前旧 `test.py` 只检查 fixture 特征，不代表模型的冲突检测准确率。

## 来源与许可

[来源清单](sources/catalog.json) 记录候选和审查状态。NarrativeQA 包含问答、文档索引与 Wikipedia 摘要；LongBench 可研究长上下文评测；HANNA 可研究人类故事评价；WritingPreferenceBench 可研究中英写作偏好。各数据子集许可需逐项确认，当前未导入任何外部故事正文。

仓库 MIT 许可不覆盖外部数据。发布数据时附带数据原许可、NOTICE、来源和改动记录。保留上游拆分，不将测试数据用于提示优化后再声称是独立测试集。
