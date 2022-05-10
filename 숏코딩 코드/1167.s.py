import sys
sys.setrecursionlimit(10**6)
n=int(input())
g=[[]for _ in range(n+1)]
for _ in range(n):
 a=list(map(int,input().split()))
 for i in range(1,len(a)-2,2):
  g[a[0]].append((a[i],a[i+1]))
  g[a[i]].append((a[0],a[i+1]))
def d(v):
 c[v]=1
 for i,w in g[v]:
  if not c[i]:
   r[i]=r[v]+w
   d(i)
r=[0]*(n+1)
c=[0]*(n+1)
d(1)
m = r.index(max(r))
r=[0]*(n+1)
c=[0]*(n+1)
d(m)
print(max(r))