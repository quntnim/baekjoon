import sys
input = sys.stdin.readline
mod = 1000000007

N = 4000001
factorial = [1] * N
for i in range(1,N):
    factorial[i] = (factorial[i-1]*i)%mod

def power(a,b):
    if b == 0:
        return 1
    if b % 2 == 1:
        return (power(a,b//2)**2*a)%mod
    else:
        return (power(a,b//2)**2)%mod

for i in range(int(input())):
    n,k = map(int,input().split())
    print(factorial[n] * power(factorial[n-k]*factorial[k]%mod, mod-2)%mod)