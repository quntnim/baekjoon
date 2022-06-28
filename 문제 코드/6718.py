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

arr = is_prime(32000)

while True:
    cnt = 0
    n = int(input())
    if n == 0:break
    for i in range(3,n//2+1):
        if arr[i] and arr[n-i]:
            cnt+=1
    if n == 4:
        print(1)
    else:
        print(cnt)