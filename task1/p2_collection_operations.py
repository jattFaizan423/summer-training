"""
Task 1 — Collection Operations

Practice lists, tuples, and sets.
Complete this file without using AI tools.
"""

# Sample data — do not edit.
sample_conditions = ["diabetes", "asthma", "hypertension"]
primary_conditions = {"diabetes", "asthma", "hypertension"}
follow_up_conditions = {"asthma", "cardiac", "diabetes"}


def list_operations(conditions: list[str]) -> list[str]:
    """Return a new, sorted list after adding and removing a condition."""
    # Work on a copy
    new_list = conditions.copy()

    # Add "cardiac"
    new_list.append("cardiac")

    # Remove "asthma" (if exists)
    if "asthma" in new_list:
        new_list.remove("asthma")

    # Return sorted list
    return sorted(new_list)


def set_operations(primary: set[str], follow_up: set[str]) -> dict[str, set[str]]:
    """Return common, all-unique, and primary-only conditions."""
    return {
        "common": primary & follow_up,
        "all_unique": primary | follow_up,
        "only_primary": primary - follow_up,
    }


if __name__ == "__main__":
    print(list_operations(sample_conditions))
    print(set_operations(primary_conditions, follow_up_conditions))
