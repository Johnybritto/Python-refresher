"""Day 1, P02: return the index of the first non-repeating character."""


def first_unique_index(text: str) -> int:

    char_count = {}
    for i in text:
        if i in char_count:
            char_count[i] +=1
        else:
            char_count[i] = 1 

    for i , a in enumerate(text):
        if char_count[a] == 1 :
            return i
       
    return -1 
        
    """Return the first index whose character occurs once, or -1.

    Characters match exactly, including case, whitespace, and Unicode.

    Target complexity:
    - O(n) time
    - O(k) extra space for k distinct characters
    """
    # TODO: First build a character-frequency dictionary.
    # TODO: Then scan the string in its original order.
    raise NotImplementedError("Implement first_unique_index before running the tests")


def run_tests() -> None:
    """Run examples plus boundary cases."""
    assert first_unique_index("leetcode") == 0
    assert first_unique_index("loveleetcode") == 2
    assert first_unique_index("aabb") == -1

    assert first_unique_index("") == -1
    assert first_unique_index("z") == 0
    assert first_unique_index("aA") == 0
    assert first_unique_index("  a") == 2
    assert first_unique_index("ééλ") == 2
    assert first_unique_index("aabbccd") == 6

    print("All First Unique Character tests passed")


if __name__ == "__main__":
    run_tests()
