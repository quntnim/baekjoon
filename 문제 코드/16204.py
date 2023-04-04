n,m,k = map(int,input().split())
print(max(n,k)-min(n-m,m-k))