from decimal import *
getcontext().prec=31
t = int(input())
for _ in range(t):
    result = Decimal()
    while True:
        n = Decimal(input())
        if n == 0:break
        result += n
    result = str(result)
    print(result.rstrip('0').rstrip('.'))