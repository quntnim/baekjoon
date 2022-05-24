v,e = map(int,input().split())
parent = [0] * (v+1)
for i in range(v+1):
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
for i in range(e):
    a,b,cost=map(int,input().split())
    arr.append((cost,a,b))
arr.sort()

total = 0
for cost,a,b in arr:
    if find(a) != find(b):
        union(a,b)
        total += cost

print(total)