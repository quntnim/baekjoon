n=int(input())
p=list(map(int,input().split()))
res = 0
for i in range(n):
    res ^= p[i]
cnt = p.count(1)
if cnt == n:
    if cnt%2 == 0:
        res = 1
    else:
        res = 0
if res==0 :
    print('cubelover')
else:
    print('koosaga')