arr = []
for y in range(10):
    s = input()
    t = [0]*10
    for x in range(10):
        if s[x] == 'O':
            t[x] = 1
    arr.append(t)

dx = [0,1,-1,0,0]
dy = [0,0,0,1,-1]

res = 101
for p in range(1024):
    arr2 = [a[:] for a in arr]
    cnt = 0

    for i in range(10):
        if p & (1<<i):
            cnt += 1
            for l in range(5):
                nx = i + dx[l]
                ny = 0 + dy[l]
                if 0 <= nx and nx <= 9 and 0 <= ny and ny <= 9:
                    arr2[ny][nx] = not arr2[ny][nx]
    
    for i in range(1,10):
        for l in range(10):
            if arr2[i-1][l]:
                for j in range(5):
                    nx = l + dx[j]
                    ny = i + dy[j]
                    if 0 <= nx and nx <= 9 and 0 <= ny and ny <= 9:
                        arr2[ny][nx] = not arr2[ny][nx]
                cnt += 1
    if sum(arr2[9]) == 0:
        res = min(res,cnt)
print(res if res != 101 else -1)