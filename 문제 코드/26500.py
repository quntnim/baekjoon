for i in range(int(input())):
    a,b = map(float,input().split())
    print(round(max(a,b)-min(a,b),1))