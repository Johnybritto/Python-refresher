# AP2 and AP3 review notes

## AP2 — Line buckets

Supplied checks pass. Independent lists prevent shared-bucket mutations.
Index modulo M assigns lines round-robin, so sizes differ by at most one.
Empty input, N < M, invalid M, generators, and exact string preservation are covered.
Time: O(N + M). Returned storage: O(N + M); additional working space: O(1).
Returning buckets retains all lines; writing directly to output files is the
follow-up for large inputs. Cleaned names, spacing and unreachable starter code.
Learner explanation remains pending.

## AP3 — Filename prefix and line counts (2026-10-03)

- `open(file, "r", "utf-8")` failed because the third positional argument is
  integer buffering. Use `encoding="utf-8"`.
- Invalid UTF-8 raises while reading, not necessarily while opening. Put both
  opening and iteration inside the try block; record None on failure.
- Catch `OSError` and `UnicodeError`, not bare `except`, which also hides bugs
  and interrupts. Save a count only after the whole file has been read.
- `is_file()` follows symlinks. Skip `is_symlink()` entries first, including
  broken links. Do not recurse into directories.
- Dictionary keys must be `file.name`, not Path objects.
- Iterate lines instead of `readlines()` to avoid retaining whole file contents.
  Blank lines count; a final line without a newline also counts.
- Missing directories raise FileNotFoundError; nondirectory inputs raise
  NotADirectoryError. Directory errors propagate rather than becoming file results.
- Sort matching paths by filename for deterministic dictionary insertion order.
- A stray `x` caused an indentation error and was removed before final review.
  Removed unreachable starter code, restored the function docstring, and cleaned spacing.

Time: O(D + K log K + B), ignoring filename lengths, where D is directory
entries, K is matching files, and B is total bytes read. Memory includes matching
paths/results, directory enumeration storage, and the longest decoded line;
budget O(D + K + L) conservatively for this pathlib implementation.
Supplied checks cover empty files/directories, matching, sorted output, nesting,
symlinks, invalid UTF-8 and simulated permission errors.
Unaided reattempt and learner complexity explanation remain pending.
