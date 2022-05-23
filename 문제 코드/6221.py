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
for i in arr:
    if i > dp[-1]:
        dp.append(i)
    else:
        index = bisect_left(dp,i)
        dp[index] = i

print(len(dp))