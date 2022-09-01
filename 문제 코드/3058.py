for i in range(int(input())):
    res = []
    arr = list(map(int,input().split()))
    for i in arr:
        if not i%2:res.append(i)
    print(sum(res), min(res))