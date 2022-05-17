import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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
        parent[a] = b
    
n,m = map(int,input().rstrip().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    c,a,b = map(int,input().rstrip().split())
    if c == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')