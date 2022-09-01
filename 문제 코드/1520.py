import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

m,n = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(m)]
check = [[-1]*(n+1) for _ in range(m+1)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
check[0][0] = 0
def dfs(x,y):
    if y == m-1 and x == n-1 :
        return 1
    res = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < m and 0 <= nx < n:
            if arr[ny][nx] < arr[y][x]:
                if check[ny][nx] >= 0:res += check[ny][nx]
                else:res += dfs(nx, ny)
    check[y][x] = res
    return res
            
print(dfs(0,0))