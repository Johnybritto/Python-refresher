"""
Day 3 Practice
Problem:
Write a function that returns the largest number in a list.
"""


def find_largest(numbers):

    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest
    # Hint:
    # 1. Start with the first item as the largest.
    # 2. Loop through the list.
    # 3. If you find a bigger number, update the largest value.
    pass


if __name__ == "__main__":
    print(find_largest([3, 7, 2, 9, 4]))   # expected: 9
    print(find_largest([10]))              # expected: 10
    print(find_largest([-5, -2, -9]))      # expected: -2
