for _ in range(int(input())):
    arr = list(map(int,input().split()))
    print(*arr)
    cnt = 0
    if 17 in arr and 18 in arr:print('both')
    elif 17 in arr:print('zack')
    elif 18 in arr:print('mack')
    else:print('none')
    print()