import heapq,sys
input=sys.stdin.readline
heap = []
for i in range(int(input())):
    a = int(input())
    if a == 0:
        if len(heap) == 0:print(0)
        else: print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(a), a))