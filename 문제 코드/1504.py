import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m = map(int,input().split())

arr = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))
    arr[b].append((a,c))

v1, v2 = map(int,input().split())

def dijkstra(st,end):
    q=[]
    heapq.heappush(q,(0,st))
    dis = [INF] * (n+1)
    dis[st] = 0

    if st==end:
        return 0
    while q:
        dist, now = heapq.heappop(q)
        
        if dis[now] < dist:continue
        for i in arr[now]:
            cost = dist+i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return dis[end]

vist1 = dijkstra(1, v1)+dijkstra(v1, v2)+dijkstra(v2, n)
vist2 = dijkstra(1, v2)+dijkstra(v2, v1)+dijkstra(v1, n)
res = min(vist1, vist2)

if res >= INF:
    print(-1)
else:
    print(res)