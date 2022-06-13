n = int(input())
for c in range(n+1,1,-1):
    for i in range(0,n-c+1):
        print(' ',end='')
    for i in range(2*c-3):
        print('*',end='')
    print()