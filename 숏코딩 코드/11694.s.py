n=int(input())
p=list(map(int,input().split()))
r=0
for i in range(n):
 r^=p[i]
c=p.count(1)
if c==n:
 if c%2==0:r=1
 else:r=0
if r==0:print('cubelover')
else:print('koosaga')