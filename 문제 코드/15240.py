import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

r,c = map(int,input().rstrip().split())
arr = []
for i in range(r):
    arr.append(list(map(int,input().rstrip())))

def dfs(x,y,col,d):
    if x >= c or x < 0 or y >= r or y < 0:
        return 0
    if arr[y][x] == d :
        arr[y][x] = col
        dfs(x-1,y,col,d)
        dfs(x+1,y,col,d)
        dfs(x,y+1,col,d)
        dfs(x,y-1,col,d)
        return 1
    else:
        return 0
a,b,co = map(int,input().split())
d = arr[a][b]
if co != d:
    dfs(b,a,co,d)

for i in arr:
    for j in i:
        print(j,end='')
    print()