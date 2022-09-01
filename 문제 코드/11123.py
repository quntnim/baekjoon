import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x<0 or x>w-1 or y<0 or y>h-1:
        return False
    if arr[y][x] == '#':
        arr[y][x] = '.'
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    else:
        return False


for i in range(int(input())):
    h,w = map(int,input().split())
    arr = []
    for i in range(h):
        arr.append(list(input()))

    cnt = 0
    for y in range(h):
        for x in range(w):
            if arr[y][x] == '#':
                dfs(x,y)
                cnt+=1
    print(cnt)