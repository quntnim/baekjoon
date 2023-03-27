import sys
sys.setrecursionlimit(123456)
input = sys.stdin.readline
n = int(input())

arr = [[] for _ in range(n+1)]
check = [False]*(n+1)
depth = [0]*(n+1)
parent = [0]*(n+1)

for i in range(n-1):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(x,d):
    check[x] = True
    depth[x] = d
    for next in arr[x]:
        if check[next]:
            continue
        parent[next] = x
        dfs(next,d+1)
dfs(1,0)

def lca(a,b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a != b:
        a = parent[a]
        b = parent[b]
    return a

m = int(input())
for i in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))