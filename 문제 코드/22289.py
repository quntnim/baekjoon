import sys
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

x,y = input().split()
lxy = len(x) + len(y)
a = list(map(int,x))
b = list(map(int,y))
res = fft_conv(a,b)
res = res[:lxy - 1]
temp = [0 for _ in range(lxy)]
for i in range(1,lxy)[::-1]:
    temp[i] += res[i-1]%10
    temp[i-1] += res[i-1]//10+temp[i]//10
    temp[i] %= 10
if temp[0] == 0:
    for i in temp[1:]:
        print(i,end='')
else:
    for i in temp:
        print(i,end='')