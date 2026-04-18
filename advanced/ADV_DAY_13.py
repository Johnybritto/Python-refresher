# Advanced Day 13 practice
# Write code that:
# - stores [1, 2, 2, 3, 4, 4, 5] in numbers
# - creates an empty list duplicates
# - uses a loop to collect duplicate values only once
# - prints duplicates
A =  [1, 2, 2, 3, 4, 4, 5]
B= []

for i in range(len(A)):
    if A[i] in A[:i] and A[i] not in B:
        B.append(A[i])
print(B)

numbers = [1, 2, 2, 3, 4, 4, 5]

#another way 
seen = set()
duplicates = set()

for item in numbers:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(duplicates)