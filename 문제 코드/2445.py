n = int(input())
for i in range(1,n+1):
    for _ in range(i):
        print('*',end='')
    for _ in range((2*n)-i*2):
        print(' ',end='')
    for _ in range(i):
        print('*',end='')
    print()

for i in range(1,n)[::-1]:
    for _ in range(i):
        print('*',end='')
    for _ in range((2*n)-i*2):
        print(' ',end='')
    for _ in range(i):
        print('*',end='')
    print()