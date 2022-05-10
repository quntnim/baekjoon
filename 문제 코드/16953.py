a,b=map(int,input().split())
cnt=1
check=False
while b!=a:
    cnt+=1
    t=b
    if b%10==1:b//=10
    elif b%2==0:b//=2
    if t==b:
        check=True
        break
if not check:print(cnt)
else:print(-1)