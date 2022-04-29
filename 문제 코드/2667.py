n = int(input());arr = []
for i in range(n):
    arr.append(list(map(int,input())))

def dfs(x, y, num):
    if x < 0 or x > n - 1 or y < 0 or y > n - 1:
        return False
    if arr[x][y] == 1:
        arr[x][y] = num
        dfs(x, y + 1, num)
        dfs(x, y - 1, num)
        dfs(x - 1, y, num)
        dfs(x + 1, y, num)
        return True
    else:
        return False

num = 2;areas = 0
for x in range(n):
    for y in range(n):
        if arr[x][y] == 1:
            dfs(x,y,num)
            num+=1;areas+=1

home = []
for num in range(2,areas+2):
    cnt = 0
    for i in arr:
        for j in i:
            if num==j:
                cnt += 1
    home.append(cnt)
home.sort()

print(areas)
for i in home:
    print(i)