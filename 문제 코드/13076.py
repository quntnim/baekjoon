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
    n=int(input())
    for i in range(temp,n+1):
        arr[i] = arr[i-1]+round(euler(i))
    temp = n
    print(arr[n]+1)