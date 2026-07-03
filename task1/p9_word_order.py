"""Task 1 — Problem 9 (Medium): Word Order"""

sample_words = ["bcdef", "abcdefg", "bcde", "bcdef"]


def word_order(words: list[str]) -> tuple[int, list[int]]:
    """Return the count of distinct words and their frequencies in order."""
    counts_dict = {}

    for word in words:
        if word in counts_dict:
            counts_dict[word] += 1
        else:
            counts_dict[word] = 1

    distinct_count = len(counts_dict)
    counts = list(counts_dict.values())

    return distinct_count, counts


if __name__ == "__main__":
    distinct_count, counts = word_order(sample_words)
    print(distinct_count)
    print(counts)
