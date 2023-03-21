from math import gcd
from random import *

def is_prime(n):
    def miller_rabin(n,b):
        s = 0
        t = n-1
        while t%2 == 0:
            s += 1
            t = t // 2
        x = pow(b,t,n)
        if x == 1 or x == n-1:
            return True
        for _ in range(0,s-1):
            x = pow(x,2,n)
            if x == n-1:
                return True
        return False

    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
        
    for i in [2,3,5,7,11,13,17,19,23,29,31,37,41]:
        if n == i: return True
        if not miller_rabin(n,i):return False
    return True

a,b = map(int,input().split())
for i in range(a,b+1):
    if is_prime(i):print(i,end=' ')