"""
Task 1 — Slicing and Loops

Practice slicing, loops, enumerate, zip, and comprehensions.
Complete this file without using AI tools.
"""

patient_ids = [101, 102, 103, 104, 105, 106, 107]
patient_names = ["Ayesha", "Omar", "Sara", "Bilal", "Hina", "Usman", "Maha"]


def slicing_examples():
    """Return examples of list slicing."""
    first_three = patient_ids[:3]
    last_three = patient_ids[-3:]
    reversed_ids = patient_ids[::-1]
    return first_three, last_three, reversed_ids


def loop_examples():
    """Practice range, enumerate, and zip."""
    for index, name in enumerate(patient_names, start=1):
        print(f"{index}. {name}")

    for patient_id, name in zip(patient_ids, patient_names):
        print(f"{patient_id} -> {name}")


def comprehension_examples():
    """Return values created using comprehensions."""
    even_ids = [pid for pid in patient_ids if pid % 2 == 0]
    upper_names = [name.upper() for name in patient_names]
    return even_ids, upper_names


if __name__ == "__main__":
    slicing_examples()
    loop_examples()
    comprehension_examples()
