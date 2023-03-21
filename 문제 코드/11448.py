import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
for i in range(int(input())):
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(input()))
    
    cnt = 0
    def dfs(x,y):
        global cnt
        if x >= n or x < 0 or y >= n or y < 0:
            return 0
        elif arr[y][x] == '-':
            cnt += 1
            arr[y][x] = '+'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y+1)
            dfs(x-1,y-1)
            dfs(x-1,y+1)
            dfs(x+1,y-1)
            return 1
        elif arr[y][x] == 'w':
            arr[y][x] = '+'
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            dfs(x+1,y+1)
            dfs(x-1,y-1)
            dfs(x-1,y+1)
            dfs(x+1,y-1)
            return 2
        else:
            return 0
    
    for y in range(n):
        for x in range(n):
            if arr[y][x] == 'w':
                dfs(x,y)
    print(cnt)