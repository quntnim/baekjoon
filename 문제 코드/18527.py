import sys
input = sys.stdin.readline

n, t = map(int, input().rstrip().split())
mod = 998244353
arr = []
num = 0
for i in range(n):
    x = int(input().rstrip())-1
    num += x
    arr.append(x)
res = t - n+1 - num
for i in range(n-1):
    num -= arr[i]
    res = res*(t-num+1)%mod
print(res)