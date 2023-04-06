from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def fibolike(n):
    if n==0:return 0
    elif n in [1,2,3]:return 1
    else:return fibolike(n-1)+fibolike(n-3)

print(fibolike(int(input())))