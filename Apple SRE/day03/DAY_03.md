# Day 3, P09: Longest Unique Substring

Today's topics are sliding windows, queues, and intervals. Start with this one
exercise; P10 Rolling Request Count and P11 Merge Intervals follow later.
Allow about one hour for the level check, your attempt, testing, and review.

## Check your current level

For `abca`, what is the longest contiguous substring with no repeated characters,
and what is its length? Answer before starting the implementation.

## One small exercise

Implement `longest_unique_length(text)` in `longest_unique_substring.py`.

- Input: a Python string. Return an integer length, not the substring itself.
- A substring is contiguous: you cannot skip characters.
- Every character in the chosen substring must be different.
- Characters match exactly: uppercase, lowercase, spaces, and Unicode count.
- An empty string returns `0`.
- Aim for O(n) expected time and O(k) extra space, where k is the number of
  distinct characters in the input.

Examples:

```text
"abcabcbb" -> 3 ("abc")
"bbbbb"    -> 1 ("b")
"pwwkew"   -> 3 ("wke"; "pwke" is not contiguous)
""         -> 0
```

Start by describing a simple approach: for each starting position, scan forward
until a character repeats. Consider what work this repeats for nearby starts.

A sliding window is a contiguous section tracked by left and right indices.
You adjust its boundaries while scanning instead of starting over each time.

First hint if needed: remember the characters inside your current window.
When the next character is already present, think about moving the left boundary
until the window can include it without duplicates.

Run from the `Apple SRE` folder:

```bash
python3 day03/longest_unique_substring.py
```

The starter intentionally raises `NotImplementedError`. Try it independently;
ask for the next hint if stuck. Afterward, explain why your window stays valid
and how often each boundary advances. During review, discuss returning the
substring itself instead of just its length.
