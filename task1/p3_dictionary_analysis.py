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
    if patient:
        return patient.get("contact", {}).get("city")
    return None


def update_patient_condition(patient_id, new_condition):
    """Update a patient's condition."""
    if patient_id in patients:
        patients[patient_id]["condition"] = new_condition
        return True

    return False


def build_patient_summary():
    """Build and return a summary dictionary."""
    total_patients = len(patients)
    if total_patients == 0:
        return {"total_patients": 0, "average_age": 0}

    total_age = sum(info["age"] for info in patients.values())
    avg_age = total_age / total_patients

    return {
        "total_patients": total_patients,
        "average_age": round(avg_age, 1),
    }


if __name__ == "__main__":

    city = get_patient_city(1)
    print(f"Patient 1 City: {city}")

    # 2. Test update_patient_condition
    print("\nUpdating Patient 2 condition")
    success = update_patient_condition(2, "flu")
    print(f"Updated Data for Patient 2: {patients[2]}")

    
    print("\n--- Summary Report ---")
    print(build_patient_summary())