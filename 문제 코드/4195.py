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
        
for _ in range(int(input())):
    f = int(input().rstrip())
    parent = [i for i in range(f+1)]

    for _ in range(f):
        a,b = input().rstrip().split()
        union(a,b)
        print(len(parent))