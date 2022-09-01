n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(input()))

def dfs(x,y,l):
    if x<0 or x>m-1 or y<0 or y>n-1:
        return False
    if arr[y][x] == '-' and l == '-':
        arr[y][x] = 0
        dfs(x-1 , y, '-')
        dfs(x+1 , y, '-')
        return True
    elif arr[y][x] == '|' and l == '|':
        arr[y][x] = 0
        dfs(x, y-1, '|')
        dfs(x, y+1, '|')
        return True
    else:
        return False
    
cnt = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] == '-':
            dfs(x,y,'-')
            cnt += 1
        if arr[y][x] == '|':
            dfs(x,y,'|')
            cnt += 1  
print(cnt)