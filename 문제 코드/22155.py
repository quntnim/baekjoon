for _ in range(int(input())):
    a,b=map(int,input().split())
    print('Yes'if a<2 and b<3 or a<3 and b<2 else'No')