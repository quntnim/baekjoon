import sys
input = sys.stdin.readline
INF = 1e9

for _ in range(int(input())):
    n,m,w = map(int,input().split())
    arr = [[] for _ in range(n+1)]
    dist = [INF]*(n+1)

    for _ in range(m):
        a,b,c = map(int,input().split())
        arr[a].append((b,c))
        arr[b].append((a,c))
    for _ in range(w):
        a,b,c = map(int,input().split())
        arr[a].append((b,-c))

    def bellman_ford(st):
        check = False
        dist[st] = 0
        for i in range(n):
            for j in range(1,n+1):
                for nn, ec in arr[j]:
                    if dist[nn] > dist[j] + ec:
                        dist[nn] = dist[j] + ec
                        if i == n-1:
                            check = True
        return check
    
    print('YES'if bellman_ford(n) else 'NO')