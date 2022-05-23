n = int(input())
m=0
for i in range(n):
    for l in range(0,m,1):
        print(' ',end='')
    for l in range(n,0,-1):
        print('*',end='')
    n-=1
    m+=1
    print()