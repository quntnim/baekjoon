from math import gcd
from itertools import combinations
t = int(input())
for _ in range(t):
    result = 0
    num = list(map(int,input().split()))
    n = num.pop(0)
    arr = list(combinations(num,2))
    for i in range(len(arr)):
        result += gcd(arr[i][0], arr[i][1])
    print(result)