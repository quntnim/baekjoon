import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**3)
n,m,r = map(int,input().split())

arr = [[] for _ in range(n+1)]
visit = [False]*(n+1)
for i in range(m):
    a,b = map(int,input().split())
    arr[a].append(b);arr[b].append(a)
    arr[a].sort();arr[b].sort()

cnt = []
def dfs(v):
    visit[v] = True
    cnt.append(v)
    for i in arr[v]:
        if not visit[i]:
            dfs(i)
    return

dfs(r)
res = [0 for _ in range(n+1)]
for i in range(len(cnt)):
    res[cnt[i]] = i+1
for i in res[1:]:
    print(i)