"""Task 1 — Problem 7 (Easy): Find the Runner-Up Score"""

sample_scores = [2, 3, 6, 6, 5]


def find_runner_up(scores: list[int]) -> int:
    """Return the runner-up score: the second highest distinct value.

    Example: [2, 3, 6, 6, 5] -> 5
    """
    unique_scores = sorted(set(scores))
    return unique_scores[-2]


if __name__ == "__main__":
    print(find_runner_up(sample_scores))
