import math
import sys
input = sys.stdin.readline
n,k = map(int,input().split())
arr = []
for _ in range(n):arr.append(int(input()))

def sliding_window(arr,k):
    mx = -math.inf
    temp = 0
    for i in range(k):
        temp += arr[i]
    mx = temp
    for i in range(k,n):
        temp += arr[i]
        temp -= arr[i-k]
        if temp > mx:mx = temp

    return mx

print(sliding_window(arr,k))