for _ in range(int(input())):
    arr = list(map(int,input().split()))
    cnt = 0
    for i in arr:
        if i>=10:cnt+=1
    print(*arr)
    print(['zilch','double','double-double','triple-double'][cnt],end='\n\n')