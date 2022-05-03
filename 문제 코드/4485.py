import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
x = [0,0,1,-1]
y = [1,-1,0,0]

def dijkstra(st,end):
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
        return dis[end]

while True:
    n = int(input())
    arr = []
    for i in range(n):
        a = list(map(int,input().split()))
        arr.append(a)

    dis = [INF] * (n+1)

    print(dijkstra(1))