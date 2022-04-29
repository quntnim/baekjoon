n = int(input());m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b);graph[b].append(a)
    graph[a].sort();graph[b].sort()

def dfs(v,visit=[]):
    visit.append(v)
    for i in graph[v]:
        if i not in visit:
            visit = dfs(i,visit)
    return visit

print(len(dfs(1))-1)