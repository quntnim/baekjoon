import sys
import math
input = sys.stdin.readline

p = 998244353
def fft(a, inv=False):
    n = len(a)
    j = 0
    for i in range(1,n):
        rev = n >> 1
        while j >= rev:
            j -= rev
            rev >>= 1
        j += rev
        if i < j:
            a[i], a[j] = a[j], a[i]

    step = 2
    while step <= n:
        half = step // 2
        u = pow(3,p//step,p)
        if inv: u = pow(u,p-2,p)
        for i in range(0, n, step):
            w = 1
            for j in range(i, i + half):
                v = a[j + half] * w
                a[j + half] = (a[j] - v)% p
                a[j] += v
                a[j] %= p
                w *= u
                w %= p
        step *= 2

    if inv:
        invn = p - (p-1) // n
        for i in range(n):
            a[i] = (a[i] * invn)%p

def fft_conv(a, b):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()
    a += [0 for _ in range(n - len(a))]
    b += [0 for _ in range(n - len(b))]
    fft(a);fft(b)
    for i in range(n):
        a[i] *= b[i]
    fft(a,True)
    return a

def dnc_power(a,b):
    if b == 0:
        return a
    t = dnc_power(a,b//2)
    if b % 2 == 1:  
        return fft_conv(t,t)
    else:
        return fft_conv(fft_conv(t,t),a)

n,k = map(int,input().split())
a = list(map(int,input().split()))
ar = [0 for i in range(max(a)+1)]
for i in a:
    ar[i] += 1
print(dnc_power(ar,k))``