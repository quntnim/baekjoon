for _ in range(int(input())):
    g,c,e = map(int,input().split())
    if g==2:g=3
    elif g==3:g=5
    print((e-c)*g if (e-c)*g>0 else 0)