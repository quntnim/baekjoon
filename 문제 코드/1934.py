from math import lcm
for _ in range(int(input())):
    arr=list(map(int,input().split()));print(lcm(arr[0], arr[1]))