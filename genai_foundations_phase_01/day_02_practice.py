"""
Day 2 Practice
Problem:
Write a function that returns a shorter version of a string.

If the string length is greater than limit, return the first limit characters.
Otherwise return the original string.
"""


def shorten_text(text, limit):
    if len(text) > limit:
        return text[:limit]
    return text

    # Hint:
    # 1. Check whether the text is longer than limit.
    # 2. If yes, use slicing.
    # 3. Otherwise return the original text.
    pass


if __name__ == "__main__":
    print(shorten_text("python", 4))          # expected: pyth
    print(shorten_text("token", 10))          # expected: token
    print(shorten_text("context window", 7))  # expected: context
