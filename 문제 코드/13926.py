from math import gcd
from random import *
from itertools import combinations
import sys
input = sys.stdin.readline

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

def euler(n):
    res=n
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            res *= 1 - (1/i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res *= 1 - (1/n)
    return res

n = int(input())
n2 = n
arr = []
while n!=1:
    a = pollard_rho(n)
    arr.append(a)
    n//=a

res = n2
arr = list(set(arr))
for i in range(1,len(arr)+1):
    temp = combinations(arr,i)
    for j in temp:
        x = 1
        for idx in j:
            x *= idx
        if i%2:res-=(n2//x)
        else:res+=(n2//x)

print(res)