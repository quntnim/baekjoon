for i in range(3):
    arr = list(map(int,input().split()))
    h = arr[3] - arr[0]
    m = arr[4] - arr[1]
    s = arr[5] - arr[2]
    while True:
        if m<0:
            m+=60
            h-=1
        elif s<0:
            s+=60
            m-=1
        else:
            break
    print(h,m,s)
