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
    
    total_age = 0
    for patient in patient_records:
        total_age += patient["age"]  
        
    return total_age / len(patient_records)


def count_active_patients(patient_records):
    """Return the number of active patients."""
    count = 0
    for patient in patient_records:
        if patient["active"] == True:  
            count += 1
            
    return count


def unique_conditions(patient_records):
    """Return a sorted list of unique conditions."""
    conditions_list = []
    
    for patient in patient_records:
        conditions_list.append(patient["condition"])
        
    return sorted(list(set(conditions_list)))


def count_by_condition(patient_records):
    """Return a dictionary containing patient count by condition."""
    counts = {}
    
    for patient in patient_records:
        condition = patient["condition"]
        
        if condition in counts:
            counts[condition] += 1
        
        else:
            counts[condition] = 1

    return counts


if __name__ == "__main__":
    print("--- Patient Summary Report ---")
    print(f"Total Patients: {total_patients(patients)}")
    print(f"Average Age: {average_age(patients):.1f}")
    print(f"Active Patients: {count_active_patients(patients)}")
    print(f"Unique Conditions: {unique_conditions(patients)}")
    print(f"Count by Condition: {count_by_condition(patients)}")
