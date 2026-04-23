# Next Phase Day 1 practice
# Write code that:
# - defines a function add_numbers(first_number, second_number)
# - returns the sum
# - stores the result of add_numbers(10, 20) in total
# - prints total

# function to convert str to int or float dynamically otherwise just use  num = float(inputvalue)
def convert_number(value):
    if isinstance(value, str):
        if "." in value:
            return float(value)
        return int(value)
    return value


def add_numbers(first_number, second_number):
    if isinstance(first_number, (int, float)) and isinstance(second_number , (int, float)):
        return first_number + second_number
    else:
        return "only numbers allowed"

total = add_numbers("5", 6)
print(total)