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

    print("First three:", first_three)
    print("Last three:", last_three)
    print("Reversed:", reversed_ids)


def loop_examples():
    """Practice range, enumerate, and zip."""
    print("--- Enumerate Example ---")

    for index, name in enumerate(patient_names, start=1):
        print(f"Patient {index}: {name}")

    print("\n--- Zip Example ---")

    for pid, name in zip(patient_ids, patient_names):
        print(f"ID: {pid} -> Name: {name}")


def comprehension_examples():
    """Return values created using comprehensions."""
    even_ids = [p_id for p_id in patient_ids if p_id % 2 == 0]
    uppercase_names = [name.upper() for name in patient_names]

    print("Even IDs:", even_ids)
    print("Uppercase Names:", uppercase_names)

    return even_ids, uppercase_names


if __name__ == "__main__":
    slicing_examples()
    loop_examples()
    comprehension_examples()
