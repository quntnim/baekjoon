from decimal import *
getcontext().prec=31
t=int(input())
for _ in range(t):
 r = Decimal()
 while True:
  n = Decimal(input())
  if n == 0:break
  r += n
 r = str(r)
 print(r.rstrip('0').rstrip('.'))