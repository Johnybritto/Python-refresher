# Apple SRE Python Program List

`[x]` = the bundled program checks pass. `[ ]` = still to implement or finish.
The current focus is the Round 2 P0 order at the bottom.

## Completed programs

- [x] `day01/two_sum.py` — Two Sum
- [x] `day01/first_unique.py` — First Unique Character
- [x] `day01/error_endpoints.py` — Parse Error Endpoints
- [x] `day02/reverse_linked_list.py` — Reverse Linked List
- [x] `day02/detect_cycle.py` — Detect Linked-List Cycle
- [x] `day02/valid_parentheses.py` — Valid Parentheses
- [x] `day02/merge_sorted_lists.py` — Merge Sorted Lists
- [x] `day03/longest_unique_substring.py` — Longest Unique Substring
- [x] `day03/rolling_request_count.py` — Rolling Request Count
- [x] `day03/merge_intervals.py` — Merge Intervals
- [x] `day03/binary_search.py` — Binary Search
- [x] `priority_drills/ipv4_validation.py` — IPv4 Validation
- [x] `priority_drills/line_buckets.py` — Split Lines into Buckets
- [x] `priority_drills/prefix_line_count.py` — Prefix File Line Counts

## Existing programs still to finish

- [ ] `priority_drills/request_duration.py` — START/END request correlation
- [ ] `day04/slo_summary.py` — SLO summary supplement
- [ ] IPv4 follow-up — guard very long numeric octets, then reattempt unaided
- [ ] Cycle-detection follow-up — implement slow/fast pointers with O(1) space

## Round 2 coding tasks

### P0 — do these first

- [x] R23-C01 `round2/normalization_count.py` — normalize/count/rank strings;
  invalid entries, ties, top-K, and file input checks pass
- [x] R23-C02 `priority_drills/line_buckets.py` — line buckets, streaming,
  round-robin allocation, and checks completed
- [x] R23-C03 `round2/string_compression.py` — returned-string and in-place
  compression checks completed
- [x] R23-C04 `round2/sort_colors.py` — three-way partition / Sort Colors
  checks completed
- [ ] R23-C05 — log/JSON aggregation with large-file input
  (`day01/error_endpoints.py` already passes its base checks)
- [ ] R23-C06 — palindrome check and remove duplicates from a sorted array
- [ ] R23-C07 — merge K sorted lists using a heap
- [ ] R23-C13 — Kubernetes Pod JSON health report

### P1 — after P0

- [ ] R23-C08 — LRU cache
- [ ] R23-C09 — rotate a square matrix 90° clockwise
- [ ] R23-C10 — longest mountain in an array
- [ ] R23-C11 — interleaving string
- [ ] R23-C12 — bounded health checker and safe retry wrapper

## Working rule

For every unchecked task: clarify the input/output and invalid-input policy,
implement from a blank editor, test normal/empty/boundary/failure cases, and
state time and space complexity. Mark it `[x]` only after its checks pass and
you can explain it without notes.
