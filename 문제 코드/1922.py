import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

arr = []
for i in range(m):
    a,b,cost=map(int,input().split())
    arr.append((cost,a,b))
arr.sort()

total = 0
for cost,a,b in arr:
    if find(a) != find(b):
        union(a,b)
        total += cost

print(total)