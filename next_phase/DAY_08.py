# Next Phase Day 8 practice
# Write code that:
# - stores [1, 2, 2, 3, 3, 3] in numbers
# - creates an empty dictionary counts
# - uses a loop to count each value
# - prints counts

numbers = [1, 2, 2, 3, 3, 3]
counts ={}

for i in numbers:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] =1 

print(counts)