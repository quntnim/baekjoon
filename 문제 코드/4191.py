import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v):
    visit[v] = True
    for i in arr[v]:
        if not visit[i]:
            dfs(i)
    return

for _ in range(int(input())):
    n,m,l = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    visit = [False]*(n+1)
    for i in range(m):
        a,b = map(int,input().split())
        arr[a].append(b)

    for i in range(l):
        dfs(int(input()))
    print(visit.count(True))