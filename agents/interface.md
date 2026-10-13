# NovelOS Agent Interface v1

所有专家 Agent 通过统一协议通信。Agent 只读取上下文并提交发现、建议和候选记忆变更；不得直接覆盖 canonical memory。

## 输入协议

```json
{
  "task_id": "TASK_001",
  "novel_context": {
    "state": {},
    "memory_refs": [],
    "context_level": 1,
    "known_constraints": []
  },
  "chapter": "第20章",
  "request": "分析女主变化",
  "constraints": ["保留作者意图"]
}
```

必填：`task_id`、`novel_context`、`request`。`chapter` 可为空（整卷任务）。上下文引用优先于复制全文。

## 输出协议

```json
{
  "agent": "character_agent",
  "summary": "",
  "findings": [
    {
      "type": "problem|strength|uncertainty|conflict",
      "description": "",
      "evidence": [{"chapter": "", "scene": "", "text": ""}],
      "impact": "high|medium|low",
      "confidence": 0.85
    }
  ],
  "recommendations": [{"priority": "P0|P1|P2", "action": ""}],
  "memory_updates": [],
  "context_requests": []
}
```

证据必须可定位；无证据的判断标记为 uncertainty。`memory_updates` 使用变更日志格式，交由 Orchestrator 审核后写入。