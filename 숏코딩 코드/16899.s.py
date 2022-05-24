def a(n):
 m=n%4
 if m==0:return n
 if m==1:return 1
 if m==2:return n+1
 return 0
r=0
for _ in range(int(input())):x,m=map(int,input().split());r^=(a(x-1)^a(x+m-1))
print('koosaga'if r>0 else'cubelover')