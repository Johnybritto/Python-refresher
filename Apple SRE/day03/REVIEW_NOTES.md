# Day 3 review notes

## P09: Longest Unique Substring

- Original issue: `i - j + 1` reversed the window boundaries and returned 1 for
  `abcdef` instead of 6.
- Correction: use `j - i + 1` for inclusive left/right indices. For indices 2
  through 5, the length is 4.
- Storing the previous position plus one and using `max` keeps the left boundary
  from moving backward.
- Current result: all 12 supplied checks pass after the hinted correction.
- Complexity: O(n) expected time and O(k) space for k distinct characters.

## P10: Rolling Request Count

- Current result: nine count cases and four invalid-window checks pass.
- The interval is `(t - window, t]`, so timestamps `<= t - window` must expire.
- Each timestamp enters and leaves the deque at most once: O(n) total time.
- Space: O(w) for the queue, where w is the maximum active request count, plus
  O(n) for returned counts.
- Suggested cleanup still pending: use `timestamp` instead of `i`, remove the
  debug `print(counts)`, and remove unreachable starter code.

## P11: Merge Intervals

The original attempt had three correctness issues, all now corrected:

| Issue | Why it failed | Correction |
|---|---|---|
| `merged_list[-1][1] = ...` | Input intervals are tuples; item assignment raises `TypeError` | Replace the entire last tuple with `(old_start, max(old_end, new_end))` |
| `last_end <= next_start` classified intervals as separate | Closed intervals that touch, such as `(1, 3)` and `(3, 5)`, overlap | Separate only when `last_end < next_start` |
| `intervals.sort(...)` | Mutates the caller's input list, violating the contract | Iterate over a copy created by `sorted(intervals, ...)` |

Taking the maximum end also preserves a larger interval when a smaller interval
is fully contained within it. Sorting by start lets each new interval be compared
with the last merged interval.

- Current result: all 11 supplied checks pass, including input preservation,
  containment, touching endpoints, duplicates, and negative endpoints.
- Complexity: O(n log n) time for sorting and O(n) extra space.
- Suggested cleanup still pending: rename `interval` (the sorted collection) to
  `sorted_intervals` and `i` to `interval`; move the docstring immediately under
  `def` and remove the unreachable TODO/raise after `return`.

Passing checks is recorded separately from the learner's complexity explanations
and unaided reattempts. Reattempt P09 and P11 without consulting the corrections.
