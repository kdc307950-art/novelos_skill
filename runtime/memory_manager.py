"""Proposal, validation, commit and snapshot boundary for Memory."""

from datetime import datetime, timezone
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List


class MemoryManager:
    def __init__(self, root: Path):
        self.root = root
        self.storage = root / "memory" / "storage"
        self.history = root / "memory" / "history"
        self.snapshots = root / "memory" / "snapshots"
        for path in (self.storage, self.history, self.snapshots):
            path.mkdir(parents=True, exist_ok=True)

    def validate(self, proposals: Iterable[Dict[str, Any]]) -> List[Dict[str, Any]]:
        valid = []
        for proposal in proposals:
            if not proposal.get("entity_id") or not proposal.get("field"):
                raise ValueError("memory proposal requires entity_id and field")
            valid.append(dict(proposal))
        return valid

    def commit(self, proposals: Iterable[Dict[str, Any]], source: str) -> int:
        proposals = self.validate(proposals)
        timestamp = datetime.now(timezone.utc).isoformat()
        for index, proposal in enumerate(proposals, start=1):
            change = {"change_id": f"{timestamp}-{index}", "source": source, "time": timestamp, "status": "canonical", **proposal}
            path = self.history / f"change_{timestamp.replace(':', '').replace('.', '')}_{index}.json"
            path.write_text(json.dumps(change, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return len(proposals)

    def snapshot(self, snapshot_id: str, chapter_boundary: str = "") -> Path:
        state = {}
        for path in sorted(self.storage.glob("*.json")):
            state[path.stem] = json.loads(path.read_text(encoding="utf-8"))
        payload = {"snapshot_id": snapshot_id, "created_at": datetime.now(timezone.utc).isoformat(), "chapter_boundary": chapter_boundary, "memory": state}
        target = self.snapshots / f"{snapshot_id}.json"
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return target
