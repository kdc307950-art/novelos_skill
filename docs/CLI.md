# CLI Guide

CLI 适合开发者、数据管理员和 CI：

```bash
python test.py
python -m benchmark_suite.validate_suite benchmark_suite/pending
python -m dataset_factory.validator.progress golden_dataset/pending
python -m interfaces.mcp.server
```

CLI 是可复现任务入口；它与 GUI、MCP 调用同一 Runtime/Core。
