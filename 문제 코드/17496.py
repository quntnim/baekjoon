sumday, grow, can, money = map(int,input().split())
growing = grow
addmoney = 0
for i in range(sumday):
    if(growing == 0):
        addmoney += (money * can)
        growing = grow-1
    else:
        growing -= 1
print(addmoney)