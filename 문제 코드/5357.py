for _ in range(int(input())):
    now = '🌱'
    for i in input():
        if i != now:
            now = i
            print(i,end='')
    print()