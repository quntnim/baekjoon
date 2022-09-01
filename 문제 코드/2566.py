idx = [1,1]
mx = 0
for i in range(9):
    temp = list(map(int,input().split()))
    if mx < max(temp):
        mx = max(temp)
        idx = [i+1,temp.index(mx)+1]
print(mx)
print(*idx)