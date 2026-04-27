# GenAI Prep Day 2 basics problem
# Write code that:
# - finds the maximum and minimum in a list
# - does not use max() or min()
# - uses a loop
# - prints the final maximum and minimum

nums = [7, 2, 9, 4, 1]

# Hint: start with the first value
current_max = nums[0]
current_min = nums[0]

for i in nums:
    if i > current_max:
        current_max = i
    if current_min > i:
        current_min = i 
print(current_max)
print(current_min)
# TODO:
# loop through the remaining numbers
# if a number is bigger than current_max, update current_max
# if a number is smaller than current_min, update current_min

# print(current_max)
# print(current_min)



