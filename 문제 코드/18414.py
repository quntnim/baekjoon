x,l,r = map(int,input().split())
m = 200000
for i in range(l,r+1):
    if abs(x-i) < m: m = abs(x-i); res = i
print(res)