# GenAI Prep Day 9 basics problem
# Write code that:
# - stores numbers = [5, 2, 9, 1, 7]
# - finds the second largest value
# - prints it


numbers = [5, 2, 9, 1, 7]

numbers.sort()

print(numbers[-2])

#print(max(numbers))

a = numbers[0]
for i in numbers:
    if i > a:
        a=i

if a in numbers:
    numbers.remove(a)
a = numbers[0]
for i in numbers:
    if i > a:
        a=i
print(a)  


numbers = [5, 2, 9, 1, 7]

largest = 1  
second = 0 

for i in numbers:
    if i > largest:
        second =largest
        largest=i
    elif i > second:
        second=i

print(second)
