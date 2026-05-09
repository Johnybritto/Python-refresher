# GenAI Prep Day 10 basics problem
# Write code that:
# - stores a = 10
# - stores b = 0
# - tries to divide a by b
# - prints the result if division works
# - otherwise prints "Cannot divide by zero"

a = 10
b = 0


try:
    c = a/b
    print(c)
except:
    print("Cannot divide by zero")