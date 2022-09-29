n,m = map(int,input().split())
arr = [[] for _ in range(n+1)]
for i in range(n):
    a,b = map(int,input().split())
    arr[a].append(b);arr[b].append(a)
    