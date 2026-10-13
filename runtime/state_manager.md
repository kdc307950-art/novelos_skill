# State Manager

维护任务运行状态：`task_id、status、current_agent、completed[]、failed[]、retry_count、artifacts[]、started_at、updated_at`。

状态：`queued → running → evaluating → updating → completed`；异常进入 `degraded` 或 `failed`。恢复时从最近完成阶段继续，不重复提交已 canonical 的变更。