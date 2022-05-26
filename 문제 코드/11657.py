import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())
arr = []
dist = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    arr.append((a,b,c))

def bellman_ford(st):
    dist[st] = 0
    for i in range(n):
        for j in range(m):
            cn = arr[j][0]
            nn = arr[j][1]
            ec = arr[j][2]
            if dist[cn] != INF and dist[nn] > dist[cn] + ec:
                dist[nn] = dist[cn] + ec
                if i == n-1:
                    return True
    return False

cycle = bellman_ford(1)

if cycle:
    print(-1)
else:
    for i in range(2,n+1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])