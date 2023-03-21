import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

while 1:
    a,b = map(int,input().split())
    if a == 0 and b == 0:break
    arr = []
    for i in range(b):
        arr.append(list(input().rstrip()))

    cnt = 0
    def dfs(x,y):
        global cnt
        if x >= a or x < 0 or y >= b or y < 0:
            return 0
        elif arr[y][x] == '.':
            cnt+=1
            arr[y][x] = 0
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return 1
        else:
            return 0

    for y in range(b):
        for x in range(a):
            if arr[y][x] == '@':
                arr[y][x] = '.'
                dfs(x,y)
    print(cnt)