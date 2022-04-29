import sys
sys.setrecursionlimit(10**6)

m,n,k = map(int,input().split())
arr = [[1] * m for _ in range(n)]

def dfs(y, x):
    global cnt
    if x < 0 or x > m - 1 or y < 0 or y > n - 1:
        return False
    if arr[y][x] == 1:
        cnt+=1
        arr[y][x] = 0
        dfs(y, x + 1)
        dfs(y, x - 1)
        dfs(y - 1, x)
        dfs(y + 1, x)
        return True
    else:
        return False

for _ in range(k):
    x0,y0,x1,y1 = map(int,input().split())
    for l in range(y0,y1):
        for i in range(x0,x1):
            arr[i][l] = 0

areas = 0
cnt = 0
count = []
for y in range(n):
    for x in range(m):
        if arr[y][x] == 1:
            cnt = 0
            dfs(y,x)
            count.append(cnt)
            areas+=1

count.sort()
print(areas)
print(*count)