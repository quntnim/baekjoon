import sys
import math
input = sys.stdin.readline

p = 469762049
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

hole = [0 for i in range(60001)]
mid = [0 for i in range(60001)]
lower = [0 for i in range(60001)]

input()
for i in list(map(int,input().split())):
    hole[i+30000] += 1
input()
for i in list(map(int,input().split())):
    mid[i+30000] += 1
input()
for i in list(map(int,input().split())):
    lower[i+30000] += 1

temp = fft_conv(hole,lower)
res = 0
for i in range(60000):
    res += temp[i*2] * mid[i]
print(res)