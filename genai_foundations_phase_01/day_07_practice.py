"""
Day 7 Practice
Problem:
Write a function that returns True only if a dictionary contains both
"topic" and "level".
"""


def is_valid_response(data):
    if "topic" in data and "level"  in data:
        return True
    return False
    # Hint:
    # 1. Check whether "topic" is in the dictionary.
    # 2. Check whether "level" is in the dictionary.
    # 3. Return True only if both are present.
    pass


if __name__ == "__main__":
    print(is_valid_response({"topic": "lists", "level": "beginner"}))  # expected: True
    print(is_valid_response({"topic": "lists"}))  # expected: False
    print(is_valid_response({"level": "beginner"}))  # expected: False
    print(is_valid_response({}))  # expected: False
