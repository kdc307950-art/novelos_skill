"""Persistent task state with resumable stages."""

from dataclasses import asdict, dataclass, field
import json
from pathlib import Path
from typing import List


@dataclass
class TaskState:
    task_id: str
    status: str = "queued"
    current_step: str = ""
    completed: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(asdict(self), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    @classmethod
    def load(cls, path: Path, task_id: str) -> "TaskState":
        if not path.exists():
            return cls(task_id=task_id)
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(**{key: data.get(key, getattr(cls(task_id), key)) for key in ("task_id", "status", "current_step", "completed", "errors")})
