"""
Day 5 Practice
Problem:
Write a function that removes duplicates from a list.
"""


def remove_duplicates(items):
    # Hint:
    result = []
    for i in items:
        if i not in result:
            result.append(i)
    return result 
    #for i in range(len(items)):
    #    if items[i] in items[:i] and items[i] not in result:
    #        result.append(items[i])
    #return result
    # 1. Create an empty list for the result.
    # 2. Loop through each item in the input list.
    # 3. If the item is not already in the result, add it.
    # 4. Return the result.
    pass


if __name__ == "__main__":
    print(remove_duplicates([1, 2, 2, 3, 1]))       # expected: [1, 2, 3]
    print(remove_duplicates(["a", "b", "a"]))       # expected: ['a', 'b']
    print(remove_duplicates([]))                    # expected: []
