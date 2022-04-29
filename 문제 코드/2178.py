from collections import deque

n,m = map(int,input().split())
arr=[]

for i in range(n):
    arr.append(list(map(int,input())))

q = deque([(0,0)])
dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    x,y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if arr[nx][ny] == 1:
                q.append((nx,ny))
                arr[nx][ny] = arr[x][y] + 1

print(arr[n-1][m-1])