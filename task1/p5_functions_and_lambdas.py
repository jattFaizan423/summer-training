"""
Task 1 — Functions and Lambda Functions

Practice reusable functions, type hints, and lambda functions.
Complete this file without using AI tools.
"""

patients = [
    {"name": "ayesha khan", "height_m": 1.65, "weight_kg": 68, "active": True},
    {"name": "omar ali", "height_m": 1.78, "weight_kg": 82, "active": False},
    {"name": "sara ahmed", "height_m": 1.60, "weight_kg": 54, "active": True},
]


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI."""
    if height_m == 0:
        return 0.0
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


def format_name(name: str) -> str:
    """Convert a name to title case."""
    return name.title()


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    return [p for p in patient_records if p["active"]]


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    return sorted(patient_records, key=lambda p: p["weight_kg"])


if __name__ == "__main__":
    print("Patient BMI Report")
    print("-------------------")

    for p in patients:
        bmi = calculate_bmi(p["weight_kg"], p["height_m"])
        category = classify_bmi(bmi)
        name = format_name(p["name"])

        print(f"{name}: BMI={bmi:.2f} ({category})")

    print("\nActive Patients:")
    active = get_active_patients(patients)
    for p in active:
        print("-", format_name(p["name"]))

    print("\nPatients Sorted by Weight:")
    sorted_patients = sort_patients_by_weight(patients)
    for p in sorted_patients:
        print(f"{format_name(p['name'])} - {p['weight_kg']} kg")
