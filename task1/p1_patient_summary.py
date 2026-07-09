"""
Task 1 — Patient Summary

Complete this file without using AI tools.
Use fake/sample data only.
"""

patients = [
    {"id": 1, "name": "Ayesha Khan", "age": 32, "condition": "diabetes", "active": True},
    {"id": 2, "name": "Omar Ali", "age": 45, "condition": "hypertension", "active": True},
    {"id": 3, "name": "Sara Ahmed", "age": 28, "condition": "asthma", "active": False},
    {"id": 4, "name": "Bilal Malik", "age": 52, "condition": "diabetes", "active": True},
]


def total_patients(patient_records):
    """Return the total number of patients."""
    return len(patient_records)


def average_age(patient_records):
    """Return the average patient age."""
    if not patient_records:
        return 0

    total_age = sum(p["age"] for p in patient_records)
    return total_age / len(patient_records)


def count_active_patients(patient_records):
    """Return the number of active patients."""
    return sum(1 for p in patient_records if p["active"])


def unique_conditions(patient_records):
    """Return a sorted list of unique conditions."""
    conditions = {p["condition"] for p in patient_records}
    return sorted(conditions)


def count_by_condition(patient_records):
    """Return a dictionary containing patient count by condition."""
    condition_counts = {}

    for p in patient_records:
        condition = p["condition"]
        condition_counts[condition] = condition_counts.get(condition, 0) + 1

    return condition_counts


if __name__ == "__main__":
    print("Patient Summary Report")
    print("----------------------")

    print("Total Patients:", total_patients(patients))
    print("Average Age:", average_age(patients))
    print("Active Patients:", count_active_patients(patients))
    print("Unique Conditions:", unique_conditions(patients))
    print("Count by Condition:", count_by_condition(patients))
