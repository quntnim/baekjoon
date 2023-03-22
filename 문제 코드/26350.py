for _ in range(int(input())):
    arr = list(map(int,input().split()))
    print("Denominations:",*arr[1:])
    check = False
    for i in range(1,arr[0]):
        if arr[i+1] < arr[i]*2:check = True
    print("Bad"if check else"Good","coin denominations!")