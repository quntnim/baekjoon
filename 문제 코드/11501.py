import math
mod = 1000000007
t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    result = math.comb(a,b)%mod
    print(result)