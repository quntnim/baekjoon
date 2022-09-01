import sys
sys.setrecursionlimit(10**6)

def dfs(v):
    global cnt
    cnt+=1
    visit[v] = True
    for i in arr[v]:
        if not visit[i]:
            dfs(i)
    return

for _ in range(int(input())):
    inpt = list(map(int,input().split()))
    n = inpt.pop(0)
    k = inpt.pop(0)
    arr = [[] for _ in range(n+1)]
    visit = [False] * (n+1)
    cnt = 0
    for i in range(0,k*2,2):
        a,b = inpt[i],inpt[i+1]
        print(a,b)
        arr[a].append(b);arr[b].append(a)

    dfs(0)
    print('Connected.'if cnt==n else'Not Connected.')