# GenAI Prep Day 13 basics problem
# Write code that:
# - stores items = [[1, 2], [3, 4], [5]]
# - flattens one level
# - prints [1, 2, 3, 4, 5]

items = [[1, 2], [3, 4], [5]]
A=[]
for i in items:
    if type(i) == list:
        for a in i:
            A.append(a)
    else:
        A.append(i)

print(A)

B=[[3,4],[5]]
flat=[]

for i in B:
    flat.extend(i)
print(flat)