import math
for i in range(int(input())):
    s = str(math.factorial(int(input())))
    for i in s[::-1]:
        if i != '0':
            print(i)
            break