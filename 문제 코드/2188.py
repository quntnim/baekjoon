import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int,input().split())
cow = [[]for _ in range(n+1)]
v = [False for _ in range(m+1)]
cnt=0
def dfs(s):
    if check[s]:
        return False
    check[s] = True
    for i in cow[s]:
        if v[i] == False or dfs(v[i]):
            v[i] = s
            return True
    return False

for i in range(1,n+1):
    arr = list(map(int,input().split()))
    for l in arr[1::]:
        cow[i].append(l)

for i in range(1,n+1):
    check = [False]*(n+1)
    if dfs(i):
        cnt += 1

print(cnt)