r,c=map(int,input().split())
arr=[]
for _ in range(r):
    arr.append(list(input()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for y in range(r):
    for x in range(c):
        if arr[y][x] == 'W':
            for i in range(4):
                next_x = x + dx[i]
                next_y = y + dy[i]
                if 0 <= next_x < c and 0 <= next_y < r:
                    if arr[next_y][next_x] == 'S':
                        print(0)
                        exit()
print(1)
for y in range(r):
    for x in range(c):
        if arr[y][x] == '.':arr[y][x] = 'D'
        print(arr[y][x],end='')
    print()