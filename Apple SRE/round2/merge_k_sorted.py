"""R23-C07 — Merge K sorted inputs with a heap.

Problem statement
-----------------
Given an iterable of K individually sorted iterables of integers, return one
sorted list containing every integer, including duplicates. Some inputs may be
empty. The outer input and each inner input may be a generator, so consume each
inner input only as needed; do not concatenate everything and call ``sort()``.

Sample input and output
-----------------------
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merge_k_sorted(lists)
    # [1, 1, 2, 3, 4, 4, 5, 6]

Approach
--------
Keep a min-heap containing at most one current value from each input. Remove
the smallest value, append it to the result, then pull and push only the next
value from that same input. Store the input index alongside each value, so tied
values do not require Python to compare iterator objects.

For N total values and K inputs: O(N log K) time, O(K) heap space, plus the
returned result. This is also the main idea for merging K sorted linked lists;
in that variant the heap stores node values and their nodes instead of iterators.
"""

from collections.abc import Iterable


def merge_k_sorted(lists: Iterable[Iterable[int]]) -> list[int]:
    """Merge sorted inputs into one sorted list without consuming them eagerly."""
    raise NotImplementedError("Implement R23-C07 before running checks")


def run_tests() -> None:
    assert merge_k_sorted([]) == []
    assert merge_k_sorted([[], []]) == []
    assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [
        1, 1, 2, 3, 4, 4, 5, 6
    ]
    assert merge_k_sorted([[-3, -1, 2], [-2, 2, 2], []]) == [
        -3, -2, -1, 2, 2, 2
    ]
    assert merge_k_sorted(iter(values) for values in [[0, 7], [1, 5], [2, 3, 8]]) == [
        0, 1, 2, 3, 5, 7, 8
    ]
    assert merge_k_sorted([[1, 1], [1], [1, 1, 1]]) == [1, 1, 1, 1, 1, 1]
    print("All R23-C07 checks passed")


if __name__ == "__main__":
    run_tests()
