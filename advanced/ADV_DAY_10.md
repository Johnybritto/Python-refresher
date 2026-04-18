# Advanced Day 10: Classes and Objects

## Quick Revision From Advanced Day 9
- `import` brings a module into your program.
- `math.sqrt(...)` gives a square root.
- `math.floor(...)` goes down.
- `math.ceil(...)` goes up.

## Today's Goal
- Understand what a class is
- Understand what an object is
- Create one simple class
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If we want to describe one student with related data and behavior, should we keep making separate variables, or should we group them in one structure?

If you can explain that grouping can help, you're ready.

## Tiny Lesson

### 1. What Is a Class?
A class is like a blueprint.

It describes what kind of object we want to create.

Example idea:
- a `Student` class
- a `Car` class
- a `Book` class

### 2. What Is an Object?
An object is one real thing created from a class.

For example:
- `Student` is the class
- one specific student object is created from it

### 3. Simple Beginner Example

```python
class Dog:
    pass
```

This creates a very simple class named `Dog`.

Now we can create an object:

```python
my_dog = Dog()
print(my_dog)
```

### 4. Why This Matters
Classes help group related ideas together.

Later, they can hold:
- data
- functions
- behavior

## Hint
For today's exercise, keep it very small.

Do not worry about `__init__` yet. That comes next.

## One Small Exercise
Write code that:
- creates a class named `Dog`
- uses `pass` inside the class
- creates an object named `my_dog`
- prints `my_dog`

## Hint 1
Start with:

```python
class Dog:
    pass
```

## Hint 2
Create the object with:

```python
my_dog = Dog()
```

## When You Finish
Send me only your Advanced Day 10 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
