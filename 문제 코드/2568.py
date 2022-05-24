from bisect import *

n = int(input())
dic = {}
arr = []
temp = []
removelist = []
for i in range(n):
    a,b = map(int,input().split())
    dic[b] = a
for i in sorted(dic):
    arr.append(dic.get(i))

dp = [arr[0]]
for i in arr:
    if i > dp[-1]:
        dp.append(i)
    else:
        index = bisect_left(dp,i)
        dp[index] = i
    temp.append(dp.index(i)+1)

l = len(dp)
for i in range(len(arr)-1,-1,-1):
    if temp[i] == l:
        removelist.append(arr[i])
        l-=1

print(n-len(dp))
for i in removelist:
    arr.remove(i)
for i in sorted(arr):
    print(i)