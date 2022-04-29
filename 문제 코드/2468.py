import sys
sys.setrecursionlimit(10**6)

n = int(input());arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y, x, m):
    visit[y][x] = True
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n:
            if not visit[next_y][next_x] and arr[next_y][next_x] > m:
                visit[next_y][next_x] = True
                dfs(next_y,next_x,m)

maxnum = max(map(max,arr))
areas = [0]*(maxnum)

for m in range(0,maxnum):
    visit = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not visit[y][x] and arr[y][x] > m:
                dfs(y,x,m)
                areas[m] += 1

print(max(areas))