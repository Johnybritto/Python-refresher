# GenAI Prep Day 5: OOP Later Topics Overview

## Quick Revision
- Objects can store data in attributes like `self.name`.
- Methods can read object data.
- Methods can also change object data.

## Today's Goal
- Get a light introduction to class methods
- Get a light introduction to static methods
- Get a light introduction to inheritance
- Understand when these are useful later

## Check Your Current Level
Before starting, ask yourself:

If something belongs to the whole class instead of one object, should it always be an instance method?

If you can explain why not, you're ready.

## Tiny Lesson

### 1. Class Method Idea
A class method works with the class itself.

It uses `cls` instead of `self`.

Example:

```python
class Dog:
    animal_type = "dog"

    @classmethod
    def get_animal_type(cls):
        return cls.animal_type
```

### 2. Static Method Idea
A static method is a function placed inside a class when the logic is related to the class, but it does not need `self` or `cls`.

Example:

```python
class Dog:
    @staticmethod
    def sound():
        return "Woof"
```

### 3. Inheritance Idea
Inheritance means one class can build on another class.

Example:

```python
class Animal:
    def eat(self):
        return "eating"

class Dog(Animal):
    def bark(self):
        return "Woof"
```

Now `Dog` can use both `eat()` and `bark()`.

### 4. What To Remember Today
You do not need mastery yet.

Just keep this simple view:
- instance method -> works with one object
- class method -> works with the class
- static method -> related helper logic
- inheritance -> one class builds on another

## Hint
Today's exercise is just a small demonstration, not deep OOP.

## One Small Exercise
Write code that:
- creates a class `Dog`
- adds a class attribute `animal_type = "dog"`
- adds a class method `get_animal_type(cls)` that returns `cls.animal_type`
- adds a static method `sound()` that returns `"Woof"`
- prints `Dog.get_animal_type()`
- prints `Dog.sound()`

## Hint 1
Use:

```python
@classmethod
```

above the class method.

## Hint 2
Use:

```python
@staticmethod
```

above the static method.

## When You Finish
Send me only your GenAI Prep Day 5 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next

## LeetCode-Style Basics Problem
This is the small basics problem for Day 5 from the roadmap.

### Problem
Write code that finds duplicate values in a list.

Use this list:

```python
numbers = [1, 2, 2, 3, 4, 4, 5]
```

Your program should print:

```python
[2, 4]
```

### Hint 3
Use a loop and make sure each duplicate is added only once.

## When You Finish The Basics Problem
Send me only your Day 5 basics-problem code.
