n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

for y in range(n):
    for x in range(n):
        if arr[y][x] == 1