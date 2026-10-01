"""Day 2, P06: detect a linked-list cycle without changing the list."""

from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node | None = None) -> None:
        self.value = value
        self.next = next


def has_cycle(head: Node | None) -> bool:

    visited = set()
    curr =head

    while curr:
        if curr in visited:
            return True

        visited.add(curr)
        curr = curr.next

    return False
    #"""Return whether a cycle exists. Target: O(n) time, O(1) extra space."""
    ## TODO: Implement without changing the nodes or their links.
    #raise NotImplementedError("Implement has_cycle before running the checks")


def run_tests() -> None:
    # Each entry gives values and the index the tail links back to (if any).
    cases = [
        ([], None, False),
        ([7], None, False),
        ([7], 0, True),
        ([1, 2], None, False),
        ([1, 2], 0, True),
        ([1, 2, 3], None, False),
        ([1, 2, 3, 4], 1, True),
        ([7, 7, 7], None, False),
    ]
    for values, entry, expected in cases:
        nodes = [Node(value) for value in values]
        for left, right in zip(nodes, nodes[1:]):
            left.next = right
        if entry is not None:
            nodes[-1].next = nodes[entry]
        original_links = [node.next for node in nodes]

        result = has_cycle(nodes[0] if nodes else None)
        assert result is expected, f"Failed: values={values}, entry={entry}"
        assert all(node.next is link for node, link in zip(nodes, original_links)), (
            "Do not change links"
        )
        assert [node.value for node in nodes] == values, "Do not change values"

    print("All Detect Cycle checks passed")


if __name__ == "__main__":
    run_tests()
