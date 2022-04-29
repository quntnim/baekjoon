n,m=map(int,input().split());w=[[]for _ in range(n+1)];v=[0 for _ in range(m+1)];c=0;p=n+1
def d(s):
 if k[s]:return 0
 k[s] = 1
 for i in w[s]:
  if v[i]==0 or d(v[i]):v[i]=s;return 1
 return 0
for i in range(1,p):
 a=list(map(int,input().split()))
 for l in a[1::]:w[i].append(l)
for i in range(1,p):
 k=[0]*(p)
 if d(i):c+=1
print(c)