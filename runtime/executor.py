"""Public entry point for running a NovelOS task."""

from pathlib import Path
from typing import Any, Callable, Dict, Iterable, Optional

from .pipeline import Pipeline


class Executor:
    def __init__(self, root: Optional[Path] = None):
        self.root = Path(root or Path(__file__).resolve().parents[1])
        self.pipeline = Pipeline(self.root)

    def run(self, task: Dict[str, Any], agents: Iterable[Callable], decision: Optional[Callable] = None, evaluate: Optional[Callable] = None) -> Dict[str, Any]:
        return self.pipeline.run(task, agents, decision=decision, evaluate=evaluate)
