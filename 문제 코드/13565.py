import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x,y):
    if x < 0 or x > m-1 or y < 0 or y > n-1:
        return False
    if arr[y][x] == 0:
        arr[y][x] = -1
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    else:
        return False

n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int,input().rstrip())))

for i in range(m):
    if arr[0][i] == 0:
        dfs(i,0)
print('YES'if -1 in arr[n-1] else'NO')