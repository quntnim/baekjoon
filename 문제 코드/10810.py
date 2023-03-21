n,m = map(int,input().split())
arr = [0 for _ in range(n)]
for _ in range(m):
    i,j,k = map(int,input().split())
    for x in range(i,j+1):arr[x-1] = k
print(*arr)