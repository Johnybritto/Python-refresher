"""R23-C04 — Sort Colors (three-way partition / Dutch National Flag).

Problem statement
-----------------
Given a list containing only 0, 1, and 2, rearrange the *same list* so all
0s appear first, then all 1s, then all 2s. Do not call ``sort()`` or create a
separate output list. Return ``None`` after modifying ``nums`` in place.

Sample input and output
-----------------------
    nums = [2, 0, 2, 1, 1, 0]
    sort_colors(nums)
    # nums is now [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    sort_colors(nums)
    # nums is now [0, 1, 2]

Approach
--------
Maintain three regions with three indexes:

* ``low``: next position where a 0 belongs.
* ``current``: value currently being examined.
* ``high``: next position where a 2 belongs.

The invariant is:

    0 .. low - 1       contains only 0s
    low .. current - 1 contains only 1s
    current .. high    is not processed yet
    high + 1 .. end    contains only 2s

When ``nums[current]`` is 0, swap it with ``nums[low]`` and move both indexes.
When it is 1, move only ``current``. When it is 2, swap it with ``nums[high]``
and move only ``high``—the value swapped into ``current`` still needs checking.

Target complexity: O(n) time and O(1) extra space.
"""


def sort_colors(nums: list[int]) -> None:

    low = 0 
    mid =  0 
    high =  len(nums) -1 

    while mid <= high : 
        if nums[mid] == 0 : 
            nums[low] , nums[mid] = nums[mid], nums[low]
            low +=1
            mid +=1
        elif nums[mid] == 1:
            mid +=1
        else:
            nums[high], nums[mid] = nums[mid] , nums[high]
            high -=1

    return None 


    """Rearrange 0, 1, and 2 values in nums without returning a new list."""
    raise NotImplementedError("Implement R23-C04 before running checks")


def run_tests() -> None:
    cases = [
        ([], []),
        ([0], [0]),
        ([2], [2]),
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([1, 1, 1], [1, 1, 1]),
        ([2, 2, 2, 0, 0, 1], [0, 0, 1, 2, 2, 2]),
        ([0, 2, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 2, 2]),
    ]
    for nums, expected in cases:
        original = nums
        result = sort_colors(nums)
        assert result is None, "Modify nums in place and return None"
        assert nums is original, "Do not replace the supplied list"
        assert nums == expected, f"Expected {expected}, got {nums}"
    print("All R23-C04 checks passed")


if __name__ == "__main__":
    run_tests()
