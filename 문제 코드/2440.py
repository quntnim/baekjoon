n = int(input())
for i in range(n):
    for l in range(n,0,-1):
        print('*',end='')
    n-=1
    print()