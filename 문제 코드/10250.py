for _ in range(int(input())):
    cnt = 0
    h,w,n = map(int,input().split())
    for j in range(1,w+1):
        for i in range(1,h+1):
            cnt+=1
            if cnt == n:print(f"{i}{j:02d}")
