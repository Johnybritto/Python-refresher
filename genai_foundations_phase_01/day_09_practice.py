"""
Day 9 Practice
Problem:
Write a function that returns "memory" if saved_preference is not empty.
Otherwise return "chat_history".
"""


def classify_context(saved_preference):
    if saved_preference:
        return "memory"
    else:
        return "chat_history"
    # Hint:
    # 1. Check whether saved_preference is empty.
    # 2. If it has a value, return "memory".
    # 3. Otherwise return "chat_history".
    pass


if __name__ == "__main__":
    print(classify_context("likes short examples"))  # expected: memory
    print(classify_context(""))  # expected: chat_history
