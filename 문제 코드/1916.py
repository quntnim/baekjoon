import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

dis = [INF] * (n+1)
arr = [[] for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))

start, end = map(int,input().split())

def dijkstra(st):
    q=[]
    heapq.heappush(q,(0,st))
    dis[st] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if dis[now] < dist:continue
        for i in arr[now]:
            cost = dist+i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
print(dis[end])