from decimal import *
getcontext().prec=200
a,b,c = map(int,input().split())
print(Decimal(a)*Decimal(b)/Decimal(c))