import decimal
decimal.getcontext().prec=1500
a,b = map(int,input().split())
print(decimal.Decimal(a)*decimal.Decimal(b))