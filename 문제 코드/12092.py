import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
r,c = map(int,input().split())
arr = []
for i in range(r):
    arr.append(list(input()))

def dfs(x,y):
    if x >= c or x < 0 or y >= r or y < 0:
        return 0
    elif arr[y][x] == '#' : 
        arr[y][x] = '?'
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        dfs(x+1,y+1)
        dfs(x-1,y-1)
        dfs(x-1,y+1)
        dfs(x+1,y-1)
        return 1
    else:
        return 0

cnt = 0
for y in range(r):
    for x in range(c):
        if arr[y][x] == '#':
            cnt+=1
            dfs(x,y)

print(cnt)