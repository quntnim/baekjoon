from decimal import *
getcontext().prec = 200
a,b=map(Decimal,input().split())
print("{:f}".format(pow(a,b)))