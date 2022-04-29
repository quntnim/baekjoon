import sys
sys.setrecursionlimit(10**6)

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())
    arr = [[0] * m for _ in range(n)]

    def dfs(y, x):
        if x < 0 or x > m - 1 or y < 0 or y > n - 1:
            return False
        if arr[y][x] == 1:
            arr[y][x] = 0
            dfs(y, x + 1)
            dfs(y, x - 1)
            dfs(y - 1, x)
            dfs(y + 1, x)
            return True
        else:
            return False

    for i in range(k):
        a,b = map(int,input().split())
        arr[b][a] = 1

    areas = 0
    for y in range(n):
        for x in range(m):
            if arr[y][x] == 1:
                dfs(y,x)
                areas+=1

    print(areas)