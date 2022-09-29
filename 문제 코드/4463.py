from math import gcd
from random import *
from functools import lru_cache
import sys
import math
sys.setrecursionlimit(10**6)


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

def pollard_rho(n):
    if is_prime(n):
        return n
    if n == 1:
        return 1
    if n%2 == 0:
        return 2
    x = randrange(2,n)
    y = x
    c = randrange(1,n)
    d = 1
    while d == 1:
        x = ((x*x%n)+c+n)%n
        y = ((y*y%n)+c+n)%n
        y = ((y*y%n)+c+n)%n
        d = gcd(abs(x-y),n)
        if d == n:
            return pollard_rho(n)
    if is_prime(d):
        return d
    else: 
        return pollard_rho(d)

@lru_cache(maxsize=None)
def fibo(n):
    if n==0:return 0
    elif n==1 or n==2:return 1
    else:return fibo(n-1)+fibo(n-2)

while True:
    try:
        lo,hi = input().split()
    except:
        break
    lo = int(lo,16)
    hi = int(hi,16)
    if lo >= hi:break
    check = False
    print(f'Range {lo} to {hi}:')
    for i in range(hi+1):
        arr = []
        l = -1
        t = fibo(i)
        if t < lo:continue
        if t > hi:break

        if t != 0:
            l = math.log2(t)
            print(f'Fib({i}) = {t}, lg is {l:.6f}')
            
            while t!=1:
                a = pollard_rho(t)
                arr.append(a)
                t//=a
            arr.sort()
            if arr:
                print('Prime factors:', *arr)
            else:
                print('No prime factors')

        else:
            print(f'Fib({i}) = {t}, lg does not exist')
            print('No prime factors')

        check = True
    if not check:
        print('No Fibonacci numbers in the range')
    print()