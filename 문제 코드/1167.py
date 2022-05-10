import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    arr = list(map(int,input().split()))
    for i in range(1,len(arr)-2,2):
        graph[arr[0]].append((arr[i],arr[i+1]))
        graph[arr[i]].append((arr[0],arr[i+1]))

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