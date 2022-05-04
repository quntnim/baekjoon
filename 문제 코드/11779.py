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
    arr[a].append((c,b))

arr2 = [i for i in range(n+1)]
start, end = map(int,input().split())

def dijkstra(st):
    q=[]
    heapq.heappush(q,(0,st))
    dis[st] = 0

    while q:
        cost, now = heapq.heappop(q)
        if dis[now] < cost:continue
        for nc, nn in arr[now]:
            if dis[nn] <= cost+nc:continue
            dis[nn] = cost+nc
            arr2[nn] = now 
            heapq.heappush(q,(dis[nn],nn))

dijkstra(start)
print(dis[end])
p = [end]
now = end
while now != start:
    now = arr2[now]
    p.append(now)
print(len(p))
print(' '.join(map(str,p[::-1])))