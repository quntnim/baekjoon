p=469762049
q=range
e=len
def o(a,h=0):
 n=e(a);j=0
 for i in q(1,n):
  d=n>>1
  while j>=d:j-=d;d>>=1
  j+=d
  if i<j:a[i],a[j]=a[j],a[i]
 s=2
 while s<=n:
  z=s//2;u=pow(3,p//s,p)
  if h:u=pow(u,p-2,p)
  for i in q(0,n,s):
   w=1
   for j in q(i,i+z):v=a[j+z]*w;a[j+z]=(a[j]-v)%p;a[j]+=v;a[j]%=p;w*=u;w%=p
  s*=2
 if h:
  k=p-(p-1)//n
  for i in q(n):a[i]=(a[i]*k)%p
def c(a,b):
 s=e(a)+e(b)-1;n=1<<s.bit_length();a+=[0]*(n-e(a));b+=[0]*(n-e(b));o(a);o(b)
 for i in q(n):a[i]*=b[i]
 o(a,1)
 return a
print(max(c(list(map(int,input())),list(map(int,input())))))