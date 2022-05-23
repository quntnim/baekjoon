import sys;p=sys.stdin.readline;m=int(p());x=0;s=0
for i in range(m):
 q=p().split();a,b=int(q[0]),int(q[-1])
 if a==1:x^=b;s+=b
 if a==2:x^=b;s-=b
 if a==3:print(s)
 if a>3:print(x)