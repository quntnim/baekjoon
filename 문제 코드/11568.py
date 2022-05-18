from bisect import *
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))

dp = [arr[0]]
for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        index = bisect_left(dp,arr[i])
        dp[index] = arr[i]

print(len(dp))