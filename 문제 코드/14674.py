from decimal import *;n,k=map(int,input().split());a=[];d=Decimal
for _ in range(n):a.append(list(map(int,input().split())))
a.sort(key=lambda x:(-d(x[2])/d(x[1]),x[1],x[0]))
for i in range(k):print(a[i][0])