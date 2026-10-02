"""Day 2, P08: merge two sorted linked lists by reusing their nodes."""

from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node | None = None) -> None:
        self.value = value
        self.next = next


def merge_sorted_lists(left: Node | None, right: Node | None) -> Node | None:

    result = Node(0)
    head = result

    while left and right:
        if left.value <= right.value:
            head.next = left
            left = left.next
        else:
            head.next = right
            right =right.next
        head = head.next

    if left:
        head.next = left 
    if right:
        head.next = right

    return result.next 

    
   # """Merge disjoint sorted lists; take left first on ties and preserve values."""
    # TODO: Target O(n + m) time and O(1) extra space.
   # raise NotImplementedError("Implement merge_sorted_lists before running the checks")


def run_tests() -> None:
    cases = [
        ([], []),
        ([], [1, 2]),
        ([1, 2], []),
        ([1], [2]),
        ([2], [1]),
        ([1, 3, 5], [2, 4, 6]),
        ([1, 2], [3, 4, 5]),
        ([1, 2, 2], [1, 2, 3]),
        ([-5, -1, 0], [-3, 0, 7]),
    ]
    for left_values, right_values in cases:
        left_nodes = [Node(value) for value in left_values]
        right_nodes = [Node(value) for value in right_values]
        for nodes in (left_nodes, right_nodes):
            for first, second in zip(nodes, nodes[1:]):
                first.next = second

        all_nodes = left_nodes + right_nodes
        original_values = [node.value for node in all_nodes]
        # Stable sorting puts left nodes first on equal values.
        expected_nodes = sorted(all_nodes, key=lambda node: node.value)
        current = merge_sorted_lists(
            left_nodes[0] if left_nodes else None,
            right_nodes[0] if right_nodes else None,
        )
        for expected in expected_nodes:
            assert current is expected, (
                f"Wrong node order or replaced nodes: {left_values}, {right_values}"
            )
            current = current.next
        assert current is None, "Merged list must end with None"
        assert [node.value for node in all_nodes] == original_values, "Preserve values"

    print("All Merge Sorted Lists checks passed")


if __name__ == "__main__":
    run_tests()
