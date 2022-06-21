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

def fft_conv(a):
    s = len(a) + len(a) - 1
    n = 1 << s.bit_length()
    a += [0 for _ in range(n - len(a))]
    fft(a)
    for i in range(n):
        a[i] *= a[i]
    fft(a,True)
    return a
    

temp = []
for _ in range(int(input())):
    temp.append(int(input()))

arr = [0]*(max(temp)*2+1)
for i in temp:
    arr[i] = 1
arr[0] = 1

res = fft_conv(arr)
res = res[:-1]
cnt = 0

for _ in range(int(input())):
    i = int(input())
    if int(res[i])>0:cnt+=1

print(cnt)