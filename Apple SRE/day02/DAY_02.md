# Day 2, P05: Reverse a Linked List

Start with P05 today. P06 Detect Cycle and P07 Valid Parentheses come after review;
P08 Merge Sorted Lists is optional. Keep today's session to about one hour.

## Check your current level

Suppose `head` refers to node A in `A -> B -> C -> None`.
If you run `head.next = None`, which nodes can you still reach by following
links from `head`? Answer before starting the implementation.

## One small exercise

Open `reverse_linked_list.py` and implement only `reverse_list` after we discuss
the level check. The supplied `Node` class stores a value and a reference to the
next node; `None` marks the end.

Contract:

- Input: the first node of a finite, acyclic singly linked list, or `None`.
- Output: the new first node after reversing the links.
- Reuse the original nodes and preserve their values. The input links will change.
- An empty list returns `None`; a single node returns that same node.
- Assume valid input; detecting cycles is the next exercise.
- Aim for O(n) time and O(1) extra space using iteration.

Example: `1 -> 2 -> 3 -> None` becomes `3 -> 2 -> 1 -> None`.

First hint, if needed: before changing a link, consider how you will keep access
to the rest of the list. We will add stronger hints only after your attempt.

Run from the `Apple SRE` folder:

```bash
python3 day02/reverse_linked_list.py
```

The starter intentionally raises `NotImplementedError` until you implement it.
The checks cover an empty list, one node, two nodes, several nodes, and duplicate
values. They also check that you reused the nodes and terminated the list.

After your attempt, share your code and explain its time and extra-space costs.
We will review correctness, readability, complexity, and one requirement change
before marking P05 complete.
