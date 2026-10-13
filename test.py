"""Run the repository's lightweight benchmark smoke suite."""

from pathlib import Path
import sys

from evaluation.benchmark_runner import run_directory


if __name__ == "__main__":
    root = Path(__file__).resolve().parent
    result = run_directory(root / "benchmark")
    print(f"{result['total']} benchmarks")
    print(f"Passed: {result['passed']}")
    print(f"Failed: {result['failed']}")
    sys.exit(0 if result["failed"] == 0 else 1)
