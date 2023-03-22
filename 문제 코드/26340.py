for i in range(int(input())):
    x,y,f = map(int,input().split())
    print("Data set:",x,y,f)
    for _ in range(f):
        if x >= y:x//=2
        elif y > x:y//=2
    print(*sorted([x,y])[::-1],'\n')