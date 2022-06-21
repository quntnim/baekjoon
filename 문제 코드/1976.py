import sys
input = sys.stdin.readline

def find(t):
    if t == parent[t]:
        return t
    else:
        parent[t] = find(parent[t])
        return parent[t]

def union(a,b):
    a = find(a)
    b = find(b)
    if a!=b:
        parent[a]=b

n = int(input())
m = int(input())
parent = [i for i in range(n)]

arr = [list(map(int,input().split())) for _ in range(n)]
for y in range(n):
    for x in range(y+1,n):
        if arr[y][x] == 1:
            union(y,x)

route = list(map(int,input().split()))
check = []
for i in route:
    check.append(find(parent[i-1]))

print('YES'if len(set(check))==1 else'NO')