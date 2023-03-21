for _ in range(int(input())):
    now = 0
    for i in input():
        if i == 'U':now+=1
        if i == 'D':
            if now == 0:break
            else:now-=1
    print(now)