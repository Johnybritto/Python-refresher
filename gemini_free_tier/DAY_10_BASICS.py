# Gemini Free Tier Day 10 basics problem
# Write code that:
# - defines a helper function that takes a list of numbers
# - returns only the even numbers
# - calls the function once
# - prints the result


# Your code here

def helper(x):
    res=[]
    for i in x:
        if i % 2 ==0:
            res.append(i)
    return res


a=[1,2,3,4,5,6,8,9]
result=helper(a)
print(result)
