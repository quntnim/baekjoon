for i in range(int(input())):
    n = int(input())
    n = str(format(n,'b'))[::-1]
    for i in range(len(n)):
        if n[i]=='1':print(i,end=' ')
    print()