n,m,v = map(int,input().split())
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

def bfs(v): 
    visit = [v]
    arr = [v]
    while arr:
        v = arr.pop(0)
        for i in graph[v]:
            if i not in visit:
                visit.append(i)
                arr.append(i)
    return visit

dfs_return = dfs(v)
bfs_return = bfs(v)

for i in dfs_return:print(i,end=' ')
print()
for i in bfs_return:print(i,end=' ')