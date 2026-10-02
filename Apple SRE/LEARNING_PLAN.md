# Apple ASE/SRE — priority-first coding plan

## Source

Use the [supplied seven-day sprint](Apple_ASE_SRE_7_Day_Interview_Preparation_Plan.md)
as the source of priorities, replacing the old five-day order. Its dates are
historical schedule labels, not newly confirmed interview dates. These are
preparation exercises, not a confirmed question bank.

Existing day folders and P01–P20 IDs stay unchanged. Source C/A/AP IDs are
separate identifiers. See [PLAN_MAPPING.md](PLAN_MAPPING.md) for coverage.
Preserve passing work; do not treat passing tests as independent mastery.

## P0 first: next coding sequence

1. **AP1 IPv4 validation — supplied checks pass; robustness repair pending.** Manual parsing, octet count/range,
   ASCII characters, explicit whitespace/leading-zero policy.
2. **AP2 N file lines into M buckets — supplied checks pass; explanation pending.** Balanced sizes, empty input, invalid M,
   large-file memory and I/O tradeoffs.
3. **AP3 Prefix-matching files and line counts — supplied checks pass; unaided retry pending.** Deterministic output,
   unreadable/missing files, nesting and symlink policy.
4. **AP4 START/END log correlation.** Request IDs, timestamps, duplicates,
   missing partners and out-of-order records.
5. **AP5 p95 latency.** Explicit percentile convention, empty/single input,
   duplicates and large-data tradeoffs.
6. **AP6 Tail last N lines.** Bounded memory, N boundaries, file/encoding errors.

This preserves the source's explicit AP1 → AP6 order. Interleave these P0 gaps
and repairs in review blocks; finish them before moving to P1:

- **C2 most frequent item:** counting in P02/P03 is partial coverage. Implement
  a dedicated result with deterministic ties and case/punctuation rules.
- **C7 cycle detection:** replace the existing visited-set approach with
  slow/fast pointers to meet O(1) extra space.
- **C6:** unaided reattempt after the window-length hint.
- **C1/C3/C4/C5:** use existing solutions for explanation/recall checks;
  demonstrate real file iteration for C5 as well as its iterable parser.
- **A1 outline:** bounded workers, timeouts versus overall deadlines, latency,
  partial failures, threads versus async. Coding A1 is P1, its outline is P0.

If a repeated weakness needs longer, give it the next full coding block, then
resume AP order. Do not wait until P1 to repair weak P0 work.

## After P0 is reliable

- AP7–AP11 in order: service error thresholds, phone-like normalization,
  missing sequences, lazy generator, debugging drill.
- C11 bounded-heap top-K and C12 graph reachability.
- A1 implementation, A2 retries, A3 configuration diff, A4 log-based error rate.
  Reuse parsing work between A4/AP7 rather than duplicating it.
- C8/C10 need unaided reattempts after hints; C9 needs explanation/recall.
  Their existing implementations already passed checks.
- P2 only afterward: C13 simple DP and C14 LRU or token-bucket design.

SLO Summary (P13) is **deferred supplemental practice**, only partly related to
A4: it lacks log parsing, invalid-record reporting and time-window handling.
Keep its starter intact. P02 First Unique Character and P10 Rolling Request
Count remain useful passed supplements. P18 Merge Event Streams and P20 Group
Anagrams are outside the source plan and deferred.

## Pacing and completion

Use a 60-minute coding block: 5 minutes clarify, 25–35 implement, 10 test/explain,
then repair/recall. One active exercise at a time; harder work can span sessions.
For every task clarify the contract, attempt without a solution, test normal,
empty, boundary and failure cases, explain correctness and complexity, discuss
one changed requirement, and reattempt from blank after help.

The source also allocates time for SRE fundamentals, Linux/networking, incidents,
distributed design, Kubernetes/capacity/DR, spoken practice, stories and mocks.
Retain those checklists in the saved source. Coding progress does not complete
them. If only one hour is available, use the coding block and carry the remaining
work forward; do not compress the full three-hour sprint into it.
