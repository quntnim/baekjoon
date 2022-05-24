import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v,e = map(int,input().split())
arr = [[] for _ in range(v+1)]
rev_arr = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    arr[a].append(b)
    rev_arr[b].append(a)

def dfs(v,s):
    visit[v] = 1
    for nx in arr[v]:
        if visit[nx] == 0:
            dfs(nx,s)
    s.append(v)

def rev_dfs(v,s):
    visit[v] = 1
    s.append(v)
    for nx in rev_arr[v]:
        if visit[nx] == 0:
            rev_dfs(nx,s)

stac = []
visit = [0]*(v+1)
for i in range(1, v+1):
    if visit[i] == 0:
        dfs(i,stac)

visit = [0]*(v+1)
res = []
while stac:
    ssc = []
    i = stac.pop()
    if visit[i] == 0:
        rev_dfs(i,ssc)
        res.append(sorted(ssc))

print(len(res))
for i in sorted(res):
    print(*i,end=' ')
    print(-1)