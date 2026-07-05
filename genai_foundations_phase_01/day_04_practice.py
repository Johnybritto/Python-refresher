"""
Day 4 Practice
Problem:
Write a function that counts the frequency of each character in a string.
"""


def count_characters(text):
    count = {}
    for i in text:
        if i in count:
            count[i] +=1
        else:
            count[i] =1 
    return count
    # Hint:
    # 1. Create an empty dictionary.
    # 2. Loop through each character in the text.
    # 3. If the character is already in the dictionary, add 1.
    # 4. Otherwise, set its count to 1.
    pass


if __name__ == "__main__":
    print(count_characters("hello"))   # expected: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(count_characters("aaa"))     # expected: {'a': 3}
    print(count_characters(""))        # expected: {}
