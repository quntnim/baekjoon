for i in range(int(input())):
    t, s = input().split()
    for l in s:
        print(l * int(t), end='')
    print()