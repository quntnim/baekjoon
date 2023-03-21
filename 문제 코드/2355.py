if a==b:print(a)
a,b=map(int,input().split())
else:print(((a+b)*(b-a+1))//2 if a<b else((b+a)*(a-b+1))//2)