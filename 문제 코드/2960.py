import math
a,b = map(int,input().split())
arr = [True] * (a+1)
arr[0] = False; arr[1] = False
res = []
for i in range(2, a+1):
    if arr[i]:
        j = 2
        if i not in res:res.append(i)
        while i*j <= a: 
            if i*j not in res:res.append(i*j)
            arr[i*j] = False
            j += 1
print(res[b-1])