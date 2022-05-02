import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v,e = map(int,input().split())
st = int(input())

dis = [INF] * (v+1)
arr = [[] for _ in range(v+1)]

for i in range(e):
    a,b,c = map(int,input().split())
    arr[a].append((b,c))

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

dijkstra(st)

for i in range(1,v+1):
    if dis[i] == INF:print('INF')
    else:print(dis[i])