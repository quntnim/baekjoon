from decimal import *
getcontext().prec = 301
n = Decimal(input())
print(f'{Decimal(Decimal(1)/Decimal(2)**n):f}')