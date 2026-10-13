# Regression Test Protocol

每次修改引擎或 Schema 后执行：

1. 校验所有 JSON Schema 可解析。
2. 用 continuity、character、scene、commercial 四组最小案例复查输出协议。
3. 检查 Agent 输出包含 `summary`、`findings`、`recommendations`、`memory_updates`。
4. 检查未知信息仍被标为待核实，而不是被升级为事实冲突。
5. 记录版本、变更文件、预期结果和实际结果。
