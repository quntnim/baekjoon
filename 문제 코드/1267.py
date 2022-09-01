n = int(input())
arr = list(map(int,input().split()))
ys = 0;ms = 0
for i in arr:
    ys += i//30*10+10
    ms += i//60*15+15
if ys == ms:
    print(f'Y M {ys}')
else:
    print(f'M {ms}'if ys > ms else f'Y {ys}')