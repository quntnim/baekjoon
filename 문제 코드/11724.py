import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(i)
    return

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n + 1)
cnt=0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b);graph[b].append(a)

for i in range(1,n+1):
    if not visit[i]:
        dfs(i)
        cnt+=1
print(cnt)