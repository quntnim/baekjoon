a=list(sorted(map(int,input().split())))
s=input()
for i in range(3):
    if s[i]=='A':print(a[0],end=' ')
    elif s[i]=='B':print(a[1],end=' ')
    else:print(a[2],end=' ')