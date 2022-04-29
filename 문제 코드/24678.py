from sys import stdin
for i in range(int(stdin.readline())):
    cnt=0
    for l in map(int,stdin.readline().split()):
        if l%2==1:cnt+=1
    if cnt==3 or cnt==2:print('B')
    elif cnt==0 or cnt==1:print('R')