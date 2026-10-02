# Apple ASE/SRE Progress Log

Mark an exercise solved only after an independent implementation and passing tests.

| ID | Priority | Solved | Tests pass | Complexity explained | Reattempt passed |
|---|---|---|---|---|---|
| P01 | P0 | [x] | [x] | [x] | [ ] |
| P02 | P0 | [x] | [x] | [x] | [ ] |
| P03 | P0 | [x] | [x] | [x] | [ ] |
| P04 | P1 | [ ] | [ ] | [ ] | [ ] |
| P05 | P0 | [ ] | [x] | [ ] | [ ] |
| P06 | P0 | [ ] | [x] | [ ] | [ ] |
| P07 | P0 | [ ] | [x] | [ ] | [ ] |
| P08 | P1 | [ ] | [x] | [ ] | [ ] |
| P09 | P0 | [ ] | [x] | [ ] | [ ] |
| P10 | P0 | [ ] | [x] | [ ] | [ ] |
| P11 | P0 | [ ] | [x] | [ ] | [ ] |
| P12 | P1 | [ ] | [ ] | [ ] | [ ] |
| P13 | P0 | [ ] | [ ] | [ ] | [ ] |
| P14 | P0 | [ ] | [ ] | [ ] | [ ] |
| P15 | P0 | [ ] | [ ] | [ ] | [ ] |
| P16 | P1 | [ ] | [ ] | [ ] | [ ] |
| P17 | P0 | [ ] | [ ] | [ ] | [ ] |
| P18 | P0 | [ ] | [ ] | [ ] | [ ] |
| P19 | P0 | [ ] | [ ] | [ ] | [ ] |
| P20 | P1 | [ ] | [ ] | [ ] | [ ] |

## Current session

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
| 2026-10-02 / P09 | Returned 1 for `abcdef` | Used `i - j + 1` for window length | Inclusive length is right minus left plus one: `j - i + 1` | Correction passes checks; unaided reattempt pending |
| 2026-10-02 / P11 | Tuple assignment raised `TypeError` | Tuples are immutable | Replace the entire tuple | Correction passes checks; unaided reattempt pending |
| 2026-10-02 / P11 | Touching intervals kept separate | Used `<=` to detect separation | Closed intervals are separate only when last end < next start | Correction passes checks; unaided reattempt pending |
| 2026-10-02 / P11 | Input list reordered | Used in-place `.sort()` | Use `sorted()` when input must remain unchanged | Correction passes checks; unaided reattempt pending |
