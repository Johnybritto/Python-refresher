# GenAI Prep Day 11 basics problem
# Write code that:
# - stores number = 7
# - checks whether it is prime
# - prints "prime" or "not prime"

number = 7
prime=True
for i in range(2, number):
    #print(i)
    if number % i == 0: 
        prime=False
        break
#   else:
#        prime=False
#        break
#
if(prime==True):
    print("prime")
else:
    print("not prime")
