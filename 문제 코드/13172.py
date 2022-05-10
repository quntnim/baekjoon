import sys
input = sys.stdin.readline
mod = 1000000007
n,k = map(int,input().split())

def power(a,b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (power(a,b//2)**2*a)%mod
    else:
        return (power(a,b//2)**2)%mod

def fac(n):
    res = 1
    for i in range(2,n+1):
        res = (res*i)%mod
    return res

a = fac(n)
b = fac(n-k)*fac(k)
print((a%mod) * (power(b,mod-2)%mod)%mod)