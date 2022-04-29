for i in range(int(input())):
    ox = list(input())
    add = 0; score = 0
    for l in ox:
        if(l == 'O'):
            add += 1
            score += add
        else:
            add = 0
    print(score)