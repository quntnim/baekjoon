import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(v,col):
    visit[v] = col
    for i in graph[v]:

        if visit[i] == col:
            return False

        if not visit[i]:
            if not dfs(i,-col):
                return False
    return True


for _ in range(int(input())):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visit = [False]*(v+1)
    for _ in range(e):
        a,b = map(int,input().split())
        graph[a].append(b);graph[b].append(a)

    bip = True
    for i in range(v+1):
        if visit[i]:
            continue
        else:
            if not dfs(i,1):
                bip = False
                break
    print('YES' if bip else'NO')