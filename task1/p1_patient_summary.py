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
    ages = [patient["age"] for patient in patient_records]
    return sum(ages) / len(ages)


def count_active_patients(patient_records):
    """Return the number of active patients."""
    return sum(1 for patient in patient_records if patient["active"])


def unique_conditions(patient_records):
    """Return a sorted list of unique conditions."""
    conditions = {patient["condition"] for patient in patient_records}
    return sorted(conditions)


def count_by_condition(patient_records):
    """Return a dictionary containing patient count by condition."""
    counts = {}
    for patient in patient_records:
        condition = patient["condition"]
        counts[condition] = counts.get(condition, 0) + 1
    return counts


if __name__ == "__main__":
    print(f"Total patients: {total_patients(patients)}")
    print(f"Average age: {average_age(patients):.2f}")
    print(f"Active patients: {count_active_patients(patients)}")
    print(f"Unique conditions: {unique_conditions(patients)}")
    print(f"Count by condition: {count_by_condition(patients)}")
