while True:
    check = False
    x,y,z = map(int,input().split())
    if x==0&y==0&z==0:break
    if x**2 + y**2 == z**2:check = True
    elif y**2 + z**2 == x**2:check = True
    elif x**2 + z**2 == y**2:check = True
    print('right'if check else'wrong')