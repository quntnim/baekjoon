for _ in range(int(input())):
    c=0;a,b=map(int,input().split())
    for i in range(a,b+1):s=str(i);c+=s.count('0')
    print(c)