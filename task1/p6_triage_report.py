"""
Task 1 — Final Problem: Triage Report

Complete this file without using AI tools.
Use fake/sample data only.

Tip: collections.Counter can make counting by risk label easier, but a
plain dictionary works too — import it yourself if you want to use it.
"""

from collections import Counter

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "risk_score": 72, "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "risk_score": 88, "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "risk_score": 35, "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "risk_score": 91, "active": True},
]


def label_risk(risk_score: int) -> str:
    """Return low, medium, or high based on risk score."""
    if risk_score < 50:
        return "low"
    elif risk_score < 80:
        return "medium"
    else:
        return "high"


def add_risk_labels(patient_records: list[dict]) -> list[dict]:
    """Return copies of patient records with a risk_label field added."""
    labeled = []

    for p in patient_records:
        new_patient = p.copy()
        new_patient["risk_label"] = label_risk(p["risk_score"])
        labeled.append(new_patient)

    return labeled


def build_triage_report(patient_records: list[dict]) -> dict:
    """Build a triage report from patient records."""
    labeled_patients = add_risk_labels(patient_records)
    counts = Counter(p["risk_label"] for p in labeled_patients)

    return {
        "total_processed": len(patient_records),
        "high_risk_count": counts.get("high", 0),
        "medium_risk_count": counts.get("medium", 0),
        "low_risk_count": counts.get("low", 0),
    }


if __name__ == "__main__":
    report = build_triage_report(patients)

    print("Generated Triage Report:")
    print(report)

    assert report["total_processed"] == 4
    assert report["high_risk_count"] == 2
    assert report["medium_risk_count"] == 1
    assert report["low_risk_count"] == 1

    print("\nAll assertions passed successfully!")
