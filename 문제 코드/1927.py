import heapq,sys
input=sys.stdin.readlne
heap = []
for i in range(int(input())):
    a = int(input())
    if a == 0:
        if len(heap) == 0:print(0)
        else: print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, a)