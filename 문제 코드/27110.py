n = int(input())
a,b,c = map(int,input().split())
res = 0
res += a if a<n else n
res += b if b<n else n
res += c if c<n else n
print(res)