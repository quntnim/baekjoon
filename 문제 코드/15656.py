from itertools import *
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
result = list(product(arr, repeat = m))
for i in range(len(result)):
    print(*result[i])