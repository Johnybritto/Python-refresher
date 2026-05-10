# GenAI Prep Day 14 basics problem
# Write code that:
# - stores numbers = [2, 7, 11, 15]
# - stores target = 9
# - finds two numbers that add up to target
# - prints the two numbers

numbers = [2, 7, 11, 15]
target = 9

comp={}
for i in numbers:
   # print(i)
    val = target - i
    if val in comp:
        print(i, val)
        break
    else:
        comp[i] = True
seen={}
for index , values in enumerate(numbers):
    v = target - values
    if v in seen:
        print(values,v)
        print(seen[v], index)
        break
    seen[v] =index
print(seen)

