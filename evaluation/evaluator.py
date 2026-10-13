"""Evaluate an Agent result for evidence and recommendation quality."""


def evaluate(result):
    findings = result.get("findings", [])
    evidence_count = sum(len(item.get("evidence", [])) for item in findings)
    recommendations = result.get("recommendations", [])
    return {
        "finding_count": len(findings),
        "evidence_coverage": round(evidence_count / max(len(findings), 1), 2),
        "recommendation_count": len(recommendations),
        "protocol_complete": all(key in result for key in ("summary", "findings", "recommendations", "memory_updates")),
    }
