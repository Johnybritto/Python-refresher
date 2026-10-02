# Source-plan coverage and remaining work

Source: [supplied seven-day sprint](Apple_ASE_SRE_7_Day_Interview_Preparation_Plan.md),
sections 5.1–5.5. Status uses recorded reviews, not a claim of independent mastery.
Local P IDs remain stable; priorities below supersede the old labels.

| Source | Priority | Existing coverage | Remaining action |
|---|---|---|---|
| C1 Reverse linked list | P0 | P05, checks passed | Explanation/recall |
| C2 Count and most frequent | P0 | P02/P03 counting mechanics only | Dedicated most-frequent result, ties and input rules |
| C3 Two Sum | P0 | P01, recorded complete | Brief recall |
| C4 Valid Parentheses | P0 | P07, checks passed | Explanation/recall |
| C5 Streaming error endpoints | P0 | P03, recorded complete | Demonstrate file iteration using existing parser |
| C6 Longest unique substring | P0 | P09, passes after hint | Unaided reattempt and explanation |
| C7 Cycle detection | P0 | P06, set-based solution passes | Slow/fast pointers required for O(1) space |
| C8 Binary search | P1 | P12, passes after fixes | Unaided reattempt and explanation |
| C9 Merge sorted lists | P1 | P08, checks passed | Explanation/recall |
| C10 Merge intervals | P1 | P11, passes after fixes | Unaided reattempt and explanation |
| C11 Heap top-K | P1 | P04 planned; P03 uses sorting | Bounded heap implementation after P0 |
| C12 Graph reachability | P1 | P17 planned, no implementation | BFS/DFS |
| C13 Simple DP | P2 | No Apple-track implementation | Defer |
| C14 LRU/token bucket | P2 | P19 generic rate limiter planned | Choose source variant later |
| A1 Health checker | P0 outline / P1 code | P14 planned | Outline first; implementation later |
| A2 Retries | P1 | P15 planned | Eligible failures, deadlines, backoff/jitter, idempotency |
| A3 Config diff | P1 | P16 planned | Deterministic diff and safe execution |
| A4 Log error rate | P1 | P13 starter/P03 parser partly related | Population, time window, invalid records; coordinate AP7 |
| AP1 IPv4 validation | P0 | New starter | Active |
| AP2 N lines to M buckets | P0 | Not implemented | Next |
| AP3 Prefix file search/count | P0 | Not implemented | After AP2 |
| AP4 START/END correlation | P0 | Not implemented; distinct from P03 | After AP3 |
| AP5 p95 latency | P0 | Not implemented | After AP4 |
| AP6 Tail last N lines | P0 | P10 deque is background only | After AP5 |
| AP7 Service error thresholds | P1 | P03/P13 partly related | Per-service task after P0 |
| AP8 Phone-like normalization | P1 | Not implemented | After AP7 |
| AP9 Missing sequences | P1 | Not implemented | After AP8 |
| AP10 Lazy record generator | P1 | Generator inputs tested, not implemented | After AP9 |
| AP11 Debug broken script | P1 | Prior reviews are useful practice | Dedicated multi-defect exercise pending |

## Supplements and fundamentals

- P02 First Unique Character: passed, not the full C2 contract.
- P10 Rolling Request Count: passed, not AP6.
- P13 SLO Summary: supplemental unimplemented starter; defer.
- P18 Merge Event Streams / P20 Group Anagrams: outside source; defer.
- Fundamentals are reinforced within exercises: collections/mutability (C2/C10),
  references (C1/C7/C9), stacks (C4), parsing (AP1), files/context managers and
  exceptions (C5/AP3/AP6), generators (AP10), testing and complexity (all tasks).
  Exposure alone does not mark fundamentals mastered.

The 11 local implementations recorded as passing are P01, P02, P03, P05, P06,
P07, P08, P09, P10, P11 and P12. Nine correspond to source core exercises;
C7 still lacks the required space optimization. Preserve pending explanations
and reattempts in the progress log.
