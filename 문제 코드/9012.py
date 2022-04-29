for _ in range(int(input())):
    a = list(input()); c=0
    for i in range(len(a)):
        if c < 0 : break
        elif a[i] == '(' : c+=1
        else : c-=1
    if c == 0:print('YES')
    else : print('NO')