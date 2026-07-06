"""
Day 6 Practice
Problem:
Write a function that checks whether a dictionary has the required keys.
"""


def has_required_keys(data, required_keys):

    for key in required_keys:
        if key not in data:
            return False
        return True
    # Hint:
    # 1. Loop through each required key.
    # 2. If any key is missing, return False.
    # 3. If all keys are present, return True.
    pass


if __name__ == "__main__":
    print(has_required_keys({"topic": "lists", "level": "beginner"}, ["topic", "level"]))  # expected: True
    print(has_required_keys({"topic": "lists"}, ["topic", "level"]))  # expected: False
    print(has_required_keys({}, ["topic"]))  # expected: False
