import sys
from bisect import *
input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input().rstrip()))

    dp = [arr[0]]
    for i in range(n):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            index = bisect_left(dp,arr[i])
            dp[index] = arr[i]

    print(len(dp))