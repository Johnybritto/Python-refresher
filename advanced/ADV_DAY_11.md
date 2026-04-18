# Advanced Day 11: `__init__` and Object Data

## Quick Revision From Advanced Day 10
- A class is a blueprint.
- An object is created from a class.
- `pass` can be used when the class is empty for now.
- `Dog()` creates an object from the `Dog` class.

## Today's Goal
- Understand what `__init__` does
- Store data inside an object
- Read object attributes
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If different dogs should have different names, where should each dog's name be stored?

If you can explain that each object should store its own data, you're ready.

## Tiny Lesson

### 1. Why `__init__` Matters
`__init__` runs when an object is created.

It helps set up the object's starting data.

### 2. Example

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

Now we can create an object:

```python
my_dog = Dog("Tommy")
print(my_dog.name)
```

This prints:

```python
Tommy
```

### 3. Beginner Idea
- `name` is the value we pass in
- `self.name` stores it inside the object

### 4. Why `self` Is There
`self` means “this object.”

It helps Python know which object's data we are talking about.

## Hint
For today's exercise, copy the basic pattern first.

Do not worry about methods beyond `__init__` yet.

## One Small Exercise
Write code that:
- creates a class named `Dog`
- adds `__init__(self, name)`
- stores `name` in `self.name`
- creates `my_dog = Dog("Tommy")`
- prints `my_dog.name`

## Hint 1
Start with:

```python
class Dog:
    def __init__(self, name):
```

## Hint 2
Inside `__init__`, use:

```python
self.name = name
```

## When You Finish
Send me only your Advanced Day 11 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
