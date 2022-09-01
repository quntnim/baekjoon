import sys
sys.setrecursionlimit(10**6)

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

def dfs(x,y):
    if x<0 or x>n-1 or y<0 or y>n-1:
        return False
    if arr[y][x] == -1:
        print('HaruHaru')
        exit()
    elif arr[y][x] != 0:
        step = arr[y][x]
        arr[y][x] = 0
        dfs(x+step,y)
        dfs(x-step,y)
        dfs(x,y+step)
        dfs(x,y-step)
        return False
    else:
        return False
dfs(0,0)
print('Hing')