n = int(input())
for c in range(1,n+1):
    for i in range(0,n-c):print(' ',end='')
    for i in range(2*c-1):print('*',end='')
    print()