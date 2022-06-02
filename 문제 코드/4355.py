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

while True:
    n = int(input())
    if n == 0:break
    print(round(euler(n)))