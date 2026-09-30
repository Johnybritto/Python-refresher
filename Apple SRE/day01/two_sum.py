"""Day 1, P01: find two distinct indices whose values sum to a target."""


def two_sum(nums: list[int], target: int) -> tuple[int, int] | None:
  # need to fetch the indcies of the value 
  # value - > incdices  thats how it is stored in dict
    compl = {} 
    for i , num in enumerate(nums):
        val = target - num 
        if val in compl:
            return ( compl[val], i)
        compl[num] = i  
    #print(type(compl))   
    return None
  # need to fetch the value 
   # seen = set()
   # for i in nums:
   #     val = target - i 
   #     if val in seen:
   #         return ( val , i )
   #     seen.add(i)

   #return None
    """Return indices of a valid pair, or None when no pair exists.

    Assumptions:
    - Any valid pair may be returned.
    - The two indices must be different.
    - The input list must not be modified.

    Target complexity:
    - O(n) average time
    - O(n) extra space
    """
    # TODO: Implement the dictionary approach from DAY_01.md.
    raise NotImplementedError("Implement two_sum before running the tests")


def assert_valid_pair(nums: list[int], target: int, result: tuple[int, int] | None) -> None:
    """Check a result without requiring one particular index order."""
    assert result is not None
    first, second = result
    assert 0 <= first < len(nums)
    assert 0 <= second < len(nums)
    assert first != second
    assert nums[first] + nums[second] == target


def run_tests() -> None:
    """Run examples plus boundary cases."""
    assert_valid_pair([2, 7, 11, 15], 9, two_sum([2, 7, 11, 15], 9))
    assert_valid_pair([3, 3], 6, two_sum([3, 3], 6))
    assert_valid_pair([-2, 1, 4], 2, two_sum([-2, 1, 4], 2))

    assert two_sum([], 1) is None
    assert two_sum([1], 2) is None
    assert two_sum([1, 2], 9) is None

    original = [1, 4, 6]
    snapshot = original.copy()
    assert_valid_pair(original, 10, two_sum(original, 10))
    assert original == snapshot

    print("All Two Sum tests passed")


if __name__ == "__main__":
    run_tests()
