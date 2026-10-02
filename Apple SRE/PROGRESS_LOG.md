# Apple ASE/SRE Progress Log

Mark an exercise solved only after an independent implementation and passing tests.
Source coverage and current priorities are in [PLAN_MAPPING.md](PLAN_MAPPING.md).
Local P IDs remain stable; `Supplement` means no exact source exercise.

| ID | Priority | Solved | Tests pass | Complexity explained | Reattempt passed |
|---|---|---|---|---|---|
| P01 | P0 | [x] | [x] | [x] | [ ] |
| P02 | Supplement | [x] | [x] | [x] | [ ] |
| P03 | P0 | [x] | [x] | [x] | [ ] |
| P04 | P1 | [ ] | [ ] | [ ] | [ ] |
| P05 | P0 | [ ] | [x] | [ ] | [ ] |
| P06 | P0 | [ ] | [x] | [ ] | [ ] |
| P07 | P0 | [ ] | [x] | [ ] | [ ] |
| P08 | P1 | [ ] | [x] | [ ] | [ ] |
| P09 | P0 | [ ] | [x] | [ ] | [ ] |
| P10 | Supplement | [ ] | [x] | [ ] | [ ] |
| P11 | P1 | [ ] | [x] | [ ] | [ ] |
| P12 | P1 | [ ] | [x] | [ ] | [ ] |
| P13 | Supplement | [ ] | [ ] | [ ] | [ ] |
| P14 | P0 outline / P1 code | [ ] | [ ] | [ ] | [ ] |
| P15 | P1 | [ ] | [ ] | [ ] | [ ] |
| P16 | P1 | [ ] | [ ] | [ ] | [ ] |
| P17 | P1 | [ ] | [ ] | [ ] | [ ] |
| P18 | Supplement | [ ] | [ ] | [ ] | [ ] |
| P19 | P2 | [ ] | [ ] | [ ] | [ ] |
| P20 | Supplement | [ ] | [ ] | [ ] | [ ] |

## Source additions and gaps

| Source | Priority | Status |
|---|---|---|
| AP1 | P0 | Active starter; no implementation yet |
| AP2–AP6 | P0 | Pending, in source order |
| C2 | P0 | Counting partly covered; dedicated most-frequent task pending |
| C7 | P0 | Set solution passes; O(1)-space slow/fast version pending |
| A1 outline | P0 | Pending; implementation remains P1 |
| AP7–AP11 | P1 | Pending after P0 |
| C11/C12, A1 code/A2/A3/A4 | P1 | Pending; reuse mapped local work |
| C13/C14 | P2 | Deferred |

## Current session

- Reconciled against the user-supplied seven-day plan. AP1 is active; SLO Summary
  is deferred supplemental work. Historical test results and pending explanations
  remain intact. See PLAN_MAPPING.md for full source coverage.
- P12 Binary Search passes all 16 checks after correcting value comparisons and
  the inclusive loop condition. Learner identified indices 2 and 3 in the range
  [2, 3]. Complexity explanation, first-match follow-up, and unaided reattempt pending.
- P11 Merge Intervals passes all 11 checks after correcting tuple assignment,
  touching-endpoint handling, and input mutation. Explanation and unaided reattempt
  pending. See [Day 3 review notes](day03/REVIEW_NOTES.md) for issues and corrections.
- P10 implementation is correct and passes nine count cases plus four invalid-window
  checks. O(n) total time, O(w) queue space plus O(n) output space. Learner explanation
  and follow-up discussion deferred. Suggested cleanup: descriptive loop variable,
  remove debug print, and move docstring/remove unreachable starter code.
- P09 passes all 12 checks after correcting the window length with a hint.
  Learner confirmed inclusive length calculation; complexity explanation,
  requirement-change discussion, and unaided reattempt remain pending.
- P08 Merge Sorted Lists implementation passes all nine checks, reusing nodes
  with O(n + m) time and O(1) extra space. Learner explanation and discussion pending.
- P07 implementation is correct for the bracket-only contract and passes all 12
  checks. O(n) time and O(n) worst-case extra space; learner explanation and
  requirement-change discussion deferred at the learner's request.
- P06 set-based implementation passes all eight checks: O(n) expected time and O(n)
  extra space. O(1)-space optimization and explanation deferred; P06 remains incomplete.
- P05's remaining discussion is deferred.
- Day 2 started with P05 Reverse Linked List.
- P05 implementation reviewed: correct iterative reversal; all five supplied cases pass.
- Explanation and requirement-change discussion remain pending before marking P05 complete.
- Cleanup noted: move the docstring before the implementation and remove unreachable starter code.

## Mistake log

| Date / problem | What failed | Why it failed | Rule to remember | Reattempt result |
|---|---|---|---|---|
| P12 | Compared `m` with target | Confused index with value | Compare `nums[m]` with target | Corrected; all checks pass; unaided reattempt pending |
| P12 | Skipped final candidate, including `[5]` | Used `l < r` for inclusive boundaries | Continue while `l <= r`; equality means one candidate remains | Corrected; all checks pass; unaided reattempt pending |
| 2026-10-02 / P09 | Returned 1 for `abcdef` | Used `i - j + 1` for window length | Inclusive length is right minus left plus one: `j - i + 1` | Correction passes checks; unaided reattempt pending |
| 2026-10-02 / P11 | Tuple assignment raised `TypeError` | Tuples are immutable | Replace the entire tuple | Correction passes checks; unaided reattempt pending |
| 2026-10-02 / P11 | Touching intervals kept separate | Used `<=` to detect separation | Closed intervals are separate only when last end < next start | Correction passes checks; unaided reattempt pending |
| 2026-10-02 / P11 | Input list reordered | Used in-place `.sort()` | Use `sorted()` when input must remain unchanged | Correction passes checks; unaided reattempt pending |
