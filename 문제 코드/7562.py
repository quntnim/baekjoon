from collections import deque

dx = [1,2,2,1,-1,-2,-2,-1]
dy = [2,1,-1,-2,-2,-1,1,2]

def bfs():
    while q:
        x,y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if arr[nx][ny] == 0:
                    q.append((nx,ny))
                    arr[nx][ny] = arr[x][y]+1

for _ in range(int(input())):
    size = int(input())
    arr = [[0 for _ in range(size)] for _ in range(size)]
    stx,sty = map(int,input().split())
    enx,eny = map(int,input().split())
    if stx == enx and sty == eny:
        print(0)
        continue
    q = deque([(stx,sty)])
    bfs()
    print(arr[enx][eny])