import sys;input=sys.stdin.readline;n,m=map(int,input().split());d={}
for i in range(1,n+1):
 a=input().rstrip()
 d[i]=a;d[a]=i
for i in range(m):
 c=input().rstrip()
 if c.isdigit():print(d[int(c)])
 else:print(d[c])