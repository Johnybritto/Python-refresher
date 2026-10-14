"""R23-C06 — Two-pointer string and array exercises.

Part 1: palindrome checking
---------------------------
Implement ``is_palindrome(text)``. Return True when a string reads the same
from left to right and right to left after ignoring non-alphanumeric characters
and letter case. Do not build a cleaned copy of the full string.

Examples:

    is_palindrome("A man, a plan, a canal: Panama") is True
    is_palindrome("race a car") is False
    is_palindrome("") is True

Use one pointer at the left and one at the right. Skip punctuation/whitespace;
compare valid characters case-insensitively. Target: O(n) time and O(1) extra
space.

Part 2: remove duplicates from a sorted list
--------------------------------------------
Implement ``remove_duplicates(nums)``. ``nums`` is already sorted. Modify the
same list so its first returned-length positions contain each distinct value
once, preserving order. Return that length; values after it do not matter.

Example:

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    length = remove_duplicates(nums)
    # length == 5
    # nums[:length] == [0, 1, 2, 3, 4]

Use a read pointer to inspect all values and a write pointer for the next unique
value. Target: O(n) time and O(1) extra space. Do not use ``set`` or create a
separate result list.
"""


def is_palindrome(text: str) -> bool:

    #initialzing l and r

    l , r = 0 , len(text) -1

    #using l<r and l<=r ( becase the middle point will be the same if we compare )
    while l < r:
        if not text[l].isalnum():
            l +=1
        elif not text[r].isalnum():
            r -=1
        elif text[l].lower() != text[r].lower():
            return False
        else:
            l +=1
            r -=1
    return True
    """Return whether text is a case-insensitive alphanumeric palindrome."""
    raise NotImplementedError("Implement R23-C06 before running checks")


def remove_duplicates(nums: list[int]) -> int:

     # if list is empty return 0
    if not nums:
        return 0

   #starting from 1 because its a sorted array and 0 is already correct
    l=1
# r also starting from 1
    for r in range(1, len(nums)):
         #comparing r with previous value
        if nums[r] != nums[ r -1 ]:
            #if there is no match that means it is a new value rather than duplicate valye and we need to update it
            nums[l] = nums[r]
            l +=1
    return l

    """Keep one copy of each sorted value in nums and return its new length."""
    raise NotImplementedError("Implement R23-C06 before running checks")


def run_tests() -> None:
    palindrome_cases = {
        "": True,
        "a": True,
        "A man, a plan, a canal: Panama": True,
        "race a car": False,
        "No 'x' in Nixon": True,
        "0P": False,
        "!!!": True,
    }
    for text, expected in palindrome_cases.items():
        assert is_palindrome(text) is expected, f"Wrong result for {text!r}"

    duplicate_cases = [
        ([], [], 0),
        ([1], [1], 1),
        ([1, 1], [1], 1),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
        ([-3, -3, -1, -1, 0, 2, 2], [-3, -1, 0, 2], 4),
    ]
    for nums, expected_prefix, expected_length in duplicate_cases:
        original = nums
        length = remove_duplicates(nums)
        assert nums is original, "Modify the supplied list rather than replacing it"
        assert length == expected_length, f"Wrong length for {original}"
        assert nums[:length] == expected_prefix, f"Wrong prefix for {original}"
    print("All R23-C06 checks passed")


if __name__ == "__main__":
    run_tests()
