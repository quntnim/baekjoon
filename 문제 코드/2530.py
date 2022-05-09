h,m,s = map(int,input().split())
t = int(input())
s+=t
while True:
    if s>=60:s-=60;m+=1
    elif m>=60:m-=60;h+=1
    elif h>=24:h-=24
    else:break
print('{0} {1} {2}'.format(h,m,s))