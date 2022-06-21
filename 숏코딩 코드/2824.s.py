import math
a=1
input()
t=list(map(int,input().split()))
for i in t:a*=i
b=1
input()
t=list(map(int,input().split()))
for i in t:b*=i
res=str(math.gcd(a,b))
l=len(res)
print(res[l-9:]if l>9 else res)