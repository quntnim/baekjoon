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

num = int(input())

arr = {2:0}
while num!=1:
    a = pollard_rho(num)
    if a not in arr.keys():
        arr[a] = 1
    else:
        arr[a] += 1
    num//=a

res = 1
for i in arr.values():
    res *= i+1
print(res)