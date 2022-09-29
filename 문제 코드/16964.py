n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b);graph[b].append(a)

tc = list(map(int,input().split()))
def dfs(v,visit=[]):
    visit.append(v)
    for i in graph[v]:
        if i not in visit:
            for t in tc:
                if t in graph[v]:
                    visit = dfs(t,visit)
    return visit

dfs_return = dfs(1)