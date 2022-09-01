import sys
input = sys.stdin.readline

p1 = 998244353
p2 = 2281701377
i1 = 253522377
i2 = -110916040
def fft(a, p, inv=False):
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

def fft_conv(a,b,p):
    s = len(a) + len(b) - 1
    n = 1 << s.bit_length()
    a += [0 for _ in range(n - len(a))]
    b += [0 for _ in range(n - len(b))]
    c = [0 for _ in range(n)]
    fft(a,p);fft(b,p)
    for i in range(n):
        c[i] = a[i] * b[i]
    fft(c,p,True)
    return c[:s]

def crt(x, y):
    return (x*p2*i2+y*p1*i1)%(p1*p2)

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

res = 0
conv = fft_conv(a,b,p1)
fft(a,p1,True)
fft(b,p1,True)
conv2 = fft_conv(a,b,p2)[:n -~ m]
for i,j in zip(conv,conv2):
    res ^= crt(i,j)
print(res)