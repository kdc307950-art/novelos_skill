"""Deterministic Runtime pipeline with observable stages."""

from typing import Any, Callable, Dict, Iterable, Optional

from .logger import ExecutionLogger
from .memory_manager import MemoryManager
from .state import TaskState


class Pipeline:
    def __init__(self, root, logger: Optional[ExecutionLogger] = None):
        self.root = root
        self.logger = logger or ExecutionLogger(root / "logs")
        self.memory = MemoryManager(root)

    def run(self, task: Dict[str, Any], agents: Iterable[Callable[[Dict[str, Any]], Dict[str, Any]]], decision: Optional[Callable] = None, evaluate: Optional[Callable] = None) -> Dict[str, Any]:
        run_id = task.get("run_id", task.get("task_id", "run"))
        state = TaskState(task_id=task.get("task_id", run_id), status="running")
        state_path = self.root / "runtime" / "state" / f"{state.task_id}.json"
        state.save(state_path)
        findings, proposals = [], []
        for agent in agents:
            name = getattr(agent, "__name__", agent.__class__.__name__)
            state.current_step = name
            state.save(state_path)
            self.logger.event(run_id, "agent_start", agent=name)
            try:
                result = agent(task)
                findings.extend(result.get("findings", []))
                proposals.extend(result.get("memory_updates", []))
                state.completed.append(name)
                self.logger.event(run_id, "agent_complete", agent=name, finding_count=len(result.get("findings", [])))
            except Exception as exc:  # isolate one Agent failure
                state.errors.append(f"{name}: {exc}")
                self.logger.event(run_id, "agent_failed", agent=name, error=str(exc))
        decision_result = decision({"task": task, "findings": findings}) if decision else {"findings": findings}
        evaluation_result = evaluate(decision_result) if evaluate else {}
        committed = self.memory.commit(proposals, source=run_id) if proposals else 0
        state.status = "completed" if not state.errors else "degraded"
        state.current_step = "completed"
        state.save(state_path)
        self.logger.event(run_id, "run_complete", status=state.status, committed=committed)
        return {"run_id": run_id, "status": state.status, "findings": findings, "decision": decision_result, "evaluation": evaluation_result, "memory_changes": committed, "errors": state.errors}
