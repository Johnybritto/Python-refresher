target = 48
a = [ 4, 8 ,32, 16 ,5]
seen = {}

for i in range(len(a)):
     val = target - a[i]
     if val in seen:
         print(i, seen[val])
         print(a[i], a[seen[val]])
     else:
            seen[a[i]] = i

                
     