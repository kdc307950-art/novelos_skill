from dataclasses import asdict, dataclass, field
from typing import List

@dataclass
class SourceRecord:
    source: str
    license: str
    files: List[str] = field(default_factory=list)
    quality_score: float = 0.0
    status: str = "candidate"

    def as_dict(self):
        return asdict(self)
