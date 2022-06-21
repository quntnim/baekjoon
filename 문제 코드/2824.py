from math import gcd
a=1
input()
temp = list(map(int,input().split()))
for i in temp:a*=i
b=1
input()
temp = list(map(int,input().split()))
for i in temp:b*=i
res = str(gcd(a,b))
if len(res)>9:print(res[len(res)-9:])
else:print(res)