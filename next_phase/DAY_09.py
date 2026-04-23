# Next Phase Day 9 practice
# Write code that:
# - prints:
#   - 1. Add
#   - 2. Subtract
# - asks the user to enter a choice
# - if the choice is "1", prints 10 + 5
# - if the choice is "2", prints 10 - 5
# - otherwise prints "Invalid choice"

print("1. Add")
print("2. Subtract")

user = input("Enter your choice: ")

if user == "1":
    first=float(input("enter 1st number"))
    second=float(input("enter 2nd number"))
    print(first + second)
elif user == "2":
    first=float(input("enter 1st number"))
    second=float(input("enter 2nd number"))
    print(first - second)
    
else:
    print("Invalid choice")
