# Advanced Day 4 practice
# Write code that:
# - stores a list like [1, 2, 2, 3, 4, 4, 5]
A = [1, 2, 2, 3, 4, 4, 5]
B=[]

for i in range(len(A)):
#    print(A[:1])
    if A[i] in A[:i] and A[i] not in B:
           B.append(A[i])
print(B)



numbers = [1, 2, 3, 4, 6, 8]

D=[x*2 for x in numbers if x%2==0]
print(D)


numbers=[7,3,9,2]

current_max=numbers[0]
current_min=numbers[0]

for i in numbers:
      if i > current_max:
            current_max=i
print(current_max)

for i in numbers:
      if i < current_min:
            current_min=i
print(current_min)