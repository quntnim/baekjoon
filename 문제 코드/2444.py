n = int(input())
for i in range(1,n+1):
    for _ in range(n-i):
        print(' ',end='')
    for _ in range(i*2-1):
        print('*',end='')
    print()

for i in range(1,n)[::-1]:
    for _ in range(n-i):
        print(' ',end='')
    for _ in range(i*2-1):
        print('*',end='')
    print()