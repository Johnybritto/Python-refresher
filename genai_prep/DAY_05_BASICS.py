# GenAI Prep Day 5 basics problem
# Write code that:
# - stores numbers = [1, 2, 2, 3, 4, 4, 5]
# - finds duplicate values
# - prints [2, 4]

numbers = [1, 2, 2, 3, 4, 4, 5]

duplicate = [] 

for i in range(len(numbers)):
    if numbers[i] in numbers[:i] and numbers[i] not in duplicate:
        duplicate.append(numbers[i])

print(duplicate)


seen = set()
dup = set ()

for i in numbers:
    if i in seen:
        dup.add(i)
    else:
        seen.add(i)
print(dup)