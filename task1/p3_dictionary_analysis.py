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
    patient = patients.get(patient_id, {})
    return patient.get("contact", {}).get("city")


def update_patient_condition(patient_id, new_condition):
    """Update a patient's condition."""
    if patient_id in patients:
        patients[patient_id]["condition"] = new_condition


def build_patient_summary():
    """Build and return a summary dictionary."""
    summary = {}
    for patient_id, patient in patients.items():
        summary[patient_id] = {
            "name": patient["name"],
            "city": patient.get("contact", {}).get("city"),
            "condition": patient.get("condition"),
        }
    return summary


if __name__ == "__main__":
    print(get_patient_city(1))
    print(get_patient_city(999))
    update_patient_condition(1, "asthma")
    print(patients[1]["condition"])
    print(build_patient_summary())
