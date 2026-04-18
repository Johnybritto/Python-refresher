# Day 8 practice
# Create a list with repeated numbers.
A = [1,2,3,3,3,3] 

z=3
t=0
for i in A:
    if i == z:
        t =t +1
print(t) 
# Convert,  it to a set.
B = set(A)
# Print the unique values.
print(B)

if (3 in B):
    print("yes 3 is in the set")


word ="banana"
t=0
check="a"
for i in word:
    if i == check:
        t = t + 1 
print(t)


word = "banana"
counts={}

for i in word:
    if i in counts:
        counts[i]=counts[i]+1
    else:
        counts[i] = 1
print(counts)



    
numbers = [1, 2, 2, 3, 3, 3]
co={}

for i in numbers:
    if i in co:
        co[i]=co[i]+1
    else:
        co[i]=1
print(co)