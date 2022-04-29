import sys;p=sys.stdin.readline;m=int(p());x=0;s=0
for i in range(m):
    q=p().split();a=int(q[0])
    if a==1:x=x^int(q[1]);s+=int(q[1])
    elif a==2:x=x^int(q[1]);s-=int(q[1])
    elif a==3:print(s)
    else:print(x)