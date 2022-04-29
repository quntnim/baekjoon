from collections import deque

m,n = map(int,input().split())
arr=[]
q = deque([])

for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    for l in range(m):
        if arr[i][l] == 1:
            q.append([i,l])


dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = arr[x][y] + 1
                    q.append([nx,ny])
bfs()

breaker = False
for i in arr:
    for l in i:
        if l == 0:
            cnt = 0
            breaker = True
            break
    if breaker:
        break
    cnt = max(cnt, max(i))
            
print(cnt-1)