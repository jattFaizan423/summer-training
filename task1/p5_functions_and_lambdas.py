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
    return round(weight_kg / (height_m**2), 2)


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25.0:
        return "Normal"
    if bmi < 30.0:
        return "Overweight"
    return "Obese"


def format_name(name: str) -> str:
    """Convert a name to title case."""
    return name.title()


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    return [p for p in patient_records if p["active"]]


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    return sorted(patient_records, key=lambda x: x["weight_kg"])


if __name__ == "__main__":
    print("--- Name Formatting ---")
    print(format_name(patients[0]["name"]))
    print(format_name(patients[1]["name"]))

    print("\n--- BMI Calculation & Classification ---")
    print("Ayesha BMI Category:", classify_bmi(calculate_bmi(68, 1.65)))
    print("Omar BMI Category:", classify_bmi(calculate_bmi(82, 1.78)))

    print("\n--- Active Patients ---")
    print(get_active_patients(patients))

    print("\n--- Sorted Patients By Weight ---")
    print(sort_patients_by_weight(patients))
