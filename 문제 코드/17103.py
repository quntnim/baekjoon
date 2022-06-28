import sys
import math
input = sys.stdin.readline

def is_prime(n):
    arr = [True] * (n + 1)
    arr[0] = False;arr[1] = False

    for i in range(2, int(math.sqrt(n)+1)):
        if arr[i] == True:
            j = 2
            while (i * j) <= n:arr[i*j] = False;j += 1

    return arr

arr = is_prime(1000000)

for _ in range(int(input())):
    cnt = 0
    n = int(input())
    for i in range(3,n//2+1):
        if arr[i] and arr[n-i]:
            cnt+=1
    if n == 4:
        print(1)
    else:
        print(cnt)