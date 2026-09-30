# Day 1, Exercise 1: Two Sum

## Today's goal

Learn how a dictionary can replace repeated searching. You will implement one function,
test its edge cases, and explain its cost.

## Check your current level

Before reading further, answer this in your own words:

If you have the number `2` and need a total of `9`, what other number must you search for?

That missing number is called the **complement**.

## 1. Clarify the contract

The function receives:

- `nums`: a list of integers
- `target`: the required sum

It returns:

- a tuple containing two different indices when a valid pair exists
- `None` when no pair exists

The function must not change `nums`. If several answers exist, any one valid pair is accepted.

Examples:

```text
[2, 7, 11, 15], target 9 -> (0, 1)
[3, 3], target 6       -> (0, 1)
[1, 2], target 8       -> None
```

Notice that the answer contains **indices**, not the values themselves.

## 2. Begin with the simple approach

A direct solution compares every element with every later element:

1. Choose an index `i`.
2. Choose a later index `j`.
3. Check whether `nums[i] + nums[j] == target`.
4. Return the two indices when it matches.

This is a useful first idea because it is easy to verify. In the worst case it checks roughly
every pair, so its time complexity is O(n²). It uses O(1) extra space.

## 3. Find the repeated work

For each number, the nested-loop solution searches the remaining list for its complement.
For a current value `value`, calculate:

```python
complement = target - value
```

A dictionary can remember values already visited and the index where each appeared.
Dictionary lookup is O(1) on average, so each list item needs one average-time lookup.

## 4. The key invariant

Before processing index `i`, the dictionary contains values from indices before `i`.

For each item:

1. Calculate its complement.
2. Check whether that complement is already in the dictionary.
3. If it is, return the stored earlier index and the current index.
4. Otherwise, store the current value and index.

Checking before insertion matters. With `[3, 3]` and target `6`, the second `3` finds the first
one. It also guarantees that one element is not paired with itself.

## 5. Complexity target

- Time: O(n) average, because the list is scanned once.
- Extra space: O(n) in the worst case, because the dictionary may store every value.

This trades additional memory for faster searching.

## Hint ladder

Use one hint at a time only if you are stuck.

### Hint 1

Create an empty dictionary before the loop. Its keys should be numbers already seen and its
values should be their indices.

### Hint 2

Use `enumerate(nums)` to receive both the current index and current value.

### Hint 3

Inside the loop, compute `target - value`, check whether it is in the dictionary, and only then
store the current value.

## One small exercise

Open `two_sum.py` and implement only the body of `two_sum`. Do not change the test cases yet.
Run it with:

```bash
python3 day01/two_sum.py
```

When all tests pass, explain these two points in your own words:

1. Why does checking before insertion handle duplicate values correctly?
2. Why is one dictionary lookup per item better than scanning the remaining list?

## Follow-up for after your solution

If `nums` were already sorted, two pointers could move inward from the left and right ends using
O(1) extra space. Sorting an unsorted input first complicates returning the original indices.

When you finish, send your `two_sum` code for review of correctness, readability, time complexity,
space complexity, and the next improvement.
