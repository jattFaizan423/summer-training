"""Task 1 — Problem 8 (Medium): The Minion Game"""

VOWELS = "AEIOU"


def minion_game(word: str) -> str:
    """Play the Minion Game and return the result."""
    kevin_score = 0
    stuart_score = 0
    n = len(word)

    for i in range(n):
        if word[i] in VOWELS:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        return f"Kevin {kevin_score}"
    elif stuart_score > kevin_score:
        return f"Stuart {stuart_score}"
    else:
        return "Draw"


if __name__ == "__main__":
    print(minion_game("BANANA"))
