# Next Phase Day 6: Class Practice II

## Quick Revision
- A method is a function inside a class.
- `self.name` stores data inside one object.
- Different objects can use the same method with different data.

## Today's Goal
- Understand instance attributes vs class attributes
- See what data belongs to each object
- See what data is shared by the whole class
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If all dogs share the same animal type, should that value be stored separately in every object or once for the whole class?

If you can explain why shared data can live on the class, you're ready.

## Tiny Lesson

### 1. Instance Attribute
An instance attribute belongs to one object.

Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name
```

Here, `self.name` can be different for every dog.

### 2. Class Attribute
A class attribute belongs to the class itself and is shared.

Example:

```python
class Dog:
    animal_type = "dog"

    def __init__(self, name):
        self.name = name
```

Here:
- `self.name` is different for each object
- `animal_type` is shared by all dogs

### 3. Example Use

```python
dog1 = Dog("Tommy")
dog2 = Dog("Rocky")

print(dog1.name)
print(dog2.name)
print(Dog.animal_type)
```

## Hint
For today's exercise, focus on seeing the difference clearly.

## One Small Exercise
Write code that:
- creates a class `Dog`
- adds a class attribute `animal_type = "dog"`
- stores `name` in `self.name`
- creates `dog1 = Dog("Tommy")` and `dog2 = Dog("Rocky")`
- prints `dog1.name`
- prints `dog2.name`
- prints `Dog.animal_type`

## Hint 1
The class attribute goes directly inside the class, not inside `__init__`.

## Hint 2
The object names still go in `self.name`.

## When You Finish
Send me only your Next Phase Day 6 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
