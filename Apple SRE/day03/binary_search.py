"""Day 3, P12: find a target in a sorted list using binary search."""


def binary_search(nums: list[int], target: int) -> int:

    l, r = 0 , len(nums) - 1

    while l <= r :
        m = (l+r) // 2
        if nums[m] < target:
            l = m+1
        elif nums[m] > target:
            r = m-1
        else:
            return m 

    return -1  
    """Return any matching index, or -1 if absent; leave nums unchanged."""
    # TODO: Use iterative index boundaries, aiming for O(log n) time, O(1) space.
    raise NotImplementedError("Implement binary_search before running checks")


def run_tests() -> None:
    cases = [
        ([], 4),
        ([5], 5),
        ([5], 2),
        ([5], 8),
        ([2, 5], 2),
        ([2, 5], 5),
        ([2, 5], 3),
        ([2, 5, 8, 12, 16], 12),
        ([2, 5, 8, 12, 16], 7),
        ([2, 5, 8, 12, 16], 2),
        ([2, 5, 8, 12, 16], 16),
        ([2, 5, 8, 12, 16], 0),
        ([2, 5, 8, 12, 16], 20),
        ([-9, -4, 0, 3], -4),
        ([1, 2, 2, 2, 5], 2),
        ([3, 3, 3, 3], 3),
    ]
    for nums, target in cases:
        original = nums.copy()
        result = binary_search(nums, target)
        assert type(result) is int, "Return an integer index"
        assert nums == original, "Do not modify the input"
        if target in original:
            assert 0 <= result < len(original), f"Invalid index for {original}, {target}"
            assert original[result] == target, f"Wrong index for {original}, {target}"
        else:
            assert result == -1, f"Return -1 for missing target {target} in {original}"

    print("All Binary Search checks passed")


if __name__ == "__main__":
    run_tests()
