import sys
sys.setrecursionlimit(13579)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    arr[y][x] = 'S'
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < a and 0 <= ny < b:
            if arr[ny][nx] == 'T':
                dfs(nx,ny)
    return 1


while True:
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        break
    arr = []
    for i in range(b):
        arr.append(list(input()))

    for y in range(b):
        for x in range(a):
            if arr[y][x] == 'S':
                dfs(x,y)
    
    for i in arr:
        for j in i:
            print(j,end='')
        print()