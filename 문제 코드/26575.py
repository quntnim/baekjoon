for i in range(int(input())):
    dog, food, money = map(float,input().split())
    print(f'${dog*food*money:.2f}')