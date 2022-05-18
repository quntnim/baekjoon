from bisect import *
import sys
input = sys.stdin.readline

for case in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    dp = [arr[0]]
    for i in range(n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            index = bisect_left(dp,arr[i])
            dp[index] = arr[i]

    print('Case #{0}'.format(case+1))
    if len(dp) >= k:
        print(1)
    else:
        print(0)