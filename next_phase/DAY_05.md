# Next Phase Day 5: Class Practice I

## Quick Revision
- A custom module is your own Python file.
- One file can define functions.
- Another file can import and use them.
- You can call functions with `module_name.function_name(...)`.

## Today's Goal
- Add a method to a class
- Use object data inside the method
- Create more than one object
- Do one small exercise

## Check Your Current Level
Before starting, ask yourself:

If a dog object stores its own name, how can that same object print or return a message using that name?

If you can explain that a method can use `self.name`, you're ready.

## Tiny Lesson

### 1. Class Method Idea
A method is a function inside a class.

Example:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return self.name + " says Woof"
```

### 2. Why `self` Matters
`self` lets the method use data stored in that object.

So:

```python
my_dog = Dog("Tommy")
print(my_dog.bark())
```

can use `"Tommy"` from `self.name`.

### 3. More Than One Object
Different objects can use the same method with different data.

Example:

```python
dog1 = Dog("Tommy")
dog2 = Dog("Rocky")
```

Then `dog1.bark()` and `dog2.bark()` can give different results.

## Hint
For today's exercise, keep the method small and use `return`.

## One Small Exercise
Write code that:
- creates a class `Dog`
- stores `name` in `self.name`
- adds a method `bark(self)` that returns `self.name + " says Woof"`
- creates two objects: `dog1 = Dog("Tommy")` and `dog2 = Dog("Rocky")`
- prints `dog1.bark()`
- prints `dog2.bark()`

## Hint 1
Start with:

```python
class Dog:
```

## Hint 2
Inside the class, write both `__init__` and `bark`.

## When You Finish
Send me only your Next Phase Day 5 code.

Then I will review it for:
- Correctness
- Readability
- Time complexity
- Space complexity
- What to improve next
