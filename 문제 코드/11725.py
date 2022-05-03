import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b);graph[b].append(a)

res = [0]*n
visit=[False]*(n+1)
def dfs(v):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            res[i-1] = v
            dfs(i)
dfs(1)
for i in range(1,n):
    print(res[i])