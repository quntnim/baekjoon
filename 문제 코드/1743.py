import sys
sys.setrecursionlimit(10**6)

n,m,k = map(int,input().split())
arr = [[0] * m for _ in range(n)]

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

for i in range(k):
    a,b = map(int,input().split())
    arr[a-1][b-1] = 1

res=[]
for y in range(n):
    for x in range(m):
        cnt = 0
        if dfs(y,x):
            res.append(cnt)

print(max(res))