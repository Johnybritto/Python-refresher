# Gemini Free Tier Day 14 basics problem
# Write code that:
# - creates a list of numbers
# - prints the total
# - prints the average


# Your code here
numbers = [ 1 ,2, 3,4 ]

res = sum([ x for x in numbers ])
print(res)

avg = res/len(numbers)
print(avg)