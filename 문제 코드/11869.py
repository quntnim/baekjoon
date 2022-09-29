from functools import reduce
from operator import xor
n=int(input())
p=list(map(int,input().split()))
res = reduce(xor, p)
if res==0:
    print('cubelover')
else:
    print('koosaga')