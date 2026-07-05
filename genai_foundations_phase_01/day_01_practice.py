"""
Day 1 Practice
Problem:
Write a function that takes a string and returns True if it is a palindrome,
otherwise False.
"""


def is_palindrome(s):
    rev =""
    for i in s:
        rev = i + rev 
    if rev == s:
        return True
    else:
        return False


if __name__ == "__main__":
    print(is_palindrome("madam"))   # True
    print(is_palindrome("python"))  # False
