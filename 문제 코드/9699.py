for case in range(int(input())):
    arr = list(map(int,input().split()))
    print("Case #{0}: {1}".format(case+1,max(arr)))