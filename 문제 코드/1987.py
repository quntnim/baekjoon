import sys
input = sys.stdin.readline
n,m = map(int,input().rstrip().split())

arr=[]
for i in range(n):
    arr.append(list(input().rstrip()))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs():
    rst=1
    q=set([(0,0,arr[0][0])])
    while q:
        y,x,alph = q.pop()
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0 <= next_x < m and 0 <= next_y < n:
                if arr[next_y][next_x] != arr[y][x]:
                    if arr[next_y][next_x] not in alph:
                        q.add((next_y,next_x,alph+arr[next_y][next_x]))
                        rst = max(rst, len(alph+arr[next_y][next_x]))
    return rst   
print(bfs())