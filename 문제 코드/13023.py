import sys
sys.setrecursionlimit (10**6)

n,m = map(int,input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b);graph[b].append(a)
visit = [False for _ in range(n)]

def dfs(v,d):
    global res
    visit[v] = True
    if d == 4:
        res = 1
        return
    for i in graph[v]:
        if not visit[i]:
            dfs(i,d+1)
            visit[i] = False

res = 0
for i in range(n):
    dfs(i,0)
    visit[i] = False
    if res == 1:
        break
if res == 1:
    print(1)
else:
    print(0)