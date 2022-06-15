import sys
input = sys.stdin.readline

def euler(n):
    res=n
    for p in range(2,int(n**0.5)+1):
        if n % p == 0:
            while n % p == 0:
                n //= p
            res *= 1 - (1/p)
    if n > 1:
        res *= 1 - (1/n)
    return res

arr = [0]*10001
temp = 1
for _ in range(int(input())):
    n,m=map(int,input().split())
    for i in range(temp,m+1):
        arr[i] = arr[i-1]+round(euler(i))
    temp = m
    print('{0} {1}'.format(n,arr[m]+1))