"""Day 3, P09: length of the longest substring without repeated characters."""


def longest_unique_length(text: str) -> int:

    visited = {}
    result = 0 
    i = 0 

    for j in range(len(text)):
        if text[j] in visited:
            i = max ( i , visited[text[j]])
        result = max ( result , j-i +1 )
        visited[text[j]] = j+1

    return result                   




    """Return the longest contiguous unique-character length; empty input gives 0."""
    # TODO: Aim for O(n) expected time using a sliding window.
    raise NotImplementedError("Implement longest_unique_length before running checks")


def run_tests() -> None:
    cases = [
        ("", 0),
        ("a", 1),
        ("abcdef", 6),
        ("bbbbb", 1),
        ("abcabcbb", 3),
        ("pwwkew", 3),
        ("abba", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5),
        ("aA", 2),
        ("a b a", 3),
        ("éλé界", 3),
    ]
    for text, expected in cases:
        result = longest_unique_length(text)
        assert type(result) is int, "Return an integer length"
        assert result == expected, f"For {text!r}: expected {expected}, got {result}"
    print("All Longest Unique Substring checks passed")


if __name__ == "__main__":
    run_tests()
