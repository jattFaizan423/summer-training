"""
Task 1 — Final Problem: Triage Report

Complete this file without using AI tools.
Use fake/sample data only.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "risk_score": 72, "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "risk_score": 88, "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "risk_score": 35, "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "risk_score": 91, "active": True},
]

# Tests ke exact standards ke mutabiq thresholds
MEDIUM_THRESHOLD = 50
HIGH_THRESHOLD = 75


def label_risk(risk_score: int) -> str:
    """Return low, medium, or high based on risk score."""
    if risk_score < 40:
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
    if not patient_records:
        return {
            "summary": {"total_patients": 0},
            "risk_counts": {"low": 0, "medium": 0, "high": 0},
            "active_high_risk_patients": [],
        }

    labeled_patients = add_risk_labels(patient_records)

    low_count = sum(1 for p in labeled_patients if p["risk_label"] == "low")
    medium_count = sum(1 for p in labeled_patients if p["risk_label"] == "medium")
    high_count = sum(1 for p in labeled_patients if p["risk_label"] == "high")

    active_high_risk = [
        p for p in labeled_patients if p["risk_label"] == "high" and p.get("active") is True
    ]

    return {
        "summary": {"total_patients": len(patient_records)},
        "risk_counts": {
            "low": low_count,
            "medium": medium_count,
            "high": high_count,
        },
        "active_high_risk_patients": active_high_risk,
    }


if __name__ == "__main__":
    report = build_triage_report(patients)
    print(report)
