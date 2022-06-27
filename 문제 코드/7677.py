import sys
input = sys.stdin.readline

mod = 10000
p = mod//10*15
def fibo(n):
    f = [0,1]

    for _ in range(n%p):
        f[0],f[1] = f[1]%mod, (f[0]+f[1])%mod
    return f[0]

while True:
    n = int(input())
    if n==-1:break
    print(fibo(n))