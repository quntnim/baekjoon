import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

dx = [0,1,-1,0,0]
dy = [0,0,0,1,-1]

res = 1e9
for p in range(1<<n):
    arr2 = [a[:] for a in arr]
    cnt = 0

    for i in range(n):
        if p & (1<<i):
            cnt += 1
            for l in range(5):
                nx = i + dx[l]
                ny = dy[l]
                if 0 <= nx and nx < n and 0 <= ny and ny < n:
                    arr2[ny][nx] = not arr2[ny][nx]
    
    for i in range(1,n):
        for l in range(n):
            if arr2[i-1][l]:
                for j in range(5):
                    nx = l + dx[j]
                    ny = i + dy[j]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        arr2[ny][nx] = not arr2[ny][nx]
                cnt += 1
    if sum(arr2[-1]) == 0:
        res = min(res,cnt)
print(res if res != 1e9 else -1)