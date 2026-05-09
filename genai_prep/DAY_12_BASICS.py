# GenAI Prep Day 12 basics problem
# Write code that:
# - stores numbers = [1, 2, 3, 4, 5, 6]
# - finds the sum of only the even numbers
# - prints the result

numbers = [1, 2, 3, 4, 5, 6]
sum=0
for i in numbers:
    if i%2==0:
        sum+=i

print(sum)
