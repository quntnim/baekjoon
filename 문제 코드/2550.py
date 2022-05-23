from bisect import *

n = int(input())
dic = {}
arr = []
for i in range(n):
    a,b = map(int,input().split())
    dic[a] = b
for i in sorted(dic):
    arr.append(dic.get(i))

dp = [-1000000001]
check = [0]*(n+1)
for i in range(1,len(arr)):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
        check[i] = len(dp)-1
        m_idx = check[i]
    else:
        check[i] = bisect_left(dp,arr[i])
        dp[check[i]] = arr[i]

print(m_idx)
res = []
for i in range(n,0,-1):
    if check[i] == m_idx:
        res.append(arr[i])
        m_idx-=1

for i in reversed(res):
    print(i,end=' ')
print()