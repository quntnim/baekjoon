import sys
i=sys.stdin.readline;p=print;n,q=map(int,i().split());h=[0]*(n+1);m=0;t=0
for _ in range(q):
 a,b,c=map(int,i().split());d=c-1
 if a==1:
  h[d]+=b
  if d!=n:t+=b;m=max(m,h[d])
 else:
  if h[-1]+b>max(m,(t+c-1)//n+1):p('YES')
  else:p('NO')