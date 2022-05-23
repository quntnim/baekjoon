from bisect import *

n = int(input())
dic = {}
arr = []
for i in range(n):
    a,b = map(int,input().split())
    dic[a] = b
for i in sorted(dic):
    arr.append(dic.get(i))

dp = [arr[0]]
for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        index = bisect_left(dp,arr[i])
        dp[index] = arr[i]

print(n-len(dp))