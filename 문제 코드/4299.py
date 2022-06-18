h,c = map(int,input().split())
if (h+c)%2:print(-1)
elif c>h:print(-1)
else:print((h+c)//2,(h-c)//2)