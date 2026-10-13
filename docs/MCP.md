# MCP Guide

MCP 是 AI 客户端入口。配置：

```json
{
  "mcpServers": {
    "novelos": {
      "command": "python",
      "args": ["-m", "interfaces.mcp.server"],
      "cwd": "/absolute/path/to/novelos_skill"
    }
  }
}
```

查询工具可直接使用；分析工具返回任务结果；写入工具先返回 proposal。正文生成和重写需要 `mode="creator"` 与显式确认。MCP 不维护独立 Memory。
