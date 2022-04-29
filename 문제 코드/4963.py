import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x, y):
    if x < 0 or x > h - 1 or y < 0 or y > w - 1:
        return False
    if arr[x][y] == 1:
        arr[x][y] = 0
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x + 1, y + 1)
        dfs(x + 1, y - 1)
        dfs(x - 1, y + 1)
        dfs(x - 1, y - 1)
        return True
    else:
        return False

while True:
    w, h = map(int,input().split());arr = []
    if w == 0 and h == 0:break
    for i in range(h):
        arr.append(list(map(int,input().split())))

    cnt = 0
    for x in range(h):
        for y in range(w):
            if dfs(x,y) == True:
                cnt += 1
    print(cnt)