# GenAI Prep Day 3 practice
# Write code that:
# - defines a decorator function my_decorator(func)
# - defines wrapper() inside it
# - prints "Before" before calling func()
# - prints "After" after calling func()
# - defines a function greet() that prints "Hello"
# - creates decorated_greet = my_decorator(greet)
# - calls decorated_greet()

def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

def greet():
    print("Hello")

decorated_greet = my_decorator(greet)
decorated_greet()


def genai(func):
    def wrapper():
        print("hello welcome to the class")
        func()
        print("end of class")
    return wrapper
@genai
def new():
    print("day1")

@genai
def last():
    print("lastday")


new()

last()