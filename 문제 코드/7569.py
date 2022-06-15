from collections import deque
import sys
input = sys.stdin.readline

n1,n2,n3 = map(int,input().split())
q = deque([])

arr=[[list(map(int,input().rstrip().split())) for _ in range(n2)]for _ in range(n3)]

for a in range(n3):
    for b in range(n2):
        for c in range(n1):
            if arr[a][b][c] == 1:
                q.append([a,b,c,0])

dc = [-1,1,0,0,0,0]
db = [0,0,-1,1,0,0]
da = [0,0,0,0,-1,1]
def bfs():
    while q:
        a,b,c,d = q.popleft()
        for i in range(6):
            na = a + da[i]
            nb = b + db[i]
            nc = c + dc[i]
            if 0 <= na < n3 and 0 <= nb < n2 and 0 <= nc < n1:
                if arr[na][nb][nc] == 0:
                    arr[na][nb][nc] = 1
                    q.append([na,nb,nc,d+1])
    return d
if q:
    d = bfs()
for a in range(n3):
    for b in range(n2):
        for c in range(n1):
            if arr[a][b][c] == 0:d=-1

print(d)