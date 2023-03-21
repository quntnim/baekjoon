for _ in range(int(input())):
    x,y = map(int,input().split())
    l=y-x
    cnt=0
    while True:
        cnt+=1
        if l<=(cnt)//2 * (cnt//2):
            print(cnt)
            break
        