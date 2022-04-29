input();d=list(map(int,input().split()));c=0;a=len
def f(b):
 global c;m=a(b)
 if m<=1:return
 if b==sorted(b):return
 v=m//2;x=b[:v];y=b[v:];f(x);f(y);l=0;r=0;n=0;s=0
 while l<a(x)and r<a(y):
  if x[l]<y[r]:b[n]=x[l];l+=1;n+=1;c+=s
  else:b[n]=y[r];r+=1;n+=1;s+=1
 while l<a(x):b[n]=x[l];l+=1;n+=1;c+=s
 while r<a(y):b[n]=y[r];r+=1;n+=1
f(d);print(c)