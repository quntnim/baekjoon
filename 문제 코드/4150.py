from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def fibo(n):
    if n==0:return 0
    elif n==1 or n==2:return 1
    else:return fibo(n-1)+fibo(n-2)

print(fibo(int(input())))