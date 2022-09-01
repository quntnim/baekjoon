import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    visit[v] = True
    for i in arr[v]:
        if not visit[i]:
            dfs(i)
    return

n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
visit = [False]*(n+1)
visit[0] = True
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b);arr[b].append(a)
    arr[a].sort();arr[b].sort()

dfs(1)
if False not in visit:
    print(0)
else:
    for i in range(1,n+1):
        if not visit[i]:
            print(i)