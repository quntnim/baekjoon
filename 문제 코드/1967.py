import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c));graph[b].append((a,c))

def dfs(v):
    visit[v] = True
    for i,w in graph[v]:
        if not visit[i]:
            res[i] = res[v]+w
            dfs(i)

res = [0]*(n+1)
visit=[False]*(n+1)
dfs(1)

m = res.index(max(res))
res = [0]*(n+1)
visit=[False]*(n+1)
dfs(m)

print(max(res))