"""Small JSONL execution logger; no private chain of thought is stored."""

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Dict


class ExecutionLogger:
    def __init__(self, log_dir: Path):
        self.log_dir = log_dir
        self.log_dir.mkdir(parents=True, exist_ok=True)

    def event(self, run_id: str, event: str, **data: Any) -> Dict[str, Any]:
        record = {"run_id": run_id, "time": datetime.now(timezone.utc).isoformat(), "event": event, **data}
        path = self.log_dir / f"{run_id}.jsonl"
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        return record
