# AP2 — Split N file lines into M buckets (P0)

## Level check

If you distribute 7 lines evenly across 3 buckets, what should the three bucket
sizes be? Put any extra lines in the earlier buckets.

## One small exercise

Implement `split_lines(lines, bucket_count)` in `line_buckets.py`.

- `lines` is an iterable of strings, such as an open text file or a generator.
- `bucket_count` is an integer. Raise `ValueError` when it is <= 0, even for empty input.
- Return exactly `bucket_count` independent lists of strings.
- Assign lines round-robin: first to bucket 0, next to bucket 1, and so on,
  returning to bucket 0 after the last bucket.
- Preserve order within each bucket and preserve each string exactly, including
  newlines and blank lines. Do not strip or split the strings further.
- Consume the iterable once; do not call `len(lines)` or first convert it to a list.
- Empty input returns the requested number of empty buckets. When N < M,
  the first N buckets get one line each and the rest stay empty.
- Assume valid string elements and an integer bucket count.

This exercise chooses round-robin distribution, not contiguous file chunks.
That choice permits one pass without knowing N in advance. The source requires
balanced sizes; it leaves the distribution policy for us to clarify.

Example:

```text
lines = ["A", "B", "C", "D", "E", "F", "G"], bucket_count = 3
result = [["A", "D", "G"], ["B", "E"], ["C", "F"]]
```

First hint if needed: a line index and the remainder operator `%` can tell you
which bucket receives that line. Create a separate list for each bucket.

Target O(N + M) time and O(N + M) returned storage (references and bucket lists),
with O(1) working space beyond the result. The result still retains every line;
this is not a constant-memory file splitter. For files too large for memory,
we will discuss writing directly to M output files after your attempt.

Run from the `Apple SRE` folder:

```bash
python3 priority_drills/line_buckets.py
```

Review: the implementation passes all supplied checks. Learner explanation and
large-file discussion remain pending. An open file can be
passed directly inside a `with open(..., encoding="utf-8")` block; the caller
owns opening and closing it. After your attempt, explain why sizes differ by at
most one and the memory/I/O tradeoff of returning lists versus writing files.
