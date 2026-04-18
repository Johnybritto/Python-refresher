# Day 10 practice
# Use a loop to print numbers from 1 to 5.

for i in range(1,6):
    print(i)


n=1
while n <=3:
    print(n)
    n=n+1


for n in range(2,8,2):
    print(n)

a = "abc"
res=""
for i in range(len(a)-1,-1,-1):
    res=res+a[i]
print(res)