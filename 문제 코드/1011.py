for _ in range(int(input())):
    x,y = map(int,input().split())
    l=y-x
    cnt=0
    while True:
        cnt+=1
        if l<=(cnt+1)//2 * (cnt//2+1):
            print(cnt)
            break