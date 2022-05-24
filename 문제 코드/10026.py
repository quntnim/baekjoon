import sys
sys.setrecursionlimit(10 ** 6)

n = int(input());arr=[]
for i in range(n):
    arr.append(list(input()))
visit = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(y, x, c):
    visit[y][x] = True
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < n and 0 <= next_y < n:
            if not visit[next_y][next_x] and arr[next_y][next_x] == c:
                visit[next_y][next_x] = True
                dfs(next_y,next_x,c)

cnt = 0;cnt2 = 0
for y in range(n):
    for x in range(n):
        if visit[y][x] == False:
            dfs(y,x,arr[y][x])
            cnt+=1

visit = [[False] * n for _ in range(n)]
for y in range(n):
    for x in range(n):
        if arr[y][x]=='R':
            arr[y][x]='G'

for y in range(n):
    for x in range(n):
        if visit[y][x] == False:
            dfs(y,x,arr[y][x])
            cnt2+=1

print(cnt, cnt2)