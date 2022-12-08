money = [25,10,5,1]
for i in range(int(input())):
    cnt = [0,0,0,0]
    c = int(input())
    for i in range(4):
        if money[i] <= c:
            while money[i] <= c:
                c -= money[i]
                cnt[i] += 1
    print(*cnt)