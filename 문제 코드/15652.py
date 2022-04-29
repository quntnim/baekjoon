from itertools import *
n,m = map(int,input().split());arr=[]
for i in range(1,n+1):
    arr.append(i)
result = list(combinations_with_replacement(arr,m))
for i in range(len(result)):
    print(*result[i])