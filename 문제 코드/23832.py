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


n=int(input())
a = 0
for i in range(1,n+1):
    a+=round(euler(i))
print(a-1)