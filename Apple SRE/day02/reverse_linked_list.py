"""Day 2, P05: reverse the links of a singly linked list in place."""

from __future__ import annotations


class Node:
    def __init__(self, value: int, next: Node | None = None) -> None:
        self.value = value
        self.next = next


def reverse_list(head: Node | None) -> Node | None:

    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev 


    """Return the new head, reusing nodes with O(n) time and O(1) extra space."""
    # TODO: Implement after answering the level check in DAY_02.md.
    raise NotImplementedError("Implement reverse_list before running the checks")


def run_tests() -> None:
    for values in ([], [7], [1, 2], [1, 2, 3, 4], [2, 2, 3]):
        nodes = [Node(value) for value in values]
        for left, right in zip(nodes, nodes[1:]):
            left.next = right

        head = nodes[0] if nodes else None
        current = reverse_list(head)

        # Bounded traversal also catches accidental cycles without hanging.
        for expected in reversed(nodes):
            assert current is expected, f"Wrong node order or new nodes for {values}"
            current = current.next
        assert current is None, f"List must end with None for {values}"
        assert [node.value for node in nodes] == values, "Preserve node values"

    print("All Reverse Linked List checks passed")


if __name__ == "__main__":
    run_tests()
