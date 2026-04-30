# GenAI Prep Day 4: OOP Quick Finish

## Quick Revision
- A decorator takes a function and returns a wrapped function.
- The wrapper is needed because the decorator must return a function.
- Decorators are useful when the same wrapping behavior repeats.

## Today's Goal
- Change object data after creation
- Add more than one method to a class
- See how objects can hold and update their own state
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a dog object starts with one name, can that object's data be changed later?

If you can explain why yes, you're ready.

## Tiny Lesson

### 1. Object Data Can Change
An object can store data in attributes like `self.name`.

That data is not frozen forever. You can update it later.

Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

Then:

```python
dog1 = Dog("Tommy")
dog1.name = "Bruno"
print(dog1.name)
```

This prints:

```python
Bruno
```

### 2. More Than One Method
A class can have many methods, not just one.

Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return self.name + " says Woof"

    def rename(self, new_name):
        self.name = new_name
```

### 3. Why This Matters
Real objects usually need to:
- store data
- show data
- change data

### 4. Simple Mental Model
- attributes store object data
- methods use or change that data

## Hint
For today's exercise, keep the class small and focus on updating one attribute.

## One Small Exercise
Write code that:
- creates a class `Dog`
- stores `name` in `self.name`
- adds a method `bark(self)` that returns `self.name + " says Woof"`
- adds a method `rename(self, new_name)` that changes `self.name`
- creates `dog1 = Dog("Tommy")`
- prints `dog1.bark()`
- changes the name to `"Bruno"` using `rename`
- prints `dog1.bark()` again

## Hint 1
Start with:

```python
class Dog:
```

## Hint 2
Inside `rename`, use:

```python
self.name = new_name
```

## When You Finish
Send me only your GenAI Prep Day 4 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 4 from the roadmap.

### Problem
Write code that counts the frequency of each character in a string.

Use this string:

```python
text = "banana"
```

Your output should be a dictionary showing how many times each character appears.

Example idea:

```python
{'b': 1, 'a': 3, 'n': 2}
```

### Hint 3
Use an empty dictionary and update the count while looping through the string.

## When You Finish The Basics Problem
Send me only your Day 4 basics-problem code.
