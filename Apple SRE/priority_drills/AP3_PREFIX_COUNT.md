# AP3 — Find files by filename prefix and count lines (P0)

## Level check

Have you used `pathlib.Path.iterdir()` and `with open(...)` before?

## One small exercise

Implement `count_prefix_lines(directory, prefix)` in `prefix_line_count.py`.
This matches **filenames**, then counts every line in each matching file.

For this exercise we choose these policies, which the source leaves open:

- Inspect only the immediate children of `directory`; do not recurse.
- Match filenames case-sensitively using `startswith(prefix)`. An empty prefix matches all filenames.
- Skip directories and all symlinks, including links to files.
- Return a dictionary mapping matching filenames to line counts, inserted in sorted filename order.
- Read UTF-8 files one line at a time. Count blank lines and a final line without a newline. An empty file has zero lines.
- For a matching file that raises `OSError` or `UnicodeError` while opening or reading, record `None` and continue. Do not return a partial count.
- Let errors accessing/listing the input directory propagate (including a missing directory or a file used as the directory).

Example: `app-a.log` contains `hello\n\nlast`, `app-b.log` is empty,
and `other.log` contains five lines. With prefix `app-`, return:

```python
{"app-a.log": 3, "app-b.log": 0}
```

First hint: `Path(directory).iterdir()` gives child paths; use each child's
`.name` for matching and sorting. Check for symlinks before following file metadata.
Use a context manager to close each opened file even if reading fails.

Allow 5 minutes to clarify, 30 to implement, and 15 to test and explain.
Discuss sorting cost, total data read, and memory for directory entries/results
plus the longest line. Avoid `read()` and `readlines()`.

Run from the `Apple SRE` folder:

```bash
python3 priority_drills/prefix_line_count.py
```

The implementation now passes supplied checks. See [review notes](REVIEW_NOTES.md)
for fixes; explanation and an unaided reattempt remain pending.
