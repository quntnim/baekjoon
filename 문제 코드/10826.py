import sys
sys.setrecursionlimit(10**6)

def fibo(n):
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n=int(input())
if n < 0:print(-1)
else:print(1)
print(fibo(abs(n)))