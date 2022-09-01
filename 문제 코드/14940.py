from collections import deque
n,m = map(int,input().split())

arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    q.append((nx,ny))
                    arr[nx][ny] = arr[x][y]+1

breaker = False
for y in range(n):
    for x in range(m):
        if arr[y][x] == 2:
            q = deque([(y,x)])
            bfs()
            breaker = True
            break
    if breaker:break

for i in arr:
    for j in i:
        print(0 if j==0 else j-2, end = ' ')
    print()