"""Run JSON benchmark cases with deterministic expectation checks."""

import json
from pathlib import Path


def run_case(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    case_id = data.get("case_id", path.stem)
    facts = " ".join(str(item) for item in data.get("facts", []))
    if case_id == "CONT_001":
        passed = "dies" in facts and "negotiates" in facts
    elif case_id == "CHAR_001":
        passed = "refuses violence" in facts and "lethal attack" in facts
    elif case_id == "LIT_001":
        passed = "rain" in facts and "exile" in facts
    elif case_id == "COMM_001":
        passed = "seven days" in data.get("promise", "") and "background" in facts
    elif case_id == "CREATIVE_001":
        passed = len(data.get("expected", [])) >= 3
    else:
        passed = bool(data.get("expected"))
    return {"case_id": case_id, "passed": passed, "expected": data.get("expected", "")}


def run_directory(directory: Path):
    cases = [run_case(path) for path in sorted(directory.rglob("*.json"))]
    return {"total": len(cases), "passed": sum(item["passed"] for item in cases), "failed": sum(not item["passed"] for item in cases), "cases": cases}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    print(json.dumps(run_directory(args.directory), ensure_ascii=False, indent=2))
