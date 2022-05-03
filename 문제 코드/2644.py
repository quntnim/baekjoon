import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
p1, p2 = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b);graph[b].append(a)

check = False
visit=[False]*(n+1)
def dfs(v,cnt):
    global check
    visit[v] = True
    if v == p2:
        print(cnt)
        check = True
    else:
        for i in graph[v]:
            if not visit[i]:
                dfs(i,cnt+1)
dfs(p1,0)
if not check:
    print(-1)