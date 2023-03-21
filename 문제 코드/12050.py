import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

for i in range(int(input().rstrip())):
    print(f"Case #{i+1}:")
    a,b = map(int,input().rstrip().split())
    arr = []
    for i in range(a):
        arr.append(list(map(int,input().rstrip())))

    def dfs(x,y):
        if x >= b or x < 0 or y >= a or y < 0:
            return 0
        elif arr[y][x] == 1 and not check[y][x]:
            check[y][x] = True
            dfs(x+1,y)
            dfs(x-1,y)
            dfs(x,y+1)
            dfs(x,y-1)
            return 1
        else:
            return 0

    for i in range(int(input().rstrip())):
        c = list(input().rstrip().split())
        if len(c) == 1:
            check = [[False for _ in range(b)]for _ in range(a)]
            cnt = 0
            for y in range(a):
                for x in range(b):
                    if arr[y][x] == 1 and not check[y][x]:
                        cnt+=1
                        dfs(x,y)
            print(cnt)
        else:
            arr[int(c[1])][int(c[2])] = int(c[3])