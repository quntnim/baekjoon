n=int(input())
p=list(map(int,input().split()))
res = 0

for n in p:
    if n&1:
        res ^= (n+1)//2
    else:
        res ^= (n-2)//2

if res==0 :
    print('cubelover')
else:
    print('koosaga')