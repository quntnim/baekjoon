for _ in range(int(input())):
    txt = input().split()
    for i in txt:
        print(i[::-1],end=' ')
    print()