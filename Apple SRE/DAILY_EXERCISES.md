# Daily Exercises

## Completed: Day 1, P01 — Two Sum

- [x] Read `day01/DAY_01.md`
- [x] State the input, output, and no-answer behavior
- [x] Explain the simple nested-loop approach
- [x] Implement the dictionary approach independently
- [x] Make all supplied tests pass
- [x] Explain time and extra-space complexity
- [ ] Reattempt later without reading the previous solution

## Completed: Day 1, P02 — First Unique Character

- [x] Read `day01/DAY_01_P02.md`
- [x] Clarify what counts as the same character
- [x] Build the frequency dictionary
- [x] Find the first character whose count is one
- [x] Make all supplied tests pass
- [x] Explain time and extra-space complexity
- [ ] Reattempt later without reading the previous solution

## Completed: Day 1, P03 — Top Error-Producing Endpoints

- [x] Read `day01/DAY_01_P03.md`
- [x] Parse each JSON line without materializing the iterable
- [x] Validate the object, path, and status
- [x] Count only HTTP 500–599 responses
- [x] Count every invalid input record
- [x] Sort by count descending and path ascending
- [x] Make all supplied tests pass
- [x] Explain time and extra-space complexity
- [ ] Reattempt later without reading the completed solution

## Implementation reviewed: Day 2, P05 — Reverse Linked List

- [ ] Answer the level check in `day02/DAY_02.md`
- [ ] Clarify the input, output, and mutation behavior
- [x] Attempt `reverse_list` in `day02/reverse_linked_list.py`
- [x] Make the supplied checks pass
- [ ] Explain why no nodes are lost during reversal
- [ ] Explain time and extra-space complexity
- [ ] Discuss one requirement change during review

Remaining discussion deferred at your request.

## Implementation reviewed: Day 2, P06 — Detect Cycle

- [ ] Answer the level check in `day02/DAY_02_P06.md`
- [x] Attempt `has_cycle` in `day02/detect_cycle.py`
- [x] Make the supplied checks pass without modifying the list
- [ ] Explain termination, time complexity, and extra-space complexity
- [ ] Discuss one requirement change during review

The set-based implementation passes checks with O(n) extra space. Optimization
to O(1) extra space and the remaining discussion are deferred at your request.

## Implementation reviewed: Day 2, P07 — Valid Parentheses

- [ ] Answer the level check in `day02/DAY_02_P07.md`
- [x] Attempt `is_valid` in `day02/valid_parentheses.py`
- [x] Make the supplied checks pass
- [ ] Explain nesting order and time and extra-space complexity
- [ ] Discuss one requirement change during review

Remaining explanation and discussion deferred at your request.

## Implementation reviewed: Day 2, P08 — Merge Sorted Lists (optional extension)

- [ ] Answer the level check in `day02/DAY_02_P08.md`
- [x] Attempt `merge_sorted_lists` in `day02/merge_sorted_lists.py`
- [x] Make the supplied checks pass, reusing nodes and preserving values
- [ ] Explain correctness and time and extra-space complexity
- [ ] Discuss one requirement change during review

Remaining discussion deferred while moving to Day 3 at your request.

## Implementation reviewed: Day 3, P09 — Longest Unique Substring

- [ ] Answer the level check in `day03/DAY_03.md`
- [ ] Describe a simple approach before optimizing
- [x] Attempt `longest_unique_length` in `day03/longest_unique_substring.py`
- [x] Make the supplied checks pass
- [ ] Explain the window invariant and time and extra-space complexity
- [ ] Discuss returning the substring itself during review

Corrected the window length with a hint; remaining discussion deferred.
Reattempt later without the hint.

## Implementation reviewed: Day 3, P10 — Rolling Request Count

- [ ] Answer the boundary level check in `day03/DAY_03_P10.md`
- [x] Attempt `rolling_request_counts` in `day03/rolling_request_count.py`
- [x] Pass example, boundary, generator-input, and invalid-window checks
- [ ] Explain time and space complexity and why old requests can be removed
- [ ] Discuss out-of-order arrivals during review

Remaining discussion deferred at your request.

## Active: Day 3, P11 — Merge Intervals

- [ ] Answer the level check in `day03/DAY_03_P11.md`
- [x] Attempt `merge_intervals` in `day03/merge_intervals.py`
- [x] Pass checks including touching endpoints, containment, and unchanged input
- [ ] Explain correctness and time and space complexity
- [ ] Discuss half-open intervals during review

Review issues and corrections: [Day 3 review notes](day03/REVIEW_NOTES.md).

## Optional backlog

- P04 Top-K Frequent Items — unlocked optional exercise
