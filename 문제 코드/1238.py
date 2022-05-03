import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

n,m,end = map(int,input().split())

arr = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))

def dijkstra(st,end):
    q=[]
    heapq.heappush(q,(0,st))
    dis = [INF] * (n+1)
    dis[st] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if dis[now] < dist:continue
        for i in arr[now]:
            cost = dist+i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
    return dis[end]

res = 0
for i in range(1,n+1):
    res = max(dijkstra(i, end)+dijkstra(end,i),res)

print(res)