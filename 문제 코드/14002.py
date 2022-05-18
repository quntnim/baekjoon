from bisect import *

n = int(input())
arr = list(map(int,input().split()))

dp = [1]*n
for i in range(n):
    for l in range(i):
        if (arr[i] > arr[l]):
            dp[i] = max(dp[i], dp[l]+1)
m = max(dp)
print(m)

m_index = dp.index(m)
arr2 = []
while m_index >= 0:
    if dp[m_index] == m:
        arr2.append(arr[m_index])
        m-=1
    m_index-=1
arr2.reverse()
for i in arr2:
    print(i,end=' ')