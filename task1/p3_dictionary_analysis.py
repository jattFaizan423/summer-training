"""
Task 1 — Dictionary Analysis

Practice dictionaries and nested dictionaries.
Complete this file without using AI tools.
"""

patients = {
    1: {
        "name": "Ayesha Khan",
        "age": 32,
        "contact": {"city": "Karachi", "phone": "000-000"},
        "condition": "diabetes",
    },
    2: {
        "name": "Omar Ali",
        "age": 45,
        "contact": {"city": "Lahore", "phone": "111-111"},
        "condition": "hypertension",
    },
}


def get_patient_city(patient_id):
    """Return the city for a given patient ID."""
    patient = patients.get(patient_id)
    if not patient:
        return None

    return patient.get("contact", {}).get("city")


def update_patient_condition(patient_id, new_condition):
    """Update a patient's condition."""
    if patient_id in patients:
        patients[patient_id]["condition"] = new_condition
        return True
    return False


def build_patient_summary():
    """Build and return a summary dictionary."""
    total = len(patients)

    avg_age = 0
    if total > 0:
        avg_age = sum(p["age"] for p in patients.values()) / total

    conditions = {p["condition"] for p in patients.values()}

    return {
        "total_patients": total,
        "average_age": avg_age,
        "unique_conditions": sorted(conditions),
    }


if __name__ == "__main__":
    print("City of patient 1:", get_patient_city(1))
    print("City of patient 3 (not exist):", get_patient_city(3))

    print("\nUpdating condition of patient 1...")
    update_patient_condition(1, "cardiac")

    print("\nPatient Summary:")
    print(build_patient_summary())
