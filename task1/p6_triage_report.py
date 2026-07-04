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
    if risk_score >= 75:
        return "high"
    if risk_score >= 50:
        return "medium"
    return "low"


def add_risk_labels(patient_records: list[dict]) -> list[dict]:
    """Return copies of patient records with a risk_label field added."""
    labelled = []
    for patient in patient_records:
        new_patient = dict(patient)
        new_patient["risk_label"] = label_risk(patient["risk_score"])
        labelled.append(new_patient)
    return labelled


def build_triage_report(patient_records: list[dict]) -> dict:
    """Build a triage report from patient records."""
    labelled = add_risk_labels(patient_records)
    risk_counts = dict(Counter(patient["risk_label"] for patient in labelled))
    active_high_risk_patients = [
        patient for patient in labelled if patient["active"] and patient["risk_label"] == "high"
    ]
    return {
        "summary": {"total_patients": len(patient_records)},
        "risk_counts": risk_counts,
        "active_high_risk_patients": active_high_risk_patients,
    }


if __name__ == "__main__":
    report = build_triage_report(patients)
    print(report)

    assert report["summary"]["total_patients"] == 4
    assert sum(report["risk_counts"].values()) == 4
    assert len(report["active_high_risk_patients"]) == 2
