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


# def build_patient_summary():
#     """Build and return a summary dictionary."""
#     # TODO: Return useful summary information.
#     pass


if __name__ == "__main__":
    # 1. Test get_patient_city
    city = get_patient_city(1)
    print(f"Patient 1 City: {city}")
    
    # 2. Test update_patient_condition
    print("\nUpdating Patient 2 condition")
    success = update_patient_condition(2, "flu")
    print(f"Updated Data for Patient 2: {patients[2]}")
