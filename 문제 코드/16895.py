from functools import reduce
from operator import xor
n=int(input())
p=list(map(int,input().split()))
r=reduce(xor, p)
if r==0:
    print(0)
else:
    cnt = 0
    for i in range(n):
        temp = 0
        for j in range(n):
            if i==j:continue
            temp ^= p[j]            
        for j in range(p[i]):
            temp2 = temp
            if temp2^j == 0:cnt+=1
    print(cnt)