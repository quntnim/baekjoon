import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = []
for i in range(m):
    arr.append(list(input().rstrip()))

w = 0
b = 0
def dfs(x,y,col):
    global cnt
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return 0
    if arr[y][x] == col:
        arr[y][x] = 0
        cnt+=1
        dfs(x, y + 1,col)
        dfs(x, y - 1,col)
        dfs(x - 1, y,col)
        dfs(x + 1, y,col)
        return 1
    else:
        return 0

for y in range(m):
    for x in range(n):
        cnt = 0
        if arr[y][x] == 'W':
            dfs(x,y,'W')
            w+=cnt**2
        elif arr[y][x] == 'B':
            dfs(x,y,'B')
            b+=cnt**2

print(w,b)