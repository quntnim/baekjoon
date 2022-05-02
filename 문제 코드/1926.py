import sys
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

def dfs(y, x):
    global cnt
    if x < 0 or x > m - 1 or y < 0 or y > n - 1:
        return False
    if arr[y][x] == 1:
        cnt+=1
        arr[y][x] = 0
        dfs(y, x + 1)
        dfs(y, x - 1)
        dfs(y - 1, x)
        dfs(y + 1, x)
        return True
    else:
        return False

pic = 0;cnt = 0;res=[]
for y in range(n):
    for x in range(m):
        cnt = 0
        if dfs(y,x):
            pic+=1
            res.append(cnt)

print(pic)
try:
    print(max(res))
except ValueError:
    print(0)