import sys

def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b)%1000000000
    return a

n=int(sys.stdin.readline())
if n < 0:
    if abs(n)%2 == 0:print(-1)
    else:print(1)
elif n == 0:
    print(0)
else:
    print(1)
print(fibo(abs(n)))