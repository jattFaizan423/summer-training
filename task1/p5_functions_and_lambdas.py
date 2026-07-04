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
    return weight_kg / (height_m**2)


def classify_bmi(bmi: float) -> str:
    """Return BMI category."""
    if bmi < 18.5:
        return "underweight"
    if bmi < 25:
        return "normal"
    if bmi < 30:
        return "overweight"
    return "obese"


def format_name(name: str) -> str:
    """Convert a name to title case."""
    return name.title()


def get_active_patients(patient_records: list[dict]) -> list[dict]:
    """Return active patients only."""
    return [patient for patient in patient_records if patient["active"]]


def sort_patients_by_weight(patient_records: list[dict]) -> list[dict]:
    """Return patients sorted by weight using a lambda."""
    return sorted(patient_records, key=lambda patient: patient["weight_kg"])


if __name__ == "__main__":
    for patient in patients:
        bmi = calculate_bmi(patient["weight_kg"], patient["height_m"])
        print(f"{format_name(patient['name'])}: BMI {bmi:.2f} ({classify_bmi(bmi)})")

    print(get_active_patients(patients))
    print(sort_patients_by_weight(patients))
