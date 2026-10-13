"""Run the repository's lightweight benchmark smoke suite."""

from pathlib import Path
import sys

from evaluation.benchmark_runner import run_directory


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    fixture_dirs = [root / "benchmark" / name for name in ("continuity", "character", "literary", "commercial", "creativity")]
    cases = []
    for directory in fixture_dirs:
        if directory.exists():
            cases.extend(run_case(path) for path in sorted(directory.glob("*.json")))
    result = {"total": len(cases), "passed": sum(item["passed"] for item in cases), "failed": sum(not item["passed"] for item in cases), "cases": cases}
    print(f"{result['total']} benchmarks")
    print(f"Passed: {result['passed']}")
    print(f"Failed: {result['failed']}")
    sys.exit(0 if result["failed"] == 0 else 1)
