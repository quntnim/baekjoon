import sys
input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
arr = [[INF] * (n) for _ in range(n)]

for _ in range(m):
    a,b,c = map(int,input().split())
    arr[a-1][b-1] = min(arr[a-1][b-1],c)

for z in range(n):
    arr[z][z] = 0
    for a in range(n):
        for b in range(n):
            arr[a][b] = min(arr[a][b], arr[a][z] + arr[z][b])

for a in range(n):
    for b in range(n):
        if arr[a][b] == INF:
            print('0', end=' ')
        else:
            print(arr[a][b], end=' ')
    print()